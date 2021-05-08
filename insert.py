from mysql.connector import MySQLConnection, Error
from py_mysql_dbconfig import read_configfile

def insert_sales(productLine, orderyear, orderValue):
    sql = "INSERT INTO sales(productLine,orderyear,orderValue)"\
        "VALUES(%s,%s,%s)"
    args = (productLine,orderyear,orderValue)

    try:
        db_config = read_configfile()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(sql,args)

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()
def main():
    insert_sales('Truck','2003', 4567)

if __name__ == '__main__':
    main()