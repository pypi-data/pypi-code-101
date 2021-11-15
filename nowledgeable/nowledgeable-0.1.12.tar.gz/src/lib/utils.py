import os
import re
import functools

from os.path import join
from werkzeug.utils import secure_filename



@functools.lru_cache(maxsize=None)
def read_file_content(path):

    with open(path, 'r') as f:
        code = "".join(f.readlines())

    return code

def get_code_folder():

    current_script_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_script_path, '..', 'tmp', 'code')

def get_user_folder(user_id):

    code_folder = get_code_folder()
    user_folder = join(code_folder, str(user_id))

    return user_folder


def setup_links_to_datasets(user_folder, paths):

    for link_to_build in paths:

        path = link_to_build['path']
        filename = link_to_build['filename']

        source = os.path.join(os.getcwd(), path, filename)
        link = os.path.join(user_folder, filename)

        if not os.path.islink(link) and not os.path.isfile(link):
            os.symlink(source, link)



def save_data_files(user_folder, data_files):

    paths = [
        save_sent_data_files(data_file, user_folder) for data_file in data_files
    ]

    return paths


def save_sent_data_files(data_file, user_folder, filename="data"):

    if isinstance(data_file, (str,)):
        return join(user_folder, data_file)

    filename = secure_filename(data_file.filename)
    full_path = join(user_folder, filename)
    data_file.save(full_path)

    return full_path
    

def get_forbidden_expressions(code_to_analyse, forbidden_expressions):

    default_lists = [
        "solution_checking",
        "rm"
    ]

    listeInterdits = default_lists + forbidden_expressions
    
    found = []
    
    for e in listeInterdits:
        
        if re.search(r'\b' + e + r'\b', code_to_analyse):
            found.append(e)
    
    return found


def code_has_forbiden_expression(codeToClean, forbidden_expressions):

    """
       doit renvoyer True dans le cas où une expression interdite
       est fait partie d'un nom de fonction définie dans l'exercice

        plusiueurs solution : ajouter une white list
        avoir un match exact

    :param codeToClean:
    :param forbidden_expressions:
    :return:
    """


    default_lists = [
        "solution_checking",
    ]
    listeInterdits = default_lists + forbidden_expressions
    
    for e in listeInterdits:
        
        if re.search(r'\b' + e + r'\b', codeToClean):
            return True
    return False

