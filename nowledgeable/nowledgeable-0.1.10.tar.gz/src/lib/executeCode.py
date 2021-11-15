#! /usr/bin/python3
# -*- coding:utf-8 -*-

import re
import os
from os.path import join

import json
import signal
import shutil
import subprocess
from subprocess import *
from subprocess import Popen, PIPE, TimeoutExpired

from werkzeug.utils import secure_filename

def my_run(command, cwd, timeout):

    with Popen(command,
               cwd=cwd,
               shell=True, # needed for pyspark
               stderr=subprocess.STDOUT,
               stdout=PIPE,
               preexec_fn=os.setsid
        ) as process:

        try:
            stdout, stderr = process.communicate(timeout=timeout)

        except TimeoutExpired:
            os.killpg(process.pid, signal.SIGINT)  # send signal to the process group
            result = process.communicate()[0]

            stdout = result.decode() + "\n timeout error: your program took too long"
            return stdout

        except Exception as e:

            process.kill()
            process.wait()
            raise

        retcode = process.poll()

        if retcode:
            raise CalledProcessError(retcode, process.args,
                                     output=stdout.decode(), stderr=stderr)

        return stdout


def run_cmd(command, cwd, timeout=25):

    if isinstance(command, list):
        command = build_unix_commands(command)

    #todo : limit memory : https://gist.github.com/s3rvac/f97d6cbdfdb15c0a32e7e941f7f4a3fa

    try:
        result = my_run(command, cwd=cwd, timeout=timeout)

        try:
            if (not isinstance(result, str)):
                result = result.decode().rstrip()

        except UnicodeDecodeError as e:
            result = result.decode(encoding='ISO-8859-1') # pour gérer le c qui n'a pas le même encoding
            #mais peut être du à mauvais gestion des caractères en c

        #except AttributeError as e2:
        #    result = result
        error = ""

    except TimeoutExpired:
        # cf https://stackoverflow.com/questions/1191374/using-module-subprocess-with-timeout
        error = "timeout error"
        result = ""

    except subprocess.CalledProcessError as e:

        error = e.output
        result = ""


    return result, error




def run_exercice_code(cwd, commands_to_run, user_picture_folder):

    """
    run_exercice_file_code

    Starts  a process to run student answer
    the process should print the json to std after all prints.

    :param cwd:
    :param commands_to_run:
    :param user_picture_folder:
    :return: dict
    """
    import time
    t1 = time.time()
    output, err = run_cmd(commands_to_run, cwd=cwd)
    script_timing = time.time() - t1

    if not err:

        output = output.splitlines()
 
        try:
            if len(output) > 1:

                status = output[-1]
                prints = output[:-1]
                print_msg = "\n".join(prints)
                assesments = json.loads(status)
            else:
                assesments = json.loads(output[-1])
                print_msg = ""

        except:

            print_msg = "\n".join(output)            
            
            assesments = {
                'isRight': False
            }

        picture_data = get_output_pictures_as_base_64(user_picture_folder)

        return {
            'status': 0,
            'stdout': print_msg,
            'pictures': picture_data,
            'assesments': assesments,
            'timing': script_timing
        }

    else:

        return {
            'status': 1,
            'stderr': err,
            'assesments': {
                'isRight': False,
            },
            'scriptTiming': script_timing
        }





def build_unix_commands(commands_to_run):
    return " && ".join(commands_to_run)


def run_command_as_script(multi_line_command, cwd):

    try:

        result = subprocess.check_output(multi_line_command,
                                         shell=True,
                                         executable='/bin/bash',
                                         universal_newlines=True,
                                         stderr=subprocess.STDOUT, cwd=cwd)
        error = ""

    except subprocess.CalledProcessError as e:

        error = e
        result = e.output

    return result, error


def compare_command_ouputs(outputs):

    differences = []
    for i in range(0, len(outputs), 2):

        expected = outputs[i]
        submited = outputs[i+1]

        if not expected == submited:
            differences.append({
                "expected": expected,
                "submitted": submited,
                "arguments": []
            })

    return differences




def get_output_pictures_as_base_64(full_path):

    pictures = []
    for filename in os.listdir(full_path):
        pictures.append(get_image_as_base_64(full_path, filename))

    return pictures


def get_image_as_base_64(user_folder, filename):
    """
    load and convert an image to a base64 string

    :param user_folder:
    :param filename:
    :return:
    """
    picture = join(user_folder, filename)

    if not os.path.isfile(picture):
        return ""

    from base64 import b64encode
    with open(picture, 'rb') as f:
        content = f.read()

    base64_bytes = b64encode(content)

    # third: decode these bytes to text
    # result: string (in utf-8)
    str_img_64 = base64_bytes.decode('utf-8')

    os.remove(picture)

    return str_img_64


def remove_folder_content(path):

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def setup_user_folder(user_folder, picture_folder):

    picture_path = join(user_folder, picture_folder)
    if os.path.isdir(picture_path):

        shutil.rmtree(picture_path)
        #remove_folder_content(picture_path)

    os.makedirs(picture_path)



def run_file_code(user_folder, picture_folder, code_to_run, commands_to_run, cwd, command_runner=run_cmd, code_filename="checking_code"):

    file_to_run = join(user_folder, code_filename)

    with open(file_to_run, 'w') as f:
        f.writelines(code_to_run)

    output, err = command_runner(commands_to_run, cwd=cwd)

    if err:
        return {
            'print': err + "\n" + output,
            'status': 1,
            'pictures': get_output_pictures_as_base_64(user_folder, picture_folder),
        }

    return {
        'print': output,
        'status': 0,
        'pictures': get_output_pictures_as_base_64(user_folder, picture_folder),

    }

