from distutils.core import setup
setup(
  name = 'pip_for_cmd',         # How you named your package folder (MyLib)
  packages = ['pip_for_cmd'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Here, you can use pip in python codes and in the cmd!',   # Give a short description about your library
  author = 'Omer Yelin',                   # Type in your name
  author_email = 'pipforcmd@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/PipForCMD/PIP_for_CMD',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/PipForCMD/PIP_for_CMD/archive/refs/tags/v1.0.tar.gz',    # I explain this later on
  keywords = ['pip', 'cmd', 'python'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'os',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)