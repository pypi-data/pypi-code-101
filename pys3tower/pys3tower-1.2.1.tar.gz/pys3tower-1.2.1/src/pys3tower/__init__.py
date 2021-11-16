import boto3
import hashlib
import json
import os
import time
import uuid


class PyS3:
    def __init__(self, path, bucket, accesskey, secretkey, region, key = ""):
        self.path = path
        self.bucket = bucket
        self.key = key
        self.client = boto3.client("s3",
                                  aws_access_key_id=accesskey,
                                  aws_secret_access_key=secretkey,
                                  region_name=region)

        self.s3_keys = {}
        self.op_keys = {}

        self.file_to_send = []
        self.file_to_delete = []
        self.file_to_ignore = []

        self.analyse = {}
        self.current = {}

    def run(self):
        bg_time = time.time()

        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}
            os.system("touch data.json")

        print("[*] - Start the research in S3")
        self._get_all_s3_objects()
        self.current["s3_time"] = time.time() - bg_time

        print("[*] - Start the research on premise")
        self._get_all_op_objects()
        self.current["op_time"] = time.time() - bg_time

        print("[*] - Sort of the files")
        self._select_files()
        self.current["sort_time"] = time.time() - bg_time

        print(f"[*] - {len(self.file_to_send)} files to send\n",
              f"[*] - {len(self.file_to_delete)} files to delete\n",
              "[*] - Send the files")
        self.send_files()
        self.current["send_time"] = time.time() - bg_time
        self.current["files_to_send"] = len(self.file_to_send)
        self.current["files_to_delete"] = len(self.file_to_delete)
        self.current["files_to_ignore"] = len(self.file_to_ignore)

        with open("data.json", "w") as f:
            self.analyse[str(uuid.uuid4())] = self.current
            data.update(self.analyse)
            json.dump(data, f, indent=4)

    def __calculate_s3_etag(self, file_path, chunk_size=8 * 1024 * 1024):
        md5s = []

        with open(file_path, 'rb') as fp:
            while True:
                data = fp.read(chunk_size)
                if not data:
                    break
                md5s.append(hashlib.md5(data))

        if len(md5s) < 1:
            return '"{}"'.format(hashlib.md5().hexdigest())

        if len(md5s) == 1:
            return '"{}"'.format(md5s[0].hexdigest())

        digests = b''.join(m.digest() for m in md5s)
        digests_md5 = hashlib.md5(digests)
        return '"{}-{}"'.format(digests_md5.hexdigest(), len(md5s))

    def _get_all_s3_objects(self,):
        if self.key == "":
            kwargs = {'Bucket': self.bucket}
        else:
            kwargs = {'Bucket': self.bucket, 'Prefix': self.key}

        while True:
            resp = self.client.list_objects_v2(**kwargs)
            try:
                resp["Contents"]
            except:
                break

            for obj in resp['Contents']:
                key = obj['Key']
                self.s3_keys[key] = obj["ETag"].replace('"', "")

            try:
                kwargs['ContinuationToken'] = resp['NextContinuationToken']
            except KeyError:
                break

    def _get_all_op_objects(self):
        folders = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(self.path)) for f in fn]

        for i in folders:
            etag = self.__calculate_s3_etag(i)
            self.op_keys[i.replace("\\", "/").replace(self.path.replace("\\", "/"), "")[1:]] = etag.replace('"', '')

    def _select_files(self):
        transit_ls = []

        for obj in self.s3_keys.items():
            value = self.op_keys.get(obj[0])
            if value == None:
                self.file_to_delete.append(obj[0])
            else:
                transit_ls.append(obj)

        for obj in self.op_keys.items():
            try :
                idx = transit_ls.index(obj)
            except:
                self.file_to_send.append(obj[0])
                continue

            if transit_ls[idx][1] == obj[1]:
                self.file_to_ignore.append(obj[0])
            else:
                self.file_to_send.append(obj[0])

    def send_files(self):
        for file in self.file_to_delete:
            print(f"[x] - File {file} has been deleted from S3")
            self.client.delete_object(Bucket=self.bucket, Key=file)

        for file in self.file_to_send:
            if self.path in file:
                path = file
                print(f"[+] - File {path} has been uploaded")
                self.client.upload_file(path, self.bucket, path.replace(self.path + "/", ""))
            else:
                path = self.path + f"/{file}"
                print(f"[+] - File {path} has been uploaded")
                self.client.upload_file(path, self.bucket, path.replace(self.path+ "/", ""))


if __name__ == "__main__":
    s3 = PyS3(path="xxx", bucket="xxx", key="xxx", accesskey="xxx", secretkey="xxx", region="xxx")
    s3.run()
