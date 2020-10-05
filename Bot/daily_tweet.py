import logging
import time

SECONDS = 10


def daily_tweet(api):
    last_tweet_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - last_tweet_time
        if elapsed_time > SECONDS:
            last_tweet_time = time.time()
            tweet = get_tweet()
            api.update_status(tweet)


def get_tweet():
    # cant send the same thing twice
    return "Test"
