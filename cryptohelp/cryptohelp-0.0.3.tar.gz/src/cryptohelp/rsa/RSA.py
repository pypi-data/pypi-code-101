from Crypto.Util.number import long_to_bytes
from factordb.factordb import FactorDB

__all__ = ['factorDB_RSA']

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
    print(decrypted)
    return decrypted

#Test
#getFlag(10588750243470683238253385410274703579658358849388292003988652883382013203466393057371661939626562904071765474423122767301289214711332944602077015274586262780328721640431549232327069314664449442016399, 5995952936037255929781924635247478684210608634033130708312547257115162490907542249878843535087479397093661825467058312432783733583919194527896596274111265902276347768535338414466405501311805051241244)