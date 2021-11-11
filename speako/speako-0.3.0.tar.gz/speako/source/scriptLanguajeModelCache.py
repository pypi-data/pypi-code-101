import json
import time
if __name__ == "__main__":
	from generateCacheLanguajeModel import generateCacheLanguajeModel
else:
	from speako.source.generateCacheLanguajeModel import generateCacheLanguajeModel


#Script que actualiza los modelos de lenguaje caché tras la inclusión de una nueva frase

#Se especifican los archivos con los que crear los modelos de lenguaje en dos listas: fileFormat (formato de los archivos) y file (nueva frase)
#Como ejemplo, se propone un frase en formato .json

timeStart = time.time()
fileFormat = "json"
file ="newSentenceCache.json" #Archivo que contiene la frase de ejemplo

#Luego, se cargan las listas y diccionarios a actualizar. Son los siguientes:

f = open("listWordsCache.txt", "r")
content = f.read()
listWords = content.split("\n")
f.close()

f = open("listWordsInfCache.txt", "r")
content = f.read()
listWordsInf = content.split("\n")
f.close()

f = open("dictNgramCache.txt", "r")
dictNgram = json.load(f)
f.close()

f = open("dictNgramInfCache.txt", "r")
dictNgramInf = json.load(f)
f.close()

f = open("dictBackoffCache.txt", "r")
dictBackoff = json.load(f)
f.close()

f = open("dictBackoffInfCache.txt", "r")
dictBackoffInf = json.load(f)
f.close()

rel_path = "verb-conj/es-verbs.txt"
verbForms = open(rel_path, encoding="utf-8") #Se abre el archivo que contiene todas las formas verbales de los verbos en español
verbs_array = verbForms.read().split()

#Se añade una nueva frase al diccionario de caché
[listWords, listWordsInf, dictNgram, dictNgramInf, dictBackoff, dictBackoffInf] = generateCacheLanguajeModel(fileFormat, file, listWords, listWordsInf, dictNgram, dictNgramInf, dictBackoff, dictBackoffInf, verbs_array)

#Se guardan todos los datos (listas y diccionarios), cada uno en un archivo .txt
f = open("listWordsCache.txt", "w")
for word in listWords:
	if word == listWords[len(listWords)-1]:
		f.write(word)
	else:
		f.write(word+'\n')
f.close()

f = open("listWordsInfCache.txt", "w")
for word in listWordsInf:
    if word == listWordsInf[len(listWordsInf)-1]:
    	f.write(word)
    else:
    	f.write(word+'\n')
f.close()

f = open("dictNgramCache.txt", "w")
json.dump(dictNgram, f)
f.close()

f = open("dictNgramInfCache.txt", "w")
json.dump(dictNgramInf, f)
f.close()

f = open("dictBackoffCache.txt", "w")
json.dump(dictBackoff, f)
f.close()

f = open("dictBackoffInfCache.txt", "w")
json.dump(dictBackoffInf, f)
f.close()

#Impresión de los resultados
timeFin = time.time() - timeStart
print("tiempo:",timeFin)