import pymysql

def get_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='health_system',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
