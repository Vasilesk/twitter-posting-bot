from mysql.connector import MySQLConnection, Error
from mysql_operations import connect, get_max_prior, get_count_by_priority, set_priority

import random

def query_with_fetchone():
    try:
        conn = connect()
        cursor = conn.cursor()

        set_priority(conn, 1, 10000)

        max_priority = get_max_prior(conn)
        random_tweet_max_number = get_count_by_priority(conn, max_priority)
        random_tweet_number = random.randint(1, random_tweet_max_number)

        query = "SELECT id, tweet FROM tweets WHERE priority = %s"
        data = (max_priority, )
        cursor.execute(query, data)

        print random_tweet_number

        for x in range (0, random_tweet_number):
            row = cursor.fetchone()

        # we work with the row here. Don't forget to decrease the priority
        print(row)

        while row is not None:
            row = cursor.fetchone()

        # print get_count_by_priority(conn,*get_max_prior(conn))
        # print random.randint(4, 5)
        # max_number = get_count_by_priority(conn,*get_max_prior(conn))

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


query_with_fetchone()
