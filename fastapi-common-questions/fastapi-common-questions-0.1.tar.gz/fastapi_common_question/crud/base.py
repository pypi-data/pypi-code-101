from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id, self.model.is_archive.is_(False)).first()

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        obj.is_archive = True
        db.commit()
        return obj

    def filter_by_args(self, *args, **kwargs)->List:
        filters = []
        for key, value in kwargs.items():
            if key.endswith('__lt'):
                key = key[:-4]
                filters.append(getattr(self.model, key) < value )
            elif key.endswith('__lte'):
                key = key[:-5]
                filters.append(getattr(self.model, key) <= value )
            elif key.endswith('__gt'):
                key = key[:-4]
                filters.append(getattr(self.model, key) > value )
            elif key.endswith('__gte'):
                key = key[:-5]
                filters.append(getattr(self.model, key) >= value )
            elif key.endswith('__in'):
                key = key[:-4]
                filters.append(getattr(self.model, key).in_(value))
            elif key.endswith('__notin'):
                key = key[:-7]
                filters.append(getattr(self.model, key).notin_(value))
            elif key.endswith('__isnull'):
                key = key[:-8]
                if value:
                    filters.append(getattr(self.model, key).is_(None))
                else:
                    filters.append(getattr(self.model, key).isnot_(None))
            elif key.endswith('__not'):
                key = key[:-5]
                filters.append(getattr(self.model, key) != value )
            elif '__' in key:
                keys = key.split('__')
                key0 = keys[0]
                key1 = keys[1]
                dc = {
                    key1: value
                }
                filters.append(getattr(self.model, key0).has(**dc))
            else:
                filters.append(getattr(self.model, key) == value)

        return filters

    def get_query(self, db:Session, *args, **kwargs)->ModelType:
        filters = self.filter_by_args(*args, **kwargs)
        return db.query(self.model).filter(*filters).first()

    def filter_query(self, db:Session, *args, **kwargs)-> List[ModelType]:
        filters = self.filter_by_args(*args, **kwargs)
        return db.query(self.model).filter(*filters).all()

    def exists(self, db: Session, *, id: int=0, title: str=None) -> bool:
        obj_id = False
        if title:
            obj_id = db.query(self.model.id).filter(self.model.title == title).scalar()
        else:
            obj_id = db.query(self.model.id).filter(self.model.id == id).scalar()
        return bool(obj_id)

    def get_or_create(self, db: Session, defaults={}, *args, **kwargs):
        created = False
        obj = self.get_query(db=db, *args, **kwargs)
        if not obj:
            created = True
            kwargs.pop("id", None)
            kwargs.pop("pk", None)
            params = {k: v for k, v in kwargs.items() if '__' not in k}
            params.update(defaults)
            obj = self.create(db=db, obj_in=params)
        return obj, created

    def update_or_create(self, db: Session, defaults={}, *args, **kwargs):
        obj, created = self.get_or_create(db=db, defaults=defaults, *args, **kwargs)
        if not created:
            obj = self.update(db=db, db_obj=obj, obj_in=defaults)
        return obj, created

    def filter_count(self, db: Session, *args, **kwargs):
        filters = self.filter_by_args(*args, **kwargs)
        return db.query(self.model).filter(*filters).count()
