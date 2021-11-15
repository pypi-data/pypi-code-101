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

from .PythonRunner import OneFilePythonRunner
from lib.custom_parser import create_custom_parser


def abs_path(path):
    return path if os.path.isabs(path) else os.path.join(os.getcwd(), path)





expected_dict = {
    "fr": "Sortie(s) attendues:",
    "en": "Expected output(s):"
}

cell_dict = {
    "fr": "Test unitaire - Cellule n°",
    "en": "Unit Test - Cell "
}

test_dict = {
    "fr": "Sortie n°",
    "en": "Output "
}


student_prefix = "student_"
image_prefix = "image_"
files_folder = "notebook_files"



image_mime = {
    "image/bmp": "bmp",
    "image/cis-cod": "cod",
    "image/gif": "gif",
    "image/ief": "ief",
    "image/jpeg": "jpg",
    "image/png": "png",
    "image/pipeg": "jfif",
    "image/svg+xml": "svg",
    "image/tiff": "tiff",
    "image/x-cmu-raster": "ras",
    "image/x-cmx": "cmx",
    "image/x-icon": "ico",
    "image/x-portable-anymap": "pnm",
    "image/x-portable-bitmap": "pbm",
    "image/x-portable-graymap": "pgm",
    "image/x-portable-pixmap": "ppm",
    "image/x-rgb": "rgb",
    "image/x-xbitmap": "xbm",
    "image/x-xpixmap": "xpm",
    "image/x-xwindowdump": "xwd"
}


def prepare_notebook(teacher_path, student_path="", lang="en"):

    teacher_notebook, abs_teacher_path = load_notebook(teacher_path)
   
    if not student_path:
        student_path = os.path.join(os.path.dirname(abs_teacher_path), 
            student_prefix + os.path.basename(abs_teacher_path))
    else:
        student_path = abs_path(student_path)

 
    # If any cell has a key containing "image" in any of its outputs' "data" field, then there are images in the notebook (that need to be extracted in the files folder)
    if any(map(lambda cell: (("image" in "".join(output["data"].keys())) if "data" in output else False for output in cell["outputs"]) if "outputs" in cell else False, teacher_notebook["cells"])):
        files_path = os.path.join(
            os.path.dirname(student_path), files_folder)

        if os.path.isdir(files_path):
            import shutil
            shutil.rmtree(files_path)

        else:
            try:
                os.mkdir(files_path)
            except OSError as e:
                print("Error: OSError when creating files folder at '{}'\n({})".format(
                    files_path, os.strerror(e.errno).capitalize()))
                print(e)
                exit(1)

    image_id = 0
    student_cells = []
    curr_guidelines = []
    desired_outputs = []

    for cell in teacher_notebook["cells"]:

        if cell["cell_type"] in ("raw", "markdown"):
            curr_guidelines.append("".join(cell["source"]))

        elif cell["cell_type"] == "code":
            image_id = process_code_cell(
                            cell, 
                            curr_guidelines, 
                            desired_outputs, 
                            student_cells, 
                            image_id, 
                            lang,
                            files_path
                            )

        # All cells have been processed
        student_notebook = teacher_notebook
        del teacher_notebook["cells"]
        student_notebook["cells"] = student_cells

    try:
        student_file = open(student_path, "w+")
        student_file.write(json.dumps(student_notebook))
        student_file.close()

    except IOError as e:
        print("Error: Unexcepted IOError on file {}.".format(student_path))
        print(e)
        exit(1)


def process_code_cell(cell, curr_guidelines, desired_outputs, student_cells, image_id, lang, files_path):

    outputs = cell["outputs"]
       
    for output in outputs:
        if output["output_type"] == "stream":
            desired_outputs.append("".join(output["text"]))

        elif output["output_type"] in ("execute_result", "display_data"):
            for data in output["data"]:
                if data.startswith("text"):
                    desired_outputs.append(
                        "".join(output["data"][data]))

                elif data.startswith("image"):
                    image_name = "{}{}.{}".format(image_prefix, str(
                        image_id), image_mime.get(data, data.split("/")[-1]))
                    image_path = os.path.join(
                        files_path, image_name)

                    image = output["data"][data]
                    """if image.endswith("\n"):
                        image = image[:-1]"""

                    try:
                        image_file = open(image_path, "wb+")
                        image_file.write(base64.b64decode(image))
                        image_file.close()

                    except IOError as e:
                        print(
                            "Error: Image file '{}' could not be created.".format(image_path))
                        print(e)
                        exit(1)

                    desired_outputs.append('\n```\n![image]({})\n```\n'.format(
                        os.path.join(files_folder, image_name)))

                    image_id += 1

                elif data.startswith("application"):
                    desired_outputs.append(
                        str(output["data"][data]))

        # All outputs of the current code cell have been processed
        student_cells.append(create_cell("md", source="\n".join(
            curr_guidelines + ["\n" + expected_dict[lang] + "\n\n```"] + desired_outputs + ["```"])))
        # metadata={"desired_outputs": desired_outputs}))
        student_cells.append(create_cell("code", ))
        curr_guidelines = []
        desired_outputs = []
        return image_id

def escape_markdown(text):
    parse = re.sub(r"([_*\[\]()~`>\#\+\-=|\.!])", r"\\\1", text)
    reparse = re.sub(r"\\\\([_*\[\]()~`>\#\+\-=|\.!])", r"\1", parse)
    return reparse


def process_outputs(outputs):  # TODO: add options
    return outputs


def process_source(source):  # TODO: add special cases and different kinds of source
    if type(source) == str:
        source_split = source.split("\n")
        source = [s + "\n" for s in source_split[:-1]]
        if source_split[-1] != "":
            source.append(source_split[-1])

    elif type(source) == dict:
        pass

    elif type(source) == list:
        pass

    return source


def prepare_notebook_submission():
    try:
        student_notebook = json.loads(student_file.read())
    except json.JSONDecodeError as e:
        print("Error: File '{}' is not a correctly formatted Jupyter/IPython notebook.").format(abs_submission_path)
        print(e)
        exit(1)

    if "cells" not in student_notebook or not student_notebook["cells"]:
        print("Error: Cells are empty, do not exist or are wrongly formatted in notebook '{}'".format(
            abs_submission_path))
        exit(1)

    student_submission = "\n".join(list(map(lambda cell: "".join(
        cell["source"]) if cell["cell_type"] == "code" else "", student_notebook["cells"])))



def check_append_extension(path, correct_extensions, default_extension=None, err_msg=None):
    if default_extension == None:
        default_extension = correct_extensions[0]

    if '.' not in os.path.basename(path):
        path = "{}.{}".format(path, default_extension)

    if any(path.endswith(ext) for ext in correct_extensions):
        return path

    else:
        print("Error: Unknown file extension.\n'Correct extensions: {}".format(
            ", ".join(correct_extensions)) if not err_msg else err_msg)
        exit(1)

def find_next(list_, cond_func, curr_idx):
    for i, val in enumerate(list_[curr_idx:]):
        if cond_func(val):
            return val, curr_idx+i

    return None


def load_notebook(path, check_path=True):
    if check_path:
        path = abs_path(check_append_extension(path, ["ipynb"]))

    try:
        notebook_file = open(path)
    except IOError as e:
        print("Error: File '{}' could not be opened on path '{}'.".format(
            os.path.basename(path), path))
        print(e)
        exit(1)

    try:
        notebook_contents = json.loads(notebook_file.read())
        notebook_file.close()
    except json.JSONDecodeError as e:
        print(
            "Error: File '{}' is not a correctly formatted Jupyter/IPython notebook.".format(path))
        print(e)
        exit(1)

    if "cells" not in notebook_contents or not notebook_contents["cells"]:
        print(
            "Error: Cells are empty, do not exist or are wrongly formatted in notebook '{}'".format(path))
        exit(1)

    return notebook_contents, path




def create_cell(cell_type, **kwargs):
    available_cell_types = ["code", "raw", "markdown", "md", "text"]
    null = None  # json.dumps convert None to null
    if cell_type == available_cell_types[0]:
        return {
            "cell_type": "code",
            "execution_count": (kwargs["execution_count"] if type(kwargs["execution_count"]) == int else int(kwargs["execution_count"])) if "execution_count" in kwargs else null,
            "metadata": (kwargs["metadata"] if type(kwargs["metadata"]) == dict else dict(kwargs["metadata"])) if "metadata" in kwargs else {},
            "outputs": process_outputs(kwargs.get("outputs", [])),
            "source": process_source(kwargs.get("source", [])),
        }

    elif cell_type == available_cell_types[1]:
        return {
            "cell_type": "raw",
            "id": kwargs.get("id", str(uuid.uuid4())[:8]),
            "metadata": (kwargs["metadata"] if type(kwargs["metadata"]) == dict else dict(kwargs["metadata"])) if "metadata" in kwargs else {},
            "source": process_source(kwargs.get("source", []))
        }

    elif cell_type in available_cell_types[2:]:
        return {
            "cell_type": "markdown",
            "metadata": kwargs.get("metadata", {}),
            "source": process_source(kwargs.get("source", []))
        }

    else:
        raise Exception("Error: Unknown cell type '{}' in function 'create_cell'.\nAvailable cell types: {}".format(
            cell_type, ", ".join(available_cell_types)))




# List of types that cannot be converted to an image by PIL
non_pil_image_type = ["image/svg+xml"]


def processOutput(output_type, output_value):
    if output_type.startswith("text") or output_type == "stream":
        output_value = filter(lambda x: x.strip() != "",
                              ("".join(output_value)).split("\n"))
        return [{"type": "text/plain", "output": re.sub(
            # Remove addresses from outputs
            # Strip each output
            r"<([\w.]*) at 0x[0-9a-z]*>", r"<\1>", output.strip()
        )} for output in output_value]

    elif output_type.startswith("image"):
        if output_type not in non_pil_image_type:
            return [{"type": output_type, "output": output_value, "image": Image.open(
                io.BytesIO(base64.b64decode(output_value))).convert('RGB')}]
        else:
            return [{"type": output_type, "output": output_value}]

    elif output_type.startswith("application"):
        return [{"type": output_type, "output": str(output_value)}]

    else:  # Default output
        return [{"type": output_type, "output": output_value}]


def flattenOutputs(outputs):
    new_outputs = []
    for output in outputs:
        if output["output_type"] == "stream":
            new_outputs.extend(processOutput(
                output["output_type"], output["text"]))

        elif output["output_type"] in ("execute_result", "display_data"):
            for data in output["data"]:
                new_outputs.extend(processOutput(data, output["data"][data]))

    return new_outputs


def findOutput(ref_output, possible_outputs, del_found=True):
    if "image" in ref_output:
        for i, output in enumerate(possible_outputs):
            if "image" in output:
                diff = ImageChops.difference(
                    ref_output["image"], output["image"])
                stat = ImageStat.Stat(diff)
                diff_ratio = sum(stat.mean) / (len(stat.mean) * 255)
                if diff_ratio < 0.01:  # 1% difference threshold for image comparison
                    if del_found:
                        del possible_outputs[i]

                    return True

        return False

    else:
        if ref_output in possible_outputs:
            if del_found:
                del possible_outputs[possible_outputs.index(ref_output)]

            return True
        else:
            return False


def compareOutputs(ref_outputs, outputs):  # Order of arguments matters
    ref_outputs, outputs = flattenOutputs(ref_outputs), flattenOutputs(outputs)
    for ref_output in ref_outputs:
        if not findOutput(ref_output, outputs):
            return False

    return True
