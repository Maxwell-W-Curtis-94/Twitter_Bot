import logging
import time
import random


def daily_tweet(api):
    seconds = 5
    print(seconds)
    last_tweet_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - last_tweet_time
        if elapsed_time > seconds:
            seconds = 86400
            last_tweet_time = time.time()
            tweet = get_tweet()
            api.update_status(tweet)


# replace with database connection
def get_tweet():
    quotes_file = open("../Bot/quotes.txt", "r", encoding="utf-8")
    quote = ""
    quotes = []
    for lines in quotes_file:
        quote += lines
        if lines == "\n":
            if len(lines) < 280:
                quotes.append(quote)
            quote = ""
    return quotes[random.randrange(0, len(quotes) - 1)]
