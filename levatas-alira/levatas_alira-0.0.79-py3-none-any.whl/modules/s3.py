from genericpath import isfile
import boto3
import uuid
import logging
import os

from pathlib import Path

from alira.instance import Instance
from alira.modules.redis import RedisModule, ServiceException

from botocore.exceptions import ClientError, EndpointConnectionError

PIPELINE_MODULE_NAME = "alira.modules.s3"


def aws_s3_upload(
    aws_s3_bucket,
    aws_s3_public,
    s3_key,
    filename,
    aws_access_key,
    aws_secret_key,
    aws_region_name,
):
    logging.info(
        f'Uploading {filename} to bucket "{aws_s3_bucket}" and location {s3_key}...'
    )

    try:
        with open(filename, "rb") as file:
            buffer = file.read()
    except FileNotFoundError as e:
        logging.exception(f"There was an error loading the file {filename}")
        return None

    try:
        session = boto3.Session(
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=aws_region_name,
        )
        client = session.client("s3")

        arguments = {"Bucket": aws_s3_bucket, "Key": s3_key, "Body": buffer}

        extension = Path(filename).suffix.lower()
        content_type = "binary/octet-stream"
        if extension in [".jpg", ".jpeg"]:
            content_type = "image/jpeg"
        elif extension == ".png":
            content_type = "image/png"

        arguments["ContentType"] = content_type

        if aws_s3_public:
            arguments["ACL"] = "public-read"

        client.put_object(**arguments)

        s3_location = f"s3://{aws_s3_bucket}/{s3_key}"
        logging.info(f"Uploaded {filename} to {s3_location}")

        return s3_location

    except EndpointConnectionError as e:
        logging.exception(e)
        raise ServiceException(e) from e
    except ClientError as e:
        logging.exception(e)
    except Exception as e:
        logging.exception(e)

    return None


class S3(RedisModule):
    def __init__(
        self,
        model_identifier: str,
        configuration_directory: str,
        aws_s3_bucket: str,
        aws_s3_key_prefix: str,
        aws_s3_public: bool,
        module_id: str = None,
        aws_access_key: str = None,
        aws_secret_key: str = None,
        aws_region_name: str = None,
        autogenerate_name: bool = False,
        redis_server: str = None,
        filtering: str = None,
        file: str = None,
        aws_s3_upload_function: callable = aws_s3_upload,
        **kwargs,
    ):
        super().__init__(
            module_id=module_id or PIPELINE_MODULE_NAME,
            model_identifier=model_identifier,
            configuration_directory=configuration_directory,
            redis_server=redis_server,
        )

        self.aws_access_key = aws_access_key or os.environ.get(
            "ALIRA_AWS_ACCESS_KEY_ID", None
        )
        self.aws_secret_key = aws_secret_key or os.environ.get(
            "ALIRA_AWS_SECRET_ACCESS_KEY", None
        )
        self.aws_region_name = aws_region_name or os.environ.get(
            "ALIRA_AWS_REGION_NAME", None
        )

        self.filtering = self._load_function(filtering)
        self.aws_s3_bucket = aws_s3_bucket
        self.aws_s3_key_prefix = aws_s3_key_prefix

        self.autogenerate_name = autogenerate_name

        if self.aws_s3_key_prefix and self.aws_s3_key_prefix.endswith("/"):
            self.aws_s3_key_prefix = self.aws_s3_key_prefix[:-1]

        self.aws_s3_public = aws_s3_public

        self.file = file
        self.aws_s3_upload_function = aws_s3_upload_function

    def run(self, instance: Instance, **kwargs):
        if self.filtering and not self.filtering(instance):
            logging.info(
                f"The instance didn't pass the filtering criteria. Instance: {instance}"
            )
            return {"status": "SKIPPED"}

        if self.file:
            filename = instance.get_attribute(self.file, default=instance.image)
        else:
            filename = instance.image

        if self.autogenerate_name:
            _, file_extension = os.path.splitext(filename)
            s3_key = f"{uuid.uuid4().hex}{file_extension}"
        else:
            s3_key = os.path.basename(filename)

        if self.aws_s3_key_prefix:
            s3_key = f"{self.aws_s3_key_prefix}/{s3_key}"

        filename = os.path.join(self.configuration_directory, "images", filename)

        if not os.path.isfile(filename):
            logging.info(f"The file {filename} does not exist")
            return {
                "status": "FAILURE",
                "message": f"The file {filename} does not exist",
            }

        arguments = {
            "aws_s3_bucket": self.aws_s3_bucket,
            "aws_s3_public": self.aws_s3_public,
            "s3_key": s3_key,
            "filename": filename,
            "aws_access_key": self.aws_access_key,
            "aws_secret_key": self.aws_secret_key,
            "aws_region_name": self.aws_region_name,
        }

        try:
            queue = self.get_redis_queue()
            if queue:
                queue.enqueue(self.aws_s3_upload_function, **arguments)
            else:
                self.aws_s3_upload_function(**arguments)

            result = {
                "status": "SUCCESS",
                "s3_file_url": f"s3://{self.aws_s3_bucket}/{s3_key}",
            }

            if self.aws_s3_public:
                result[
                    "s3_file_public_url"
                ] = f"https://{self.aws_s3_bucket}.s3.amazonaws.com/{s3_key}"

            return result

        except Exception as e:
            logging.exception("There was an error uploading the image")
            return {
                "status": "FAILURE",
                "message": f"Error uploading the image",
            }
