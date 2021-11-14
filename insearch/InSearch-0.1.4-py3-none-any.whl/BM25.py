import math
from . import TokenAnalyzer as ta


    # IDF값 계산
    # parameter : int document_count, int fq_document
    # return : float
def IDF(document_count, fq_document):
    return math.log(1 + ((document_count - fq_document + 0.5)/(fq_document + 0.5)))


    # document들의 평균 길이 계산
    # parameter : dic document_len, int list document_id, int document_count
    # return : float
def get_avg_document_len(document_len_dic, document_id_list, document_count):
    total_length = 0
    for id in document_id_list:
        total_length += document_len_dic[id]
    return total_length / document_count


    # full-text(query)에 대해 각 document의 점수 계산
    # parameter : InSearch table, string query, int list document_id, dic document_len
    # return : float list
def bm25(table, query, document_len_dic):
    score_list = []
    # K1은 1.2 ~ 2.0 사이의 상수
    K1 = 1.2
    # B는 0.75인 상수
    B = 0.75
    document_id_list = document_len_dic.keys()
    document_count = len(document_id_list)
    # document들의 평균 길이 계산
    avgdl = get_avg_document_len(document_len_dic, document_id_list, document_count)
    # query문을 형태소 분석
    query_token = ta.token_analyzer(query)
    # 각 document마다 반복
    for id in document_id_list:
        score = 0
        # query문의 각 형태소마다 반복
        for token in query_token:
            if table.get(token) == None:
                # 해당 token을 포함하는 document개수
                fq_document = 0
                # document에서 token의 개수(빈도)
                fq_count = 0
            else:
                fq_document = len(table[token].keys())      
                fq_count = table[token].get(id, 0)
            # IDF
            token_idf = IDF(document_count, fq_document)
            # TF
            token_tf = (fq_count * (K1 + 1))/(fq_count + K1 * (1 - B + B * (document_len_dic[id]/avgdl)))
            score += token_idf * token_tf
        # score(D,Q) = sigma(IDF*TF)
        score_list.append((score, id))
    return score_list
