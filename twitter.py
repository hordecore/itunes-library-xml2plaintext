#!/usr/bin/python

# coding: utf-8
# author: oleg

import tweepy
from config import consumer_key, consumer_secret, access_key, access_secret

def tweet(msg):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    tweepy.API(auth).update_status(msg)

def top_of_diff(diff):
    tweet("mmm, что это тут у нас, ммм, lastfm с твиттером")
