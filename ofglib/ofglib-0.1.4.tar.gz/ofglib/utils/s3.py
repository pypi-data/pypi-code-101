import boto3
import boto3.session
import io
import pickle


class S3_Connector():
    def __init__(self,
                 ACCESS_KEY: str = '',
                 SECRET_KEY: str = '',
                 BUCKET_NAME: str = ''):

        session = boto3.session.Session(
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY
        )
        self.s3 = session.client(
            service_name='s3',
            endpoint_url='https://storage.yandexcloud.net'
        )

        self.bucket = BUCKET_NAME

    def get_csv(self, file_name):

        # download file in memory
        file_stream = io.BytesIO()
        self.s3.download_fileobj(self.bucket, file_name, file_stream)
        file_stream.seek(0)

        return file_stream

    def get_model(self, model_name):

        # download file in memory
        file_stream = io.BytesIO()
        self.s3.download_fileobj(
            self.bucket,
            f"{model_name}.model",
            file_stream
        )
        file_stream.seek(0)

        return pickle.load(file_stream)

    def save_obj(self, model_name, file_stream, ext):

        try:
            file_stream.seek(0)
            self.s3.upload_fileobj(
                file_stream, self.bucket, f"{model_name}{ext}"
            )
            file_stream.close()
        except Exception:
            pass
        return 0
