import typing

import aiohttp

from . import crud_objects
from . import models
from .core.api import ApiClient
from .core.auth import AuthManager
from .core.exceptions import ApiException


class AlfaClient:
    """Class for work with AlfaCRM API"""

    def __init__(
            self,
            hostname: str,
            email: str,
            api_key: str,
            branch_id: int,
            connections_limit: typing.Optional[int] = None,
            session: typing.Optional[aiohttp.ClientSession] = None,
    ):
        self._connector_class: typing.Type[aiohttp.TCPConnector] = aiohttp.TCPConnector

        if session is None:
            session = self._create_session()

        self._hostname = hostname
        self._branch_id = branch_id
        self._session = session
        self._email = email
        self._api_key = api_key
        self.auth_manager = AuthManager(
            email,
            api_key,
            hostname,
            session,
        )

        self.api_client = ApiClient(
            self._hostname,
            self._branch_id,
            self.auth_manager,
            self._session,
        )

        # Set API objects
        self.branch = crud_objects.Branch(self.api_client, model_class=models.Branch)
        self.location = crud_objects.Location(self.api_client, models.Location)
        self.customer = crud_objects.Customer(self.api_client, models.Customer)
        self.study_status = crud_objects.StudyStatus(self.api_client, models.StudyStatus)
        self.subject = crud_objects.Subject(self.api_client, models.Subject)
        self.lead_status = crud_objects.LeadStatus(self.api_client, models.LeadStatus)
        self.lead_source = crud_objects.LeadSource(self.api_client, models.LeadSource)
        self.group = crud_objects.Group(self.api_client, models.Group)
        self.lesson = crud_objects.Lesson(self.api_client, models.Lesson)
        self.room = crud_objects.Room(self.api_client, models.Room)
        self.task = crud_objects.Task(self.api_client, models.Task)
        self.tariff = crud_objects.Tariff(self.api_client, models.Tariff)
        self.regular_lesson = crud_objects.RegularLesson(self.api_client, models.Tariff)
        self.pay_item = crud_objects.PayItem(self.api_client, models.PayItem)
        self.pay_item_category = crud_objects.PayItemCategory(self.api_client, models.PayItemCategory)
        self.pay_account = crud_objects.PayAccount(self.api_client, models.PayAccount)
        self.pay = crud_objects.Pay(self.api_client, models.Pay)
        self.lesson_type = crud_objects.LessonType(self.api_client, models.LessonType)
        self.lead_reject = crud_objects.LeadReject(self.api_client, models.LeadReject)

    @classmethod
    def _create_session(cls) -> aiohttp.ClientSession:
        """
        Create session
        :return: session
        """
        return aiohttp.ClientSession()

    async def auth(self):
        await self.auth_manager.refresh_token()

    async def check_auth(self) -> bool:
        """Check authentification"""
        try:
            await self.auth()
            return True
        except ApiException:
            return False

    async def close(self):
        """Close connections"""
        await self._session.close()

    @property
    def hostname(self) -> str:
        return self._hostname

    @property
    def email(self) -> str:
        return self._email

    @property
    def api_key(self) -> str:
        return self._api_key

    @property
    def branch_id(self) -> int:
        return self._branch_id
