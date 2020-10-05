from Twitter_Bot.Bot.Oath import authentication
from Twitter_Bot.Bot.daily_tweet import *
import threading
import logging


def start():
    api = authentication()
    if api is not None:
        threading.Thread(target=daily_tweet, args=(api,)).start()
    # start the daily timer -> create a new thread for this
    # main thread will what for events then respond based off// game loop|| subscriber model
    else:
        logging.error("Bot Failed to Authenticate")


if __name__ == '__main__':
    start()
