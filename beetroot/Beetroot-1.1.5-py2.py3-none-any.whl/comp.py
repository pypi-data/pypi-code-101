import zlib
import lzma
import sys

from .exception import *
from .objtype import objtype

class compr:
    def strcompress(self, str_):
        """Compresses a strings with hybrid zlib/lzma"""
        a = str(str_)
        aa = "n" + a
        ab = "z" + zlib.compress(a.encode("utf-8")).decode("iso-8859-1")
        ac = "l" + lzma.compress(a.encode("utf-8")).decode("iso-8859-1")
        
        yay = [aa, ab, ac]
        yay2 = [sys.getsizeof(aa), sys.getsizeof(ab), sys.getsizeof(ac)]
        
        return yay[yay2.index(min(yay2))]
    
    def strdecompress(self, str_):
        """Decompresses a strings with hybrid zlib/lzma"""
        if str(str_).startswith("n"):
            return str(str_)[1:]
        
        elif str(str_).startswith("z"):
            return zlib.decompress(str(str_)[1:].encode("iso-8859-1")).decode("utf-8")
        
        elif str(str_).startswith("l"):
            return lzma.decompress(str(str_)[1:].encode("iso-8859-1")).decode("utf-8")
        
        else:
            raise StringError("This string could not be properly decompressed.")
        
    def bytecompress(self, b):
        """Compresses a strings with hybrid zlib/lzma"""
        if objtype(b) != "bytes":
            raise InvalidTypeError("argument \"b\" must be bytestring")
        
        a = b
        
        aa = str("n" + a.decode("iso-8859-1")).encode("iso-8859-1")
        ab = str("z" + zlib.compress(a).decode("iso-8859-1")).encode("iso-8859-1")
        ac = str("l" + lzma.compress(a).decode("iso-8859-1")).encode("iso-8859-1")
        
        yay = [aa, ab, ac]
        yay2 = [sys.getsizeof(aa), sys.getsizeof(ab), sys.getsizeof(ac)]
        
        return yay[yay2.index(min(yay2))]
    
    def bytedecompress(self, b):
        """Decompresses a strings with hybrid zlib/lzma"""
        if objtype(b) != "bytes":
            raise InvalidTypeError("argument \"b\" must be bytestring")
        
        if b.decode("iso-8859-1").startswith("n"):
            return str(b.decode("iso-8859-1"))[1:].encode("iso-8859-1")
        
        elif b.decode("iso-8859-1").startswith("z"):
            return zlib.decompress(b.decode("iso-8859-1")[1:].encode("iso-8859-1"))
        
        elif b.decode("iso-8859-1").startswith("l"):
            return lzma.decompress(b.decode("iso-8859-1")[1:].encode("iso-8859-1"))
        
        else:
            raise StringError("This string could not be properly decompressed.")
        
comp = compr()
del compr