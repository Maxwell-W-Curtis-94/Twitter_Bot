import logging as lo
import tweepy


class Functions:
    pass

    def __init__(self):
        lo.info("Functions starting")

    def tweet_out(self, api, tweet):
        lo.info("tweeting->{tweet}".format(tweet=tweet))
        api.update_status(tweet)

    def read_timeline(self, api):
        pass

    def get_user(self, api, twitter_handle):
        pass

    def add_follower(self, api, twitter_handle):
        pass

    def like_post(self, api, twitter_handle):
        if twitter_handle == None:
            tweets = api.home_timeline(count=1)
            tweet = tweets[0]
            api.create_favorite(tweet.id)
        else:
            pass

    def block_user(self, api, twitter_handle):
        pass
