import os

class PDBProcessor:
    def __init__(self):
        self.elemtotal = 0
        self.elemcounts = {}
        self.aatotal = 0
        self.aacounts = {}
        self.totalaacounts = {}
        self.path = "/Home"
        self.searchelem = ""
        self.searchaa = ""
        self.elemcount = 0
        self.aacount = {}
        self.aatotalcount = 0
    
    def set_path(self, path):
        if path.startswith('/'):
            self.path = path
        else:
            self.path = os.getcwd() + '/' + path
    
    def process_pdb_elems(self):
        with open(self.path, 'r') as pdb:
            for line in pdb.readlines():
                l = line.split()
                if l[0] == "ATOM":
                    self.elemtotal += 1
                    if l[-1] not in self.elemcounts.keys():
                        self.elemcounts[l[-1]] = 1
                    else:
                        self.elemcounts[l[-1]] += 1
                        
    def process_pdb_aas(self):
        with open(self.path, 'r') as pdb:
            for line in pdb.readlines():
                l = line.split()
                if l[0] == "SEQRES":
                    chain = l[2]
                    if chain not in self.aacounts.keys():
                        self.aacounts[chain] = {}
                    for aa in l[4:]:
                        if aa not in self.aacounts[chain].keys():
                            self.aacounts[chain][aa] = 1
                        else:
                            self.aacounts[chain][aa] += 1
        for chain in list(self.aacounts.keys()):
            for aa in self.aacounts[chain].items(): 
                if aa[0] not in self.totalaacounts.keys():
                    self.totalaacounts[aa[0]] = int(aa[1])
                else:
                    self.totalaacounts[aa[0]] += int(aa[1])

    def elem_search(self):
        with open(self.path, 'r') as pdb:
            self.elemcount = 0
            for line in pdb.readlines():
                l = line.split()
                if l[0] == "ATOM" and l[-1] == self.searchelem:
                    self.elemcount += 1
                    
    def aa_search(self):
        with open(self.path, 'r') as pdb:
            self.elemcount = 0
            for line in pdb.readlines():
                l = line.split()
                if l[0] == "SEQRES":
                    if l[2] not in self.aacount.keys():
                        self.aacount[l[2]] = sum([1 for i in l if i == self.searchaa])
                    else:
                        self.aacount[l[2]] += sum([1 for i in l if i == self.searchaa])
        for chain in self.aacount.items():
            self.aatotalcount += chain[1]
                    
    def set_elem(self, elem):
        self.searchelem = elem
        
    def set_aa(self, aa):
        self.searchaa = aa
                
    def print_elem_report(self):
        print("#PDB PROCESSOR ELEMENT REPORT#")
        print()
        print(f"Finished analyzing PDB file: {self.path}")
        print()
        print(f"Atoms found: {self.elemtotal}")
        print()
        print("Summary of elements found:")
        for elem in self.elemcounts.items():
            print(f"{elem[0]}: {elem[1]}")
        print()
        print("#END OF REPORT#")
        
    def print_aa_report(self):
        print("#PDB PROCESSOR AMINO ACID REPORT#")
        print()
        print(f"Finished analyzing PDB file: {self.path}")
        print()
        print("Amino acids found:")
        print(f"Total: {sum(self.totalaacounts.values())}")
        for chain in sorted(self.aacounts.items()):
            print(f"In chain {chain[0]}: {sum([int(aa[1]) for aa in chain[1].items()])}")
        print()
        print("Summary of amino acids found:")
        print("In all chains:")
        for aa in sorted(self.totalaacounts.items()):
            print(f"{aa[0]}: {aa[1]}")
        for chain in self.aacounts.items():
            print(f"In chain {chain[0]}:")
            for aa in sorted(chain[1].items()):
                print(f"{aa[0]}: {aa[1]}")
        print()
        print("#END OF REPORT#")
                
    def print_aa_debug(self):
        print(self.aacounts)
        print(self.aacounts.keys())
        print(self.totalaacounts)
        print(self.debugtracker)
        
        
    def print_elem_count(self):
        print("#PDB PROCESSOR ELEMENT COUNT#")
        print(f"Finished analyzing PDB file: {self.path}")
        print(f"Looked for element: {self.searchelem}")
        print(f"Instances found: {self.elemcount}")
        print("#END OF REPORT#")
        
    def print_aa_count(self):
        print("#PDB PROCESSOR AMINO ACID COUNT#")
        print(f"Finished analyzing PDB file: {self.path}")
        print(f"Looked for amino acid: {self.searchaa}")
        print("Instances found:")
        print(f"Total: {self.aatotalcount}")
        for chain in self.aacount.items():
            print(f"In chain {chain[0]}: {chain[1]}")
        print("#END OF REPORT#")