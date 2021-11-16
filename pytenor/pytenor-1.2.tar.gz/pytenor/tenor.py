from typing import Union
import aiohttp
import urllib
import datetime as dt

from .exceptions import *
from .classes import *


class Helpers:
    async def get_url_as_gif(self, url: str, **params) -> Union[GIF, None]:
        """Returns the GIF object of the provided tenor url. None if not found or url is invalid."""

        segments = url.split("-")
        id_ = segments[-1]

        try:
            int(id_)
        except ValueError:
            return None
        
        gifs = await self.get_gifs(id_, **params)
        if not gifs:
            return None
        return gifs[0]

class Constructors:
    def construct_url(self, url: str = None, **params) -> str:
        """
        Construct a url with parameters.

        Parameters
        ----------
        `url` : str
            The base url. Defaults to self.base
        **params

        Returns
        -------
        `str` :
            The constructed url.
        """

        if not url:
            url = self.base

        parameters = {**self.baseparams, **params}
        parameters = urllib.parse.urlencode(parameters)
        return url + "?" + parameters
    
    def construct_media(self, data: dict, return_format: bool = False) -> Media:
        """Construct a Media object."""

        for k, v in data.items():

            media = Media(v["preview"], v["url"], tuple(v["dims"]), v["size"], k)

            if not return_format:
                return media
            return media, k

    def construct_gif(self, data: dict, response: APIResponse) -> GIF:
        """Construct a GIF object."""

        data["created"] = dt.datetime.utcfromtimestamp(data["created"])
        media = []
        available_formats = []

        for m in data["media"]:
            media_object, format = self.construct_media(m, return_format=True)

            media.append(media_object)
            available_formats.append(format)
        
        return GIF(
            data["created"],
            data["hasaudio"],
            data["id"],
            media,
            data["tags"],
            data["title"],
            data["itemurl"],
            data["hascaption"],
            data["url"],
            response,
            available_formats
        )
    
    def construct_category(self, data: dict, response: APIResponse) -> Category:
        """Construct a Category object."""

        return Category(
            data["searchterm"],
            data["path"],
            data["image"],
            data["name"],
            self
        )


class Tenor(Constructors, Helpers):
    """
    Initialize the Tenor api wrapper.

    Parameters
    ----------
    `key` : str
        Your API key.
    `locale` : str
        Locale. Default to en_US. Read tenor's API documentation for more information.
    `content_filter` : str 
        Specify the the content safety filter level. Defaults to off. Applicable values are 'basic', 'minimal', and 'off'.
    `optional_params` : str
        Other parameters to pass into the base url. Read tenor's API documentation for more information.
    """

    def __init__(self, key: str, locale: str = "en_US", content_filter: str = "off", optional_params: dict = None, **kwargs) -> None:

        self.key = key
        self.locale = locale
        self.content_filter = content_filter

        # Create default
        optional_params = {} if not optional_params else optional_params

        self.baseparams = {**{"key": self.key, "locale": self.locale,
                           "contentfilter": self.content_filter}, **optional_params}
        self.base = kwargs.get("base", "https://g.tenor.com/v1/")

    async def get(self, endpoint: str, **params) -> APIResponse:
        """
        Performs a get request to the api using aiohttp and also constructs a APIResponse object.

        Parameters
        ----------
        `endpoint` : str
            The API endpoint.
        `**params` :
            Parameters to be passed when making the get request.

        Returns
        -------
        `APIResponse`

        Raises
        ------
        `RateLimitError` :
            Raised when the rate limit has been exceeded.
        `APIError` :
            Raised when the api has raised an error.
        """

        url = self.construct_url(self.base + endpoint, **params)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:

                if r.status == 200:
                    data = await r.json()
                    if "error" in data.keys():
                        code = data.get("code")

                        if code == 429:
                            raise RateLimitError
                        raise APIError(code=code, msg=data["error"])

                    response = APIResponse(r.status, r.reason, endpoint.replace("/", ""), data, params)
                    return response
                else:
                    raise APIError(r.status, r.reason)

    async def search(self, q: str = None, **params) -> List[GIF]:
        """Search for gifs. Returns a list of GIF objects."""

        q = q if q else ""
        response = await self.get("search", q=q, **params)
        gifs = [self.construct_gif(r, response) for r in response.json["results"]]
        return gifs

    async def trending(self, **params) -> List[GIF]:
        """Returns a list of trending gifs in a GIF object."""

        response = await self.get("trending", **params)
        gifs = [self.construct_gif(r, response) for r in response.json["results"]]
        return gifs

    async def categories(self, **params) -> List[Category]:
        """Returns a list of gif Category objects."""

        response = await self.get("categories", **params)
        categories = [self.construct_category(x, response) for x in response.json["tags"]]
        return categories
    
    async def search_suggestions(self, q: str = None, **params) -> List[str]:
        """Returns a list of search suggestions as a string."""

        q = q if q else ""
        response = await self.get("search_suggestions", q=q, **params)
        return response.json["results"]
    
    async def autocomplete(self, q: str = None, **params) -> List[str]:
        """Returns a list of autocomplete suggestions as a string."""

        q = q if q else ""
        response = await self.get("autocomplete", q=q, **params)
        return response.json["results"]
    
    async def trending_terms(self, **params) -> List[str]:
        """Returns a list of trending search terms as a string."""

        response = await self.get("trending_terms", **params)
        return response.json["results"]
    
    async def register_share(self, id_: str, **params) -> APIResponse:
        """Registers a gif as shared. This is used to improve tenor's API. Does not return anything but an APIResponse object which contains no gif data whatsoever."""

        response = await self.get("registershare", id=id_, **params)
        return response
    
    async def get_gifs(self, ids: Union[str, List[str]], **params) -> List[GIF]:
        """Gets a list of gifs from the provided gif ids."""

        if isinstance(ids, str):
            ids = [ids]

        ids = ",".join(ids)

        response = await self.get("gifs", ids=ids, **params)
        gifs = [self.construct_gif(x, response) for x in response.json["results"]]
        return gifs
