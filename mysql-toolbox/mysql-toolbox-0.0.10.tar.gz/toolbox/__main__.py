from . import xml_formatter_main, mysqlx_main
from importlib_metadata import version

if __name__ == "__main__" :
    print("# mysql-toolbox, version {}".format(version('mysql-toolbox')))
    print("# by Yonghang Wang, 2021")
    print("mysqlx                -  yet another mysql client to better work with shell utilities.")
    print("mysql-xml-formatter   -  formatting 'mysql --xml' output.")
