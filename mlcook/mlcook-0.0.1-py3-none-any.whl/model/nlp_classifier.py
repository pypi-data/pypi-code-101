import numpy as np
from keras.callbacks import EarlyStopping
from keras.layers import Dense, Dropout
from keras.models import Sequential
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder


class NlpClassifier:

    def fit(self, texts: np.array, y: np.array, texts_val: np.array, y_val: np.array) -> None:
        pass

    def predict(self, texts: np.array) -> np.array:
        pass

    def get_binary(self):
        pass

    def set_from_binary(self, model_binary: dict):
        pass


class TfidfNnModel(NlpClassifier):  # possible de import as NlpClassifier et modif ici

    params_tfidf = {'sublinear_tf': False,
                    'min_df': 1,  # 1
                    'analyzer': 'char',  # 'char'
                    'ngram_range': (2, 7)  # (2, 7)
                    }

    def __init__(self):
        self.tfidf = self.__get_tfidf(TfidfNnModel.params_tfidf)
        self.nn = None  # possible to add parameters here if needed

    def fit(self, texts: np.array, y: np.array, texts_val: np.array, y_val: np.array):
        # get tfidf embeddings
        embeddings_tfidf = self.tfidf.fit_transform(texts).toarray()

        # get tfidf embeddings on val data
        embeddings_tfidf_val = self.tfidf.transform(texts_val).toarray()

        # fit nn model
        self.nn = self.__compute_nn(embeddings_tfidf, y, embeddings_tfidf_val, y_val)

    def predict(self, texts: np.array) -> np.array:
        embeddings_tfidf = self.tfidf.transform(texts).toarray()
        predictions = self.nn.predict(embeddings_tfidf)
        return predictions

    def get_binary(self):
        return {'tfidf': self.tfidf, 'nn_weigths': self.nn.get_weights()}

    def set_from_binary(self, model_binary: dict):
        self.tfidf = model_binary['tfidf']
        self.nn = self.__get_nn()
        # self.nn.build(input_shape=(len(self.tfidf.idf_),))
        self.nn.set_weights(model_binary['nn_weigths'])

    def __compute_nn(self, X: np.array, y: np.array, X_val: np.array, y_val: np.array):
        ohe = OneHotEncoder()
        one_hot_encode_y = ohe.fit_transform(y.reshape(-1, 1)).toarray()
        one_hot_encode_y_val = ohe.transform(y_val.reshape(-1, 1)).toarray()
        nn = self.__get_nn()
        es = EarlyStopping(monitor='val_loss', mode='min', verbose=1,
                           patience=2, restore_best_weights=True)

        nn.fit(X, one_hot_encode_y, epochs=30, batch_size=10,
               validation_data=(np.array(X_val), one_hot_encode_y_val), shuffle=True,
               callbacks=[es])
        return nn

    @staticmethod
    def __get_tfidf(params_tfidf: dict) -> TfidfVectorizer:
        return TfidfVectorizer(**params_tfidf)

    def __get_nn(self) -> Sequential:
        nn = Sequential()
        nn.add(Dense(200, activation="relu", input_shape=(len(self.tfidf.idf_),)))
        nn.add(Dropout(0.7))
        nn.add(Dense(40, activation="relu"))
        nn.add(Dropout(0.7))
        nn.add(Dense(3, activation="softmax"))  # a completer
        nn.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return nn
