"""Declares :class:`Connection`."""
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker


class Connection:
    """A wrapper around :class:`databases.Database`."""
    async_schemes = {
        'mysql'     : 'mysql+aiomysql',
        'postgresql': 'postgresql+asyncpg',
        'sqlite'    : 'sqlite+aiosqlite'
    }

    def __init__(self, dsn):
        self.__dsn = dsn
        self.__engine = None
        self.__session_factory = None

    def begin(self):
        """Begin a transaction without any session management using the
        underlying database connection.
        """
        return self.__engine.begin()

    async def connect(self, debug: bool = False, *args, **kwargs) -> None:
        """Connect to the database server."""
        if self.__engine is not None:
            raise RuntimeError("Connection already established.")
        self.__engine = create_async_engine(
            self.get_dsn_async(),
            echo=debug
        )
        self.__session_factory = sessionmaker(
            self.__engine,
            expire_on_commit=False,
            class_=AsyncSession
        )

    async def disconnect(self, *args, **kwargs) -> None:
        """Disconnect from the database server."""
        if self.__engine is None:
            return
        await self.__engine.dispose()
        self.__engine = None
        self.__session_factory = None

    def get_session(self, *args, **kwargs) -> AsyncSession:
        """Establish a new session."""
        return self.__session_factory(*args, **kwargs)

    def get_dsn_async(self) -> str:
        """Return a string containing the Data Source Name (DSN)
        for asynchronous connections.
        """
        return str.replace(
            self.__dsn.geturl(),
            self.__dsn.scheme,
            self.async_schemes[self.__dsn.scheme]
        )
