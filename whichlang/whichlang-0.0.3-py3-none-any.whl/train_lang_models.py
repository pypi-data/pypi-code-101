import os
import sys
import argparse
try:
    import cPickle as pickle
except:
    import pickle
from whichlang import cleanup_data, get_input_ngrams, get_ngram_ranks
from whichlang import LANGUAGE_MODELS


def create_language_model(data, language):
    """[summary]

    Args:
        data ([string]): [input data for training]
        language ([type]): [language]
    """
    data = cleanup_data(data)
    input_ngrams = get_input_ngrams(data)
    input_ngram_ranks = get_ngram_ranks(input_ngrams)
    name = '{0}\\{1}.p'.format(LANGUAGE_MODELS, language)
    pickle.dump(input_ngram_ranks, open(name, "wb"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', required=True, help="input file")
    parser.add_argument('-l', required=True, help="language")
    args = parser.parse_args()
    language = args.l
    with open(args.f) as file:
        data = file.read()
    file.close()
    create_language_model(data, language)
    return


if __name__ == "__main__":
    main()
