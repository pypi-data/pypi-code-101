from Crypto.Util.number import long_to_bytes
from factordb.factordb import FactorDB

#Prints the flag if the factorisation of the modulus is available on factorDB, fefault public exponent value is 65537

def factorDB_RSA(n, ct, e=65537):
    f = FactorDB(n)
    f.get_factor_list()
    f.connect()
    factorList = f.get_factor_list()
    
    eulerTotient = 1
    for i in factorList: eulerTotient = (i-1) * eulerTotient
    
    d = pow(e, -1, eulerTotient)
    pt = pow(ct, d, n)
    decrypted = long_to_bytes(pt)
    return decrypted

