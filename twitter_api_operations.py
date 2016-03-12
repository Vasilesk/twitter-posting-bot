import tweepy
from configparser import ConfigParser

def read_twitter_config(filename='config.ini', section='twitter_api'):
    # Read twitter api configuration file and return a dictionary object
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section
    twitter_config = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            twitter_config[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return twitter_config

def tweepy_api_create():

    twitter_config = read_twitter_config()

    try:
        auth = tweepy.OAuthHandler(twitter_config['consumer_key'], twitter_config['consumer_secret'])
        auth.set_access_token(twitter_config['access_key'], twitter_config['access_secret'])

        api = tweepy.API(auth)

    except Error as error:
        print(error)

    return api

def get_favs(api):
    print "not yet"
