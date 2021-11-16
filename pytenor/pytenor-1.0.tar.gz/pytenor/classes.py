from dataclasses import dataclass
import datetime as dt
from typing import List
from urllib import parse

from pytenor.exceptions import MediaNotFound
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .tenor import Tenor


@dataclass
class APIResponse:
    status: int
    reason: str
    endpoint: str
    json: dict
    params: dict


@dataclass
class Media:
    preview: str
    url: str
    dims: tuple
    size: int
    format: str


@dataclass
class GIF:
    created: dt.datetime
    has_audio: bool
    id: str
    media: List[Media]
    tags: List[str]
    title: str
    item_url: str
    has_caption: bool
    url: str
    response_object: APIResponse
    available_formats: List[str]

    def __get_media(self, f: str) -> Media:
        try:
            return [x for x in self.media if x.format == f][0]
        except IndexError:
            raise MediaNotFound(f)

    @property
    def gif(self) -> Media:
        return self.__get_media("gif")

    @property
    def medium_gif(self) -> Media:
        return self.__get_media("mediumgif")

    @property
    def tinygif(self) -> Media:
        return self.__get_media("tinygif")

    @property
    def nanogif(self) -> Media:
        return self.__get_media("nanogif")

    @property
    def mp4(self) -> Media:
        return self.__get_media("mp4")

    @property
    def looped_mp4(self) -> Media:
        return self.__get_media("loopedmp4")

    @property
    def tiny_mp4(self) -> Media:
        return self.__get_media("tinymp4")

    @property
    def nano_mp4(self) -> Media:
        return self.__get_media("nanomp4")

    @property
    def webm(self) -> Media:
        return self.__get_media("webm")

    @property
    def tiny_webm(self) -> Media:
        return self.__get_media("tinywebm")

    @property
    def nano_webm(self) -> Media:
        return self.__get_media("nanowebm")


@dataclass
class Category:
    search_term: str
    path: str
    image: str
    name: str
    api: "Tenor"

    async def gifs(self, **params) -> List[GIF]:
        """Returns a list of GIF objects that is in this category. All this really does is perform a search using the provided search term."""

        base_params = parse.urlsplit(self.path).query
        base_params = dict(parse.parse_qsl(base_params))

        search = await self.api.search(**{**base_params, **params})
        return search
