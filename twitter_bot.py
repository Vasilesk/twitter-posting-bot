from mysql.connector import MySQLConnection, Error
from mysql_operations import connect

def proceed_row(id, tweet, label, priority):
    print(priority)

def get_max_prior(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(priority) FROM tweets")
    return cursor.fetchone()

def get_count_by_priority(conn, priority):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM tweets WHERE priority="+str(priority))
    return cursor.fetchone()

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


# def insert_tweet (conn, tweet, label):
#     query = "INSERT INTO tweets(tweet,label) " \
#             "VALUES(%s,%s)"
#     args = (tweet, label)
#
#     try:
#         cursor = conn.cursor()
#         cursor.execute(query, args)
#
#         if cursor.lastrowid:
#             print('last insert id', cursor.lastrowid)
#         else:
#             print('last insert id not found')
#
#         conn.commit()
#     except Error as error:
#         print(error)
#
#     finally:
#         cursor.close()
#
# def to_db_from_file():
#     try:
#         dbconfig = read_db_config()
#         conn = MySQLConnection(**dbconfig)
#
#         f = open('../quotes', 'r')
#         for line in f:
#             print line
#             insert_tweet(conn, line, "favs")
#
#     except Error as e:
#         print(e)
#
#     finally:
#         f.close()
#         conn.close()


if __name__ == '__main__':
    # connect()
    query_with_fetchone()
