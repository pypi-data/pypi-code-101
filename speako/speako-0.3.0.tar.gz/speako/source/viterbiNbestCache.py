if __name__ == "__main__":
	from viterbiNbest import evaluateNgram
else:
	from speako.source.viterbiNbest import evaluateNgram

def viterbiNbestCache(sentence, maxNgram, maxNumPaths, maxNumWords, listWords, dictNgram, dictBackoff, listWordsCache, dictNgramCache, dictBackoffCache, listDefaultPaths, alfa): #Función que devuelve las listas de palabras más probables para continuar la frase inicial dada
	"""Parámetros de entrada:
		- sentence: frase inicial a continuar
		- maxNgram: máximo orden de los N-gramas a evaluar. Por defecto: 5
		- maxNumPaths: máximo número de soluciones a devolver
		- maxNumWords: máximo número de palabras de las frases devueltas
		- listWords: listado de todas las palabras que aparecen en el diccionario de N-gramas
		- dictNgram: diccionario de N-gramas
		- dictBackoff: diccionario de bigramas con sus parámetros de backoff
		- listWordsCache: listado de todas las palabras que aparecen en el diccionario caché de N-gramas
		- dictNgramCache: diccionario caché de N-gramas
		- dictBackoffCache: diccionario de bigramas con sus parámetros de backoff
		- listDefaultPaths: lista de caminos por defecto
		- alfa: peso que se le da al diccionario caché respecto al total, inlcuyendo el diccionario general (valor entre 0 y 1)

		Resultado:
		- pathsSelected: caminos más probables (en forma de lista de strings) para continuar la frase inicial
		"""
	listSign = [".", "?", "!", "¿", "¡", ",",";"] #Se indica la lista de signos de puntuación para no considerarlos en la evaluación de palabras
	sentenceWords = sentence.split() #Se transforma la frase inicial en lista de palabras
	nGram = [] #Se inicializa la lista de palabras que forman un N-grama
	pathsSaved = dict() #Se inicializa el diccionario de caminos guardados
	pathsNext = list() #Como primer camino guardado, se escoge la frase inicial
	pathsNext.append("") 
	nGramBack = list() #Lista de palabras de la parte inicial de la frase para el cálculo del backoff
	probPaths = list() #Lista de las probabilidades de los caminos activos

	keysDict = list(dictNgram.keys()) #Se obtienen las claves del diccionario de N-gramas general en forma de lista
	valuesDict= list(dictNgram.values()) #Se obtienen los valores del diccionario de N-gramas general en forma de lista
	keysDictCache = list(dictNgramCache.keys()) #Se obtienen las claves del diccionario de N-gramas Caché en forma de lista
	valuesDictCache= list(dictNgramCache.values()) #Se obtienen los valores del diccionario de N-gramas Caché en forma de lista

	keysDictBack = list(dictBackoff.keys()) #Se obtienen las claves del diccionario de Backoff general en forma de lista
	valuesDictBack = list(dictBackoff.values()) #Se obtienen los valores del diccionario de Backoff general en forma de lista
	keysDictBackCache = list(dictBackoffCache.keys()) #Se obtienen las claves del diccionario de Backoff caché en forma de lista
	valuesDictBackCache = list(dictBackoffCache.values()) #Se obtienen los valores del diccionario de Backoff caché en forma de lista

	
	for nWords in range(maxNumWords): #Se añaden palabras a la frase mientras no supere el máximo marcado
		for pathEv in pathsNext: #Se evalúan todos los caminos marcados
			wordToAdd = pathEv.split() #Se transforma el camino a evaluar en lista de palabras
			probIni = pathsSaved.get(pathEv,0) #Se recoge la probabilidad acumulada del camino en evaluación

			sentenceWordsEv = sentence.split() #Se inicializa la lista de palabras con la frase inicial
			for wTA in wordToAdd: #Se añaden las palabras del camino en estudio a la frase inicial
				sentenceWordsEv.append(wTA)
			nIni = min(len(sentenceWordsEv), maxNgram-1) #Se obtiene la longitud de la frase a evaluar (como máximo el orden máximo del N-grama establecido menos 1 ya que hay que añadir la nueva palabra a evaluar)
			sentenceWordsEv = sentenceWordsEv[len(sentenceWordsEv)-nIni:len(sentenceWordsEv)] #Se utilizan las N primeras palabras para realizar la predicción
			sentenceEv = ' '.join(sentenceWordsEv) #Se construye la frase inicial a analizar
			listWordsEv = list() #Lista de palabras a evaluar
			while len(listWordsEv) == 0 and len(sentenceWordsEv)>0: #Se buscan palabras objetivo mientra no haya ninguna y el N-grama a evaluar no esté vacío
				for key, value in dictNgram.items(): #Se obtienen aquellas palabras que se encuentran en las frases del diccionario general que incluyen la frase inicial
					if sentenceEv in key:
						wordsSentece = key.split()
						for w in wordsSentece:
							if w not in listWordsEv and w not in listSign: #Se guardan aquellas palabras que aún no se encuentran en la lista, no se considerando los signos de puntuación
								listWordsEv.append(w)

				for keyCache, valueCache in dictNgramCache.items(): #De la misma forma que para el diccionario general, se obtienen aquellas palabras que se encuentran en las frases del diccionario caché que incluyen la frase inicial
					if sentenceEv in keyCache:
						wordsSenteceCache = keyCache.split()
						for w in wordsSenteceCache:
							if w not in listWordsEv and w not in listSign:
								listWordsEv.append(w)

				if len(listWordsEv) == 0 and len(sentenceWordsEv)>0: #Si la frase completa no se encuentra en el diccionario, se va acortando el N-grama eliminando las palabras iniciales
					nGramBack.append(sentenceWordsEv[0])
					sentenceWordsEv.remove(sentenceWordsEv[0])
					sentenceEv = ' '.join(sentenceWordsEv)


			n = min(len(sentenceWordsEv), maxNgram-1) #Se obtiene el número de palabras iniciales sobre las que trabajar (como máximo el orden máximo del N-grama establecido menos 1 ya que hay que añadir la nueva palabra a evaluar)
			nBack = nIni - n #Diferencia entre el número de palabras de la frase inicial y el de la frase con la que trabajar; utilizado para el cálculo del backoff
			probBackGen = 1 #Se inicializa la probabilidad de backoff general a 1; no influye en aquellos casos no necesarios
			probBackCache = 1 #Se inicializa la probabilidad de backoff del diccionario caché también a 1
			if nBack > 0:
				nGramBack.append(sentenceWordsEv[0]) #Se añade la primera palabra de la parte final de la frase (evaluación diccionario) para incluirla en backoff
				try: #Se evaluan los bigrama de inicio de frase para recoger su parámetro de backoff tanto en el diccinario general como en el de caché
					for b in range(nBack): 
						bigram = nGramBack[b]+" "+nGramBack[b+1]
						indexSentenceBack = keysDictBack.index(bigram)
						indexSentenceBackCache = keysDictBackCache.index(bigram)
						probBackGen = probBackGen*valuesDictBack[indexSentenceBack][4]
						probBackCache = probBackCache*valuesDictBackCache[indexSentenceBackCache][4]
				except: #Si algún bigrama no se encuentra en el diccionario, se inicializa la probabilidad de backoff
					probBackGen = 1
					probBackCache = 1
					

			try:
				for i in range(n):
					listWordsEv.remove(sentenceWordsEv[len(sentenceWordsEv)-(i+1)]) #Se elimina las palabras de la frase inicial para no repetirlas en la predicción
			except:
				listWordsEv

			for i in range(n): #Se construye el N-grama inicial sobre el que trabajar
				nGram.append(sentenceWordsEv[len(sentenceWordsEv)-n+i])

			for word in listWordsEv: #Se recorre la lista de palabras para calcular su probabilidad y se añade a la lista de probabilidades
				probGen = evaluateNgram(word, nGram, keysDict, valuesDict, nBack, probBackGen)
				probCache = evaluateNgram(word, nGram, keysDictCache, valuesDictCache, nBack, probBackCache)
				prob = (1-alfa)*probGen + alfa*probCache #La probabilidad finals se calcula ponderando la probabilidad obtenida con el diccionario general y con el caché
				keyWord = pathEv + ' ' + word
				pathsSaved[keyWord] = prob + probIni
			
		
		pathsSavedOrdered = dict(sorted(pathsSaved.items(), key=lambda item: item[1], reverse = True)) #Se ordenan las palabras evaluadas en orden decreciente de probabilidad
		pathsNext.clear()
		pathsNextPrev = list(pathsSavedOrdered.keys())[0:maxNumPaths] #Se filtran los caminos de mayor probabilidad, sobre los que se realizará una nueva iteración 
		for j in range(len(pathsNextPrev)): #Solo se seleccionan aquellos que no se han evaluado previamente, para no repetir de nuevo el mismo proceso
			if len(pathsNextPrev[j].split()) > nWords:
				pathsNext.append(pathsNextPrev[j])
		
		if(len(pathsNext)==0): #Si no hay ningún camino que cumpla las condiciones anteriores, se finaliza el algoritmo
			break


	pathsSO = list(pathsSavedOrdered.keys()) #Se obtiene la lista de caminos guardados ordenada por probabilidad

	pathsSelected = list() 
	for pthSd in range(min(maxNumPaths,len(pathsSO))): #Se recogen los K caminos más probables, siendo K el número máximo de caminos a devolver
		pathsSelected.append(pathsSO[pthSd])

	ind = 0
	while len(pathsSelected) < maxNumPaths: #Si no hay suficientes caminos calculados, los más probables por defecto
		pathsSelected.append(listDefaultPaths[ind])
		ind = ind + 1

	return pathsSelected #Se devuelven los caminos más probables

def conjugateSentenceCache(sentence, path, maxNgram, dictNgram, dictNgramCache, verbs_array, alfa):#Función que sustituye los verbos (en infinitivo) de una frase dada por su conjugación más probable
	"""Parámetros de entrada:
		- sentence: frase inicial
		- path: frase final a procesar
		- maxNgram: máximo orden de los N-gramas a evaluar. Por defecto: 5
		- dictNgram: diccionario de N-gramas
		- dictNgramCache: diccionario de N-gramas para el diccionario caché 
		- verbs_array: archivo que contiene todas las formas verbales de los verbos en español
		- alfa: peso que se le da al diccionario caché respecto al total, inlcuyendo el diccionario general (valor entre 0 y 1)

		Resultado:
		- final_sentence: frase conjugada
		"""
	wordsSentece = sentence.split() #Se convierte la frase inicial en lista de palabras
	lenIni = len(wordsSentece) #Se obtiene el número de palabras de la frase inicial
	final_path = wordsSentece #Inicialización de la lista de palabras que formarán la frase final

	keysDict = list(dictNgram.keys()) #Se obtienen las claves del diccionario de N-gramas en forma de lista
	valuesDict= list(dictNgram.values()) #Se obtienen los valores del diccionario de N-gramas en forma de lista
	keysDictCache = list(dictNgramCache.keys()) #Se obtienen las claves del diccionario de N-gramas Caché en forma de lista
	valuesDictCache= list(dictNgramCache.values()) #Se obtienen los valores del diccionario de N-gramas Caché en forma de lista

	infinitives_array = [] #Se inicializa la lista de infinitivos
	for verbs in verbs_array: #Se recorren todos los verbos para adjuntar a la lista sus infinitivos (primera posición del array donde aparecen todas las conjugaciones para cada verbo)
		single_verbs = verbs.split(',')
		infinitives_array.append(single_verbs[0].lower())

	sentenceWords = path.split() #Se convierte la frase inicial en una lista de palabras
	for word in sentenceWords: #Se comprueba si cada palabra es un infinitivo
		if word in infinitives_array: #Si lo es, se intercambia por su conjugación más probable
			indexVerb = infinitives_array.index(word) #Primero, se identifica el verbo encontrado
			conj = verbs_array[indexVerb].split(',') #Para recoger todas sus formas verbales en una lista
			nGram = final_path #Luego, se forma el N-grama anterior al verbo encontrado. 
			while len(nGram) > maxNgram: #Si es mayor que la longitud máxima, se van eliminando las palabras iniciales hasta ajustar su longitud
				nGram.pop(0)

			maxProb = -10000
			nIni = 0
			while maxProb == -10000 and nIni <= len(nGram):#Se evaluan las conjugaciones objetivo mientras no se haya encontrado ninguna palabra y el N-grama a evaluar no esté vacío
				probList = []
				for verb in conj: #Posteriormente, se evalúa cada forma verbal tras el N-grama anterior
					probGen = evaluateNgram(verb, nGram[nIni:len(nGram)], keysDict, valuesDict, 0, 1)
					probCache = evaluateNgram(verb, nGram[nIni:len(nGram)], keysDictCache, valuesDictCache, 0, 1)
					prob = (1-alfa)*probGen + alfa*probCache #La probabilidad finals se calcula ponderando la probabilidad obtenida con el diccionario general y con el caché
					probList.append(prob)
				maxProb = max(probList) #Se calcula la máxima probabilidad de entre todas las formas verbales evaluadas
				if maxProb == -10000 :#Si el N-grama completo no encuentra conjugaciones, se va acortando el N-grama eliminando las palabras iniciales
					nIni = nIni + 1
	
			indexMax = probList.index(maxProb) #Y se obtiene el índice donde ha acontecido esta máxima probabilidad 

			wordConj = conj[indexMax] #Finalmente, se recoge esta forma verbal
			final_path.append(wordConj) #Y se añade a la lista final de palabras
		else: #Si no, se añade a la lista final tal cual
			final_path.append(word)


	for i in range(lenIni): #Se eliminan las palabras de la frase inicial del resultado
		try:
			final_path.pop(0)
		except:
			final_path

	final_sentence = " ".join(final_path) #Se convierte la lista de palabras en un string que conforma la frase final

	return final_sentence #Se devuelve la frase con los verbos conjugados