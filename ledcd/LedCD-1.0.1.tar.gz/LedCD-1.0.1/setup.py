from setuptools import setup
import platform
import os
import requests
import shutil
import glob
import sys
import atexit
from setuptools.command.install import install

root_dir = os.getcwd()
temp_dir = os.path.join(root_dir, "temp")


def find_module_path():
    for p in sys.path:
        if os.path.isdir(p):
            res = glob.glob(os.path.join(p, "*main_LedCD*"))
            if len(res) > 0:
                return res[0]


def download_release(api_url, ofile, name_key_word):
    output_file = os.path.join(temp_dir, ofile)
    assets = requests.get(api_url).json()["assets"]
    win_release = list(filter(lambda a: name_key_word in a["name"], assets))[0]
    with requests.get(win_release["browser_download_url"], stream=True) as r:
        with open(os.path.join(temp_dir, output_file), "wb") as f:
            shutil.copyfileobj(r.raw, f)

    print("OK" if os.path.exists(output_file) else "ERROR")
    return os.path.exists(output_file)


def _post_install_win():
    # dll_dir = find_module_path()
    dll_dir = os.path.join(os.path.dirname(sys.executable), "Lib", "site-packages")

    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    arch = 64 if sys.maxsize > 2 ** 32 else 32

#    tmp_glew = os.path.join(temp_dir, "ge")
    tmp_glfw = os.path.join(temp_dir, "gf")

#    print("Downloading GLEW dlls: ")
#    download_release(
#        "https://api.github.com/repos/nigels-com/glew/releases/latest",
#        tmp_glew,
#        "win32",
#    )
#    shutil.unpack_archive(tmp_glew, temp_dir, format="zip")
#    glew_dir = glob.glob(os.path.join(temp_dir, "*glew*"))[0]
    print("Downloading GLFW dll's: ")
    download_release(
        "https://api.github.com/repos/glfw/glfw/releases/latest",
        tmp_glfw,
        "WIN64" if arch == 64 else "WIN32",
    )
    shutil.unpack_archive(tmp_glfw, temp_dir, format="zip")
    glfw_dir = glob.glob(os.path.join(temp_dir, "*glfw*"))[0]
    print(dll_dir)
#    for file in glob.glob(  # Move all .lib's
#        os.path.join(
#            glew_dir,
#            "bin",
#            "Release",
#            "x64" if arch == 64 else "Win32",
#            "*.dll",
#        )
#    ):
#        shutil.copy(file, dll_dir)

    for file in glob.glob(  # Move all .lib's
        os.path.join(
            glfw_dir,
            "lib-vc2019",
            "*.dll",
        )
    ):
        shutil.copy(file, dll_dir)

    shutil.rmtree(temp_dir, ignore_errors=True)


class new_install(install):
    def __init__(self, *args, **kwargs):
        super(new_install, self).__init__(*args, **kwargs)
        if platform.system() == "Windows":
            atexit.register(_post_install_win)


setup(
    name="LedCD",
    install_requires=["main_LedCD"],
    cmdclass={"install": new_install},
)
