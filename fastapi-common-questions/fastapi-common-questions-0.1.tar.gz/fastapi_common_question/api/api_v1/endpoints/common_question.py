from fastapi_pagination import PaginationParams
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from starlette import status
from starlette.datastructures import QueryParams

from ....crud import crud
from ....exceptions import ItemNotFound
from ....schemas.common_question import CommonQuestionIn


# admin

class CommonQuestionWrapper(object):

    def get_question(self, db: Session, question_id: int):
        question = crud.common_question.get(db, id=question_id)
        if not question:
            raise ItemNotFound(status.HTTP_404_NOT_FOUND, val="common_question")
        return question

    def list_questions(self, db: Session, params: PaginationParams, filters: QueryParams):
        questions = crud.common_question.get_all(db, filter_query_params=filters)
        return paginate(questions, params)

    def create_question(self, db: Session, question_schema: CommonQuestionIn):
        question = crud.common_question.create(db=db, obj_in=question_schema)
        return question

    def update_question(self, db: Session, question_id: int, question_schema: CommonQuestionIn):
        question = crud.common_question.get(db, id=question_id)
        if not question:
            raise ItemNotFound(status.HTTP_404_NOT_FOUND, val="common_question")
        question = crud.common_question.update(db, db_obj=question, obj_in=question_schema)
        return question

    def delete_question(self, db: Session, question_id: int):
        question = crud.common_question.get(db, id=question_id)
        if not question:
            raise ItemNotFound(status.HTTP_404_NOT_FOUND, val="common_question")
        question = crud.common_question.remove(db, id=question_id)
        return question


common_question_wrapper = CommonQuestionWrapper()
