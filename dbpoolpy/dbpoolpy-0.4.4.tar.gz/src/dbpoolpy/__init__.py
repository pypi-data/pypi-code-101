from pymysql import install_as_MySQLdb
install_as_MySQLdb()

from .dbpool import init_pool
from .dbpool import connect_db
from .dbpool import connect_without_exception
from .dbpool import with_connect_db
from .table import SelectTable as Select
from .table import UpdateTable as Update
from .table import DeleteTable as Delete
from .table import InsertTable as Insert
from .config import settings
