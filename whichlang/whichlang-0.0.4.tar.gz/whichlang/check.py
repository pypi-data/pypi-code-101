from whichlang import whichlang as wl
import codecs
f= codecs.open('sample-test-files\\sample-assamese.txt','r', encoding='utf-8')
data = f.read()

print (wl.which_lang(data))