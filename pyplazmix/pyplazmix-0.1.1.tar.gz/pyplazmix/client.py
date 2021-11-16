from requests_html import AsyncHTMLSession
from .enums import *
import ujson
from .user import User
from .moderator_alert import ModeratorAlert
from .online_now import *
from .news import NewsObject
from typing import Union
from .errors import ApiError


class ApiClient:
    """[pyplazmix.ApiClient] - Plazmix API Client

    :param token: Api token
    :type token: str
    """
    def __init__(self, token: str):
        self.session = AsyncHTMLSession()

        # vars
        self.__token = token
        self.__base_url = "https://api.plazmix.net/v1/"

    # request - system
    def __request(self, method: str, url: str, data: dict=None):
        async def request():
            headers = {"Authorization": f"APP-BEARER {self.__token}"}
            r = await self.session.request(method, self.__base_url+url, headers=headers, json=data)
            return r
        return self.session.run(request)[0]

    # get user
    def get_user(self, nickname: str=None, uuid: str=None, _id: int=None):
        """[pyplazmix.ApiClient.get_user] - Get user

        :param nickname: User nickname,
            defaults to None
        :param uuid: User UUID,
            defaults to None
        :param _id: User ID,
            defaults to None
        :type nickname: str,
            optinal
        :type uuid: str,
            optinal
        :type _id: int,
            optinal

        :raises SyntaxError: If nothing is specified or not specified correctly
        :raises ApiError: If user not found

        :return: User object
        :rtype: pyplazmix.User
        """
        if nickname is None and uuid is None and _id is None: raise SyntaxError("Nothing is specified!")
        elif nickname is not None and uuid is not None and _id is not None: raise SyntaxError("Not specified correctly!")
        elif nickname is not None and uuid is not None or nickname is not None and _id is not None or uuid is not None and _id is not None: raise SyntaxError("Not specified correctly!")
        else:
            payload = {}
            if nickname is not None: payload['nickname'] = nickname
            elif uuid is not None: payload['uuid'] = uuid
            elif _id is not None: payload['id'] = _id

            r = self.__request('POST', 'User.get', payload)
            if r.status_code == 404: return ApiError('User not found!')
            elif r.status_code == 200:
                return User(ujson.loads(r.text))

    # get staff list
    def get_staff_users(self, group: Permissions):
        """[pyplazmix.ApiClient.get_staff_users] - Get staff users
        
        :param group: Staff Group
        :type group: pyplazmix.ext.enums.Permissions

        :raises ApiError: If specified group not staff

        :return: User objects
        :rtype: List[pyplazmix.User]
        """
        if group not in [Permissions.TESTER, Permissions.ART, Permissions.BUILDER, Permissions.BUILDER_PLUS,
                         Permissions.JUNIOUR, Permissions.MODERATOR, Permissions.MODERATOR_PLUS, Permissions.DEVELOPER,
                         Permissions.ADMINISTRATOR, Permissions.OWNER]:
            raise ApiError("Specified group not staff")
        
        r = self.__request('POST', 'User.staff', {"staff_group": group})
        return [User(x) for x in ujson.loads(r.text)['staffs']]

    # get online now
    def get_online_now(self):
        """[pyplazmix.ApiClient.get_online_now] - Get online now

        :return: Online now
        :rtype: pyplazmix.OnlineNow
        """
        r = self.__request('GET', 'Online.now')
        return OnlineNow(ujson.loads(r.text))

    # get online from identification
    def get_online_from_identification(self, identification: Union[Identifications, str]):
        """[pyplazmix.ApiClient.get_online_from_identification] - Get online from identification

        :param identification: Mode identification
        :type identification: Union[Identifications, str]

        :return: Online now
        :rtype: pyplazmix.OnlineObject
        """
        r = self.__request('POST', 'Online.getFromIdentification', {"identification": identification.value if type(identification) != str else identification})
        return OnlineObject(ujson.loads(r.text))

    # get moderator alerts
    def get_moderator_alerts(self, uuid: str):
        """[pyplazmix.ApiClient.get_moderator_alerts] - Get moderator alerts
        
        :param uuid: Moderator uuid
        :type uuid: str

        :return: ModeratorAlert objects
        :rtype: List[pyplazmix.ModeratorAlert]
        """
        r = self.__request('POST', 'ModeratorAlert.getModerator', {"uuid": uuid})
        return [ModeratorAlert(x) for x in ujson.loads(r.text)['alerts']]

    # get_alert
    def get_alert(self, _id: int):
        """[pyplazmix.ApiClient.get_alert] - Get alert
        
        :param _id: Alert id
        :type _id: int

        :return: ModeratorAlert object
        :rtype: pyplazmix.ModeratorAlert
        """
        r = self.__request('POST', 'ModeratorAlert.get', {"alert_id": _id})
        return ModeratorAlert(ujson.loads(r.text))

    # get all news
    def get_all_news(self, page: int=1, count_per_page: int=50):
        """[pyplazmix.ApiClient.get_all_news] - Get all news
        
        :param page: Page number,
            defaults to 1
        :param count_per_page: Count objects on page,
            defaults to 50
        :type page: int,
            optinal
        :type count_per_page: int,
            optinal

        :return: News objects
        :rtype: List[pyplazmix.NewsObject]
        """
        r = self.__request('POST', 'News.all', {"paginate": {"page": page, "count_per_page": count_per_page}})
        return [NewsObject(x) for x in ujson.loads(r.text)['news']]

    # get news object
    def get_news_object(self, _id: int):
        """[pyplazmix.ApiClient.get_news_object] - Get news object
        
        :param _id: News object id
        :type _id: int

        :return: News object
        :rtype: pyplazmix.NewsObject
        """
        r = self.__request('POST', 'News.get', {"news_id": _id})
        return NewsObject(ujson.loads(r.text))