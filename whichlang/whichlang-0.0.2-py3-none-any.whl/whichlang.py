import os
import sys
import math
import re
import argparse
import codecs
import string
try:
    import cPickle as pickle
except:
    import pickle
from collections import defaultdict


LANGUAGES = {"as": "Assamese", "gu": "Gujarati", "hi": "Hindi",
             "ka": "Kannada", "ml": "Malayalam",
             "mr": "Marathi", "or": "Oriya", "pa": "Punjabi", "ta": "Tamil", "te": "Telugu"}

MIN_NGRAM_LENGTH = 1
MAX_NGRAM_LENGTH = 3
MAX_NUM_OF_NGRAMS = 1000
PENALTY = 1250
LANGUAGE_MODELS = 'language-models'


def get_input_ngrams(input):
    """[summary]

    Args:
        input ([string]): [input text by user]

    Returns:
        [list of tupeles]: [Each tuple contains ngram and its frequency]
    """
    ngram_counts = {}
    input = cleanup_data(input)
    for length in range(MIN_NGRAM_LENGTH, MAX_NGRAM_LENGTH + 1):
        for i in range(len(input) - length):
            ngram = input[i:i + length]
            if ngram in ngram_counts:
                ngram_counts[ngram] += 1
            else:
                ngram_counts[ngram] = 1
    ngram_tuples = (sorted(ngram_counts.items(),
                           key=lambda item: item[1], reverse=True))
    return ngram_tuples


def get_ngram_ranks(ngram_tuples):
    """[summary]

    Args:
        ngram_tuples ([list of tuples]): [Each tuple in the list contains an ngram and its frequency]

    Returns:
        [dictionary]: [key is ngram and value is its rank when sorted in decreasing order]
    """
    ngram_ranks = {}
    ranks_limit = MAX_NUM_OF_NGRAMS
    if len(ngram_tuples) >= MAX_NUM_OF_NGRAMS:
        ranks_limit = MAX_NUM_OF_NGRAMS
    else:
        ranks_limit = len(ngram_tuples)
    for i in range(ranks_limit):
        ngram = ngram_tuples[i][0]
        ngram_ranks[ngram] = i
    return ngram_ranks


def cleanup_data(data):
    """[summary]

    Args:
        data ([string]): [input data]

    Returns:
        [string]: [clean up of punctuations, numbers]
    """
    exclude = set(string.punctuation)
    data = ''.join(ch for ch in data if ch not in exclude)
    data = ''.join(ch for ch in data if not ch.isdigit())
    data = " " + data + " " * (MAX_NGRAM_LENGTH - 1)
    if not isinstance(data, unicode):
        return unicode(data, "utf-8", errors='strict')
    return data


def load_language_models():
    """[summary]

    Returns:
        [dictionary]: [Contains language model that was already trained for each language]
    """
    dic = {}
    for lang in LANGUAGES:
        lang_dic = pickle.load(
            open('{0}\\{1}.p'.format(LANGUAGE_MODELS, LANGUAGES[lang]), "rb"))
        dic[LANGUAGES[lang]] = lang_dic
    return dic


def get_difference(input_ngram_ranks, language_model):
    """[summary]

    Args:
        input_ngram_ranks ([dictionary]): [contains ngram and its frequency of input]
        language_model ([dictionary]): [contains ngram and frequency of language train data]

    Returns:
        [int]: [score reflecting matching ngrams between input and language]
    """
    difference = 0
    for ngram in input_ngram_ranks:
        if ngram in language_model:
            position_in_text = input_ngram_ranks[ngram]
            position_in_language = language_model[ngram]
            difference += abs(position_in_language - position_in_text)
        else:
            difference += PENALTY
    return difference


def compare_input_with_languages(language_models, input_ngram_ranks):
    """[summary]

    Args:
        language_models ([dict]): [contains ngram and its frequency of train data]
        input_ngram_ranks ([dict]): [contains ngram and frequency of input]

    Returns:
        [list]: [contains list of tuples with language and its difference with given input]
    """
    differences = []
    for language in language_models:
        difference = get_difference(
            input_ngram_ranks, language_models[language])
        differences.append((language, difference))
    return differences


def get_closest_language(differences):
    """[summary]

    Args:
        differences ([list]): [contains tuples with language and difference score]

    Returns:
        [tuple]: [containing 3 closest possible languages to given input]
    """
    # print(differences)
    differences_sorted = sorted(differences, key=lambda item: item[1])
    return differences_sorted[0][0], differences_sorted[1][0], differences_sorted[2][0]


def which_lang(input):
    """[summary]

    Args:
        input ([string]): [description]

    Returns:
        [tuple]: [containing 3 closest possible languages to given input]
    """
    language_models = load_language_models()
    input_ngrams = get_input_ngrams(input)
    input_ngram_ranks = get_ngram_ranks(input_ngrams)
    # print(len(input_ngram_ranks))
    # print(len(input))
    # print(input_ngram_ranks)
    # sys.exit()
    differences = compare_input_with_languages(
        language_models, input_ngram_ranks)
    return get_closest_language(differences)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', required=True, help="input file")
    args = parser.parse_args()
    with open(args.f) as file:
        input = file.read()
    file.close()
    print((which_lang(input)))


if __name__ == "__main__":
    main()
