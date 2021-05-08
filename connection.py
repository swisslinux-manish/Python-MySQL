from mysql.connector import MySQLConnection, Error
from py_mysql_dbconfig import read_configfile

def connect():
    """ Connection to MySQL Database"""

    db_config = read_configfile()
    conn = None
    try:
        print('Connecting to MySQL database')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('successfully connected')
        else:
            print('failled to connect database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection closed')

if __name__ == '__main__':
    connect()

