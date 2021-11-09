import os
import base64


class Helpers:

    @classmethod
    def base64_encode_file(cls, file):
        with open(file, 'rb') as f:
            return base64.b64encode(f.read())

    @classmethod
    def traverse_supporting_files_directory(cls, directory):
        return_dict = {}
        return_list = []
        for dirpath, dirnames, files in os.walk(directory):
            if files:
                for file in files:
                    if file.endswith('.yaml') or file.endswith('.md'):
                        continue
                    if '/' in dirpath:
                        full_path = f"{dirpath}/{file}"
                    else:
                        full_path = f"{dirpath}\{file}"
                    return_list.append(full_path)
                   # return_dict[full_path] = cls.base64_encode_file(full_path)
        return return_list

    @classmethod
    def get_supporting_files(cls, file):
        if os.path.exists(file):
            # if value is a directory then get each file
            if os.path.isdir(file):
                return cls.traverse_supporting_files_directory(file)
            elif os.path.isfile(file):
                return {file: cls.base64_encode_file(file)}
        return {}
