#!/usr/bin/env python3
import tweepy

import settings
from src.twitter import StreamListener

if __name__ == '__main__':
    # Twitter Auth
    auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
    auth.set_access_token(settings.TWITTER_ACCESS_KEY, settings.TWITTER_ACCESS_SECRET)
    api = tweepy.API(auth)

    # Set up the listener.
    listener = StreamListener()
    stream = tweepy.Stream(auth=auth, listener=listener)

    # Stream Filter by words
    stream.filter(track=settings.TWITTER_FILTER_WORDS, languages=['pt'])
