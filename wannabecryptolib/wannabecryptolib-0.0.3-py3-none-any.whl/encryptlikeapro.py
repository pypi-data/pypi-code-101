class UltraSafeCipher():
    def __init__(self, seed,dif):
        self.seed = seed
        self.dif = dif

    def gen(self):
        import random
        random.seed(None)
        first = random.choice([i for i in range(self.seed,self.seed**2)])
        last = first-self.dif if first > self.dif else first+self.dif
        return (first,last) if first < last else (last,first)

    def encrypt(self, plaintext):
        (first,last) = self.gen()
        ciphertext=""
        for c in range(len(plaintext)):
            if c%2==0:
                ciphertext += str(ord(plaintext[c])^first) + " "
            else:
                ciphertext += str(ord(plaintext[c])^last) + " "
        return ciphertext

