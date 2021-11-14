import random
def generate_key(length=10,include_letters=True,split=True,split_char="-",split_every=5):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    key = ""
    for i in range(length):
        if random.randint(1,2) == 1:
            key = key +str(random.randint(0,9))
        elif include_letters == True:
            if random.randint(1,2) == 1:
                key = key + random.choice(letters)
            else:
                key = key + random.choice(letters).upper()
        else:
            key = key +str(random.randint(0,9))
    if split == True:
        key = split_char.join(key[i:i+split_every] for i in range(0, len(key), split_every))
    return key
