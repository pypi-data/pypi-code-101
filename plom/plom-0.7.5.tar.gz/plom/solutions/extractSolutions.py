# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2021 Andrew Rechnitzer

import os
from pathlib import Path
import shutil
import tempfile

from PIL import Image
import toml

from plom.messenger import ManagerMessenger
from plom.plom_exceptions import PlomExistingLoginException
from plom.scan.scansToImages import processFileToBitmaps
from plom.specVerifier import checkSolutionSpec

source_path = Path("sourceVersions")
solution_path = Path("solutionImages")


def getSpec(server, password):
    if server and ":" in server:
        s, p = server.split(":")
        msgr = ManagerMessenger(s, port=p)
    else:
        msgr = ManagerMessenger(server)
    msgr.start()

    try:
        msgr.requestAndSaveToken("manager", password)
    except PlomExistingLoginException:
        print(
            "You appear to be already logged in!\n\n"
            "  * Perhaps a previous session crashed?\n"
            "  * Do you have another script running,\n"
            "    e.g., on another computer?\n\n"
            'In order to force-logout the existing authorisation run "plom-solutions clear"'
        )
        raise

    try:
        spec = msgr.get_spec()
    finally:
        msgr.closeUser()
        msgr.stop()

    return spec


def check_solution_files_present(numberOfVersions):
    print(f"Looking for solution files in directory '{source_path}'")
    for v in range(1, numberOfVersions + 1):
        filename = source_path / f"solutions{v}.pdf"
        print(f"Checking file {filename}")
        if not filename.is_file():
            return (False, f"Missing solution for version {v}")
    return (True, "All solution files present")


def glueImages(image_list, destination):
    # https://stackoverflow.com/questions/30227466/combine-several-images-horizontally-with-python
    images = [Image.open(img) for img in image_list]
    widths, heights = zip(*(img.size for img in images))
    total_width = sum(widths)
    max_height = max(heights)
    new_image = Image.new("RGB", (total_width, max_height))
    x_offset = 0
    for img in images:
        new_image.paste(img, (x_offset, 0))
        x_offset += img.size[0]

    new_image.save(destination)


def createSolutionSpec(testSpec):
    soln = {}
    soln["numberOfVersions"] = testSpec["numberOfVersions"]
    soln["numberOfPages"] = testSpec["numberOfPages"]
    soln["numberOfQuestions"] = testSpec["numberOfQuestions"]
    soln["solution"] = {}
    for q in range(1, testSpec["numberOfQuestions"] + 1):
        soln["solution"][str(q)] = {"pages": testSpec["question"][str(q)]["pages"]}
    return soln


def saveSolutionSpec(solutionSpec):
    with open("solutionSpec.toml", "w") as fh:
        toml.dump(solutionSpec, fh)


def loadSolutionSpec(spec_filename):
    with open(spec_filename, "r") as fh:
        solutionSpec = toml.load(fh)
    return solutionSpec


def extractSolutionImages(server, password, solution_spec_filename=None):
    testSpec = getSpec(server, password)

    if solution_spec_filename is None:
        solutionSpec = createSolutionSpec(testSpec)
        saveSolutionSpec(solutionSpec)
    elif Path(solution_spec_filename).is_file() is False:
        print(f"Cannot find file {solution_spec_filename}")
        return False
    else:
        solutionSpec = loadSolutionSpec(solution_spec_filename)

    valid, msg = checkSolutionSpec(testSpec, solutionSpec)
    if valid:
        print("Valid solution specification - continuing.")
    else:
        print(f"Error in solution specification = {msg}")
        return False

    success, msg = check_solution_files_present(solutionSpec["numberOfVersions"])
    if success:
        print(msg)
    else:
        print(msg)
        return False

    # create a tempdir for working
    tmpdir = Path(tempfile.mkdtemp(prefix="tmp_images_", dir=os.getcwd()))
    print(f"temp dir is {tmpdir}")

    # split sources pdf into page images
    for v in range(1, testSpec["numberOfVersions"] + 1):
        # TODO: Issue #1744: this function returns the filenames...
        processFileToBitmaps(source_path / f"solutions{v}.pdf", tmpdir)

    # time to combine things and save in solution_path
    solution_path.mkdir(exist_ok=True)
    for q in range(1, testSpec["numberOfQuestions"] + 1):
        sq = str(q)
        mxv = testSpec["numberOfVersions"]
        if testSpec["question"][sq]["select"] == "fix":
            mxv = 1  # only do version 1 if 'fix'
        for v in range(1, mxv + 1):
            print(f"Processing solutions for Q{q} V{v}")
            # TODO: Issue #1744: need proper fix coordinating with filenames
            #       from processFileToBitmaps
            if solutionSpec["numberOfPages"] >= 100:
                raise NotImplementedError("Need proper fix for #1744")
            if solutionSpec["numberOfPages"] >= 10:
                # 10 quite likely off by one
                image_list = [
                    tmpdir / f"solutions{v}-{p:02}.png"
                    for p in solutionSpec["solution"][sq]["pages"]
                ]
            else:
                image_list = [
                    tmpdir / f"solutions{v}-{p}.png"
                    for p in solutionSpec["solution"][sq]["pages"]
                ]
            # check the image list - make sure they exist
            for fn in image_list:
                if not fn.is_file():
                    print("Make sure structure of solution pdf matches your test pdf.")
                    print(f"Leaving tmpdir {tmpdir} in place for debugging")
                    raise RuntimeError(
                        f"Error - could not find solution image = {fn.name}"
                    )
            destination = solution_path / f"solution.q{q}.v{v}.png"
            glueImages(image_list, destination)

    shutil.rmtree(tmpdir)

    return True
