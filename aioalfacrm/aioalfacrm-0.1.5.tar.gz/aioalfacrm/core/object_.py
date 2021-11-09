import typing

from .api import ApiClient
from .exceptions import NotFound
from .page import Page
from .paginator import Paginator


class BaseCRUDAlfaObject:
    """Class for description API object"""
    object_name = None

    def __init__(self, api_client: ApiClient):
        self._api_client = api_client

    async def _list(self, page: int, count: int = 100, **kwargs) -> typing.Dict[str, typing.Any]:
        """
        Get objects list from api
        :param page: number of page
        :param count: count items on page
        :param kwargs: additional filters
        :return: objects list
        """
        list_url = self._api_client.get_url_for_method(self.object_name, 'index')
        payload = {
            'page': page,
            **kwargs
        }
        result = await self._api_client.request(list_url, json=payload, params={'per-page': count})
        return result

    async def _get(self, id_: int) -> typing.Dict[str, typing.Any]:
        """
        Get one object from api
        :param id_: object id
        :return: object
        """
        get_url = self._api_client.get_url_for_method(self.object_name, 'index')
        result = await self._api_client.request(get_url, json={'id': id_})
        if result['count'] == 0:
            raise NotFound(404, f'{self.object_name} not found')
        return result['items'][0]

    async def _create(self, **kwargs) -> typing.Dict[str, typing.Any]:
        """
        Create object in api
        :param kwargs: fields
        :return: created object
        """
        create_url = self._api_client.get_url_for_method(self.object_name, 'create')
        result = await self._api_client.request(create_url, json=kwargs)
        return result['model']

    async def _update(self, id_: int, **kwargs) -> typing.Dict[str, typing.Any]:
        """
        Update object in api
        :param id_: object id
        :param kwargs: fields
        :return: updated object
        """
        update_url = self._api_client.get_url_for_method(self.object_name, 'update')
        result = await self._api_client.request(update_url, params={'id': id_}, json=kwargs)
        return result['model']

    async def _save(self, **kwargs) -> typing.Dict[str, typing.Any]:
        if 'id' in kwargs:
            return await self._update(kwargs.pop('id'), **kwargs)
        else:
            return await self._create(**kwargs)


T = typing.TypeVar('T')


class AlfaCRUDObject(BaseCRUDAlfaObject, typing.Generic[T]):
    def __init__(self, api_client: ApiClient, model_class: typing.Type[T], **kwargs):
        super(AlfaCRUDObject, self).__init__(api_client=api_client)
        self._model_class = model_class

    async def list(
            self,
            page: int = 0,
            count: int = 100,
            **kwargs
    ) -> typing.List[T]:
        raw_data = await self._list(page, count, **kwargs)
        return [self._model_class(item.pop('id'), **item) for item in raw_data['items']]

    async def get(
            self,
            id_: int,
    ) -> T:
        raw_data = await self._get(id_)
        return self._model_class(id_=raw_data.pop('id'), **raw_data)

    async def save(
            self,
            model: T,
    ) -> T:
        raw_data = await self._save(**model.serialize())
        return self._model_class(id_=raw_data.pop('id'), **raw_data)

    async def page(self, page: int = 0, count: int = 100, **kwargs) -> Page[T]:
        raw_data = await self._list(page, count, **kwargs)
        items = [self._model_class(item.pop('id'), **item) for item in raw_data['items']]
        return Page(
            number=page,
            items=items,
            total=raw_data['total'],
        )

    def paginator(self, start_page: int = 0, page_size: int = 100, **kwargs) -> Paginator[T]:
        return Paginator(
            alfa_object=self,
            start_page=start_page,
            page_size=page_size,
            filters=kwargs,
        )
