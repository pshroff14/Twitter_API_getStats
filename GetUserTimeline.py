# Getting User Timeline through entry of twitter handle 
# Using Python-Twitter https://github.com/twitterdev/search-tweets-python

import twitter
from searchtweets import collect_results


consumer_key = '<Enter Here>'
consumer_secret = '<Enter Here>'
access_token = '<Enter Here>'
access_secret = '<Enter Here>'


# Authenticate to Twitter
api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_secret)


(api.VerifyCredentials())

#GetUserTimeline
x = 0
print("Enter Twitter Handle:   ")

user=api.GetUserTimeline(
                         user_id= None,
                         screen_name= input(x),
                         max_id=None,
                         count=None,
                         include_rts=True,
                         trim_user=False,
                         exclude_replies=False)
print(user)
