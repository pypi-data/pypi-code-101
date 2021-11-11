if __name__ == '__main__':
    from source.generateGeneralLanguajeModel import generateGeneralLanguajeModel
else:
    from speako.source.generateGeneralLanguajeModel import generateGeneralLanguajeModel
import json
import os
import statistics as stats
import random

try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources

class trainer:

    def __init__(self, data_path, data_format = "txt", model = "base", model_dir = "./", language = "es"):
        """
		Description:
		initialization method

		Inputs:
        - data_path (str): The absolute path for the file with the phrases that will be used as data.
        The class also provides a method to train with multiple files at once, in case that's desired then
        pass any path to this parameter and provide the correct path for the multiple files directory
        when the train_multiple method is called.
        - data_format (str, optional): one of "json", "txt" or "any". Ensurance that the file is 
        correctly loaded, the data format of the file will be detected and compared to this parameter. 
        It can be one of two: "json" or "txt". Pass "any" if you don't want any checking of data format. 
        Specially important when using the multiple_train method.
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
        self._data_path = data_path
        self._data_format = data_format
        self._model = model
        self._model_dir = model_dir
        self._language = language

        #Initialization of model files data
        self._listWords = ['.', '?','!'] 
        self._listWordsInf = ['.', '?','!'] 
        self._dictNgram = {} 
        self._dictNgramInf = {} 
        self._dictBackoff = {} 
        self._dictBackoffInf = {}

        self._verbsArray = self._load_language()

    def _model_exists(self):
        """
        Description:
        method to check if the defined model already exists
        """
        return any([self._model == m for m in os.listdir(self._model_dir)])
        
    def _model_loaded(self):
        """
        Description:
        checks if the model files have already been loaded (true) of if they are on initialized mode (false)
        """
        return not all((self._listWords == [".", "?", "!"],
					    self._listWordsInf == [".", "?", "!"],
					    self._dictNgram == {},
					    self._dictNgramInf == {},
					    self._dictBackoff == {},
					    self._dictBackoffInf == {},
				        ))

    def _model_status(self):
        """
        Description
        method for checking the current status of the model, and asking the user if they want to continue
        or stop the training process and change some stuff before training again
        """
        if self._model_loaded():
            while True:
                print("There's already a model loaded into the instance, will continue training data on it.")
                print("If you were trying to train a completely new model stop this process and move this model folder from the model directory or change the model parameter.")
                ans = str(input("Keep training? [[y]/n]: "))
                if ans == "y" or ans == "":
                    print("Starting training on already loaded model.")
                    break
                elif ans == "n":
                    raise KeyboardInterrupt("Training process stopped.")
                else:
                    print("Invalid option.")
        else:
            if self._model_exists():
                while True:
                    print("Another model with the same name was found on the models directory.")
                    print("If you continue the training this model will be loaded and trained on.")
                    print("If you were trying to train a completely new model stop this process and move this model folder from the model directory or change the model parameter.")
                    ans = str(input("Keep training? [[y]/n]: "))
                    if ans == "y" or ans == "":
                        self._load_model()
                        print("Model loaded, starting training on it.")
                        break
                    elif ans == "n":
                        raise KeyboardInterrupt("Training process stopped.")
                    else:
                        print("Invalid option.")
            else:
                print("Starting training with a brand new model.")


    def _load_model(self):
        """
        Description:
        method for loading the model files
        """
        load_dir = os.path.join(self._model_dir, self._model)
        try:
            f = open(os.path.join(load_dir, "listWords.txt"), "r")
            content = f.read()
            self._listWords = content.split("\n")
            f.close()
            
            f = open(os.path.join(load_dir, "listWordsInf.txt"), "r")
            content = f.read()
            self._listWordsInf = content.split("\n")
            f.close()
            
            f = open(os.path.join(load_dir, "dictNgram.txt"), "r")
            self._dictNgram = json.load(f)
            f.close()
            
            f = open(os.path.join(load_dir, "dictNgramInf.txt"), "r")
            self._dictNgramInf = json.load(f)
            f.close()
            
            f = open(os.path.join(load_dir, "dictBackoff.txt"), "r")
            self._dictBackoff = json.load(f)
            f.close()
            
            f = open(os.path.join(load_dir, "dictBackoffInf.txt"), "r")
            self._dictBackoffInf = json.load(f)
            f.close()
        
        except FileNotFoundError as e:
            print("The model loading process failed because: ", e)
            print("Will set the model data to a new instance.")
            self._listWords = ['.', '?','!'] 
            self._listWordsInf = ['.', '?','!'] 
            self._dictNgram = {} 
            self._dictNgramInf = {} 
            self._dictBackoff = {} 
            self._dictBackoffInf = {}

    def _train_model(self, train_file, train_file_format):
        """
        Description:
        method for carrying out the training process, it's done sepparately to reuse it for both the train and train multiple.
        """
        [self._listWords, self._listWordsInf, 
        self._dictNgram, self._dictNgramInf, 
        self._dictBackoff, self._dictBackoffInf] = generateGeneralLanguajeModel(train_file_format, train_file, 
                                                                                self._listWords, self._listWordsInf, 
                                                                                self._dictNgram, self._dictNgramInf, 
                                                                                self._dictBackoff, self._dictBackoffInf, 
                                                                                self._verbsArray)
    
    def _save_model(self):
        """
        Description:
        method for saving the model files
        """
        save_dir = os.path.join(self._model_dir, self._model)

        f = open(os.path.join(save_dir, "listWords.txt"), "w")
        for word in self._listWords[:-1]:
            f.write(word+'\n')
        f.close()
        f = open(os.path.join(save_dir, "listWords.txt"), "a")
        f.write(self._listWords[-1])
        f.close()
        
        f = open(os.path.join(save_dir, "listWordsInf.txt"), "w")
        for word in self._listWordsInf[:-1]:
            f.write(word+'\n')
        f.close()
        f = open(os.path.join(save_dir, "listWordsInf.txt"), "a")
        f.write(self._listWordsInf[-1])
        f.close()
        
        f = open(os.path.join(save_dir, "dictNgram.txt"), "w")
        json.dump(self._dictNgram, f)
        f.close()
        
        f = open(os.path.join(save_dir, "dictNgramInf.txt"), "w")
        json.dump(self._dictNgramInf, f)
        f.close()
        
        f = open(os.path.join(save_dir, "dictBackoff.txt"), "w")
        json.dump(self._dictBackoff, f)
        f.close()
        
        f = open(os.path.join(save_dir, "dictBackoffInf.txt"), "w")
        json.dump(self._dictBackoffInf, f)
        f.close()

    def _load_language(self):
        """
        Description:
        method to load the language from
        """
        try:
            if __name__ == '__main__':
                scan_path = os.path.join("lang", f"{self._language}-verbs.txt")
                verb_file = open(scan_path, encoding="utf-8") #Se abre el archivo que contiene todas las formas verbales de los verbos en español
            else:
                from . import lang
                verb_file = pkg_resources.open_text(lang, f"{self._language}-verbs.txt")
            va = verb_file.read().split()
        except FileNotFoundError:
            print("""The language input does not exist in our database, check if the input was
            right or raise an issue on our github page in case it's not loaded yet.""")
            va = None
        return va

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

    def train(self, check_model_status = True):
        """
        Description:
        method for carrying out the training on the file define on initialization or with the trainer.new_data method.
        If check_model_status is set to True the algorithm will check for other instances of the model
        both loaded on memory or saved on the models directory. In case it finds any of those, it'll ask
        the user if they want to keep the training going or stop it to make some modifications to avoid overwrite.
        If declared data_format is not "any" it'll check the filetype and stop the training process if 
        these are not the same. Althoug setting it to "any" is easier, it's not recommended since it can
        wrongly include files that are not supposed to act as training files and break the model data.
        After training, it saves the model files inside a folder with the model name in the models directory.

        Inputs:
        - check_model_staus (boolean, optional): if True will check for other instances of the model in memory or
        inside the models directory, and ask the user on wether to keep training with these or not. Default is True.

        Outputs:
        None
        """
        if check_model_status:
            self._model_status()

        detected_format = self._data_path.split(".")[-1]
        if detected_format == self._data_format or self._data_format == "any":
            passing_format = detected_format
        else:
            raise ValueError(f'The detected format "{detected_format}" does not coincide with the passed format "{self._data_format}"')

        self._train_model(self._data_path, passing_format)

        if not self._model_exists():
            os.mkdir(os.path.join(self._model_dir, self._model))
        self._save_model()

    def train_multiple(self, files_dir, check_model_status = True, save_progress = True, remove_done = False):
        """
        Description:
        method for carrying out the training on the files found on files_dir.
        If check_model_status is set to True the algorithm will check for other instances of the model
        both loaded on memory or saved on the models directory. In case it finds any of those, it'll ask
        the user if they want to keep the training going or stop it to make some modifications to avoid overwrite.
        If declared data_format is not "any" it'll check the filetype and skip them from the training process if 
        these are not the same. Althoug setting it to "any" is easier, it's not recommended since it can
        wrongly include files that are not supposed to act as training files and break the model data.

        Inputs:
        - files_dir (str): absolute path to the directory where the training files are located.
        - check_model_staus (boolean, optional): if True will check for other instances of the model in memory or
        inside the models directory, and ask the user on wether to keep training with these or not. Default is True.
        - save_progress (boolean, optional): if True, will save the model files progressively after it's done 
        training each file, and log which files still need to be trained on, in case the algorithm crashes. 
        Otherwise it will only save the progress after all the training progress is finished. Default is True.
        - remove_done (boolean, optional): if True, will remove each file after training on it is done. CAUTION:
        this is not recommended unless a safe copy of the training files is done, in which case is useful to track
        the training progress and continue it in case the ejecution crashes.

        Outputs:
        None
        """
        if check_model_status:
            self._model_status()

        if self._data_format == "any":
            datapath_list = os.listdir(files_dir)
            format_list = [f.split(".")[-1] for f in datapath_list]
        else:
            datapath_list = [f for f in os.listdir(files_dir) if f.split(".")[-1] == self._data_format]
            format_list = [self._data_format]*len(datapath_list)

        for data, form in zip(datapath_list, format_list):
            self._train_model(os.path.join(files_dir, data), form)

            if save_progress:
                if not self._model_exists():
                    os.mkdir(os.path.join(self._model_dir, self._model))
                self._save_model()
                print(f'Saved model in training progress up to {data}.')
                print(f'-> Remaining: {datapath_list[datapath_list.index(data)+1:]}.')

            if remove_done:
                os.remove(os.path.join(files_dir, data))

        if not self._model_exists():
            os.mkdir(os.path.join(self._model_dir, self._model))
        self._save_model()
    
    def new_data(self, data_path, **kwargs):
        """
        Description:
        method for changing the data and/or data format set on initialization.

        Inputs:
        - data_path (str): The absolute path for the file with the phrases that will be used as data.
        - data_format (str, optional): one of "json", "txt" or "any". Ensurance that the file is 
        correctly loaded, the data format of the file will be detected and compared to this parameter. 
        It can be one of two: "json" or "txt". Pass "any" if you don't want any checking of data format.

        Outputs:
        None
        """
        if "data_format" in kwargs.keys():
            self._data_format = kwargs["data_format"]
        self._data_path = data_path
        print("New data loaded.")

    def data_summary(self):
        """
        Description:
        method to generate and log a summary of the dataset characteristics, such as average word count,
        empty sentences; and some examples of how the model will receive this data.

        Inputs:
        None

        Outputs:
        None
        """
        if self._data_format == "txt":
            with open(self._data_path, "r", encoding="utf-8") as f:
                data = f.read().split("\n")
                f.close()
        elif self._data_format == "json":
            with open(self._data_path, "r", encoding="utf-8") as f:
                data_dict = json.load(f)
                data = [d["frase"] for d in data_dict]
                f.close()

        print("-->> Data Summary: <<--")
        print(f'The database has {len(data)} sentences to train with.')
        print(">> These are some of them:")
        for r in [random.randint(0, len(data)-1) for _ in range(5)]:
            print(f'{r}) {data[r]}\n')
        lens = [len(s.split(" ")) for s in data]
        mean = stats.mean(lens)
        std = stats.stdev(lens, mean)
        print('<- - - - ->')
        print(f'Roughly the amount of words per sentence is {int(mean)} +/- {[int(std) if int(std) != 0 else 1][0]}')
        oddball = [i for i in range(len(lens)) if (lens[i] <= mean - 3*std or lens[i] >= mean +3*std)]
        if len(oddball) > 0:
            print(f'{len(oddball)} of them are way off the average amount of words per sentence. This is nothing bad but maybe you should check this is not a bug in the database')
            print(f'These are {oddball}')
        empties = [i for i in range(len(lens)) if (lens[i] == 0 or data[i] == "" or data[i] == " ")]
        if len(empties)>0:
            print('\n<- - - - ->')
            print(f'Some of the phrases are empty. This might raise errors and bugs. We suggest checking them.')
            print(f'These are {empties}')

if __name__ == "__main__":

    tr = trainer("example_database/example.txt", model="en-ex")
    tr.data_summary()
    tr.train()
    