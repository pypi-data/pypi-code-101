"""
Exercice entrypoint. 

run-checks (runChecks): Runs unit tests on student file (requires a config file exercice.yml to be in the same folder).
watch (watchTest): Watch changes to run tests every time the student file is modified (requires a config file exercice.yml to be in the same folder).
prepare-nb (prepareNotebook): Converts a teacher notebook to a student notebook that can be filled in.
test-nb (testNotebook): Test a student notebook against a teacher notebook.

See exercice.yml format at https://nowledgeable.com/todo
"""

import sys
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

from lib.custom_parser import create_custom_parser
from nowledgeable.external_exercice_tools import run_checks

from nowledgeable.notebook_utils import *
from nowledgeable.notebook_test import test_notebook

VERSION = 1.0


available_langs = ["en", "fr"]

texts = {
    "main_description": {
        "fr": "Accédez aux commandes Nowledgeable de testing python en local sur votre machine via nowledgeable.py",
        "en": "Use commands of the Nowledgeable Python testing suite on your local machine via nowledgeable.py"
    },

    "command": {
        "fr": "commande",
        "en": "command"
    },

    "command_desc": {
        "fr": "Commande à lancer",
        "en": "Command to run"
    },

    "command_list": {
        "fr": "Les commandes actuellement disponibles sont :",
        "en": "Available commands:"
    },

    "arguments": {
        "fr": "Arguments de la sous-commande",
        "en": "Subcommand arguments"
    },

    "yaml_path": {
        "fr": "Chemin de la configuration de l'exercice (YAML)",
        "en": "Path of the configuration file of the exercice (YAML)"
    },

    "teacher_path": {
        "fr": "Chemin du notebook de référence",
        "en": "Path of reference teacher notebook"
    },

    "student_path": {
        "fr": "Chemin du notebook étudiant",
        "en": "Path of student notebook"
    },

    "lang": {
        "fr": "Langue des énoncés",
        "en": "Guidelines language"
    },

    "mode_desc": {
        "fr": "Mode de testing de notebook",
        "en": "Notebook testing mode"
    },

    "mode_list": {
        "fr": "Liste des modes disponibles :",
        "en": "List of available modes:"
    },
}

modes = {
    "cell": {
        "fr": "Teste le notebook cellule-par-cellule",
        "en": "Tests the notebook cell-by-cell"
    },

    "output": {
        "fr": "Teste le notebook output-par-output (une cellule peut avoir plusieurs outputs)",
        "en": "Tests the notebook output-by-output (a cell can have multiple outputs)"
    }
}


RUN_CHECK_COMMAND = "run-checks"
WATCH_COMMAND     = "watch"
PREPARE_NOTEBOOK_CMD = "prepare-notebook"
TEST_NOTEBOOK_CMD = "test-notebook"

available_commands = {
    RUN_CHECK_COMMAND: {
        "en": "Runs unit tests on a .py file (depending on a YAML config)",
        "fr": "Lance des tests unitaires sur un fichier (dépend d'une config YAML)"
    },

    WATCH_COMMAND: {
        "en": "Runs unit tests on a .py file each time it is modified (as long as the program keeps running, depending on a YAML config)",
        "fr": "Lance des tests unitaires à chaque fois qu'un fichier .py est modifié tant que le programme tourne (dépend d'une config YAML)"
    },

    PREPARE_NOTEBOOK_CMD: {
        "en": "Prepares a .ipynb exercice notebook from a reference notebook",
        "fr": "Prépare un notebook (.ipynb) d'exercices à partir d'un notebook de référence"
    },

    TEST_NOTEBOOK_CMD: {
        "en": "Runs comparison tests between an exercice notebook and a reference notebook",
        "fr": "Lance les tests de comparaisons entre un notebook d'exercice et son notebook de référence"
        }
}

commands = list(available_commands.keys())

longest_str_cmd = max(map(len, commands))
longest_str_mode = max(map(len, modes.keys()))


def main():

    parser, lang = create_custom_parser(
        texts, 
        "python3 nowledgeable.py", "Nowledgeable Standalone Tester v.{}".format(VERSION))
    
    command_description = texts["command_desc"][lang]
    
    command_list_txt = texts["command_list"][lang]
    
    command_helps = ["  {:<{length}}  {}".format( command_list_txt, cmd[lang], length=longest_str_cmd) for cmd in available_commands.values()]
    
    command_helps = "\n".join(command_helps)

    help_data = '''{}
    
{}

{}

'''.format(command_description, available_commands, command_helps)

    parser.add_argument('command', help=help_data)

    parser.add_argument('args', nargs='?', help=texts["arguments"][lang])

    default_exercice_yaml = "exercice.yaml"

    try:
        args = parser.parse_args(sys.argv[1:2])
    except:
        parser.print_help()
        exit(1)

    if not args.command in commands:
        print('Error: Unrecognized command\n')
        parser.print_help()
        exit(1)

    if args.command == RUN_CHECK_COMMAND:
        command = RUN_CHECK_COMMAND

        command_parser, lang = create_custom_parser({
                "main_description": available_commands[command]
            }, 
            "python3 nowledgeable.py {}".format(command), 
            "Nowledgeable Standalone Tester v.{}".format(VERSION)
        )
        
        command_parser.add_argument(
            'yaml_path', 
            nargs='?', 
            help=texts["yaml_path"][lang],
            default=default_exercice_yaml
        )

        command_args = command_parser.parse_args(sys.argv[2:])
        yaml_path = command_args.yaml_path
        
        run_checks(yaml_path)

    elif args.command == WATCH_COMMAND:

        command = WATCH_COMMAND

        command_parser, lang = create_custom_parser({
            "main_description": available_commands[command]
        }, "python3 nowledgeable.py {}".format(command), "Nowledgeable Standalone Tester v.{}".format(VERSION))
        command_parser.add_argument(
            'yaml_path', 
            nargs='?',
            help=texts["yaml_path"][lang], 
            default=default_exercice_yaml)

        command_args = command_parser.parse_args(sys.argv[2:])
        yaml_path = command_args.yaml_path
        watch_test(yaml_path)

    elif args.command == commands[2]:
        command_parser, lang = create_custom_parser({
            "main_description": available_commands[commands[2]]
        }, "python3 nowledgeable.py {}".format(commands[2]), "Nowledgeable Standalone Tester v.{}".format(VERSION))
        command_parser.add_argument(
            'teacher_path', nargs=1, help=texts["teacher_path"][lang])
        command_parser.add_argument(
            'student_path', nargs='?', help=texts["student_path"][lang], default="")
        command_parser.add_argument(
            'lang', nargs='?', help=texts["lang"][lang], default=lang)

        command_args = command_parser.parse_args(sys.argv[2:])

        prepare_notebook(command_args.teacher_path[0],
                        command_args.student_path, command_args.lang)

    elif args.command == TEST_NOTEBOOK_CMD:
        command_parser, lang = create_custom_parser({
            "main_description": available_commands[commands[3]]
        }, "python3 nowledgeable.py {}".format(commands[3]), "Nowledgeable Standalone Tester v.{}".format(VERSION))
        command_parser.add_argument(
            'teacher_path', nargs=1, help=texts["teacher_path"][lang])
        command_parser.add_argument(
            'student_path', nargs=1, help=texts["student_path"][lang])
        command_parser.add_argument(
            'lang', nargs='?', help=texts["lang"][lang], default=lang)
        command_parser.add_argument('mode', nargs='?', help='''{}
    
{}

{}

'''.format(texts["mode_desc"][lang], texts["mode_list"][lang],
           "\n".join(["  {:<{length}}  {}".format(m, modes[m][lang],
                                                  length=longest_str_mode) for m in modes]), default=lang))

        command_args = command_parser.parse_args(sys.argv[2:])
        test_notebook(command_args.teacher_path[0],
                     command_args.student_path[0], command_args.lang)


if __name__ == "__main__":
    main()
    
