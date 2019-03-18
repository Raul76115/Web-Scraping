from mysql.connector import MySQLConnection, Error
from py_mysql_dbconfig import read_db_config

def connect(conn):
    try:

        if conn.is_connected():
            print('connection established')
        else:
            print('connection failed')
        
    except Error as error:
        print(error)


def close_conn(conn):
    conn.close()
    print('Connection closed')

def query(conn,qry):
        cursor = conn.cursor()
        cursor.execute(qry)
        rows = cursor.fetchall()

        print('Total Row(s): ', cursor.rowcount)
        for row in rows:
            print(row)
        cursor.close()


if __name__ == '__main__':
    db_config = read_db_config()
    conn = MySQLConnection(**db_config)
    connect(conn)
    close_conn(conn)