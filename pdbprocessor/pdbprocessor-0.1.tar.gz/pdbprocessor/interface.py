from appinfo import AppInfo

class Interface:
    def __init__(self):
        pass

    @staticmethod
    def display_start():
        print(f"PDBProcessor by {AppInfo.AUTHOR}, version {AppInfo.VERSION}")
        
    @staticmethod
    def prompt_path():
        print("Enter file path:")

    @staticmethod
    def display_menu():
        print("Available modes:")
        print("elemreport - element composition report")
        print("elemsearch - element search")
        print("Select option: ")

    @staticmethod
    def display_elem_count():
        print("Element count initiated")
    
    @staticmethod
    def prompt_element():
        print("Enter element symbol: ")
        
    @staticmethod
    def display_aa_count():
        print("Amino acid count initiated")
        
    @staticmethod
    def prompt_aa():
        print("Enter three-letter amino acid symbol: ")