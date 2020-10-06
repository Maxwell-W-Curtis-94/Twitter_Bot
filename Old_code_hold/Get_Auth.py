import os
import traceback
import tweepy
import Bot.Driver as driver
import logging as lo
import threading


class OAUTH:

    def __init__(self):
        lo.basicConfig(level=lo.INFO)
        lo.info("Starting Bot...")
        self.API_KEY = os.environ.get("API_KEY")
        self.API_SECRET = os.environ.get("API_SECRET")
        self.API_TOKEN = os.environ.get("API_TOKEN")
        self.ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
        self.ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")
        self.Authenticate()

    def Authenticate(self):
        lo.info("Starting Authentication...")
        auth = tweepy.OAuthHandler(self.API_KEY, self.API_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        try:
            api.verify_credentials()
            lo.info("Auth Passed")
            driver.Diver(api)
        except:
            lo.error("msg", stack_info=traceback.print_exc())


if __name__ == '__main__':
    OAUTH()
