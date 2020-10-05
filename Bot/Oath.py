import logging
import os
import traceback
import tweepy
from tweepy import TweepError

API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")


def authentication():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, API_SECRET)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        return api
    except TweepError:
        logging.error("MSG", stack_info=traceback.print_exc())
        return None
