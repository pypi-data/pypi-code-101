import re
import os

import file_utils
from pattern_replacer import PatternReplace, Replace

temp_file_path = 'temp_file'


def replace_pattern_and_copy(pattern_replace: PatternReplace) -> bool:
    temp = open(temp_file_path, 'w', encoding='utf8')
    content = replace_pattern(pattern_replace)
    temp.write(content)
    temp.close()
    success = file_utils.backup_file_and_replace(temp_file_path, pattern_replace.path)
    file_utils.delete_file(temp_file_path)
    return success


def replace_pattern(pattern_replace: PatternReplace) -> str:
    content = None

    path = pattern_replace.path+".bak" if os.path.isfile(pattern_replace.path+".bak") else pattern_replace.path

    with open(path, 'r', encoding='utf8') as f:
        content = f.read()

    if not bool(content):
        print(f'empty file/ None object found for file {pattern_replace.path}')
        exit(1)

    new_content = content

    for replace in pattern_replace.replacer:
        new_content = get_replaced_string(new_content, replace=replace)
    return new_content


def get_replaced_string(content: str, replace: Replace) -> str:
    replace_all = replace.replace_all
    changed_contents = content
    change_count = 0

    if not replace_all:
        return re.sub(replace.replace_on, replace.replace_with, changed_contents)

    replaced_all_strings = False
    while not replaced_all_strings:
        new_content = re.sub(replace.replace_on, replace.replace_with, changed_contents)
        change_count = change_count + 1
        if changed_contents == new_content:
            replaced_all_strings = True
        changed_contents = new_content
    return changed_contents
