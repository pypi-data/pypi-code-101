from setuptools import setup, find_packages

setup(

  name = 'cube_plugin_async_w_kafka',         # How you named your package folder (MyLib)
  packages = find_packages("."),
  include_package_data=True,
  version = '1.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Kafka service provider for Outbound traffic in asynchronous mode',   # Give a short description about your library
  author = 'Abdallah Ben Hamida',                   # Type in your name
  author_email = 'noemail@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/QuanticData',   # Provide either the link to your github or to your website
  #download_url = 'https://github.com/QuanticData/SchemaV/archive/refs/tags/v_01.tar.gz',    # I explain this later on
  keywords = ['dict', 'python', 'kafka'],   # Keywords that define your package best
  install_requires=[
      'confluent-kafka', #update this section with requirements file and include dependencies versions
      'schemav'

      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support

  ],
)

