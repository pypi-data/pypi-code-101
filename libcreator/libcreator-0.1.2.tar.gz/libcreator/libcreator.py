import os
import wheel
import twine

class Library():
    def __init__(self):
        pass

    def get_information(self):
        self.setup_core = ""
        self.package_path = ""
        print("Automated library creation guide")
        self.library_name = str(input("What should be the libraries name: "))
        self.library_version = str(input("Version (standard:0.0.1): ") or "0.0.1")
        self.description = str(input("Description: "))
        self.author = str(input("Author: "))
        self.author_email = str(input("Authors email: "))
        self.license = str(input("License (standard:MIT): ") or "MIT")
        self.requirements = input("Required libraries (seperated by kommas) (enter for none): ") or [] # process string
        if self.requirements != []:
            self.requirements = self.requirements.replace(" ", "").split(",")
            for i in range(len(self.requirements)):
                self.requirements[i] = "'" + self.requirements[i] + "'"
            self.requirements = "[" + ",".join(self.requirements) + "]"


    def fill_in_information(self):
        self.setup_core = f"""
from setuptools import find_packages, setup

setup(
    name='{self.library_name}',
    packages=find_packages(include=['{self.library_name}']),
    version='{self.library_version}',
    description='{self.description}',
    author='{self.author}',
    license='{self.license}',
    install_requires={self.requirements}
)
        """
    def create_library(self):
        lib_path = "./" + self.library_name + "/"
        self.package_path = lib_path + self.library_name + "/"
        os.makedirs(lib_path)
        os.makedirs(self.package_path)
        with open(lib_path + "setup.py", "w") as setup_file:
            setup_file.write(self.setup_core)
        with open(lib_path  + "README.MD", "w") as README_file:
            pass
        with open(self.package_path + self.library_name + ".py", "w") as library_file:
            pass
        with open(self.package_path + "__init__.py", "w") as init_file:
            pass
    
    def compile_library(self):
        print("Start compiling...")
        os.system("python ./" + self.library_name + "/setup.py sdist bdist_wheel")
        print("Finished compiling")

if __name__ == "__main__":
    new_lib = Library()
    new_lib.get_information()
    new_lib.fill_in_information()
    new_lib.create_library()
    print("Now fill the " + new_lib.package_path + new_lib.library_name + ".py" + " with your modules and press enter to compile")
    input("Waiting...")
    new_lib.compile_library()