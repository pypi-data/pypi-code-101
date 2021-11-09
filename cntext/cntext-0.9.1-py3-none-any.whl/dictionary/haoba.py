words = open('dict/unformal_pos.txt').read().split('\n')
words = [w.replace(' ','') for w in words if w]
with open('dict.py', 'a+', encoding='utf-8') as f:
    text = '['
    for w in words:
        text += "'{}',".format(w)
    text += ']'
    text.replace(',]', ']')
    f.write(text)

