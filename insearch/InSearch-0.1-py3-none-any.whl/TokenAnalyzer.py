from eunjeon import Mecab


# # text에 document의 token과 id를 추가
# # parameter : string document
# # return : list token
def token_analyzer(document):
    morphs_analyzer = Mecab()
    token_list = morphs_analyzer.morphs(document)
    return token_list
