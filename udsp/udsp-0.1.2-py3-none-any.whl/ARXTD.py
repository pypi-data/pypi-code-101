

class ARXTD:
    def __init__(self, source, endl, empty=None):
        self.s = source
        self.endl = endl
        self.empty = empty
        
        self.busy = False
        self.buf = []
        self.piece = bytearray()
    
        
    
    def Update(self):
        tmp = self.s()
        if tmp == self.empty: return
        #print(tmp)
        if len(self.piece): # 从上次的中断处继续
            
            end_index = tmp.find(self.endl)
            if end_index != -1:
                self.Push(self.piece + tmp[:end_index])
            else:
                self.piece += tmp
        else:  # 新的操作
            while len(tmp):
                end_index = tmp.find(self.endl)
                if end_index != -1:
                    self.Push(tmp[:end_index])
                    tmp = tmp[end_index + 2:]
                else:
                    self.piece = tmp
                    break
    
    def Push(self, item):
        while self.busy: ...
        self.busy = True
        self.buf += [self.RemoveZeros(item)]
        self.busy = False
        
    def Pop(self, index=0):
        while self.busy: ...
        self.busy = True
        tmp = self.buf.pop(0)
        self.busy = False
        return tmp
    
    def __len__(self):
        return len(self.buf)
        
    @staticmethod
    def RemoveZeros(item):  # 去除开头的若干个0
        i = 0
        while item[i] == 0:
            i += 1
        return item[i:]
    