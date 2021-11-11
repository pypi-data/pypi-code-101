import json
if __name__ == "__main__":
	from generateGeneralLanguajeModel import addSentenceToDictionary
	from generateGeneralLanguajeModel import replacePunctuation
	from generateGeneralLanguajeModel import replaceToInfinitive
	from generateGeneralLanguajeModel import generateDictBackoffKatz
else:
	from speako.source.generateGeneralLanguajeModel import addSentenceToDictionary
	from speako.source.generateGeneralLanguajeModel import replacePunctuation
	from speako.source.generateGeneralLanguajeModel import replaceToInfinitive
	from speako.source.generateGeneralLanguajeModel import generateDictBackoffKatz

def generateCacheLanguajeModel(fileFormat, arg, listWords, listWordsInf, dictNgram, dictNgramInf, dictBackoff, dictBackoffInf, verbs_array): 
	#Función que crea el modelo de lenguaje general de N-gramas (con N<=5) a partir de un archivo .txt o un array JSON
	"""Parámetros de entrada:
		- fileFormat: Formato del archivo a procesar
		- arg: Archivo a procesar
		- listWords: Lista existente de palabras añadidas al diccionario de N-gramas
		- listWordsInf: Lista existente de palabras añadidas al diccionario de N-gramas de infinitivos
		- dictNgram: Diccionario existente de N-gramas
		- dictNgramInf: Diccionario existente de N-gramas de infinitivos
		- dictBackoff: Diccionario existente de backoff por bigramas
		- dictBackoffInf: Diccionario existente de backoff por bigramas de infinitivos
		Resultado:
		- listWords: Lista actualizada de palabras añadidas al diccionario de N-gramas
		- listWordsInf: Lista actualizada de palabras añadidas al diccionario de N-gramas de infinitivos
		- dictNgram: Diccionario actualizado de N-gramas
		- dictNgramInf: Diccionario actualizado de N-gramas de infinitivos
		- dictBackoff: Diccionario actualizado de backoff por bigramas
		- dictBackoffInf: Diccionario actualizado de backoff por bigramas de infinitivos"""

	keySentence = "frase" #Parámetro del array JSON que contiene la frase
	keyWeight = "frecuencia" #Parámetro del array JSON que contiene la frecuencia de ocurrencia de la frase
	valid = True #Indica si el archivo proporcionado es válido para su procesado
	maxNgramSize = 5 #Tamaño máximo de los N-gramas
	finishOperators = ['.', '?','!']  #Carácteres que identifican el final de una frase

	if fileFormat == 'txt': #Caso de archivos .txt que contienen una frase por línea
		input_file = open(arg, encoding="utf-8") #Apertura del archivo .txt con el formato de codificación de caracteres UTF-8, indicado para el uso de caracteres especiales como vocales con tilde o letra Ñ.
		input_file_filtered = replacePunctuation(input_file.read()) #Ver explicación en la función
		text_array = input_file_filtered.split('\n') #Separación del archivo en frases, a partir del caracter \n que indica una nueva línea

		for item in text_array: #Procesado de cada frase para su inclusión en el modelo de lenguaje
			words = item.split() #Se separa la frase en palabras
			wordsInf = replaceToInfinitive(words, verbs_array) #Se obtienen las frases pasando todos los verbos a infinitivo

			for w in words: #Se incluyen las nuevas palabras en la lista de palabras 
				if w.lower() not in listWords:
					listWords.append(w.lower())
			for wI in wordsInf: #Se incluyen las nuevas palabras en la lista de palabras que solo incluye infinitivos
				if wI.lower() not in listWordsInf:
					listWordsInf.append(wI.lower())

			weight = 1 #Cada nueva frase se suma con peso 1 a los diccionarios existentes.

			sizeSentence = len(words) #Tamaño de la frase en número de palabras
			if(sizeSentence > 0):	#Si la frase no acaba en un signo de puntuación, se le añade uno. En este caso el punto.
				if words[sizeSentence-1] not in finishOperators:
					words.append('.') 
					wordsInf.append('.') 

			for nSize in range(maxNgramSize+1): #Se generan los N-gramas contenidos en la frase que está siendo analizada. Desde el 1-grama (diccionario de palabras) al N-grama.
				dictNgram = addSentenceToDictionary(words, weight, dictNgram, nSize)
				dictNgramInf = addSentenceToDictionary(wordsInf, weight, dictNgramInf, nSize)

	elif fileFormat == "json": #Caso de arrays JSON
		input_file = open(arg, encoding="utf-8") #Apertura del array JSON con el formato de codificación de caracteres UTF-8, indicado para el uso de caracteres especiales como vocales con tilde o letra Ñ.
		json_array = json.load(input_file) #Carga del array separado por objetos JSON.
		
		for item in json_array: 
			words = replacePunctuation(item[keySentence]).split() #Se obtiene la frase del array JSON, se separa en palabras y se procesan los signos de puntuación (ver explicación en función 'replacePunctuation')
			wordsInf = replaceToInfinitive(words, verbs_array) #Se obtienen las frases pasando todos los verbos a infinitivo
			for w in words: #Se incluyen las nuevas palabras en la lista de palabras 
				if w.lower() not in listWords:
					#print(w)
					listWords.append(w.lower())
			for wI in wordsInf: #Se incluyen las nuevas palabras en la lista de palabras que solo incluye infinitivos
				if wI.lower() not in listWordsInf:
					listWordsInf.append(wI.lower())
			weight = 1 #Cada nueva frase se suma con peso 1 a los diccionarios existentes.

			sizeSentence = len(words) #Tamaño de la frase en número de palabras
			if(sizeSentence > 0): #Si la frase no acaba en un signo de puntuación, se le añade uno. En este caso el punto.
				if words[sizeSentence-1] not in finishOperators:
					words.append('.')
					wordsInf.append('.')

			for nSize in range(maxNgramSize+1): #Se generan los N-gramas contenidos en la frase que está siendo analizada. Desde el 1-grama (diccionario de palabras) al N-grama.
				dictNgram = addSentenceToDictionary(words, weight, dictNgram, nSize)
				dictNgramInf = addSentenceToDictionary(wordsInf, weight, dictNgramInf, nSize)

	else: #Si el formato de archivo introducido no es válido, se le indica al usuario. Además, se cambia el boolean 'valid' a falso.
		print('Formato no válido. Indique "txt" o "json".')
		valid = False

	if valid: #Se generan los diccionarios del parámetro Backoff tanto para el diccionario regular como para el de infinitivos si se ha proporcionado un archivo de entrada válido
		dictBackoff = generateDictBackoffKatz(dictNgram) 
		dictBackoffInf = generateDictBackoffKatz(dictNgramInf)

	return listWords, listWordsInf, dictNgram, dictNgramInf, dictBackoff, dictBackoffInf #Se devuelven las listas de palabras y diccionarios generados
	