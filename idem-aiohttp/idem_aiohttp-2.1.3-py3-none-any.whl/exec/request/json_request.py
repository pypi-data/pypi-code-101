from typing import Dict
from typing import List

__virtualname__ = "json"


async def delete(
    hub,
    ctx,
    url: str,
    headers: Dict[str, str] = None,
    success_codes: List[int] = None,
    **kwargs,
):
    if not success_codes:
        success_codes = [200]
    if not headers:
        headers = {}
    if not headers.get("content-type"):
        headers["content-type"] = "application/json"

    async with await hub.tool.request.session.delete(
        ctx, url=url, headers=headers, **kwargs
    ) as response:
        success = response.status in success_codes
        if success:
            ret = hub.tool.type.dict.namespaced(await response.json())
        else:
            hub.log.debug("Delete error: {}".format(await response.read()).strip())
            ret = {}
        return {
            "ret": ret,
            "status": success,
            "status_code": response.status,
            "comment": response.reason,
            "headers": response.headers,
        }


async def get(
    hub,
    ctx,
    url: str,
    headers: Dict[str, str] = None,
    success_codes: List[int] = None,
    **kwargs,
):
    if not success_codes:
        success_codes = [200]
    if not headers:
        headers = {}
    if not headers.get("content-type"):
        headers["content-type"] = "application/json"

    async with await hub.tool.request.session.get(
        ctx, url=url, headers=headers, **kwargs
    ) as response:
        success = response.status in success_codes
        if success:
            ret = hub.tool.type.dict.namespaced(await response.json())
        else:
            hub.log.debug("Get error: {}".format(await response.read()).strip())
            ret = {}
        return {
            "ret": ret,
            "status": success,
            "status_code": response.status,
            "comment": response.reason,
            "headers": response.headers,
        }


async def head(
    hub,
    ctx,
    url: str,
    headers: Dict[str, str] = None,
    success_codes: List[int] = None,
    **kwargs,
):
    if not success_codes:
        success_codes = [200]
    if not headers:
        headers = {}
    if not headers.get("content-type"):
        headers["content-type"] = "application/json"

    async with await hub.tool.request.session.head(
        ctx, url=url, headers=headers, **kwargs
    ) as response:
        success = response.status in success_codes
        if success:
            ret = hub.tool.type.dict.namespaced(await response.json())
        else:
            hub.log.debug("Head error: {}".format(await response.read()).strip())
            ret = {}
        return {
            "ret": ret,
            "status": success,
            "status_code": response.status,
            "comment": response.reason,
            "headers": response.headers,
        }


async def patch(
    hub,
    ctx,
    url: str,
    headers: Dict[str, str] = None,
    success_codes: List[int] = None,
    **kwargs,
):
    if not success_codes:
        success_codes = [200]
    if not headers:
        headers = {}

    if not headers.get("content-type"):
        headers["content-type"] = "application/json"

    async with await hub.tool.request.session.patch(
        ctx, url=url, headers=headers, **kwargs
    ) as response:
        success = response.status in success_codes
        if success:
            ret = hub.tool.type.dict.namespaced(await response.json())
        else:
            hub.log.debug("Patch error: {}".format(await response.read()).strip())
            ret = {}
        return {
            "ret": ret,
            "status": success,
            "status_code": response.status,
            "comment": response.reason,
            "headers": response.headers,
        }


async def post(
    hub,
    ctx,
    url: str,
    headers: Dict[str, str] = None,
    success_codes: List[int] = None,
    **kwargs,
):
    if not success_codes:
        success_codes = [200]
    if not headers:
        headers = {}
    if not headers.get("content-type"):
        headers["content-type"] = "application/json"

    async with await hub.tool.request.session.post(
        ctx, url=url, headers=headers, **kwargs
    ) as response:
        success = response.status in success_codes
        if success:
            ret = hub.tool.type.dict.namespaced(await response.json())
        else:
            hub.log.debug("Post error: {}".format(await response.read()).strip())
            ret = {}
        return {
            "ret": ret,
            "status": success,
            "status_code": response.status,
            "comment": response.reason,
            "headers": response.headers,
        }


async def put(
    hub,
    ctx,
    url: str,
    headers: Dict[str, str] = None,
    success_codes: List[int] = None,
    **kwargs,
):
    if not success_codes:
        success_codes = [200]
    if not headers:
        headers = {}

    headers["content-type"] = "application/json"
    async with await hub.tool.request.session.put(
        ctx, url=url, headers=headers, **kwargs
    ) as response:
        success = response.status in success_codes
        if success:
            ret = hub.tool.type.dict.namespaced(await response.json())
        else:
            hub.log.debug("Put error: {}".format(await response.read()).strip())
            ret = {}
        return {
            "ret": ret,
            "status": success,
            "status_code": response.status,
            "comment": response.reason,
            "headers": response.headers,
        }
