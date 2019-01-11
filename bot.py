import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def save_the_date(title, day, month, date, time, location):
    title_part = "Save the date for %s " % (title)
    date_part  = "on %s, %s %s at %s. " % (day, month, date, time)
    loc_part = "%s." % (location)
    tweet = title_part + date_part + loc_part
    return tweet

def one_week_before(title, day, month, date, time, location):
    title_part = "Next week: %s " % (title)
    date_part  = "on %s, %s %s at %s. " % (day, month, date, time)
    loc_part = "%s." % (location)
    tweet = title_part + date_part + loc_part
    return tweet

def three_days_before(day, time, title, location):
    tweet = "See you on %s at %s at %s. %s." % (day, time, title, location)
    return tweet

def day_before(title, location):
    title_part = "Can you believe %s is tomorrow? " % (title)
    location_part = "It's in %s!" % (location)
    tweet = title_part + location_part
    return tweet

def day_of(time, location, title):
    return "TODAY AT %s in %s %s." % (time, location, title)

def send_tweet(api, tweet):
    status = api.update_status(tweet)
    return status
    
    
title = "Not-A-Real-Event"
day = "Monday"
month = "December"
date = 23
time = "1pm"
location = "Not-A-Real-Place"

tweet = save_the_date(title, day, month, date, time, location)
status = send_tweet(api, tweet)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)
