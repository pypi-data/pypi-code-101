import sys
from iban import IBAN

if __name__ == '__main__':
    if IBAN.validarDv(sys.argv[1]):
        print("IBAN integro")
    else:
        print("IBAN corrompido")
