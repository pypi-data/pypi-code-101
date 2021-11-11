import boto3
from botocore.exceptions import ClientError
import sys
import pytz
from pathlib import Path

credential_file_path = str(Path.home())+'\\.aws\\credentials'

with open(credential_file_path, 'r') as file:
    credentials = file.read().split('\n')

AWS_ACCESS_KEY_ID = credentials[1].split(' = ')[1]
AWS_SECRET_ACCESS_KEY = credentials[2].split(' = ')[1]
AWS_MFA_SERIAL = credentials[3].split(' = ')[1]

try:
    SESSION_DURATION = int(input("How many seconds do you want the token to last for? [Default = 3600]: ") or 3600)
except ValueError:
    print('Please retry using only integers in seconds.')
    sys.exit(1)


ONE_TIME_PASSWORD = input("Please enter your 6 digit one time password: ")

if len(str(ONE_TIME_PASSWORD)) != 6:
    print('Invalid one time password.')
    sys.exit(1)

sts_client = boto3.client('sts')

token_response = sts_client.get_session_token(
    DurationSeconds=SESSION_DURATION,
    SerialNumber=AWS_MFA_SERIAL,
    TokenCode=str(ONE_TIME_PASSWORD)
)

token_credentials = token_response['Credentials']
expiry = token_credentials['Expiration'].astimezone(pytz.timezone('Australia/Adelaide'))
print('Token will expire at', expiry)

try:
    find_mfa = credentials.index('[mfa]')
    credentials[find_mfa+1] = f"aws_access_key_id = {token_credentials['AccessKeyId']}"
    credentials[find_mfa+2] = f"aws_secret_access_key = {token_credentials['SecretAccessKey']}"
    credentials[find_mfa+3] = f"aws_session_token = {token_credentials['SessionToken']}"
    credentials[find_mfa+4]  = f"Expiry = {expiry}"
except ValueError:
    credentials.append('')
    credentials.append('[mfa]')
    credentials.append(f"aws_access_key_id = {token_credentials['AccessKeyId']}")
    credentials.append(f"aws_secret_access_key = {token_credentials['SecretAccessKey']}")
    credentials.append(f"aws_session_token = {token_credentials['SessionToken']}")
    credentials.append(f"Expiry = {expiry}")

with open(credential_file_path, 'w') as file:
    file.write('\n'.join(credentials))