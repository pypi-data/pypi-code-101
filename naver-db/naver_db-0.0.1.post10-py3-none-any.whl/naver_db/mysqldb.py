try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    __path__ = __import__('pkgutil').extend_path(__path__, __name__)

import os    
from flask_mysqldb import MySQLdb

class MySQLDB(object):
    def __init__(self):
        self.db = MySQLdb.connect(host=os.environ.get('MYSQLHOSTNAME'), user=os.environ.get('MYSQLUSER'), passwd=os.environ.get('MYSQLPASSWD'), db=os.environ.get('MYSQLDB'))
                        
    def query_db(self, query, args=()):
        cur = self.db.cursor()
        cur.execute(query, args)
        r = [dict((cur.description[i][0], value)
                for i, value in enumerate(row)) for row in cur.fetchall()]
        cur.connection.close()
        return r


    def execute_db(self, query, args=()):
        cur = self.db.cursor()
        try:
            cur.execute(query, args)
            cur.connection.close()
            return True
        except cur.Error:
            cur.connection.close()
            return False
