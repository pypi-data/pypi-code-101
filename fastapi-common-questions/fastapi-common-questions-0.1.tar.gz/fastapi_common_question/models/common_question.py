
from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import JSON

from db.base_class import Base


class CommonQuestion(Base):
    __tablename__ = 'moj_common_question'
    updated_at = None
    question = Column(String(1024))
    answer = Column(String(1024))
    additional_data = Column(JSON, default=dict(), )
    is_active = Column(Boolean(), default=True)
