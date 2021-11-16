"""
Copyright 2020 Odd Gunnar Aspaas

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import argparse
from lazylicense.utils.file_scanner import get_files
from lazylicense.utils.read_write import (
    read_file, get_comments, 
    file_contains_license, 
    write_license_to_file
)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--extension')
    parser.add_argument('-f', '--folder')
    parser.add_argument('-a', '--author')
    parser.add_argument('-y', '--year')
    args = parser.parse_args()
    arguments_dict = vars(args)
    extension = arguments_dict["extension"]
    folder = arguments_dict["folder"]
    author = arguments_dict["author"]
    year = arguments_dict["year"]
    files = get_files(extension=extension, folder=folder)
    for current_file in files:
        current_doc = read_file(current_file)
        comments = get_comments(current_doc)
        if not file_contains_license(comments=comments):
            write_license_to_file(file=current_file, author=author, year=year)
            print(f"Added license to {current_file}.")
        else:
            print(f"Possible license already exist in {current_file}.")

if __name__ == '__main__':
    main()
