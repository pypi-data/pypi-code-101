from whichlang import which_lang
import codecs
f= codecs.open('sample-test-files\\sample-assamese.txt','r', encoding='utf-8')
data = f.read()

print (which_lang(data))