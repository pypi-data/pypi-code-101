# -*- coding: utf-8 -*-
from datetime import datetime
from functools import reduce
import warnings
import os
import sys
import json
import string
import logging
import logging.handlers as handlers
from datetime import datetime
from functools import reduce
from subprocess import Popen, PIPE
try:
    import requests
    from requests.adapters import HTTPAdapter
    from requests.sessions import Session
    from requests.adapters import Retry
except ImportError:
    warnings.warn("Please install 'requests'. 'pip install requests'")
    sys.exit(1)

import re



import re
import json
import string

pattern = re.compile(r"""(?P<propertyName>(?=^)\w[\s\w,]+)(?(1):)(?:\s|\n)?(?P<propertyData>[\W\w\s]+)""", re.MULTILINE)
f_pattern = re.compile(r"""(?P<propertyName>(?=^)\w[\s\w,]+)(?(1):)""", re.MULTILINE)


def to_iso(data):
    if isinstance(data, str):
        data = str.join("", list([x for x in data if x in string.printable]))
        return data.strip()
    elif isinstance(data, bytes):
        data = data.decode('utf-8', errors='ignore').strip()
        data = str.join("", list([x for x in data if x in string.printable]))
        return data.strip()
    elif isinstance(data, dict):
        for key in data:
            data[key] = to_iso(data[key])
        return data
    elif isinstance(data, list):
        new_list = []
        for item in data:
            new_list.append(to_iso(item))
        return new_list
    else:
        return data

def execute(commandLine):
    commandLine = commandLine  # + login_details
    logging.debug("CMD: '{}'".format(commandLine))
    process = Popen(commandLine, shell=True, stdout=PIPE, stderr=PIPE)
    out = process.stdout.read().decode('utf-8', errors='ignore').strip()
    out = str.join("", list([x for x in out if x in string.printable]))
    logging.debug("CMD: '{}' RESULT: {}".format(commandLine, out))
    error = process.stderr.read().decode('utf-8', errors='ignore').strip()
    error = str.join("", list([x for x in error if x in string.printable]))
    if error and not out:
        process.kill()
        logging.error("CMD: '{}' IF ERR OUT {}".format(commandLine, out))
        logging.error("CMD: '{}' {}".format(commandLine, error))
        raise Exception(error)
    return out


def detect_endline(text):
    if text.find("\r\n") != -1:
        return "\r\n"
    if text.find("\r") != -1:
        return "\r\r"
    if text.find("\n\n") != -1:
        return "\n\n"
    return ""

def get_last_branch_changeSet(branch, numberOfChangets):
    # output = execute(MoveToMainDirectory + TF_Branches_History.format(branch) + (
    #     "" if numberOfChangets == None else " /stopafter:{}".format(numberOfChangets)))
    commandLine = "cat ./mock-output-new.txt"
    output = execute(commandLine)

    endline_char = detect_endline(output)

    changeSetList = []

    # output = output.replace("\r", "")
    output_list = [item.lstrip() for item in output.split("-" * 79 + endline_char) if item]

    idx = 0

    for changeset_raw in output_list:
        changeSetDict = {}
        itemsDict = {}

        changeSetDict['branch'] = 'branch'
        changeSetDict['items'] = itemsDict

        changeset_info_items = list()

        propertyNames = f_pattern.findall(changeset_raw)
        for item in propertyNames:
            cur_idx = propertyNames.index(item)
            next_idx = propertyNames.index(item) + 1
            if next_idx <= len(propertyNames) - 1:
                itm = changeset_raw[
                      changeset_raw.find(propertyNames[cur_idx])
                      :changeset_raw.find(propertyNames[next_idx])]
            else:
                itm = changeset_raw[
                      changeset_raw.find(propertyNames[cur_idx]):]
            changeset_info_items.append(itm)

        # changeset_info_items = changeset_raw.split(endline_char + endline_char)
        changeset_items = list()

        for changeset_info_item in changeset_info_items:
            if any(changeset_info_item.startswith(keyword) for keyword in ['Changeset', 'User', 'Date']):
                changeset_info_item = changeset_info_item.split(endline_char)
                changeset_items.extend(changeset_info_item)
            else:
                changeset_info_item = changeset_info_item.replace(endline_char, '\n')
                changeset_items.append(changeset_info_item)

        idx += 1
        for changeset_item in changeset_items:

            for item in pattern.finditer(changeset_item):
                propertyName, propertyData = item.groups()
                propertyName = propertyName.lstrip().rstrip().replace(' ', '_').lower()
                propertyData = propertyData.lstrip().rstrip()

                changeSetDict[propertyName] = propertyData

                if propertyName == 'items':
                    for i in propertyData.split('\n'):
                        i = i.lstrip().rstrip()
                        action = i[:i.find("$/")]
                        filename = i[i.find("$/"):]

                        action = action.lstrip().rstrip()
                        filename = filename.lstrip().rstrip()

                        if ',' in action:
                            actions = action.split(', ')
                            if all(s in actions for s in ('delete', 'source rename')):
                                action = 'delete'
                            if all(s in actions for s in ('delete', 'rollback')):
                                action = 'delete'
                            elif all(s in actions for s in ('encoding', 'edit')):
                                action = 'edit'
                            elif all(s in actions for s in ('merge', 'edit')):
                                action = 'edit'
                            elif all(s in actions for s in ('edit', 'rollback')):
                                action = 'edit'
                            elif all(s in actions for s in ('rename', 'edit')):
                                action = 'rename'
                            elif all(s in actions for s in ('add', 'source rename')):
                                action = 'add'

                        if action not in itemsDict:
                            itemsDict[action] = [filename, ]
                        else:
                            itemsDict[action].append(filename)

                    for item in itemsDict:
                        itemsDict[item] = list(set(itemsDict[item]))

                    changeSetDict['items'] = itemsDict

        changeSetList.append(changeSetDict)

    return changeSetList




def wrap_changeset_push_event(arr, rest_api_data, file_tree=None, isBlameRequired=True, shouldRunRestApi=False):
    length = len(arr)

    commits = []
    for changeSet in arr:
        files = []

        items = changeSet.get('items', {})
        # print(changeSet)
        changesetId = changeSet.get('changeset')
        if changesetId is None:
            value = changeSet.get('edit')
            if value is not None:
                # Changeset:
                # length of above string is 11
                changesetId = value[11:]
            else:
                raise Exception("changesetId is not set")

        date = changeSet.get('date', datetime.now().strftime("%A, %B %d, %Y %I:%M:%S %p"))

        for key in items:
            if ',' in key:
                keys = key.split(",")
                if all(s in keys for s in ('delete', 'source rename')):
                    key = 'delete'
                else:
                    raise Exception("Handle multiple keys")

            status = ''

            if key == "edit":
                status = "modified"
            elif key == "add" or key == "branch":
                status = "added"
            elif key == "delete":
                status = "deleted"
            elif key == "rename":
                status = "renamed"

            if isinstance(items[key], (list, tuple)):
                for file_item in items[key]:
                    splittedFiles = file_item.split(";")
                    splittedFile = splittedFiles[0]
                    fileName = splittedFile[splittedFile.rfind("/") + 1:]

                    blame = ''
                    if isBlameRequired and "." in fileName and status == 'modified':
                        blame = ""

                    files.append({
                        'status': status,
                        'deletions': 0,
                        'previous_filename': '',
                        'patch': '',
                        'blame': blame,
                        'sha': changesetId,
                        'additions': 0,
                        'filename': file_item,
                        'changes': 0
                    })

            elif isinstance(items[key], str):
                splittedFiles = items[key].split(";")

                splittedFile = splittedFiles[0]
                fileName = splittedFile[splittedFile.rfind("/") + 1:]

                blame = ''
                if isBlameRequired and "." in fileName and status == 'modified':
                    blame = ""
                files.append({
                    'status': status,
                    'deletions': 0,
                    'previous_filename': '',
                    'patch': '',
                    'blame': blame,
                    'sha': changesetId,
                    'additions': 0,
                    'filename': items[key],
                    'changes': 0
                })

        added = [x for x in files if 'add' in x['status']]
        modified = [x for x in files if 'edit' in x['status']]
        removed = [x for x in files if 'delete' in x['status']]
        renamed = [x for x in files if 'rename' in x['status']]
        try:
            datetime_object = datetime.strptime(
                date, "%A, %B %d, %Y %I:%M:%S %p")
            date = datetime_object.strftime("%Y-%m-%dT%H:%M:%S")
        except ValueError:
            datetime_object = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            date = datetime_object.strftime("%Y-%m-%dT%H:%M:%S")
        else:
            date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

        commit = {
            'files': files,
            'added': added,
            'stats': {
                'deletions': 0,
                'files': len(files),
                'additions': 0,
                'total': 0,
                'changes': 0
            },
            'modified': modified,
            'tree': '',
            'sha': changesetId,
            'parents': [],
            'date': date,
            'branches': [changeSet['branch']],
            'message': changeSet.get('comment'),
            'removed': removed,
            'renamed': renamed
        }

        user = changeSet.get('user', 'unknown user')
        commit['author'] = {
            'date': date,
            'name': user,
        }
        commit['committer'] = {
            'date': date,
            'name': user
        }

        commits.append(commit)

    commits.sort(key=lambda x: x['sha'])

    skipFirst = True
    for index, value in (enumerate(commits)):
        if skipFirst:
            skipFirst = False
            continue

        copy = commits[index - 1].copy()
        copy.pop('parents')
        value['parents'] = [copy]

        for file in value['files']:
            if 'edit' in file['status']:
                file['patch'] = ""

                if '@@' in file['patch']:
                    patches = file['patch'].split('\n')
                    startParse = False

                    for patch in patches:
                        if startParse:
                            if '-' in patch:
                                file['deletions'] += len(patch[1:])

                            if '+' in patch:
                                file['additions'] += len(patch[1:])

                            if '===================================================================' in patch:
                                break

                        if '@@' in patch:
                            startParse = True

                    file['changes'] = sum(file['deletions'] for file in value['files']) + sum(
                        file['additions'] for file in value['files'])

        value['stats']['deletions'] = reduce(
            lambda x, y: x+y['deletions'], value['files'], 0)
        value['stats']['additions'] = reduce(
            lambda x, y: x+y['additions'], value['files'], 0)
        value['stats']['changes'] = value['stats']['deletions'] + \
            value['stats']['additions']
        value['stats']['total'] = value['stats']['changes']

    data = {
        'size': length,
        'commits': commits,
        'head_commit': commits[length - 1],
        'file_tree': file_tree,
        'repository': {
            'name': "REPOSITORY",
            'full_name': '{}/{}'.format("USERNAME", "REPOSITORY")
        },
        'ref_type': 'commit',
        'after': "",
        'ref': '',
        'base_ref': '',
        'before': commits[length - 1]['sha']
    }

    data = to_iso(data)
    return json.dumps(data)
    # return data


data = wrap_changeset_push_event(get_last_branch_changeSet('branch', numberOfChangets=None), rest_api_data=False)

print('Finish')
