import datetime
from typing import Optional, List

from .. import fields
from ..core import AlfaObject


class Customer(AlfaObject):
    id: Optional[int] = fields.Integer()
    name: Optional[str] = fields.String()
    branch_ids: Optional[List[int]] = fields.ListField(fields.Integer())
    teacher_ids: Optional[List[int]] = fields.ListField(fields.Integer())
    is_study: Optional[bool] = fields.Bool()
    study_status_id: Optional[int] = fields.Integer()
    lead_status_id: Optional[int] = fields.Integer()
    lead_source_id: Optional[int] = fields.Integer()
    assigned_id: Optional[int] = fields.Integer()
    legal_type: Optional[int] = fields.Integer()
    legal_name: Optional[str] = fields.String()
    company_id: Optional[int] = fields.Integer()
    dob: Optional[datetime.date] = fields.DateField()
    balance: Optional[float] = fields.Float()
    balance_base: Optional[float] = fields.Float()
    last_attend_date: Optional[datetime.date] = fields.DateField()
    b_date: Optional[datetime.datetime] = fields.DateTimeField()
    e_date: Optional[datetime.datetime] = fields.DateField()
    paid_lesson_count: Optional[int] = fields.Integer()
    phone: Optional[List[str]] = fields.ListField(fields.String())
    email: Optional[List[str]] = fields.ListField(fields.String())
    web: Optional[List[str]] = fields.ListField(fields.String())
    addr: Optional[List[str]] = fields.ListField(fields.String())
    note: Optional[List[str]] = fields.String(fields.String())

    def __init__(
            self,
            id_: Optional[int] = None,
            name: Optional[str] = None,
            branch_ids: Optional[List[int]] = None,
            teacher_ids: Optional[List[int]] = None,
            is_study: Optional[bool] = None,
            study_status_id: Optional[int] = None,
            lead_status_id: Optional[int] = None,
            assigned_id: Optional[int] = None,
            legal_type: Optional[int] = None,
            legal_name: Optional[str] = None,
            company_id: Optional[int] = None,
            dob: Optional[datetime.date] = None,
            balance: Optional[float] = None,
            balance_base: Optional[float] = None,
            last_attend_date: Optional[datetime.date] = None,
            b_date: Optional[datetime.datetime] = None,
            e_date: Optional[datetime.date] = None,
            paid_lesson_count: Optional[int] = None,
            phone: Optional[List[str]] = None,
            email: Optional[List[str]] = None,
            web: Optional[List[str]] = None,
            addr: Optional[List[str]] = None,
            note: Optional[str] = None,
            **kwargs,
    ):
        super(Customer, self).__init__(
            id=id_,
            name=name,
            branch_ids=branch_ids,
            teacher_ids=teacher_ids,
            is_study=is_study,
            study_status_id=study_status_id,
            lead_status_id=lead_status_id,
            assigned_id=assigned_id,
            legal_type=legal_type,
            legal_name=legal_name,
            company_id=company_id,
            dob=dob,
            balance=balance,
            balance_base=balance_base,
            last_attend_date=last_attend_date,
            b_date=b_date,
            e_date=e_date,
            paid_lesson_count=paid_lesson_count,
            phone=phone,
            email=email,
            web=web,
            addr=addr,
            note=note,
            **kwargs,
        )
