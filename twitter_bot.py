from mysql.connector import MySQLConnection, Error
from mysql_operations import connect, proceed_row, get_max_prior, get_count_by_priority

def query_with_fetchone():
    try:
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tweets")
        row = cursor.fetchone()

        while row is not None:
            # proceed_row(*row)
            print(row)
            row = cursor.fetchone()

        print get_count_by_priority(conn,*get_max_prior(conn))

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


query_with_fetchone()
