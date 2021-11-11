if __name__ == '__main__':
	from source.calcularPrediccionCache import calcularPrediccionCache
	from source.calcularPrediccionMultPal import calcularPrediccion
	from source.generateCacheLanguajeModel import generateCacheLanguajeModel
else:
	from speako.source.calcularPrediccionCache import calcularPrediccionCache
	from speako.source.calcularPrediccionMultPal import calcularPrediccion
	from speako.source.generateCacheLanguajeModel import generateCacheLanguajeModel
import json
import os

try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources

class predictor:

	# --- Private Methods ---
	_inCaseNoDefaultPathsIsFound = "quiero, hola, yo, estás, comer,\
									la, tengo, con, a, jugar"
	def __init__(self, model = "base", model_dir = "./", language = "es"):
		"""
		Description:
		initialization method

		Inputs:
		- model (str, optional): The name of the model that's going to be used for the prediction.
		There should be a folder with the same name as this on the model's directory that
		contains the corresponding files for this model. Default is "base".
		- model_dir (str, optional): The absolute path to the directory where the model and language files
		are stored. If they are located where the model is being executed from this parameter can be
		left as default.
		- language (str, optional): This is the language that will be used for the prediction. On
		the model's directory there should be a folder name "verb-conj" with the verb conjugations for each
		language named "lang-verbs.txt" where "lang" is a short string representing each language: "es" for 
		spanish, "en" for english and so.

		Outputs:
		predictor (Instance of predictor Class)
		"""
		self._model = model
		if model_dir == "":
			self._model_dir = os.getcwd()
		else:
			self._model_dir = model_dir
		self._language = language

		self._load_model()

	def _load_model(self):
		(self._listWords, self._listWordsInf) = self._load_listWords()
		(self._dictNgram, self._dictNgramInf
		, self._dictBackoff, self._dictBackoffInf)  = self._load_dicts()
		(self._listWordsCache, self._listWordsInfCache) = self._load_listWords(is_cache = True)
		(self._dictNgramCache, self._dictNgramInfCache
		, self._dictBackoffCache, self._dictBackoffInfCache)  = self._load_dicts(is_cache = True)
		self._verbsArray = self._load_language()
		self._defaultPaths = self._load_def_paths()

	def _load_listWords(self, is_cache = False):
		if is_cache:
			scan_dir = os.path.join(self._model_dir, "cache")
			print("Loading files from:", scan_dir)
			try:
				f = open(os.path.join(scan_dir, "listWordsCache.txt"), "r")
				content = f.read()
				lw = content.split("\n")
				f.close()

				f = open(os.path.join(scan_dir, "listWordsInfCache.txt"), "r")
				content = f.read()
				lwi = content.split("\n")
				f.close()
			except FileNotFoundError:
				lw, lwi = [".", "?", "!"], [".", "?", "!"] 
		else:
			scan_dir = os.path.join(self._model_dir, self._model)
			print("Loading files from:", scan_dir)
			try:
				f = open(os.path.join(scan_dir, "listWords.txt"), "r")
				content = f.read()
				lw = content.split("\n")
				f.close()

				f = open(os.path.join(scan_dir, "listWordsInf.txt"), "r")
				content = f.read()
				lwi = content.split("\n")
				f.close()
			except FileNotFoundError:
				print("The model you're trying to use does not exist, please check the model name or models directory.")
				lw, lwi = None, None
		return lw, lwi

	def _load_dicts(self, is_cache = False):
		if is_cache:
			scan_dir = os.path.join(self._model_dir, "cache")
			print("Loading files from:", scan_dir)
			try:
				f = open(os.path.join(scan_dir, "dictNgramCache.txt"), "r")
				dn = json.load(f)
				f.close()
				#nTot = list(dictNgram.values())[0][3]#Tamaño del diccionario de N-gramas principal

				f = open(os.path.join(scan_dir, "dictNgramInfCache.txt"), "r")
				dni = json.load(f)
				f.close()

				f = open(os.path.join(scan_dir, "dictBackoffCache.txt"), "r")
				db = json.load(f)
				f.close()

				f = open(os.path.join(scan_dir, "dictBackoffInfCache.txt"), "r")
				dbi = json.load(f)
				f.close()
			except FileNotFoundError:
				dn, dni, db, dbi = {}, {}, {}, {}
		else:
			scan_dir = os.path.join(self._model_dir, self._model)
			print("Loading files from:", scan_dir)
			try:
				f = open(os.path.join(scan_dir, "dictNgram.txt"), "r")
				dn = json.load(f)
				f.close()
				#nTot = list(dictNgram.values())[0][3]#Tamaño del diccionario de N-gramas principal

				f = open(os.path.join(scan_dir, "dictNgramInf.txt"), "r")
				dni = json.load(f)
				f.close()

				f = open(os.path.join(scan_dir, "dictBackoff.txt"), "r")
				db = json.load(f)
				f.close()

				f = open(os.path.join(scan_dir, "dictBackoffInf.txt"), "r")
				dbi = json.load(f)
				f.close()
			except FileNotFoundError:
				print("The model you're trying to use does not exist, please check the model name or models directory.")
				dn, dni, db, dbi = None, None, None, None
		return dn, dni, db, dbi

	def _load_language(self):

		try:
			if __name__ == '__main__':
				scan_path = os.path.join("lang", f"{self._language}-verbs.txt")
				verb_file = open(scan_path, encoding="utf-8") #Se abre el archivo que contiene todas las formas verbales de los verbos en español
			else:
				verb_file = pkg_resources.open_text(__package__, f"{self._language}-verbs.txt")
			va = verb_file.read().split()
		except FileNotFoundError:
			print("""The language input does not exist in our database, check if the input was
				right or raise an issue on our github page in case it's not loaded yet.""")
			va = None
		return va

	def _load_def_paths(self):
		scan_path = os.path.join(self._model_dir, "listDefaultPaths.txt")
		print("Loading files from:", scan_path)
		try:
			verb_file = open(scan_path, "r", encoding="utf-8") 
			dp = verb_file.read().split()
		except FileNotFoundError:
			print("Could not find a default path file, so we'll set the default paths to:")
			print(self._inCaseNoDefaultPathsIsFound)
			dp = self._inCaseNoDefaultPathsIsFound.split(", ")
		return dp

	def _is_cache_initial(self):
		return any((self._listWordsCache == [".", "?", "!"],
					self._listWordsInfCache == [".", "?", "!"],
					self._dictNgramCache == {},
					self._dictNgramInfCache == {},
					self._dictBackoffCache == {},
					self._dictBackoffInfCache == {},
				  ))

	def change_model_params(self, **kwargs):
		"""
		Description: 
		method to change the parameters used for the prediction.

		Inputs:
		- model (str, optional): The name of the model that's going to be used for the prediction.
		There should be a folder with the same name as this on the model's directory that
		contains the corresponding files for this model. If not passed, the model name stays the same.
		- model_dir (str, optional): The absolute path to the directory where the model and language files
		are stored. If they are located where the model is being executed from this parameter can be
		passed a "./". If not passed, the model dir stays the same.
		- language (str, optional): This is the language that will be used for the prediction. On
		the model's directory there should be a folder name "verb-conj" with the verb conjugations for each
		language named "lang-verbs.txt" where "lang" is a short string representing each language: "es" for 
		spanish, "en" for english and so. If not passed, the model language stays the same.

		Outputs:
		None
		"""
		for k in kwargs.keys():
			if k == "model":
				self._model = kwargs[k]
			elif k == "model_dir":
				self._model_dir = kwargs[k]
			elif k == "language":
				self._language = kwargs[k]
			else:
				print(f'{k} is not a valid parameter.')
		self._load_model()

	def get_model_description(self):
		"""
		Description:
		logs the model parameters including model name, directory and language, which
		can be changed with the change_model_params method.

		Inputs:
		None

		Outputs:
		None
		"""
		print(f'The currently load model is:\n \
				\t-> model name: {self._model}\n \
				\t-> model directory: {self._model_dir}\n \
				\t-> language: {self._language}')

	def predict(self, sentence = "", maxNgram = 5, maxNumPaths = 4, maxNumWords = 1, cacheAlfa = 0.6):
		"""
		Description:
		method in charge of carrying out the prediction on a certain phrase and returning a dictionary with
		the predicted options as output. Other than "sentence" which takes the partial phrase to make
		predictions on, other parameters control how the prediction will be done.

		Inputs:
		- sentence (str, optional): partial phrase to make predictions on. Default is empty phrase, where
		the model will provide the default starting paths.
		- maxNgram (int, optional): max amount of words from last to first the model will use for the
		predictions. For example, for the phrase "I want a candy" with maxNgram=3 the model will use "candy", "a candy"
		and "want a candy" as bases for the prediction. The higher this value is the more accurate the 
		prediction will be, but the longer it'll take. Default is 5.
		- maxNumPaths (int, optional): max possible options the model will offer predictions for. The higher
		this number is, the more options for continuing the phrase the model might predict, but the longer it'll take.
		Default is 4.
		- maxNumWords (int, optional): max amount of words the algorithm will try to go for on a each prediction.
		For example, with a maxNumWords=3, for the phrase "Hi" the model might predict "what's up" (2 words) or
		"my name is" (3 words), but with maxNumWords=1 it'll predict "my" or "what's".
		- cacheAlfa (float, optional): ratio, between 0 and 1, of the prediction that will come from the cache database.

		Outputs:
		-jsonPathsConjugated (dict): dictionary with the number of prediction as keys and the predictions as values. 
		"""
		if self._is_cache_initial():
			json_pathsConjugated = calcularPrediccion(sentence, maxNgram, maxNumPaths, maxNumWords, 
													self._listWords, self._listWordsInf, 
													self._dictNgram, self._dictNgramInf, 
													self._dictBackoff, self._dictBackoffInf, 
													self._verbsArray, self._defaultPaths
													)
		else:
			json_pathsConjugated = calcularPrediccionCache(sentence, maxNgram, maxNumPaths, maxNumWords, 
													self._listWords, self._listWordsInf, 
													self._dictNgram, self._dictNgramInf, 
													self._dictBackoff, self._dictBackoffInf,
													self._listWordsInfCache, 
													self._dictNgramCache, self._dictNgramInfCache, 
													self._dictBackoffInfCache, 
													self._verbsArray, self._defaultPaths,
													cacheAlfa
													)

		return json_pathsConjugated

	def update_cache(self, sentence):
		"""
		Description:
		method dedicated to updating the data in the cache folder on the model's directory
		(or initializing it for the first time). This cache data works as a separate model that
		complements the prediction made by the main model to adapt it to each particular user.
		When a sentence is passed as a parameter, the cache model will be updated on said phrase,
		making it more likely to appear as a prediction on following predictions, even when
		the main model is not updated on that phrase.

		Inputs:
		- sentence (str): sentence the cache model will be updated on.

		Outputs:
		None
		"""
		cache_dir = os.path.join(self._model_dir, "cache")
		sen_json_path = os.path.join(cache_dir, "newSentenceCache.json")
		f = open(sen_json_path, "w")
		sen_dict = {"frase": sentence}
		json_data = json.dumps(sen_dict) #Se convierte el diccionario en un string JSON
		json_paths = json.loads(json_data) # Se crea el objeto JSON
		f.write("[")
		json.dump(json_paths,f)
		f.write("]")
		f.close()
		(self._listWordsCache, self._listWordsInfCache, 
		self._dictNgramCache, self._dictNgramInfCache, 
		self._dictBackoffCache, self._dictBackoffInfCache) = generateCacheLanguajeModel("json", sen_json_path, 
																				self._listWordsCache, self._listWordsInfCache, 
																				self._dictNgramCache, self._dictNgramInfCache, 
																				self._dictBackoffCache, self._dictBackoffInfCache, 
																				self._verbsArray)

		f = open(os.path.join(cache_dir, "listWordsCache.txt"), "w")
		for word in self._listWordsCache:
			if word == self._listWordsCache[len(self._listWordsCache)-1]:
				f.write(word)
			else:
				f.write(word+'\n')
		f.close()

		f = open(os.path.join(cache_dir, "listWordsInfCache.txt"), "w")
		for word in self._listWordsInfCache:
			if word == self._listWordsInfCache[len(self._listWordsInfCache)-1]:
				f.write(word)
			else:
				f.write(word+'\n')
		f.close()

		f = open(os.path.join(cache_dir, "dictNgramCache.txt"), "w")
		json.dump(self._dictNgramCache, f)
		f.close()

		f = open(os.path.join(cache_dir, "dictNgramInfCache.txt"), "w")
		json.dump(self._dictNgramInfCache, f)
		f.close()

		f = open(os.path.join(cache_dir, "dictBackoffCache.txt"), "w")
		json.dump(self._dictBackoffCache, f)
		f.close()

		f = open(os.path.join(cache_dir, "dictBackoffInfCache.txt"), "w")
		json.dump(self._dictBackoffInfCache, f)
		f.close()
	
	#Missing: adding updating cache to interactive, since now it is crashing
	def interactive_predict(self, sentence = "", maxNgram = 5, maxNumPaths = 4, maxNumWords = 1, 
							cacheAlfa = 0.6, cache_update = "none"):
		"""
		Description:
		this is method implements a basic example of an application made with
		the help of this class, where the sentence and params are passed to the predictor,
		the results of the prediction are shown and the user input is solicitated to choose
		one, which is used then to build up on the sentence and run the prediction again, repeating
		the process untill the user stops it with and input of 0.

		Inputs:
		cache_update (str, optional): this can be "all", to update cache after every prediction;
		"final" to update it only when the user finishes the sentence building, or "none" for the cache not to
		be updated by this method. Default is "none".
		See predictor.predict method for the description of the parameters.

		Outputs:
		final (str): when the user inputs a 0 the process is terminated and the final sentence
		is returned as a string.
		"""

		if all([cache_update != s for s in ["all", "final", "none"]]):
			raise ValueError(f'{cache_update} is not a valid option for cache_update. See doc to check available options.')

		choice = -1
		paths = self.predict(sentence, maxNgram , maxNumPaths, maxNumWords, cacheAlfa)
		print(f'Prediction for {sentence}:')
		print(paths)
		while choice != 0:
			try:
				choice = int(input("Enter your choice, or 0 to end prediction: "))
				if 0 < choice < len(paths) + 1:
					sentence += (" " + paths[str(choice)]) 
					paths = self.predict(sentence, maxNgram , maxNumPaths, maxNumWords, cacheAlfa)
					print(f'Prediction for {sentence}:')
					print(paths)
					if cache_update == "all":
						self.update_cache(sentence)
				elif choice == 0:
					print(f'Sentence ended as {sentence}')
					if cache_update == "final":
						self.update_cache(sentence)
					return sentence
				else:
					print(f'Invalid input, should be a value greater or equal than zero and lesser or equal than {len(paths)}.')
			except ValueError:
				print(f'Invalid input, should be a value greater or equal than zero and lesser or equal than {len(paths)}.')

if __name__ == "__main__":

	pred = predictor(model = "med", model_dir="C:/Users/Juanma/OTTAA - Lixi/PictogramsPredictionsLibrary/")
	final = pred.interactive_predict("Quiero", cache_update = "all")
	print(final)