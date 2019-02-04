import json
import tweepy
import time
import twitter
import os
from profanityfilter import ProfanityFilter

def clean_tweets(username):
    """A program to clean up all your twitter of any profanity."""

    # Get API keys #
    keys_path = os.getcwd() + "/clean/twitter/secrets.json"
    with open(keys_path, 'r') as filein:
            try:
                keys = json.load(filein)
            except ValueError:  # simplejson.decoder.JSONDecodeError
                print("Error_JSON could not read json file")
                exit(1)

    
    # Authorization to consumer key and consumer secret 
    auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"]) 

    # Access to user's access key and access secret 
    auth.set_access_token(keys["access_token"], keys["access_token_secret"]) 

    # Calling api 
    api = tweepy.API(auth) 
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print ('Error! Failed to get request token.')

    # Get tweets #

    # 200 tweets to be extracted 
    number_of_tweets=200
    tweets = api.user_timeline(screen_name=username, tweet_mode='extended', count = number_of_tweets) 

    # profanity filter
    pf = ProfanityFilter()
    # Printing the tweets 
    for tweet in tweets:
        if not(pf.is_clean(tweet.full_text)):
            print(tweet.full_text + "\n") 

  

# my_statuses = api.user_timeline()
# count = 0
# for status in my_statuses:
#     print("ID: " + str(status.id) + "\nTWEET: " + status.text)
#     if count > 0 and count < 6:
#         api.destroy_status(status.id)
#     count = count + 1
    
# Get the User object for twitter...
# user = api.get_user('twitter')

