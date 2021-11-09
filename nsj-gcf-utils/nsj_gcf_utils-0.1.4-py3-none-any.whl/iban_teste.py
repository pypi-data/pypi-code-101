import sys
from iban import IBAN

if __name__ == '__main__':
    conta = IBAN();
    #conta.setPais("BR").setBanco("0").setAgencia("87").setConta("26394X").setTipo("C").setTitular(1)
    #print(conta.getIban())
    conta.parseIban(sys.argv[1], True);
    print(conta.getIban())

    paises = ["BR"]
    print("Indique o pais")
    print("0 - Brasil")
    pais = input("Pais: ")
    conta.setPais(paises[int(pais)])

    bancos = ["0", "60701190"]
    print("Indique o banco")
    print("0 - Banco do Brasil")
    print("1 - Itaú")
    banco = input("Banco: ")
    conta.setBanco(bancos[int(banco)])

    print("Indique a agencia sem dígito verificador")
    agencia = input("Agencia: ")
    conta.setAgencia(agencia)

    print("Indique a conta com dígito verificador")
    numconta = input("Conta: ")
    conta.setConta(numconta)

    tipos = ["C", "P"]
    print("Indique o tipo de conta")
    print("0 - Corrente")
    print("1 - Polpança")
    tipo = input("Tipo: ")
    conta.setTipo(tipos[int(tipo)])

    print("Indique o número do titular")
    titular = input("Titular: ")
    conta.setTitular(int(titular))

    print(conta.getIban())
