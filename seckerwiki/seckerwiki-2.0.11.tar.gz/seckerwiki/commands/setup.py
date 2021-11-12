"""
functions for setting up seckerwiki
"""
import os
import getpass
import pathlib

EXAMPLE_CONTENTS = """---
wiki-root: ~/path/to/wiki
encrypted-journal-path: Personal/Life/Journal/Encrypted
receipts-path: Personal/Life/Receipts
toc-excluded-dirs:
  - images
  - uploads
  - .git
  - venv
"""

AUTH_CONTENTS = """---
password: {0}
"""


def setup():
  """
  Create config file and auth file
  """
  auth_path = os.path.expanduser("~/.config/seckerwiki/credentials.yml")
  cfg_path = os.path.expanduser("~/.config/seckerwiki/config.yml")

  if os.path.exists(cfg_path):
    print(f"Error: seckerwiki config file already exists at {cfg_path}")
    return False

  if os.path.exists(auth_path):
    print(f"Error: seckerwiki auth file already exists at {auth_path}")
    return False

  # make directories
  # todo: now that using pathlib, can we simplify other stuff
  path = pathlib.Path(cfg_path)
  path.parent.mkdir(parents=True, exist_ok=True)
    
  with open(cfg_path, 'w') as f:
      f.write(EXAMPLE_CONTENTS)
  os.chmod(cfg_path,0o600)

  print(f"Configuration file written to {cfg_path}")

  journal_password = getpass.getpass(prompt="Enter journal passphrase: ")


  # create auth directory
  os.makedirs(os.path.dirname(auth_path), exist_ok=True)
    
  with open(auth_path, 'w') as f:
      f.write(AUTH_CONTENTS.format(journal_password))
  os.chmod(auth_path,0o600)

  print(f"Credentials file written to {auth_path}")