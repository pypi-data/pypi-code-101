
import boto3
from boto3 import session
from botocore.client import Config
from boto3.s3.transfer import S3Transfer

from proai.constants import DO_ACCESS_ID, DO_SECRET_KEY

# Initiate session
session = session.Session()
client = session.client('s3',
                        region_name='sgp1',  # enter your own region_name
                        endpoint_url='https://sgp1.digitaloceanspaces.com',  # enter your own endpoint url

                        aws_access_key_id=DO_ACCESS_ID,
                        aws_secret_access_key=DO_SECRET_KEY)

transfer = S3Transfer(client)

# Uploads a file called 'name-of-file' to your Space called 'name-of-space'
# Creates a new-folder and the file's final name is defined as 'name-of-file'
transfer.upload_file('name-of-file', 'name-of-space', 'new-folder' + "/" + 'new-name-of-file')

# This makes the file you are have specifically uploaded public by default.
response = client.put_object_acl(ACL='public-read', Bucket='name-of-space', Key="%s/%s" % ('new-folder', 'new-name-of-file'))
view raw.py hosted with ❤ by GitHub
