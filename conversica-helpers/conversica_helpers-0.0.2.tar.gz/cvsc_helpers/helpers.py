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
from detect_delimiter import detect
from datetime import datetime, timedelta
from pymongo import MongoClient
from pathlib import Path
from openpyxl import Workbook
import re, time, csv, pysftp, os, subprocess, glob, json, shutil, requests, chardet, aiohttp, asyncio
import cchardet as chardetf

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
get_time = lambda : datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
        return None


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
      print_log(f"No data to fill {new_field}  found for {row['CONVERSICA ID']} {row['STATE']}", level=2, **kwargs)

## Loots are more direct but potentilly more ineficient for large repeated data
# TODO: this function grew inorganically, need to redesign it
def new_field_loot(row, loot, lookup_field, new_field, mode=None, cache=None, **kwargs):
    new_data = ''
    try:
      existing_data = row[new_field]
      if mode == 'preserve' and existing_data != '': return False
    except:
      existing_data = ''
    try:
      if cache:
        cycle_value = row[lookup_field] if lookup_field != '' else next(iter(loot.keys()))
        new_data = loot[str(cycle_value)][cache[cycle_value][0]]
      else:
        if mode == 'carry_over':
          new_data = str(row[lookup_field]) if lookup_field != '' else next(iter(loot.keys()))
        elif mode == 'upgrade':
          if lookup_field != '':
            new_data = [str(row[luf]) for luf in lookup_field] if isinstance(lookup_field, list) else [str(row[lookup_field])]
          else: new_data = next(iter(loot.keys()))
        else:
          if loot:
            new_data = loot[str(row[lookup_field])] if lookup_field != '' else next(iter(loot.values())) # Why not keys?
          else:
            new_data = str(row[lookup_field]) if lookup_field != '' else ''
      if   mode == 'update'  : new_data = f"{existing_data} {new_data}"
      elif mode == 'upgrade' : new_data = existing_data.format(*new_data)
      elif mode == 'reformat':
        if   new_data == 'title'        : new_data = existing_data.title() #Assuming too many things
        elif new_data == 'price'        : new_data = f"${existing_data}"
        elif new_data == 'invert_order' : new_data = " ".join(existing_data.split()[::-1])
        elif new_data == 'first_name_3' : new_data = f"{existing_data.split()[2]} {existing_data.split()[0]}"
        elif new_data == 'date_no_hour' : new_data = f"{existing_data.split()[0]}"
        elif new_data == 'whatsapp_name': new_data = f"{existing_data.split()[0].rstrip().title()}"
        else: new_data = existing_data
      row.update( {new_field : new_data } )
      return True
    except:
      print_log(f"Look up table does not contain data for {row[lookup_field]} to be used in new field {new_field}.", level=1, **kwargs)
      print_log(f"{mode} {new_data}", **kwargs)
      print_log(f"{jds(row)}", **kwargs)
      print_log(f"{jds(loot)}", **kwargs)
      return None

def update_field_loot(row, loot, lookup_field, update_field, **kwargs):
  new_field_loot(row, loot, str(lookup_field), update_field, **kwargs)


def field_mod(row, **kwargs):
    pass

def filter_field_loot(row, loot, lookup_field, new_field=None, **kwargs):
  rtv = False
  try:
    if row[str(lookup_field)] in str(loot[str(lookup_field)]): rtv = True
  except:
    print_log(f"Look up field {lookup_field} not present in row {row}.", level=1, **kwargs)
  return rtv

def split_note_field(row, input_field='NOTES', output_field=['NOTE DATE', "NOTE BODY"], multi_cols=False, sepp='jw,]_Wm5=.;c.tY', **kwargs):
  """Designed to split Note field into date an body \n(This could be more generic and make it into many, the rule may be complicated though)"""
  try:
    note = row[input_field]
    note_date = ''
    note_txt = ''
    if note != '':
      # Current implementation asumes format. TODO: make it more robust with re
      # Hack for GTD-Residencial, notes: n-cols
      if multi_cols == True:
        notes_int = re.sub('([0-9\ \-\/:]{15,22})', sepp+r'\1' , note)
        notes = re.split(sepp, notes_int)
        notes.pop(0)
        for out_field, note in zip(output_field, notes):
          row.update({ out_field : note})  
      else:
        note_date = re.findall("[0-9\ \-\/:]{19}", note)
        note_txt1 = re.sub("[0-9\ \-\/:]{22}","", note, 1)
        note_txt = re.sub("[0-9\ \-\/:]{22}","", note_txt1)
        row.update({output_field[0] : "\r".join(note_date)})
        row.update({output_field[1] : note_txt})
      row.pop(input_field)
  except:
    print_log(f"No NOTES field present for CVSC ID {row['CONVERSICA ID']} ", level=1, **kwargs)

# Inneficient if used row by row
def header_mod(row, cvsc_field, user_field, **kwargs):
    try:
      row[user_field] = row.pop(cvsc_field)
    except:
      print_log(f"The field {cvsc_field} was supposed to be converted to {user_field} but it was not provided.", level=1, **kwargs)

# Core SFTP functionality should be moved to the SFTP class
def upload(config, filename, external_copy=False , debug_mode=True):
  # Quick prototype, need to add checks
  rtv = 0
  try:
    sftp_var = os.environ["CSV_SFTP_TOOL"]
  except:
    sftp_var = None

  if sftp_var and sftp_var == "sftp":
    output=subprocess.run(["assets/run_sftp.sh", config.ftp_config['username'], config.UPLOAD_DIR, filename, config.ftp_config['private_key'], config.ftp_config['host']])
    print(output)
    # External Copy only handled in shell sftp for now, temporary hardcoded version for MAF
    if external_copy:
      output=subprocess.run(["assets/run_sftp.sh", config.ext_ftp_config['username'], "Entrada", filename, config.ext_ftp_config['private_key'], config.ext_ftp_config['host']])
      print(output)
    if output.returncode == 0: rtv = 1
  else:
    # TODO: understand better how to log known hosts
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

  with pysftp.Connection(**config.ftp_config, cnopts=cnopts) as sftp:
    sftp.chdir(config.UPLOAD_DIR)
    print(f'sftp.put({filename})') if debug_mode else sftp.put(filename)
    rtv = 1
  return rtv

def upload_shell(config, filename):
    output=subprocess.run(["assets/run_sftp.sh", config.ftp_config['username'], config.UPLOAD_DIR, filename, config.ftp_config['private_key']])
    print(output)
    rtv = 1
    if output.returncode != 0: rtv = 0
    return rtv

# Added as a generic function as it identicall for current supported customers
# Text and patterns for name generation may be loaded from config file if needed
def upload_backup(config, external_copy=False, debug_mode=True, api_mode=False, **kwargs):
  rtv = 0
  ext = config.csv_output.rsplit('.')[-1]
  datename = time.strftime("%Y%m%d", time.localtime())
  if config.csv_upload_name != '':
    datename = f"{config.csv_upload_name}_{datename}"
  csv_upload_name = f"Conversica_{datename}.{ext}"
  csv_bas_back_name = f"Conversica_baseline_{datename}.csv"
  csv_backup = os.path.join(config.BACKUP_PATH, csv_bas_back_name)
  csv_stored = os.path.join(config.LOCAL_UPLOAD_DIR, csv_upload_name)

  if debug_mode: print(csv_upload_name)
  if os.path.isfile(config.csv_baseline):
    shutil.copy2(config.csv_baseline, csv_backup)
  if os.path.isfile(config.csv_output):
    # Simple prototype, need to check if folder exists
    shutil.copy2(config.csv_output,csv_stored)
  
  if not api_mode:
    rtv = upload(config, filename=csv_stored, external_copy=external_copy, debug_mode=debug_mode)
  else:
    with open(csv_stored, 'r', encoding=config.encodings['out']) as f:
      rtv = 1
      count = 0
      read = csv.DictReader(f, delimiter=config.out_delimiter)
      asyncio.run(fast_upload(config.API_config, read, count, debug=debug_mode, **kwargs))
      #for row in read:
      #  #print(jds(row))
      #  r = upload_api(config.API_config, row, debug=False)
      #  if not r:
      #    count += 1
      #    print_log(f"API POST failed for {jds(row)}.", level=1, **kwargs)
      if count > 0:
        count = 2 if count < read.line_num else 0
      print_log(f"Attempted to upload {read.line_num} entries, from which {count} where not successfull.", level=0, **kwargs)

  # tmp update Disabled as the flask web page is no longer used
  #sftp_browser(config, update=1)

  return rtv

async def fast_upload(creds, rows, count, **kwargs):
  tasks = []
  async with aiohttp.ClientSession() as session:
    for row in rows:
      task = asyncio.ensure_future(upload_api_v2(creds, row, session, **kwargs))
      await asyncio.sleep(1/80)
      tasks.append(task)

    responses = await asyncio.gather(*tasks)
    for response in responses:
     if not response['success']:
      count+=1
      print_log(f"API POST failed for {jds(response['row'])}.", level=1, **kwargs)

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
  """Text encoding detector based on chardet.\n
  Returns the encoding found and the confidence level"""
  encoding, confidence = 'None', 0
  try:
    filepath = Path(file)
    blob = filepath.read_bytes()

    detection = chardetf.detect(blob)
    encoding = detection["encoding"]
    confidence = detection["confidence"]
    kwargs['level']=0
    print(f"Charset {encoding} was identified for file {file} with a confidence level of {confidence}")#, **kwargs)
  except:
    kwargs['level']=0
    print(f"Charset faile to identify encoding  for file {file}")#, **kwargs)
  
  return encoding, confidence

def charset_check_old(file, **kwargs):
  """Text encoding detector based on chardet.\n
  Returns the encoding found and the confidence level"""
  detector, d = UniversalDetector(), 0
  detector.reset()
  try:
    for line in open(file, 'rb'):
      detector.feed(line)
      d += 1
      if detector.done or d == 1000 : break
    detector.close()
    kwargs['level']=0
    print(f"Charset {detector.result['encoding']} was identified for file {file} with a confidence level of {detector.result['confidence']}")#, **kwargs)
  except:
    pass
  return detector.result['encoding'], detector.result['confidence']

def remove_lead(data, to_be_removed, **kwargs):
  for nw in to_be_removed:
    try:
      data.pop(nw)    
      print_log(f"User with CVSC ID {nw} removed by rule.", level=0, **kwargs) 
    except KeyError:
      ## Maybe it is better to just print out a summary with the total, at least in update mode
      print_log(f"User with CVSC ID {nw} not found during removal.", level=1, **kwargs) 

def filterout_by_field(row, field, values, **kwargs):
  """"""
  # So far it just handles one filter
  return row[field] in values

def write_csv(file, data,  encoding, fieldnames, delimiter, rename_headers={}, limit=None, old_header_mod=True,**kwargs):
  with open(file, 'w', newline='', encoding=encoding, errors='replace') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=delimiter, dialect='excel', 
                            extrasaction='ignore', quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    count = 1
    for d in data:
      # There should be a cleaner and faster way to change the header
      if rename_headers is not None:
        for rh in rename_headers:
          if old_header_mod:
            header_mod(data[d], rename_headers[rh]['orig'], rename_headers[rh]['new'], **kwargs)
          else:
            header_mod(data[d], rh['orig'], rh['new'], **kwargs)
      writer.writerow(data[d])
      # Maybe have the write function twice to avoid the if on avey case is not needed, would be a better idea
      if limit and isinstance(limit, int) and count >= limit: break
      count += 1

def write_xlsx(file, csv_input, encoding, delimiter, password=None, **kwargs):
  """CSV to XLSX converter based on openpyxl"""
  wb = Workbook()
  ws = wb.active
  with open(csv_input, 'r', encoding=encoding) as f:
    for row in csv.reader(f, delimiter=delimiter):
      ws.append(row)
  if password:
    print(f"Using password {password}")
    wb.security.workbookPassword = str(password)
    wb.security.lockStructure = True
  wb.save(file)

def write_csv_gen(file, data,  encoding, fieldnames, delimiter, rename_headers={}, limit=None, **kwargs):
  with open(file, 'w', newline='', encoding=encoding, errors='replace') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=delimiter, dialect='excel', 
                            extrasaction='ignore', quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    count = 1
    for values in data:
      # There should be a cleaner and faster way to change the header
      if rename_headers is not None:
        for rh in rename_headers:
          #header_mod(data[d], rename_headers[rh]['orig'], rename_headers[rh]['new'], **kwargs)
          header_mod(values, rh['orig'], rh['new'], **kwargs)
      writer.writerow(values)
      # Maybe have the write function twice to avoid the if on avey case is not needed, would be a better idea
      if limit and isinstance(limit, int) and count >= limit: break
      count += 1

def key_csv_data(file, encoding='utf8', delimiter=',', **kwargs):
  """Reads a CSV file based on the encoding and delimiter defined\n
  It returns a data in a list and the headers"""
  count, headers = 0, []
  try:
    with open(file, 'r', encoding=encoding) as din:
      data = csv.DictReader(din, delimiter=delimiter)
      headers = data.fieldnames
      for row in data:
        # This approach fails for invalid rows
        count += 1
  except:
    print_log(f"File {file} could not be open. Aborting", level=2, **kwargs)
  return count, headers


def open_log_handler(file, **kwargs):
  rtv = None
  try:
    rtv = open(file, 'w')
  except:
    # Should we abort?
    print_log(f"Log file {file} could not be open wor writing!", level=3)
  return rtv


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
      if field == 'LAST ACTIVITY':
        row[field] = time.strftime(out_format, time.strptime(row['SCHEDULED DATE'], in_format))

def clean(config, mode):
  rtv=0
  files=glob.glob(os.path.join(config.RUN_DIRECTORY, "*.csv"))
  #for f in glob.glob(os.path.join(config.RUN_DIRECTORY, "*.txt")): files.append(f)
  for f in glob.glob(os.path.join(config.RUN_DIRECTORY, "*.xlsx")): files.append(f)
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

def print_slack(msg_slack, channel=''):
  channels = {
    'dev_test': 'https://hooks.slack.com/services/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',
    'survivors_tech_ops' : 'https://hooks.slack.com/services/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' }
  if channel in channels:
    r = requests.post( channels[channel], data=json.dumps({"text":msg_slack}))
  print(msg_slack)

def update_db_status(status, cid, verbose=True):
  uri = 'https://bluebox.gonmalo.dev/api/customers/tool_status'
  body = {'tool': 'daily_report', 'status': status, 'cid': cid}
  print(body)
  r = requests.post(uri, data=jds(body), headers={'Content-Type': 'Application/json'})
  rtv = True if re.search('OK', r.text) else False
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

def find_delimiter(input_file, default_sep=',', encoding='utf8'):
  """Finds the delimiter used on a CSV file, based on detect_delimier.\n
  Currently it just analyses the headers row"""
  rtv = None  
  with open(input_file, 'r', encoding=encoding) as f:
    line = f.readline()
    rtv = detect(line, default=default_sep)
  return rtv

def test():
    return "holi"

#return a starting date provided a Customer's rules of how many day's back to look based on the day of the week
#if an exception is given, that will be used as the number of days to look back, regardless of the rules.
def dateHandler(customerRules, ruleException = None):
    currentDate = datetime.today()
    currentDay = currentDate.strftime('%A')
    if ruleException and isinstance(ruleException, int):
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

# Maybe it is a good idea to handle the cache in a class
def cache_dict(to_distribute):
  """Creates a cache dict for each element in a DICT.\n
  The values of those elements is expected to be a list and the return data is a list with 2 elements\n
   -index 0: current value of the cache, reseted to 0\n
   -index 1: length of the input list, to be used as the max current value of the cache during cycling\n
   Returns a DICT with the same input keys having its values as defined above"""
  cache = {}
  for item in to_distribute:
    cache[item] = [0, len(to_distribute[item])]
  return cache

def cycle_list(cache):
  # Ugly hardcode
  count, size = 0, 1
  cache[count] += 1
  if cache[count] >= cache[size]: cache[count] = 0

def external_update(addr:str, filt=None):
  """Does a GET query to the given address and returns the data if any with the type according to the header"""
  r = requests.get(addr.format(filt)) if filt else requests.get(addr)
  rtv = None
  if r.status_code == 200:
    rtv = r.json() if r.headers['content-type'] == 'application/json' else r.text
  return rtv

def get_configs(endpoint, cid):
  rtv = None
  if cid:
    r = requests.get(endpoint.format(cid))
    if r.status_code == 200:
      rtv = r.json()
      if rtv['status'] == 1: rtv = rtv['data']
      else:
        print(f'Customer with CVSC_ID {cid} not found')
        rtv = {}
  return rtv

def check_equals(rows, checks_file):
  customer_checks = yaml_parse(checks_file)
  fields_not_found = {}
  for rule in customer_checks:
    current_rule = customer_checks[rule]
    fields_not_found.update({current_rule['target']: {'values': [], 'rule': rule}})
    try:
      for row in rows:
        check_field = rows[row][current_rule['target']]
        if current_rule['mode'] == 'in':
          if check_field.strip() not in current_rule['data']: 
            fields_not_found[current_rule['target']]['values'] = [*fields_not_found[current_rule['target']]['values'], check_field]
    except:
      print_log(f"The column {current_rule['target']} from {rule} was not found on row", level=1)
  not_found = False
  for fields in fields_not_found:
    if len(fields_not_found[fields]['values']):
      fields_not_found[fields]['values'] = list(dict.fromkeys(fields_not_found[fields]['values']))
      not_found = True

  if not_found: return fields_not_found
  else: return {}

def write_local_files(filename, route, file_content, unicode=False):
  with open(os.path.join(route, filename), 'w+') as f:
    try:
      config_file = yaml_parse(f)
    except:
      config_file = dict()
    config_file.update(file_content)
    doc = dump(config_file, f, allow_unicode=unicode ,encoding='utf-8', sort_keys=False)

def update_settings(customer, endpoint, config_path, unicode=False):
  config_files =  get_configs(endpoint, customer.cvsc_id)
  new_files = []
  if config_files:
    print(f"INFO: Updating {customer.name} config files")
    for file, settings in config_files.items():
      filename, route, file_content = None,None,None
       #TODO: Make this code more generic and remove harcoded stuff ('assets', 'config')
      if(file == 'assets' and settings):
        print(f"INFO: Writing assets:")
        for asset, content in settings.items():
          filename = asset+'.yaml'
          route = customer.ASSETS_DIR
          print(f"      - {filename}")
          new_files.append(filename)
          write_local_files(filename, route, content, unicode)
      elif(file == 'configs' and settings):
        filename = file+'.yaml'
        route = config_path
        print(f"INFO: Writing {filename}")
        new_files.append(filename)
        write_local_files(filename, route, settings, unicode)
    print(f"INFO: Updating process completed sucessfully")
  else:
    print(f"WARNING: Customer settings not found, local files will be used instead")
  return new_files

def update_customer_data(endpoint, fields):
  if fields:
    post_data = {
      'cid': fields['cid'],
      'fields': fields['data'],
      'action': 'file_handler',
      'mode': fields['mode']
    }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    rtv = None
    r = requests.post(endpoint, data=json.dumps(post_data), headers=headers )
    if r.status_code == 200:
      rtv = 0
    else: rtv = 1
    return rtv

def post_run_status(endpoint, fields):
  rtv = None
  # supported_tools = ['csv_enabler, csv_merger', 'csv_translator', 'bbox_metrics', 'daily_report']
  # if fields['tool'] in supported_tools:
  headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  print('RUN: ', fields)
  r = requests.post(endpoint, data=json.dumps(fields), headers=headers)
  if r.status_code == 200:
    rtv = True
  return rtv

def upload_api(api_data, row, debug=False):
  rtv = False
  headers = {'Content-type': 'application/json'}
  try:
    r = requests.post(api_data['endpoint'], data=json.dumps(row), auth=(api_data['user'], api_data['password']),  headers=headers)
    #requests.post("https://bluebox.gonmalo.dev/api/test2", data=json.dumps(row), auth=(api_data['user'], api_data['password']),  headers=headers)
    if r.status_code == 200: rtv = True
  except Exception as e:
    print(e)

  return rtv

async def upload_api_v2(api_data, row, session, debug=False, **kwargs):
  rtv = False
  uri = "https://bluebox.gonmalo.dev/api_dev/test" if debug else api_data['endpoint']
  async with session.post(uri, json=row, auth=aiohttp.BasicAuth(api_data['user'], api_data['password'], encoding="utf8")) as response:
    r_text = await response.text()
    if response.status == 200: rtv = True
  return {'success': rtv, 'status_code': response.status, 'response_text': r_text, 'row': row}
