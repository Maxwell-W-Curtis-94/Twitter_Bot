from Twitter_Bot.Old_code_hold.Functions import Functions as twitter
import Twitter_Bot.Old_code_hold.Functions as twitter
import sched, time
import logging as lo
import random


class Diver:
    # 86400

    def __init__(self, api):
        self.index = 0
        self.start_bot(api=api)
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.scheduler.enter(1, 1, self.daily_tweet, (api,))
        self.scheduler.run()

    def start_bot(self, api):
        lo.info("Starting Driver")

    # def like_post(self, api, twitter_handle):
    def daily_tweet(self, api):
        lo.info("Daily Tweet")
        tweet = self.get_daily_tweet()
        twitter.Functions.tweet_out(self, api=api, tweet=tweet)
        twitter.Functions.like_post(self, api=api, twitter_handle=None)
        self.scheduler.enter(5, 1, self.daily_tweet, (api,))

    def get_daily_tweet(self):
        quotes = open("../Bot/quotes.txt", "r", encoding="utf-8")
        quotes_list = []
        used = []
        string = ""
        for i in quotes:
            string += i
            if i == "\n":
                if len(string) < 280:
                    quotes_list.append(string)
                string = ""
        return quotes_list[self.gen_index(range=len(quotes_list) - 1)]

    def gen_index(self, range):
        lo.info(self.index)
        index = random.randrange(0, range, 1)
        lo.info("gen index-{index}".format(index=index))
        if self.index == index:
            self.gen_index()
            self.index = index
        else:
            return index
