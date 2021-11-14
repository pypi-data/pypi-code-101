from setuptools import setup, find_packages

package = 'jdl'
version = '0.1'

setup(name=package,
      version=version,
      description="json data logger",
      url='https://github.com/hash-p-3/json-data-logger',
      packages=find_packages(),
      install_requires=[
          'appdirs',
          'flask',
          'jinja2',
          'requests',
        ],
      zip_safe=False,
      entry_points={
        #'console_scripts': ['jdl=jdl.__main__:main']
        },
      include_package_data=True,
      package_data={
          #'jdl': ['jdl/templates/*.jdt']
      }
)
