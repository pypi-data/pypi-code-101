from distutils.core import setup
setup(
  name='load-shedding',
  packages=['load-shedding'],
  version='0.0.1',
  license='MIT',
  description='A python library for getting Load Shedding schedules from Eskom.',
  author='Werner Pieterson',
  author_email='wernerhp@gmail.com',
  url='https://gitlab.com/wernerhp/load-shedding',
  keywords=['eskom', 'loadshedding', 'south africa'],
  install_requires=[
          'beautifulsoup4',
          'certifi',
          'urllib3',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Programming Language :: Python :: 3.9',
  ],
)
