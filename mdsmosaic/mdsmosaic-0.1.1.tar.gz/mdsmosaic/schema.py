import datetime
from typing import Any, Optional, Mapping

from marshmallow import Schema, fields, post_load, EXCLUDE, ValidationError

from .model import Identity


class DateTimeObjField(fields.Field):

    def _serialize(self, value: Any, attr: str, obj: Any, **kwargs):
        if value is None:
            return None

        return value

    def _deserialize(self, value: Any, attr: Optional[str], data: Optional[Mapping[str, Any]], **kwargs):
        if not isinstance(value, datetime.datetime):
            raise ValidationError("Date time object must be an instance of datetime.datetime")

        return value


class IdentitySchema(Schema):
    # required attributes
    first_name = fields.Str(required=True, data_key="firstName")
    last_name = fields.Str(required=True, data_key="lastName")
    gender = fields.Str(required=True)
    birth_date = DateTimeObjField(required=True, data_key="birthDate")
    # optional attributes
    birth_place = fields.Str(data_key="birthPlace", missing=None)
    civil_status = fields.Str(data_key="civilStatus", missing=None)
    degree = fields.Str(missing=None)
    external_date = DateTimeObjField(data_key="externalDate", missing=None)
    middle_name = fields.Str(data_key="middleName", missing=None)
    mother_tongue = fields.Str(data_key="motherTongue", missing=None)
    mothers_maiden_name = fields.Str(data_key="mothersMaidenName", missing=None)
    nationality = fields.Str(missing=None)
    prefix = fields.Str(missing=None)
    race = fields.Str(missing=None)
    religion = fields.Str(missing=None)
    suffix = fields.Str(missing=None)

    @post_load
    def make_identity(self, data, **kwargs):
        return Identity(**data)

    class Meta:
        unknown = EXCLUDE


def load_identity(data: dict[str, Any]) -> Identity:
    return IdentitySchema().load(data)


def dump_identity(identity: Identity) -> dict[str, Any]:
    return IdentitySchema().dump(identity)
