import logging
import time
import random

SECONDS = 86400


def daily_tweet(api):
    while True:
        tweet = get_tweet()
        api.update_status(tweet)
        time.sleep(SECONDS)


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
