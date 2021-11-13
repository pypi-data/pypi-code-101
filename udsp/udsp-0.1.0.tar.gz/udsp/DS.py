import struct

class DS:
    def __init__(self, buf, index=0, length=0, left=None):
        self.buf = buf

        if not left: left = len(self.buf) - length - index
        self.Loading(index, length, left)

    def Loading(self, *args):
        self.index = args[0]
        self.len = args[1]
        self.left = args[2]

    @staticmethod
    def CalcRawSize(fmt):
        i, rec, _len, _size, _child = 0, 0, len(fmt), 0, ''
        while i < _len:
            if fmt[i].isalpha():
                rec = i
                i += 1
                while _len - i and not fmt[i].isalpha():
                    i += 1
                i -= 1
            else:
                i += 1
                continue

            i += 1

            #debug# print(':', rec, i, fmt[rec:i])
            a = struct.calcsize(fmt[rec:i])
            _size += a
            #debug# print("raw add:", a)
        return _size

    def O(self, fmt):
        fmt = '<' + fmt
        size = self.CalcRawSize(fmt)
        #debug# print("calc size ", size)
        if (self.len < size): raise Exception("[Error]: Ran out <length> of stream.\n\tfmt:%s\n\tlen = %d\n\tindex = %d\n\tleft = %d\n\tdata:%s\n"%(str(fmt), self.len, self.index, self.left, self.buf))
        rtn = struct.unpack_from(fmt, self.buf, self.index)
        self.index += size
        self.len -= size
        return rtn if len(rtn) != 1 else rtn[0]


    def I(self, fmt, *data):
        fmt = '<' + fmt
        size = self.CalcRawSize(fmt)
        #debug# print("add len:", size)
        if (self.left < size): raise Exception("[Error]: fill over <left> of stream.\n\tfmt:%s\n\tlen = %d\n\tindex = %d\n\tleft = %d\n\tdata:%s\n"%(str(fmt), self.len, self.index, self.left, self.buf))
        struct.pack_into(fmt, self.buf, self.index + self.len, *data)
        self.len += size
        #debug# print("len ", self.len)
        self.left -= size

    def __str__(self):
        return "<content:>{}...; <index:>{}; <len:>{}; <left:>{}".format(self.buf[:10], self.index, self.len, self.left)
    def __repr__(self):
        return str(self)
    def __len__(self):
        return self.len

if __name__ == '__main__':
    ba = bytearray(60)
    ds = DS(ba)
    ds.I('I', 4096)
    print(ba)
