import sys
from iban import IBAN

if __name__ == '__main__':
    iban = IBAN()
    iban.parseIban(sys.argv[1])
    print(f"Pais: {iban.getPais()}")
    print(f"Banco: {iban.getBanco()}")
    print(f"Agencia: {iban.getAgencia()}")
    print(f"Conta: {iban.getConta()}")
    print(f"Tipo: {iban.getTipo()}")
    print(f"Titular: {iban.getTitular()}")
