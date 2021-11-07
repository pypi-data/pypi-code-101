from setuptools import setup
import pathlib


setup(name="gsk_geo_encryption",
      version="1.0",
      description="Geological Password Encryption",
      long_description="""# Note: Internet is mandatory for getting your current location

## Project Description

This program is to create a encryption password with a given Key and can get access when both the encryption  is at same location as 
   the password is created with the latitude and longitude
----------------------------------------------------------------
# Change the ipinfo API Token (if needed):

Code:
     <p>gsk_geo_encryption.TOKEN="API_TOKEN"</p>
----------------------------------------------------------------
## Getting the encrypted_password and timer with a class:


Code:
<p>object1=gsk_geo_encryption.Keys()<p>
password,seconds=object1.password_encrypted()

----------------------------------------------------------------
Classes: 
        <p> Keys
----------------------------------------------------------------
Inbuilt Functions(Unchangable):
<p>
                  geo_lat_long_convertor()
<p>
                  encryption()
<p></p>
----------------------------------------------------------------
<p>
Usable Functions(Changable):<p>
                            password_encrypter
<p>

---------------------------------------------------------------
Exceptions:
<p>
           ConnectionError


""",
      author="G S SRENATH KUMAR",
      long_description_content_type="text/markdown",
      packages=['gsk_geo_encryption'],
      include_package_data=True,
      install_requires=[],
      zip_safe=False
      )