######
#               -*- coding: utf-8 -*-
# Author:       gonzalof 03.03.2020
# Abstract:     Helpers for implementing things hahahahahaha
# Todo:
#               - Make the code more decent :|
#               - pyDocument all helpers
#               - File handlers should be moved to a separate module
#####

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
from chardet.universaldetector import UniversalDetector
from datetime import datetime, timedelta
import re, time, csv, pysftp, os, subprocess, glob, json, shutil

## Vars

####
## loot: one to one mapping
## map: one to list mapping
####

## Functions

# Inline helpers
jds = lambda d: json.dumps(d, indent=2)
serialize = lambda s: '\',\''.join(s)
crpath = lambda p,f: os.path.join(p,f)

## Not sure if it is worth to encapsulate this small code
def yaml_parse(input_file):
    try:
        with open(input_file, 'r') as din: return load(din, Loader=Loader)
    except:
        raise FileExistsError

## No clue on if its better to keep it as csv or to switch to yaml as the
## format for the input file
def parse_map_csv(file, encoding="utf8", **kwargs):
    # TODO: check args
    rtv = {}
    try:
        with open(file, 'r', encoding=encoding) as f:
            read = csv.DictReader(f)
            mapping_index, mapped_index = read.fieldnames[0:2]
            for row in read:
                mapped  = row[mapped_index]
                mapping = row[mapping_index]
                if not rtv.get(mapped):
                    rtv[mapped] = list()
                rtv[mapped].append(mapping)
    except FileExistsError:
        print_log(f"Look up table file {file} not found or not accesible.", level=2, **kwargs)
    return rtv
    
## YAML version of the parser for loot creation
def parse_loot_yaml(file, **kwargs):
    try:
        return yaml_parse(file)
    except FileExistsError:
        print_log(f"Look up table file {file} not found or not accesible.", level=2, **kwargs)


def new_field(row, mapping, lookup_field, new_field, debug=False, **kwargs):
    # TODO: Add check to verify the lookup field exists and the new field does not in row.
    # And make sure both fields are in the mapping dict. Remove debug code when stable.
    found=False
    for mp in mapping:
      print_log(f"Checking assistant {mp}", debug=debug, level=9)
      print_log(f"Associated campaigns are {mapping[mp]}", debug=debug, level=9)
      print_log(f"Lookup {row[lookup_field]}", debug=debug, level=9)
      if row[lookup_field] in mapping[mp]:
        row.update( { new_field : mp} )
        print_log('Assistant found an assigned', debug=debug, level=9)
        found=True
        break
    if not found:
      print_log(f"No Assistant found for {row['STATE']}", level=1, **kwargs)

## Loots are more direct but potentilly more ineficient for large repeated data
def new_field_loot(row, loot, lookup_field, new_field, mode=None, **kwargs):
    try:
      new_data = loot[str(row[lookup_field])]
      if mode == 'update' : new_data = f"{row[new_field]}{new_data}"
      row.update( {new_field : new_data } )
    except:
      print_log(f"Look up table does not contain {row[lookup_field]} data for new field {new_field}.", level=2, **kwargs)
      print_log(f"{jds(row)}", **kwargs)
      print_log(f"{jds(loot)}", **kwargs)

def update_field_loot(row, loot, new_field, data):
  pass

def field_mod(row, **kwargs):
    pass

# Inneficient if used row by row
def header_mod(row, cvsc_field, user_field, **kwargs):
    try:
      row[user_field] = row.pop(cvsc_field)
    except:
      print_log(f"The provided field {cvsc_field} is not available.", level=1, **kwargs)

# Core SFTP functionality should be moved to the SFTP class
def upload(config, filename, debug_mode=True):
  # Quick prototype, need to add checks
  rtv = 0
  # TODO: understand better how to log known hosts
  cnopts = pysftp.CnOpts()
  cnopts.hostkeys = None

  with pysftp.Connection(**config.ftp_config, cnopts=cnopts) as sftp:
    sftp.chdir(config.UPLOAD_DIR)
    print('sftp.put(filename)') if debug_mode else sftp.put(filename)
    rtv = 1
  return rtv

# Added as a generic function as it identicall for current supported customers
# Text and patterns for name generation may be loaded from config file if needed
def upload_backup(config, debug_mode=True):
  rtv = 0
  datename = time.strftime("%Y%m%d", time.localtime())
  if config.csv_upload_name != '':
    datename = f"{config.csv_upload_name}_{datename}"
  csv_upload_name = f"Conversica_{datename}.csv"
  csv_bas_back_name = f"Conversica_baseline_{datename}.csv"
  csv_backup = os.path.join(config.BACKUP_PATH, csv_bas_back_name)
  csv_stored = os.path.join(config.LOCAL_UPLOAD_DIR, csv_upload_name)

  if debug_mode: print(csv_upload_name)
  if os.path.isfile(config.csv_baseline):
    shutil.copy2(config.csv_baseline, csv_backup)
  if os.path.isfile(config.csv_output):
    # Simple prototype, need to check if folder exists
    shutil.copy2(config.csv_output,csv_stored)
    rtv = upload(config, filename=csv_stored, debug_mode=debug_mode)
  # tmp update
  sftp_browser(config, update=1)

  return rtv

def sftp_browser(config, depth=5, update=0):
  csv_out = []
  # Cache handling 
  ftp_file_name = f"ftp_{config.user}.txt"
  ftp_file_data = os.path.join(config.WORK_DIR, ftp_file_name)

  # TODO: understand "better" how to log known hosts
  cnopts = pysftp.CnOpts()
  cnopts.hostkeys = None
  name_pos = 8

  # Current return value asumes the flow is always successful, need to enhance this
  if update or not os.path.isfile(ftp_file_data):      
    with pysftp.Connection(**config.ftp_config, cnopts=cnopts) as sftp:
      sftp.chdir(config.UPLOAD_DIR)
      # HACK: Hard to work with, will save into a file an parse it from there
      with open(ftp_file_data, 'w') as tmp:
        for a in sftp.listdir_attr():
            #tmp.write(a)
            print(f"{a}", file=tmp)

  with open(ftp_file_data, 'r') as tmp:
      for line in tmp:
        tl = line.split()
        if re.match(config.ftp_pattern, tl[name_pos]):
            csv_out.append(tl)

  # Assuming the order based on filename, a nmore robust approach should filter by date
  return csv_out[-depth:]


def check_files(config, mode="full", **kwargs):
  rtv = 1
  if 'req_files' not in kwargs:
    req_files=[config.csv_input]
    if mode == "update":
      req_files=[config.csv_baseline, config.csv_update]
  else:
    req_files = kwargs['req_files']
  for f in req_files:
      if not os.path.isfile(f):
          rtv = 0
  return rtv

def charset_check(file, **kwargs):
    detector, d = UniversalDetector(), 0
    detector.reset()
    try:
        for line in open(file, 'rb'):
            detector.feed(line)
            d += 1
            if detector.done or d == 100 : break
        detector.close()
        kwargs['level']=0
        print_log(f"Charset {detector.result['encoding']} was identified for file {file} with a confidence level of {detector.result['confidence']}", **kwargs)
    except:
        pass

def remove_lead(data, to_be_removed, **kwargs):
  for nw in to_be_removed:
    try:
      data.pop(nw)    
      print_log(f"User with CVSC ID {nw} removed by rule.", level=0, **kwargs) 
    except KeyError:
      ## Maybe it is better to just print out a summary with the total, at least in update mode
      print_log(f"User with CVSC ID {nw} not found during removal.", level=1, **kwargs) 

def write_csv(file, data,  encoding, fieldnames, delimiter, rename_headers={}, **kwargs):
  with open(file, 'w', newline='', encoding=encoding, errors='replace') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=delimiter, dialect='excel', 
                            extrasaction='ignore', quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    for d in data:
      # There should be a cleaner and faster way to change the header
      for rh in rename_headers:
        #header_mod(data[d], rename_headers[rh]['orig'], rename_headers[rh]['new'], **kwargs)
        header_mod(data[d], rh['orig'], rh['new'], **kwargs)
      writer.writerow(data[d])

def custom_escape(row, custom_escape):
    for f in custom_escape:
      field = custom_escape[f]['field']
      row[field] = re.subn(custom_escape[f]['orig'],custom_escape[f]['new'], row[field])[0] 

# TODO: define if passing the class or arguments, helpers are not consistent
def check_not_empty(row, cond_field, check_field, cond_val, cond_change, **kwargs):
    if row[cond_field] in cond_val:
        if not row[check_field]:
            # Print alert to error file and Apply the rule
            print_log(f"Unexpected empty message body for CVSC ID {row['CONVERSICA ID']}, changing status to {cond_change} by rule", level=1, **kwargs)
            row.update({"STATUS":cond_change})
            #row[cond_field]='EML03'

## This should be generic. TODO: consistency
def charset_exeption_handler(row, file, pattern, **kwargs):
  print_log(f"{file} does not have the CONVERSICA ID field.", level=2, **kwargs)
  for fl in row:
    ff = re.match(pattern, fl)
    if ff:
      ## Something is not working here, temporary changed format for war (f->r)
      print_log(r"-----> There is a field {fl} found, there may be a codification or excel writing issue.", **kwargs)
  return 0, "Row CONVERSICA ID not found in file"

def run_checks(config):
    rtv=subprocess.run([config.check_script, config.RUN_DIRECTORY], capture_output=True)
    return rtv

def time_format(row, fields, out_format, in_format="%Y-%m-%d %H:%M:%S"):
  """The CVSC date format will be modified according to the one provided in out_format variable.
  Fields shall be a list of fields"""
  # Pending to validate args and print message
  for field in fields:
    #print(f"DEBUG: {field} {row[field]}")
    # Try is a new hack to WA CVSC BUG: "LAST ACTIVITY": "-0001-11-30 04:00:00"
    try:
      if row[field]: row[field] = time.strftime(out_format, time.strptime(row[field], in_format))
    except:
      if row[field] and row[field] == 'LAST ACTIVITY':
        row[field] = time.strftime(out_format, time.strptime(row['SCHEDULED DATE'], in_format))

def clean(config, mode):
  rtv=0
  files=glob.glob(os.path.join(config.RUN_DIRECTORY, "*.csv"))
  for f in glob.glob(os.path.join(config.RUN_DIRECTORY, "*.txt")):
      files.append(f)
  # Need 2 implement try
  if len(files) > 0:
      for f in files:
        # Temporary hack to make sure the new baseline doesnt get lost by mistake
        if mode == "clean" and f == config.csv_output_b:
            continue
        os.remove(f)
      if os.path.isfile(config.csv_output_b):
        os.rename(config.csv_output_b, config.csv_baseline)
      rtv=1
  else:
      rtv=2
  return rtv

def number_only(row, fields, **kwargs):
  """Strips out any non digit character including spaces"""
  if kwargs['headers']:
    valid = list(filter(lambda f: f in kwargs['headers'], fields))
  for field in valid:
    if row[field]: row[field] = re.sub(r'[^\d]', '', row[field])

def parse_sql(sql_file, include_vars=False, debug=False, **kwargs):
  """Returns the SQL query in a string. It can also return a tuple with the variables to be filled"""
  rtv, rtv2 = False, None
  with open(sql_file, 'r') as sql:
    query = "".join(sql.readlines()).split(';')
    # Limited support for now --- it  just handle a single query per sql file
    rtv = query[0] + ';'
    print_log("Parsed query:\n", rtv, debug=debug, level=9, **kwargs)
  if include_vars: 
    rtv2 = extract_sql_vars(rtv, debug=debug, **kwargs)
    return rtv, rtv2
  return rtv

def extract_sql_vars(sql, debug=False, **kwargs):
  """Receives an SQL query as a string an returns a list of the variables present in the query"""
  # A warning should be issued when there are special characters in the variable, before re.sub
  print(sql)
  rtv = list(map( lambda v: re.sub(r'\W', '', v), re.findall(r'{[\w]+}', sql)))
  print_log("Query received:\n", sql, "\n found variables\n", rtv, debug=debug, level=9, **kwargs)
  return rtv

def print_log(*message, debug=None, logfile=None, level=None):
  """
  Can print the list of provided messages to stdout and to a file handler.
  It can also add at the beginnig a severity word based on the level.
  """
  lvl_msg = ""
  levels={0:'INFO:', 1:"WARNING:", 2:"ERROR:", 3:"FATAL:", 9:"DEBUG:"}
  use_as_print = (debug is None and logfile is None)

  if level is not None and level in levels:
      lvl_msg = levels[level] 
  if debug or use_as_print: print(lvl_msg, *message)
  # Pending to check if it is a valid handler
  if logfile: print(lvl_msg, *message, file=logfile)

def test():
    return "holi"

#return a starting date provided a Customer's rules of how many day's back to look based on the day of the week
#if an exception is given, that will be used as the number of days to look back, regardless of the rules.
def dateHandler(customerRules, ruleException = ''):
    currentDate = datetime.today()
    currentDay = currentDate.strftime('%A')
    if ruleException.isdigit():
        daysBefore = ruleException
    elif currentDay in customerRules.keys():
        daysBefore = customerRules[currentDay]
    else:
        daysBefore = 1
    diff = currentDate - timedelta(days = daysBefore)
    result = datetime(diff.year, diff.month, diff.day)
    endTime = datetime(currentDate.year, currentDate.month, currentDate.day)
    return result, endTime

#given a list of file headers and a RE pattern, verify if any headers match the pattern and return a boolean 
def headerMatch(headerList, pattern):
  for header in headerList:
    if re.match(pattern , header.strip(), re.IGNORECASE) != None:
      return True
  return False