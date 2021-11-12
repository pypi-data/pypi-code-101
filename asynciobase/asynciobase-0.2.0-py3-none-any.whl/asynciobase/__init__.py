import io
from abc import abstractmethod, ABC
from typing import List

version = "0.2.0"


class AsyncIOBase(io.IOBase, ABC):
    def __aiter__(self):
        return self

    async def __anext__(self) -> bytes:
        val = await self.readline()
        if val == b'':
            raise StopAsyncIteration
        return val

    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    async def close(self):
        pass

    @property
    @abstractmethod
    def closed(self):
        pass

    # noinspection SpellCheckingInspection
    async def fileno(self):
        raise io.UnsupportedOperation

    async def flush(self):
        pass

    async def isatty(self) -> bool:
        return False

    @property
    def mode(self) -> str:
        return 'rb'

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    async def read(self, amount=-1) -> bytes:
        pass

    @abstractmethod
    async def readable(self) -> bool:
        pass

    async def readall(self) -> bytes:
        return await self.read()

    @abstractmethod
    async def readinto(self, buffer) -> int:
        pass

    async def readline(self, size: int = -1) -> bytes:
        if size == -1:
            size = float('inf')

        # TODO: should be done better, any ideas?
        if await self.seekable():
            buf = bytearray()
            buf_size = io.DEFAULT_BUFFER_SIZE
            read = b''
            while b'\n' not in read:
                read = await self.read(min(buf_size, size))

                buf += read
                if not read or len(read) >= size:
                    break
                size -= len(read)

            i = buf.find(b'\n')
            if i != -1:
                await self.seek(i - len(buf) + 1, io.SEEK_CUR)
                return bytes(buf[:i+1])
            else:
                return bytes(buf)

        else:
            buf = bytearray()
            read = b''
            while read != b'\n' and len(buf) != size:
                read = await self.read(1)
                if not read:
                    break
                buf += read

            return bytes(buf)

    # noinspection SpellCheckingInspection
    async def readlines(self, size=-1) -> List[bytes]:
        return [line async for line in self]

    async def seek(self, offset, whence=io.SEEK_SET) -> int:
        raise io.UnsupportedOperation

    async def seekable(self) -> bool:
        return False

    async def tell(self) -> int:
        raise io.UnsupportedOperation

    async def truncate(self, size=None):
        raise io.UnsupportedOperation

    async def writable(self) -> bool:
        return False

    async def write(self, *args, **kwargs):
        raise io.UnsupportedOperation

    async def writelines(self, lines):
        raise io.UnsupportedOperation
