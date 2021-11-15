from distutils.core import setup

setup(
  name = 'IndexNow',         # How you named your package folder (MyLib)
  packages = ['IndexNow'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'TYPE YOUR DESCRIPTION HERE',   # Give a short description about your library
  author = 'Ajit Jasrotia',                   # Type in your name
  author_email = 'ajitjasrotia012@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/ajitjasrotia/indexnow',
  download_url = 'https://github.com/ajitjasrotia/indexnow/archive/v_01.tar.gz',
  keywords = ['index', 'indexnow'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
