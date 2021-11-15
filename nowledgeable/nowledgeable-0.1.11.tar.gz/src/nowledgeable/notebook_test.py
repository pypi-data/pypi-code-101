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


from .notebook_utils import *


def run_notebook_cells(student_nb_path):
    name =  os.path.basename(student_nb_path) 
    folder = os.path.dirname(student_nb_path)
    
    cmd = "jupyter nbconvert --to notebook --inplace --execute {}".format(name)
    p = subprocess.Popen([cmd], 
                        shell=True,
                        cwd=folder)
    p.communicate()

def test_notebook(reference_nb_path, student_nb_path, lang="en", mode="cell"):

    """
    Test a notebook by comparing that the submitted notebook output match a reference notebook. 
    """
    abs_student_path = abs_path(
        check_append_extension(student_nb_path, ["ipynb"]))

    if not os.path.isfile(abs_student_path):
         raise Exception(
            "Error: file '{}' does not exist.".format(abs_student_path))
       
    run_notebook_cells(abs_student_path) #in case he did not submit cells


    reference_nb, abs_reference_path = load_notebook(reference_nb_path)
    student_nb, abs_student_path = load_notebook(student_nb_path)

    student_cells, reference_cells = ([cell for cell in student_nb["cells"] if cell["cell_type"] == "code" and len(cell["outputs"]) > 0],
                                      [cell for cell in reference_nb["cells"] if cell["cell_type"] == "code" and len(cell["outputs"]) > 0])

    if len(student_cells) < len(reference_cells):
        student_cells = [cell for cell in student_nb["cells"]
                         if cell["cell_type"] == "code"][:len(reference_cells)]

        if len(student_cells) < len(reference_cells):
            raise Exception("Error: Student notebook ({}) has less code cells than reference notebook ({}).".format(
                abs_student_path, abs_reference_path))

    elif len(student_cells) > len(reference_cells):
        raise Exception("Error: Student notebook ({}) has more code cells with outputs than reference notebook ({}).".format(
            abs_student_path, abs_reference_path))

    tests = []

    available_modes = ["cell", "output"]
    
    if mode == "cell":
        for i, (cell, matching_cell) in enumerate(zip(student_cells, reference_cells)):
            tests.append({
                "isRight": compareOutputs(matching_cell["outputs"], cell["outputs"]),
                "name": "{}{}".format(cell_dict[lang], i+1),
            })

    elif mode == "output":
        for i, (cell, matching_cell) in enumerate(zip(student_cells, reference_cells)):
            ref_outputs, outputs = flattenOutputs(
                matching_cell["outputs"]), flattenOutputs(cell["outputs"])
            for j, ref_output in enumerate(ref_outputs):
                tests.append({
                    "isRight": findOutput(ref_output, outputs),
                    "name": "{}{}: {}{} ({})".format(cell_dict[lang], i+1, test_dict[lang], j+1, ref_output["type"]),
                })

    else:
        raise Exception("Unknown testNotebook mode {}. Available modes: {}".format(
            mode, available_modes))

    output = {
        "isRight": not any(not test["isRight"] for test in tests),
        "tests": tests
    }

  
    return output

