from mysql.connector import MySQLConnection, Error
from py_mysql_dbconfig import read_configfile

def fetchone_query():
    try:
        dbconfig = read_configfile()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        sql = 'select * from sales where ordervalue = 619161.48 '
        cursor.execute(sql)
        row = cursor.fetchone()
        print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    fetchone_query()

