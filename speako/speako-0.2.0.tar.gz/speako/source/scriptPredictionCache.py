import json
import time
import os
if __name__ == "__main__":
	from calcularPrediccionCache import calcularPrediccionCache
	from generateCacheLanguajeModel import generateCacheLanguajeModel
else:
	from speako.source.calcularPrediccionCache import calcularPrediccionCache
	from speako.source.generateCacheLanguajeModel import generateCacheLanguajeModel


#Script donde se especifica una frase y se obtienen las predicciones
timeStart = time.time() 
#Datos de entrada:
sentence = "Quiero" #Frase inicial sobre la que calcular la predicción
maxNgram = 5 #Máximo orden del N-grama
maxNumPaths = 4 #Máximo número de caminos devueltos tras la ejecución del algoritmo
maxNumWords = 3 #Máximo número de palabras de las frases solución

#Carga de todos los archivos que forman los modelos de lenguaje (normal y de infinitivos)
f = open("listWords.txt", "r")
content = f.read()
listWords = content.split("\n")
f.close()

f = open("listWordsInf.txt", "r")
content = f.read()
listWordsInf = content.split("\n")
f.close()

f = open("dictNgram.txt", "r")
dictNgram = json.load(f)
f.close()
nTot = list(dictNgram.values())[0][3]#Tamaño del diccionario de N-gramas principal

f = open("dictNgramInf.txt", "r")
dictNgramInf = json.load(f)
f.close()

f = open("dictBackoff.txt", "r")
dictBackoff = json.load(f)
f.close()

f = open("dictBackoffInf.txt", "r")
dictBackoffInf = json.load(f)
f.close()

#Carga de formas verbales en español
script_dir = os.path.dirname(__file__)
rel_path = "es-verbs.txt"
fileDictVerbs = os.path.join(script_dir, rel_path) 
verbForms = open(fileDictVerbs, encoding="utf-8") #Se abre el archivo que contiene todas las formas verbales de los verbos en español
verbs_array = verbForms.read().split() #Se obtiene una lista de arrays. Cada array contiene todas las conjugaciones para un mismo verbo.

#Carga de lista de caminos por defecto (a utilizar con aquella frases iniciales que no existan en el diccionario)
f = open("listDefaultPaths.txt", "r", encoding="utf-8")
content = f.read()
listDefaultPaths = content.split("\n")
f.close()

#Parte adicional para diccionarios caché
f = open("listWordsCache.txt", "r")
content = f.read()
listWordsCache = content.split("\n")
f.close()

f = open("listWordsInfCache.txt", "r")
content = f.read()
listWordsCacheInf = content.split("\n")
f.close()

f = open("dictNgramCache.txt", "r")
dictNgramCache = json.load(f)
f.close()
nCache = list(dictNgramCache.values())[0][3]#Tamaño del diccionario de N-gramas de caché

f = open("dictNgramInfCache.txt", "r")
dictNgramCacheInf = json.load(f)
f.close()

f = open("dictBackoffCache.txt", "r")
dictBackoffCache = json.load(f)
f.close()

f = open("dictBackoffInfCache.txt", "r")
dictBackoffCacheInf = json.load(f)
f.close()

time1 = time.time() - timeStart
print("Abrir archivos:",time1)

#Peso, sobre 1, que se le da al diccionario caché
#alfa = (nCache^2)/(nCache+nTot)#Una opción para obtener el parámetro es alfa es ponderarlo en función de los tamaños de los diccionarios
alfa = 0.6 #Otra opción es utilizar valores fijos

#print("frase inicial:",sentence)
#Una vez recopilados todos los datos, se calcula la predicción basada en el algoritmo Viterbi
json_pathsConjugated = calcularPrediccionCache(sentence, maxNgram, maxNumPaths, maxNumWords, listWords, listWordsInf, dictNgram, dictNgramInf, dictBackoff, dictBackoffInf, listWordsCacheInf, dictNgramCache, dictNgramCacheInf, dictBackoffCacheInf, verbs_array, listDefaultPaths, alfa)
#Impresión de los resultados
timeFin = time.time() - timeStart
print(sentence, ": ", json_pathsConjugated,"tiempo:",timeFin)
timeStart2 = time.time()
json_pathsConjugated2 = calcularPrediccionCache(sentence, maxNgram, maxNumPaths, maxNumWords, listWords, listWordsInf, dictNgram, dictNgramInf, dictBackoff, dictBackoffInf, listWordsCacheInf, dictNgramCache, dictNgramCacheInf, dictBackoffCacheInf, verbs_array, listDefaultPaths, alfa)
timeFin2 = time.time() - timeStart2
print(sentence, ": ", json_pathsConjugated2,"tiempo sin apertura:",timeFin2)

try: #Se pregunta al usuario acerca de la opción que desea elegir para completar la frase y, así, guardarla en el diccionario caché.
	choice = int(input("Selecciona la opción para completar la frase: "))
	while(choice>len(json_pathsConjugated) or choice < 1): #Si el usuario indica un valor más alto que las opciones disponibles, se le pregunta hasta que indica un número válido.
		choice = int(input("Valor incorecto. Selecciona una opción válida para completar la frase: "))
except: #Si el usuario no indica un valor numérico, se elige la primera opción por defecto.
	choice = 1
	print("Valor incorrecto. Selecionada opción 1 por defecto.")

timeStartSaving = time.time()
#Guardado de la opción seleccionada por el usuario en los diccionarios caché
fileFormat = "json"
f = open("newSentenceCache.json", "w")
dictSen = dict()
keySen = "frase"
completeSentece =  sentence + " " + json_pathsConjugated.get(str(choice))
dictSen[keySen] = completeSentece
json_data = json.dumps(dictSen) #Se convierte el diccionario en un string JSON
json_paths = json.loads(json_data) # Se crea el objeto JSON
f.write("[")
json.dump(json_paths,f)
f.write("]")
f.close()
file ="newSentenceCache.json"

[listWordsCache, listWordsCacheInf, dictNgramCache, dictNgramCacheInf, dictBackoffCache, dictBackoffCacheInf] = generateCacheLanguajeModel(fileFormat, file, listWordsCache, listWordsCacheInf, dictNgramCache, dictNgramCacheInf, dictBackoffCache, dictBackoffCacheInf)


#Se guardan todos los datos (listas y diccionarios), cada uno en un archivo .txt
f = open("listWordsCache.txt", "w")
for word in listWordsCache:
	if word == listWordsCache[len(listWordsCache)-1]:
		f.write(word)
	else:
		f.write(word+'\n')
f.close()

f = open("listWordsInfCache.txt", "w")
for word in listWordsCacheInf:
    if word == listWordsCacheInf[len(listWordsCacheInf)-1]:
    	f.write(word)
    else:
    	f.write(word+'\n')
f.close()

f = open("dictNgramCache.txt", "w")
json.dump(dictNgramCache, f)
f.close()

f = open("dictNgramInfCache.txt", "w")
json.dump(dictNgramCacheInf, f)
f.close()

f = open("dictBackoffCache.txt", "w")
json.dump(dictBackoffCache, f)
f.close()

f = open("dictBackoffInfCache.txt", "w")
json.dump(dictBackoffCacheInf, f)
f.close()

timeSavingCache = time.time() - timeStartSaving
print(completeSentece,",","tiempo guardado:",timeSavingCache,", alfa:",alfa)