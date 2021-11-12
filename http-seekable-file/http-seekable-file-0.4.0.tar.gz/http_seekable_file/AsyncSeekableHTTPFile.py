import cgi
import io
from typing import Optional

import aiohttp
from asynciobase import AsyncIOBase
import asyncio_rlock

# https://github.com/JuniorJPDJ/pyChomikBox/blob/master/ChomikBox/utils/SeekableHTTPFile.py
class AsyncSeekableHTTPFile(AsyncIOBase):
    async def __aenter__(self) -> 'AsyncSeekableHTTPFile':
        async with self._lock:
            if not self.__inited:
                f = await self.sess.head(self.url, headers={'Range': 'bytes=0-'}, timeout=self.timeout)
                if (f.status == 206 and 'Content-Range' in f.headers) or (
                    f.status == 200 and 'Accept-Ranges' in f.headers):
                    self._seekable = True
                self.resp_headers = f.headers
                self.len = int(f.headers["Content-Length"])
                # TODO: handle files without Content-Length
                if self._name is None:
                    if "Content-Disposition" in f.headers:
                        value, params = cgi.parse_header(f.headers["Content-Disposition"])
                        if "filename" in params:
                            self._name = params["filename"]

                    if self._name is None:
                        self._name = self.url.rsplit('/', 1)[-1]
                await f.release()

                self._closed = False
                self.__inited = True

            await self._reopen_stream()

            return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        async with self._lock:
            await self.close()

    def __init__(self, url: str, name: Optional[str] = None, aiohttp_session: Optional[aiohttp.ClientSession] = None, timeout: int = 30):
        # SHOULD BE CREATED USING ASYNC CONTEXT MANAGER OR `create()` METHOD
        self.__inited = False

        self._lock = asyncio_rlock.RLock()

        self.url = url
        self.sess = aiohttp.ClientSession(skip_auto_headers=(aiohttp.hdrs.ACCEPT_ENCODING,)) if aiohttp_session is None else aiohttp_session
        self._local_session = aiohttp_session is None
        self._seekable = False
        self.timeout = timeout
        self._init_called = False
        self._name = name
        self.len = None
        self.resp_headers = None
        self._closed = True

        self._pos = 0
        self._r: Optional[aiohttp.ClientResponse] = None


    def __len__(self) -> int:
        return self.len

    async def _reopen_stream(self):
        async with self._lock:
            if self._r is not None:
                await self._r.release()
            if self._seekable:
                self._r = await self.sess.get(self.url, headers={'Range': 'bytes={}-'.format(self._pos)}, timeout=self.timeout)
            else:
                self._pos = 0
                self._r = await self.sess.get(self.url, timeout=self.timeout)
            self.resp_headers = self._r.headers

    async def close(self):
        async with self._lock:
            if self._r is not None:
                await self._r.release()
            if self._local_session:
                await self.sess.close()
            self._closed = True

    @property
    def closed(self):
        return self._closed

    @classmethod
    async def create(cls, url: str, name: Optional[str] = None, aiohttp_session: Optional[aiohttp.ClientSession] = None, timeout: int = 30) -> 'AsyncSeekableHTTPFile':
        self = cls(url, name, aiohttp_session, timeout)
        await self.__aenter__()
        return self

    @property
    def name(self) -> str:
        return self._name

    @property
    def mimetype(self):
        return self.resp_headers["Content-Type"]

    async def read(self, amount: int = -1) -> bytes:
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        if not await self.readable():
            raise io.UnsupportedOperation

        async with self._lock:
            if self._r is None or self._r.closed:
                await self._reopen_stream()
            if amount < 0:
                content = await self._r.content.read()
            else:
                content = await self._r.content.read(amount)
            self._pos += len(content)
            return content

    async def readable(self) -> bool:
        return not self.closed

    async def seek(self, offset: int, whence: int = io.SEEK_SET) -> int:
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        if not await self.seekable():
            raise io.UnsupportedOperation

        async with self._lock:
            if whence == io.SEEK_SET:
                self._pos = 0
            elif whence == io.SEEK_CUR:
                pass
            elif whence == io.SEEK_END:
                self._pos = self.len
            self._pos += offset
            if self._r is not None:
                await self._r.release()
            return self._pos

    async def seekable(self) -> bool:
        return self._seekable

    async def tell(self) -> int:
        return self._pos
