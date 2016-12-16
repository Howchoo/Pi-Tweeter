import subprocess
import tweepy

from settings import (consumer_key, consumer_secret,
                      access_token, access_token_secret)


def tweet():
    if not (access_token and access_token_secret and consumer_key
            and consumer_secret):
        raise Exception('Add your Twitter API credentials to settings.py.')

    # Authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Tweet uptime
    uptime = subprocess.check_output(['uptime'])
    api.update_status(uptime)


if __name__ == '__main__':
    tweet()
