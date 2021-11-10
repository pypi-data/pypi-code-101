from fastapi.encoders import jsonable_encoder
from sqlalchemy import desc
from sqlalchemy.orm import Session, aliased
from starlette import status

from exceptions import ItemNotFound
from models import models
from models.choice_types import ChoiceTypes
from ..models.models import CommonQuestion
from models.user import User
from ..schemas.common_question import CommonQuestionOut, CommonQuestionIn
from .base import CRUDBase


class CRUDCommonQuestion(CRUDBase[CommonQuestion, CommonQuestionIn, CommonQuestionOut]):

    def create(self, db: Session, *, obj_in: CommonQuestionIn) -> CommonQuestion:
        db_obj = CommonQuestion(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_all(self, db: Session, filter_query_params: list) -> CommonQuestion:
        return db.query(self.model).filter(self.model.is_archive.is_(False)).filter(*filter_query_params).order_by(desc(self.model.created_at))


common_question = CRUDCommonQuestion(CommonQuestion)

