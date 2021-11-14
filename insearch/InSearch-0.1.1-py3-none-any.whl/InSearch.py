from .TokenAnalyzer import token_analyzer
from .BM24 import bm24


class InSearch:
    def __init__(self):
        # key : value = string token : {dictionary document_id : frequency}
        # id_n_len_in_table, table에 들어있는 doc id와 len의 딕셔너리
        self.table = {}
        self.id_n_len_in_table = {}

    # table에 document의 token과 id를 추가
    # parameter : int document_id, string document
    # return : boolean
    def add_document(self, document_id, document):
        # 해당 id가 없는지 확인
        if document_id in self.id_n_len_in_table:
            return False
        # document 형태소 분석
        token_list = token_analyzer(document)
        # id_n_len_in_table에 해당 doc의 id와 len 추가
        self.id_n_len_in_table[document_id] = len(token_list)
        # table에 { token : {document id : frequency} }를 추가
        # token이 table에 있을 때
        #   id가 없으면, 해당 {id : freq = 0}을 추가
        #   id가 있으면, 해당 {id : freq += 1}을 추가
        # token이 table에 없을 때
        #   token과 {id : freq = 0}을 추가
        for token in token_list:
            if token in self.table.keys():
                if document_id in self.table[token]:
                    self.table[token][document_id] += 1
                else:
                    self.table[token][document_id] = 1
            else:
                self.table[token] = {document_id:1}
        return True

    # table에 해당 id를 가진 document의 token을 삭제
    # parameter : int document_id
    # return : boolean
    def delete_document(self, document_id):
        # 해당 id가 있는지 확인
        if document_id not in self.id_n_len_in_table:
            return False

        copy_table = self.table.copy()
        # 삭제하려는 id를 따라 table을 돌며 삭제
        for key in copy_table.keys():
            value = copy_table[key]
            if document_id in value:
                del self.table[key][document_id]
                if len(self.table[key]) == 0:
                    del self.table[key]
        # id_in_table에 해당 id 삭제
        self.id_n_len_in_table.pop(document_id)
        return True

    # table의 해당 document의 기록을 new_document로 변경
    # parameter : int document_id, string new_document
    # return : boolean
    def update_document(self, document_id, new_document):
        self.delete_document(document_id)
        self.add_document(document_id, new_document)
        return True

    # 전체 table을 딕셔너리로 반환
    # parameter : int document_id
    # return : Dictionary table
    def return_table(self):
        return self.table

    # 검색어와 가장 부합한 document의 id를 table에서 찾아 반환
    # parameter : string query
    # return : list rank_of_document_id
    def search(self, query):
        score_list = bm24(self.table, query, self.id_n_len_in_table)
        score_list.sort(reverse=True)
        rank_of_document_id = [i[1] for i in score_list]
        return rank_of_document_id

    def search_top_n(self, query, top_n):
        return self.search(query)[:top_n]

    # table 초기화
    # return : boolean
    def delete_all(self):
        self.table.clear()
        self.id_n_len_in_table.clear()
        return True
