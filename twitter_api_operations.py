from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser

def read_db_config(filename='config.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db

def connect():
    """ Connect to MySQL database """

    db_config = read_db_config()

    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('connection established.')
        else:
            print('connection failed.')

    except Error as error:
        print(error)

    return conn

def get_max_prior(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(priority) FROM tweets")
    return cursor.fetchone()[0]

def get_count_by_priority(conn, priority):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM tweets WHERE priority="+str(priority))
    return cursor.fetchone()[0]

def set_priority(conn, id, priority):
    cursor = conn.cursor()

    query = "UPDATE tweets SET priority = %s WHERE id = %s"
    data = (priority, id)

    cursor.execute(query, data)

def to_db_from_file(conn):
    try:
        f = open('../quotes.txt', 'r')
        for line in f:
            print line
            insert_tweet(conn, line, "favs")

    except Error as e:
        print(e)

    finally:
        f.close()
