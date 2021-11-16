__version__ = "0.1.2"
__author__ = 'Modelbit'

class __Modelbit:
  from .dataset_apis import print_datasets, get_dataset_df, _storeDatasetResultIfMissing, _dsFilepath, _decryptFile

  _API_HOST = 'https://app.modelbit.com/'
  _LOGIN_HOST = _API_HOST
  _API_URL = None
  _state = {}
    
  def __init__(self):
    import threading, os
    if os.getenv('MB_JUPYTER_API_HOST'):
      self._API_HOST = os.getenv('MB_JUPYTER_API_HOST')
    if os.getenv('MB_JUPYTER_LOGIN_HOST'):
      self._LOGIN_HOST = os.getenv('MB_JUPYTER_LOGIN_HOST')
    self._API_URL = f'{self._API_HOST}api/jupyter/'

    self._state = self._state
    self._check_token_thread = threading.Thread(target=self._check_token_polling)

  def _is_authenticated(self):
    return 'user_email' in self._state

  def _get_json(self, path):
    from urllib import request, parse
    import json
    try:
      data = {}
      if "jwt" in self._state:
        data = { "token": self._state["jwt"] }
      with request.urlopen(f'{self._API_URL}{path}', parse.urlencode(data).encode()) as url:
          return json.loads(url.read().decode())
    except BaseException as err:
      return {"error": f'Unable to reach Modelbit. ({err})'}

  def _print_mk(self, str):
    from IPython.display import display, Markdown
    display(Markdown(str))

  def _login(self):
    if self._is_authenticated():
      connectedTag = '<span style="color:green; font-weight: bold;">connected</span>'
      self._print_mk(f'You\'re {connectedTag} to Modelbit as {self._state["user_email"]}.')
      return

    if 'uuid' not in self._state:
      data = self._get_json('get_token')
      self._state['uuid'] = data['uuid']
      self._state['jwt'] = data['jwt']

    displayUrl = 'modelbit.com/t/' + self._state["uuid"]
    linkUrl = f'{self._LOGIN_HOST}/t/{self._state["uuid"]}'
    aTag = f'<a style="text-decoration:none;" href="{linkUrl}" target="_blank">{displayUrl}</a>'
    helpTag = '<a style="text-decoration:none;" href="/" target="_blank">Learn more.</a>'
    self._print_mk('**Connect to Modelbit**<br/>' +
      f'Open {aTag} to authenticate this kernel, then re-run this cell. {helpTag}')
    if not self._check_token_thread.is_alive():
      self._check_token_thread.start()

  def _check_token(self):
    data = self._get_json(f'check_token')
    if 'user_email' in data:
      self._state['user_email'] = data['user_email']

  def _check_token_polling(self):
    from time import sleep
    error_count = 0
    while not self._is_authenticated():
      try:
        self._check_token()
      except:
        error_count += 1
      sleep(3)

  def _call_api_or_print_error(self, path):
    data = self._get_json(path)
    if 'error' in data and data['error'] == 'jwt expired':
      if 'uuid' in self._state: del self._state['uuid']
      if 'user_email' in self._state: del self._state['user_email']
      data['error'] = 'Your modelbit session has expired. Re-run `mb = modelbit.login()` to re-authenticate.'

    if 'error' in data:
      self._print_mk(f'**Error:** {data["error"]}')
      return False
    return data

def login():
  _modelbit = __Modelbit()
  _modelbit._login()
  return _modelbit

