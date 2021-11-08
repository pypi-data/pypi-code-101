from datetime import datetime
from typing import Optional
from pydantic import BaseModel, validator


class Account(BaseModel):
    title: str
    companyId: int
    accountType: str
    currencyCode: str
    longTitle: Optional[str]
    description: Optional[str]
    accountType: Optional[str]
    accountAcct: Optional[str]
    correspondentAcct: Optional[str]
    accountBik: Optional[str]
    accountBank: Optional[str]
    active: Optional[bool]
    remainder: Optional[float]
    remainderDate: datetime
    externalId: Optional[str]
    accountGroupId: Optional[int]

    @validator('remainderDate')
    def remainder_date(cls, v):
        return v.strftime('%Y-%m-%d')


class OperationPart:
    def __init__(self,
                 operation_category_id: int,
                 project_id: int,
                 value: float
                 ):
        self.value = value
        if operation_category_id == 0:
            self.operation_category_id = None
        else:
            self.operation_category_id = operation_category_id
        if project_id == 0:
            self.project_id = None
        else:
            self.project_id = project_id


class MoveOperation:
    def __init__(self,
                 is_committed: bool,
                 date: datetime,
                 comment: str,
                 value_outcome: float,
                 value_income: float,
                 account_id_income: int,
                 account_id_outcome: int,
                 external_id=None
                 ):
        self.date = date
        self.is_committed = is_committed
        self.params = {
            "debitingDate": date.strftime('%Y-%m-%d'),
            "admissionDate": date.strftime('%Y-%m-%d'),
            "admissionAccountId": account_id_income,  # Счет зачисления
            "debitingAccountId": account_id_outcome,  # Счет списания
            "admissionValue": value_income,  # Сумма зачисления
            "debitingValue": value_outcome,  # Сумма списания
            "isCommitted": False,
            "externalId": external_id,
            "comment": comment}
        if is_committed:
            self.params.update({
                "calculationDate": date.strftime('%Y-%m-%d'),
                "isCalculationCommitted": True,
                "isCommitted": True})


class Operation:
    def __init__(self,
                 is_committed: bool,
                 date: datetime,
                 comment: str,
                 value: float,
                 account_id: int,
                 external_id=None
                 ):
        self.date = date
        self.is_committed = is_committed
        self.params = {
            "operationDate": date.strftime('%Y-%m-%d'),
            "accountId": account_id,
            "value": value,
            "isCommitted": False,
            "externalId": external_id,
            "comment": comment,
            "items": list()}
        if is_committed:
            self.params.update({
                "calculationDate": date.strftime('%Y-%m-%d'),
                "isCalculationCommitted": True,
                "isCommitted": True})

    def append_item(self, item: OperationPart):
        self.params['items'].append({
            "calculationDate": self.date.strftime('%Y-%m-%d'),
            "isCalculationCommitted": self.is_committed,
            "operationCategoryId": item.operation_category_id,
            "projectId": item.project_id,
            "value": item.value
        })