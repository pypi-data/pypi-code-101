if __name__ == "__main__":
	from generateGeneralLanguajeModel import replaceToInfinitive
	from viterbiNbestCache import viterbiNbestCache
	from viterbiNbestCache import conjugateSentenceCache
	from viterbiNbest import convertToJSON
else:
	from speako.source.generateGeneralLanguajeModel import replaceToInfinitive
	from speako.source.viterbiNbestCache import viterbiNbestCache
	from speako.source.viterbiNbestCache import conjugateSentenceCache
	from speako.source.viterbiNbest import convertToJSON


def calcularPrediccionCache(sentence, maxNgram, maxNumPaths, maxNumWords, listWords, listWordsInf, dictNgram, dictNgramInf, dictBackoff, dictBackoffInf, listWordsCacheInf, dictNgramCache, dictNgramCacheInf, dictBackoffCacheInf, verbs_array, listDefaultPaths, alfa): 
	#Función que realiza la predicción a partir de una frase dada y devuelve los resultados en un array JSON. Utiliza diversas funciones creadas en el archivo 'viterbiNbest'.
	"""Parámetros de entrada:
		- sentence: frase inicial a continuar
		- maxNgram: máximo orden de los N-gramas a evaluar. Por defecto: 5
		- maxNumPaths: máximo número de soluciones a devolver
		- maxNumWords: máximo número de palabras de las frases solución
		- listWords: listado de todas las palabras que aparecen en el diccionario de N-gramas
		- listWordsInf: listado de todas las palabras que aparecen en el diccionario de N-gramas con todos los verbos en infinitivos
		- dictNgram: diccionario de N-gramas
		- dictNgramInf: diccionario de N-gramas de infinitivos
		- dictBackoff: diccionario de bigramas con sus parámetros de backoff
		- dictBackoffInf: diccionario de bigramas de infinitivos con sus parámetros de backoff
		- listWordCachesInf: listado de todas las palabras que aparecen en el diccionario de N-gramas caché con todos los verbos en infinitivos
		- dictNgram: diccionario de N-gramas caché
		- dictNgramCacheInf: diccionario de N-gramas caché de infinitivos
		- dictBackoffCacheInf: diccionario caché de bigramas de infinitivos con sus parámetros de backoff
		- verbs_array: lista con todas las formas verbales de los verbos en español
		- listDefaultPaths: lista de caminos por defecto
		- alfa: peso que se le da al diccionario caché respecto al total, inlcuyendo el diccionario general (valor entre 0 y 1)

		Resultado:
		- json_pathsConjugated: array JSON con todas las predicciones calculadas (ordenadas de mayor a menor probabilidad)
		"""
	sentenceList= sentence.split() #Se convierte la frase inicial en lista de palabras
	sentenceLower = ''
	for w in range(len(sentenceList)): #Se pasan todas las palabras a minúsculas para evitar 'case sensitive'
		sentenceLower = sentenceLower + sentenceList[w].lower() + " "

	sentenceInfList = replaceToInfinitive(sentenceLower.split(), verbs_array) #Se cambian los verbos por su infinitivo
	sentenceInf = ''
	for w in range(len(sentenceInfList)): #Se convierte la lista de palabras con verbos en infinitivo en string
		sentenceInf = sentenceInf + sentenceInfList[w] + " "

	pathsSelected = viterbiNbestCache(sentenceInf, maxNgram, maxNumPaths, maxNumWords, listWordsInf, dictNgramInf, dictBackoffInf, listWordsCacheInf, dictNgramCacheInf, dictBackoffCacheInf, listDefaultPaths, alfa)  #Se ejecuta el algoritmo Viterbi Caché para obtener las predicciones de continuación de la frase inicial

	pathsConjugated = [] #Inicialización de la lista donde se guardarán las frases cuyos verbos estarán conjugados
	for path in pathsSelected: #Conjugación de todos los verbos que aparecen en las frases resultado del algoritmo Viterbi
		pathConj = conjugateSentenceCache(sentenceLower, path, maxNgram, dictNgram, dictNgramCache, verbs_array, alfa)
		pathsConjugated.append(pathConj)

	json_pathsConjugated = convertToJSON(pathsConjugated) #Se convierte la lista de resultados en array JSON

	return json_pathsConjugated #Se devuelve el array JSON