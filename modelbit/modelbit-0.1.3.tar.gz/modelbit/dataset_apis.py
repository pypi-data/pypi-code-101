def _dsFilepath(self, dsId):
  import tempfile, os
  mbTempDir = os.path.join(tempfile.gettempdir(), 'modelbit')
  if not os.path.exists(mbTempDir):
    os.makedirs(mbTempDir)
  return os.path.join(mbTempDir, dsId)

def _storeDatasetResultIfMissing(self, dsName, dsId, url):
  import urllib.request, os
  filepath = self._dsFilepath(dsId)
  if os.path.exists(filepath):
    return
  self._print_mk(f'_Downloading "{dsName}"..._')
  urllib.request.urlretrieve(url, filepath)

def _decryptFile(self, dsId, key64, iv64):
  from Crypto.Cipher import AES
  from Crypto.Util.Padding import unpad
  import os, base64
  filepath = self._dsFilepath(dsId)
  if not os.path.exists(filepath):
    self._print_mk(f'**Error:** Couldn\'t find local data at {filepath}')

  cipher = AES.new(base64.b64decode(key64), AES.MODE_CBC, iv=base64.b64decode(iv64))

  fileIn = open(filepath, 'rb')
  raw = fileIn.read()
  fileIn.close()
  return(unpad(cipher.decrypt(raw), AES.block_size))

def print_datasets(self):
  import timeago, datetime
  data = self._call_api_or_print_error(f'datasets/list')
  if not data: return
      
  formatStr = "| Name | Data Refreshed | SQL Updated |\n" + \
    "|:-|-:|-:|\n"
  for d in data['datasets']:
    dataTimeVal = ''
    sqlTimeVal = ''
    if 'recentResultMs' in d and d["recentResultMs"] != None:
      dataTimeVal = timeago.format(datetime.datetime.fromtimestamp(d["recentResultMs"]/1000), datetime.datetime.now())
    if 'sqlModifiedAtMs' in d and d["sqlModifiedAtMs"] != None:
      sqlTimeVal = timeago.format(datetime.datetime.fromtimestamp(d["sqlModifiedAtMs"]/1000), datetime.datetime.now())
    formatStr += f'| <pre>{ d["name"] }</pre> | { dataTimeVal } | { sqlTimeVal } |\n'
  self._print_mk(formatStr)

def get_dataset_df(self, ds_name):
  from urllib.parse import quote_plus
  import csv, io, pandas
  data = self._call_api_or_print_error(f'datasets/get?dsName={quote_plus(ds_name)}')
  if not data: return

  self._storeDatasetResultIfMissing(ds_name, data['id'], data['signedDataUrl'])
  rawDecryptedData = self._decryptFile(data['id'], data['key64'], data['iv64'])

  stStream = io.StringIO(rawDecryptedData.decode('utf-8'))
  df = pandas.read_csv(stStream, sep='|')
  df.drop(0, inplace=True) # remove column types
  return df
