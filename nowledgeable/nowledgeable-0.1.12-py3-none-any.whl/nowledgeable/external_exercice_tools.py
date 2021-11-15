import os
import sys
import yaml
import time

import errno
import uuid
import json
import base64
import mimetypes
import io
import re
import ctypes
import locale

import subprocess

from PIL import Image
from PIL import ImageChops
from PIL import ImageStat

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from .PythonRunner import OneFilePythonRunner
from .notebook_test import test_notebook

correct_file_extensions = [
    ".py", ".ipynb"
]

import requests

def send_answer_status(url, exercice_data, assesments):

    payload = {

        "studentId": exercice_data['studentId'],
        "orderedContentId": exercice_data['orderedContentId'],
        #answer: answer,
        "assesments": assesments['assesments']
        
    }

    r = requests.post(url, json=payload)
    
    if (r.status_code != 200):
        print("could not save answer status to nowledeable")
    

def check_notebook(yaml_path, exercice_data):

    path = os.path.join(os.getcwd(), os.path.dirname(yaml_path), 'exercice.ipynb')
    
    with open(path, 'r') as f:
        student_notebook = f.read()
    
    url = exercice_data['submissionUrl']
    
    payload = {
        "studentId": exercice_data['studentId'],
        "orderedContentId": exercice_data['orderedContentId'],
        "studentNotebook": student_notebook 
    }

    r = requests.post(url, json=payload)
    
    if (r.status_code != 200):
        print("Unable to submit notebook")
        print(r.text)
        exit(1)
        
    return output.json()

def run_checks(yaml_path):

    """ 
    loads a yaml exercice path and make run the exercice corrections
    depending on the exercice type 

    Todo : hash check
    """

    exercice_data = load_yaml(yaml_path)
    exercice_type = exercice_data['type']
    if exercice_type == "InputOutputExercice" :
        from nowledgeable import CommandTester
        
        output = CommandTester().run_output_tests(exercice_data)

    elif exercice_type == "JupyterNotebookExercice":
        output = check_notebook(yaml_path, exercice_data)

    elif exercice_type == "OneFileExercice":
        output = check_exercice(yaml_path, exercice_data)
    else:
        raise "exercice not supported"


    send_output = True
    pretty_print_output(output)

    if send_output:
        url = exercice_data['submissionUrl']       
        send_answer_status(url, exercice_data, output)

    return output

def watch_test(yaml_path):

    exercice_params = load_yaml(yaml_path)

    base_path = os.path.dirname(yaml_path)
    student_filename = exercice_params['studentFile']

    abs_submission_path = os.path.join(base_path, exercice_params['testMainFile'])
    student_file_path   = os.path.join(base_path, student_filename) 
    event_handler = ModifiedFileHandlerTester(student_filename, yaml_path, 500)

    observer = Observer()
    observer.schedule(event_handler, path=student_file_path, recursive=False)

    try:
        observer.start()
    except OSError as e:
        print("Error: File '{}' does not exist. Make sure you have not deleted the default exercice file or create a new file '{}'".format(
            abs_submission_path, student_file_path))
        print(e)
        exit(1)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()


def load_yaml(yaml_path):
   
    """# Relative to nowledgeable.py
    abs_yaml_path = os.path.join(os.path.dirname(__file__), yaml_path)"""

    # Relative to CWD
    abs_yaml_path = os.path.join(os.getcwd(), yaml_path)

    try:
        yaml_file = open(abs_yaml_path)
    except IOError as e:
        print("Error: Exercice YAML ({}) doesn't exist.".format(abs_yaml_path))
        print(e)
        exit(1)

    try:
        params = yaml.load(yaml_file, Loader=yaml.Loader)
    except yaml.YAMLError as e:
        print("Error: Exercice YAML ({}) is wrongly formatted.".format(abs_yaml_path))
        print(e)
        exit(1)

    yaml_file.close()

    yaml_param_check(abs_yaml_path, params, "studentId")
    yaml_param_check(abs_yaml_path, params, "exerciceId")
    yaml_param_check(abs_yaml_path, params, "type")

   
    check_hash(params) #todo


    
    return params


class ModifiedFileHandlerTester(FileSystemEventHandler):

    def __init__(self, filename, yaml_path, min_interval):
        super().__init__()
        self.filename = filename
        self.yaml_path = yaml_path
        self.min_interval = min_interval
        self.last_event = self.current_milli_time()

    def current_milli_time(self):
        return round(time.time() * 1000)

    def on_modified(self, event):

        event_time = self.current_milli_time()

        delta_time = event_time - self.last_event
        if not event.is_directory and event.src_path.endswith(self.filename) and delta_time > self.min_interval:
            print("{} ms".format(delta_time))
            self.last_event = event_time
            run_checks(self.yaml_path)
     



def pretty_print_output(output):

    if output['status'] != 0:
        print(output['stderr'])
        return

    assesments = output['assesments']
    is_right = assesments['isRight']
    print("")
    print("--- Exercies checks ---")
    print("")
    print( "Exercice is right ! " if assesments['isRight'] else "wrong")
    print("")
    if not is_right:
        for i, assesment in enumerate(assesments['tests']):
            print("--- Test n° {} : {} ---".format(i+1, assesment['name']))
            
            print("ok" if assesment['isRight'] else "ko")

def get_answer(path):
    
    with open(path, 'r') as f:
        lines = f.readlines()

    return lines

def check_exercice(yaml_path, exercice_data):
    
    runner = get_runner(exercice_data)

    output = runner.run_external_check(yaml_path, exercice_data)
    #pretty_print_output(output)
    return output

    

def get_language():

    if os.name != 'posix':
        windll = ctypes.windll.kernel32
        lang = locale.windows_locale[windll.GetUserDefaultUILanguage()]
    else:
        lang = os.environ['LANG']

    return lang

def abs_path(path):
    return path if os.path.isabs(path) else os.path.join(os.getcwd(), path)


def invalid_metadata_error(abs_submission_path, submission_path):

    print("""Error: File '{}' does not exist. 
            Make sure you have not deleted the default 
            exercice file or create a new file '{}'""".format(
            abs_submission_path, submission_path))
    print(e)
    exit(1)

def get_runner(exercice_data):

    return OneFilePythonRunner()

def yaml_param_check(abs_yaml_path, all_params, param):
        if param not in all_params:
            raise Exception(
                "Error: '{}' is not defined in YAML exercice settings file! ({})".format(param, abs_yaml_path))
        return True


def check_hash(params):
    print('todo')
    if False:
        raise Exception('do not modify internal files, you cheater')
