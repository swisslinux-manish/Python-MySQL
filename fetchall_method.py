from mysql.connector import MySQLConnection, Error
from py_mysql_dbconfig import read_configfile

def fetchall_query():
    try:
        dbconfig = read_configfile()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        sql = 'select * from sales'
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except Error as e:
        print(e)
    
    finally:
        cursor.close()
        conn.close()

if __name__ =='__main__':
    fetchall_query()



