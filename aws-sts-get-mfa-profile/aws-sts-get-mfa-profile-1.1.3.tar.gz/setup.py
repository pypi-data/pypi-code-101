from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='aws-sts-get-mfa-profile',
   version='1.1.3',
   description='A library to setup an AWS CLI profile for an account with MFA enabled',
   author='Inception Consulting Engineers',
   long_description=long_description,
   long_description_content_type="text/markdown",
   license='MIT',
   author_email='hello@inceptiongroup.com.au',
   url='https://github.com/Inception-Consulting-Engineers/aws-sts-get-mfa-profile',
   key_words="AWS,STS,MFA,SESSION,TOKEN",
   scripts=['./get-sts-token.py'],
   install_requires=['boto3', 'pytz']
)
