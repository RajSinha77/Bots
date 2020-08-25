import tweepy 
from time import sleep 
from credentials import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME 

auth = tweepy.OAuthHandler('TZOCY856j0YL8XPlyzK325UOT', 'zD7be4s8eFdNfAKnIMG1K3j5pgXRhcDqvZdPbSW3urEpIA0lE9') 
auth.set_access_token('1180841409676550144-iSeJKD8RE90cZWtzXxTa6RCtMhZben', 'Zrbcgis07qwQZLSWg4tscawrUnsVWY5IOsV5ld3y48Gsd') 
api = tweepy.API(auth) 

print("Twitter bot which retweets, like tweets and follow users") 
print("Bot Settings") 
print("Like Tweets :", LIKE) 
print("Follow users :", FOLLOW) 

for tweet in tweepy.Cursor(api.search, q = QUERY).items(): 
	try: 
		print('\nTweet by: @' + tweet.user.screen_name) 

		tweet.retweet() 
		print('Retweeted the tweet') 

		# Favorite the tweet 
		if LIKE: 
			tweet.favorite() 
			print('Favorited the tweet') 

		# Follow the user who tweeted 
		# check that bot is not already following the user 
		if FOLLOW: 
			if not tweet.user.following: 
				tweet.user.follow() 
				print('Followed the user') 

		sleep(SLEEP_TIME) 

	except tweepy.TweepError as e: 
		print(e.reason) 

	except StopIteration: 
		break
