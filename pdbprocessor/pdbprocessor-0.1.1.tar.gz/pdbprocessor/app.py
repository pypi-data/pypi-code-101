import sys, os
from interface import Interface
from processor import PDBProcessor
   
class Application:
    def __init__(self):
        self.proc = PDBProcessor()
        self.interface = Interface()
    def run_app(self):
        os.system("cls" if os.name == "nt" else "clear")
        if len(sys.argv) == 1:
            self.interface.display_start()
            self.interface.prompt_path()
            self.proc.set_path(input())
            self.interface.display_menu()
            self.mode = input()
            if self.mode == "elemreport":
                self.proc.process_pdb_elems()
                self.proc.print_elem_report()
            elif self.mode == "elemsearch":
                self.interface.display_elem_count()
                self.interface.prompt_element()
                self.proc.set_elem(input())
                self.proc.elem_search()
                self.proc.print_elem_count()
            elif self.mode == "aareport":
                self.proc.process_pdb_aas()
                #self.proc.print_aa_debug()
                self.proc.print_aa_report()
            elif self.mode == "aacount":
                self.interface.display_aa_count()
                self.interface.prompt_aa()
                self.proc.set_aa(input().upper())
                self.proc.aa_search()
                self.proc.print_aa_count()
            elif self.mode.lower() == "sus":
                print("#AMOGUS#") 
            else:
                print("Wrong mode!")
        else:
            self.interface.display_start()
            self.proc.set_path(sys.argv[1])
            self.mode = sys.argv[2]
            if self.mode == "elemreport":
                self.proc.process_pdb_elems()
                self.proc.print_elem_report()
            elif self.mode == "elemsearch":
                self.proc.set_elem(sys.argv[3])
                self.proc.elem_search()
                self.proc.print_elem_count()
            elif self.mode == "aareport":
                self.proc.process_pdb_aas()
                #self.proc.print_aa_debug()
                self.proc.print_aa_report()
            elif self.mode == "aacount":
                self.proc.set_aa(sys.argv[3].upper())
                self.proc.aa_search()
                self.proc.print_aa_count()
            else:
                print("Wrong mode!")
