from distutils.core import setup
import site
import sys
site.ENABLE_USER_SITE = "--user" in sys.argv[1:]
import setuptools



with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
      name='nowledgeable',
      version='0.1.11',
      description='Auto checker',
      author = "Laurent CETINSOY",
      author_email =  "laurent.cetinsoy+pypi@nowledgeable.com" ,
      url='https://www.python.org/sigs/distutils-sig/',
      long_description = long_description,
      long_description_content_type = "text/markdown",
      classifiers=[
        'License :: OSI Approved :: GNU Affero General Public License v3'
      ],
      package_dir={"": "src"},
      packages= ['nowledgeable', 'lib'],

      install_requires=['pandas', 'pyyaml', 'matplotlib', 'werkzeug' 'numpy', 'requests', 'scipy', 'watchdog'],
      entry_points={
        'console_scripts': ['nowledgeable=nowledgeable.main:main']
      }
)
