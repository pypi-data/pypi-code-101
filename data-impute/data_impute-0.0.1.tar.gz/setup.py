from distutils.core import setup
setup(
  name = 'data_impute',
  packages = ['data_impute'],
  version = '0.0.1',
  license='MIT',
  description = 'Data_impute is a data imputataion library which imputes the missing data in the dataframe.',
  author = 'Vijeth Moudgalya',
  author_email = 'vijethmoudgalya.conatact@gmail.com',
  #url = 'https://github.com/vijethmoudgalya/Flipkart-Scrapper',
  #download_url = 'https://github.com/sourangshupal/pyarithcalc/releases/download/0.5/pyarithcalc-0.5.tar.gz',
  keywords = ['Data_Cleaning','EDA','Data_preprocessing','utils'],
  install_requires=[
          'pandas',
          'numpy',
          'matplotlib',
          'seaborn',
          'scikit-learn',
          
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ]
)
