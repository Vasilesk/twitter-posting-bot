from mysql.connector import MySQLConnection, Error
from mysql_operations import connect, get_max_prior, get_count_by_priority, set_priority

import random

from twitter_api_operations import tweepy_api_create

def quote_post():
    try:
        # twitter api
        api = tweepy_api_create()

        # mysql api
        conn = connect()
        cursor = conn.cursor()

        max_priority = get_max_prior(conn)
        random_tweet_max_number = get_count_by_priority(conn, max_priority)
        random_tweet_number = random.randint(1, random_tweet_max_number)

        query = "SELECT id, tweet FROM tweets WHERE priority = %s"
        data = (max_priority, )
        cursor.execute(query, data)

        for x in range (0, random_tweet_number):
            row = cursor.fetchone()

        tweet_id = row[0]
        tweet_text = row[1]

        while row is not None:
            row = cursor.fetchone()

        api.update_status(tweet_text)
        set_priority(conn, tweet_id, max_priority - 1)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def test_mysql():
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

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def test_twi_api():
    try:
        print "Hi"
        api = tweepy_api_create()

        api.update_status("Status with tweepy!")

    except Error as e:
        print(e)

quote_post()
