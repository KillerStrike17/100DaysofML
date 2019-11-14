# Calling All the Heavenly Bodies 
from twitter_credentials import *
from tweepy import OAuthHandler, Stream, Cursor, API
from tweepy.streaming import StreamListener
import tweepy
import pandas as pd
import numpy as np
import json
import time
import re
import os.path

class Authenticate_Twitter():

	# ###
	# Class to Authenticate user to Twitter API
	#
	# Attributes: 
	# ----------
	#	auth: OAuthHandler Class object authenticating the user to use the API
	# 	consumer_key: Unique key to identify user
	#	consumer_secret: Unique secret key to identify user
	#	access_token: Unique token to check for required access permissions
	#	access_secret: Unique token secret to check for required access permissions
	#
	# Function:
	# --------
	#	authenticate_twitter_api: returns authenticated OAuthHandler class object
	# ###

	def authenticate_twitter_api(self):

	# ###	
	# This function is used for authentication
	#
	# Parameter:
	# ---------
	#
	# Raises:
	# ------
	# 	Exception:
	# 		To handle any kind of Exception
	# ###

		try:
			auth = OAuthHandler(consumer_key,consumer_secret)
			auth.set_access_token(access_token, access_secret)
			return auth

		except Exception as e:
			print("Exception at Authenticate_Twitter Class: ",e)

class Clean_Data():

	# ###
	# Class to convert data to a clean format
	# 
	# Attributes:
	# ----------
	#	data: The variable holds tweets in json format
	#	friendlist: The variable holds details of user in json format
	#	df: DataFrame
	#
	# Function:
	# --------
	#	tweets_to_df: This function is used to convert the incoming tweet to a 
	#					clean and readable format and store in a dataframe and
	#					return it to the incoming function
	#	friends_to_df:This function is used to extract the user data from the list
	#					and store in a dataframe and return it to the calling functions
	#	stream_tweet_to_df: This function will convert the incoming stream of tweet to dataframe
	#					and return a dataframe
	# ###

	def clean_text(self, data):
		try:
			return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", data).split())
		except Exception as e:
			print("Exception at class Clean_Data over function clean_text:" ,e)


	def tweets_to_df(self,data):

		# ###	
		# This function is used to convert the incoming tweets to dataframe
		#
		# Parameter:
		# ---------
		#	data:It is a variable containing tweet in json format
		#
		# Raises:
		# ------
		# 	Exception:
		# 		To handle any kind of Exception
		# ###

		try:
			df = pd.DataFrame()
			for tweet in data:
				# print(tweet,"\n\n\n\n\n")
				retweet_check = tweet._json.get("retweeted_status")
				if None != retweet_check:
					df = df.append([[self.clean_text(str(retweet_check.get("full_text"))),len(self.clean_text(str(retweet_check.get("full_text")))),tweet.created_at,tweet.source,tweet.favorite_count,tweet.retweet_count,	tweet.coordinates,tweet.geo,tweet.lang]],ignore_index = True)

				else:
					df = df.append([[self.clean_text(tweet.full_text),len(self.clean_text(tweet.full_text)),tweet.created_at,tweet.source,tweet.favorite_count,tweet.retweet_count,	tweet.coordinates,tweet.geo,tweet.lang]],ignore_index = True)
				
				#print(df)
			df.columns = ['Tweet','Tweet Length','Date of Creation','Source','Likes','Retweets','Coordinates','Geo','Language']
			#print(df)
			
			with open('user_tweets.csv','a') as f:
				fileEmpty = os.stat('user_tweets.csv').st_size == 0
				if fileEmpty:
					print("adding headers")
					df.to_csv(f,header  = True,index = False,line_terminator = '\n')
				else:
					df.to_csv(f,header  = False,index = False,line_terminator = '\n')
			return df

		except Exception as e:
			print("Exception at Clean Data class over tweets_to_df function:", e)

	def friends_to_df(self, friendlist):

		# ###	
		# This function is used to extract the friend_name and screenname from the friendlist 
		# and return a dataframe
		#
		# Parameter:
		# ---------
		#	friendlist:It is a variable containing user details in json format
		#
		# Raises:
		# ------
		# 	Exception:
		# 		To handle any kind of Exception
		# ###

		try:
			df = pd.DataFrame()
			for friend in friendlist:
				df = df.append([[friend.name,friend.screen_name]])
			df.columns = ['Name','Screen_Name']
			with open('friend_list.csv','a') as f:
				df.to_csv(f,header  = False,index = False,line_terminator = '\n')
			print (df)
			return df

		except Exception as e:
			print("Exception at Clean Data class over friends _to_df function:", e)
	
	def stream_tweet_to_df(self, tweet,data_frame):
		try:
			# df = pd.dataframe()
			print(tweet)
			# all_data = json.loads(tweet)
			# data_frame = pd.DataFrame([[all_data["text"],len(all_data["text"]),all_data["created_at"],all_data["source"],all_data["favorite_count"],all_data["retweet_count"],	all_data["coordinates"],all_data["geo"],all_data["lang"]]])
			# # print(data_frame)
			# with open('stream_tweet.csv','a') as f:
			# 	data_frame.to_csv(f,header  = False,index = False,line_terminator= '\n')

		except Exception as e:
			print("Exception at Clean_Data class at function stream_tweet_to_df: ",e)

class Twitter_Listener(StreamListener):

	# ###
	# Twitter Listener Class inherting StreamListener Class.
	# This class is used to get the data
	# 
	# Attributes:
	# ----------
	# 	data: it is a variable containing a tweet  in json format
	#	status: It is variable which stores the status of process
	#	tweet: Dataframe containing the cleaned tweet
	# 
	# Function:
	# --------
	# 	__init__: creates a Clean_Data class object
	#	on_data: It is an overriden function used to get the incoming data
	#	on_error: It is an overriden function used triggered in Error
	# ###

	def __init__(self):

		# ###	
		# This is a constructor to initialize Clean_Data class object
		#
		# Parameter:
		# ---------
		#
		# Raises:
		# ------
		#
		# ###

		self.clean_data = Clean_Data()
		self.df = pd.DataFrame()
		#columns = ['Tweet','Tweet Length','Date of Creation','Source','Likes','Retweets','Coordinates','Geo','Language']
	
	def on_data(self,data):

		# ###	
		# This is an overriden function used to accept the incoming data in json and
		# perform cleaning and convert it to dataframe
		#
		# Parameter:
		# ---------
		#	data:It is a variable containing tweet in json format
		#
		# Raises:
		# ------
		# 	Exception:
		# 		To handle any kind of Exception
		# ###

		try:
			self.df = self.clean_data.stream_tweet_to_df(data,self.df)
			#print(self.df)
			# return self.df


		except Exception as e:
			print("Exception at on_data function: ",e)

		return True

	def on_error(self,status):

		# ###	
		# This is an overriden function to trigger on geting the error
		#
		# Parameter:
		# ---------
		#	data:It is a variable containing tweet in json format
		#
		# Raises:
		# ------
		# 	Exception:
		# 		To handle any kind of Exception
		# ###
		
		if status == 420: #returning false on datamethod incase rate limit occurs
			return False
		print(status)

class Stream_Tweets():

	# ###
	# Stream Tweet Class is used to authenticate and stream the data containing the hashed list words
	#
	# Attributes:
	# ----------
	#	hashed_list: It is a list containting words of interest provided by user
	#	stream: It is a Stream class object
	#	twitter_listener: It is a Twitter_Listener class object
	#
	# Function:
	# --------
	# 	__init__: It is a constructor used to create a Authenticate_Twitter class object
	#	stream_data: This function has the task to stream tweets containing words of interest.
	# ###

	def __init__(self):

		# ###	
		# This is a constructor to create Authenticate_Twitter Class object
		#
		# Parameter:
		# ---------
		#
		# Raises:
		# ------
		#
		# ###

		self.auth_twitter = Authenticate_Twitter()

	# Function to steam the filtered data
	def stream_data(self,hashed_list):

		# ###	
		# This function filters tweets based on the word of interest
		#
		# Parameter:
		# ---------
		#	hashed_list: contains a list of word of interest
		#
		# Raises:
		# ------
		# 	Exception:
		# 		To handle any kind of Exception
		# ###

		try:
			twitter_listener = Twitter_Listener()
			auth = self.auth_twitter.authenticate_twitter_api()
			stream=Stream(auth,twitter_listener,tweet_mode = 'extended')
			print(stream.filter(track =hashed_list))
		except Exception as e:
			print("Exception at Stream_Tweet Class: ",e)

class User_Tweets():

	# ###
	# Class to get Tweets from a User 
	# 
	# Attributes:
	# ----------
	#	tweets: List of Tweets of a particular user
	#	friendlist: List of friends of a particular user
	#	twitter_username: Variable containing the username
	#	num_tweets: Variable containing the number of tweets to fetch
	#	num_friends: Variable containing the number of friends to fetch 
	#
	# Function:
	# --------
	#	__init__: It is a constructor used to create an Authenticate_Twitter class object, API object and Exception 
	#				_Handler class object
	#	get_user_timeline_tweet: It is used to get the recent n feeds from the timeline of a particular user
	#	get_friendlist_of_user: It is used to get n friends of a particular user. 
	# ###
	
	def __init__(self):

		# ###	
		# Constructor to Authenticate Twitter Account, and create object of API and Exception_Handler class
		#
		# Parameter:
		# ---------
		#
		# Raises:
		# ------
		#
		# ###

		self.auth = Authenticate_Twitter().authenticate_twitter_api()
		self.twitter_client = API(self.auth)
		self.exception_handler  = Exception_Handler()
		#self.twitter_username = twitter_username

	def get_user_timeline_tweet(self,num_tweets,twitter_username = None):

		# ###	
		# This function filters tweets based on the word of interest
		#
		# Parameter:
		# ---------
		#	num_tweets: It is a variable containing the number of tweets required to fetch
		#	twitter_username: It is a varible containing the username of the user whose tweet is required
		#	tweet: It is a list of tweets 
		#
		# Raises:
		# ------
		# 	Exception:
		# 		To handle any kind of Exception
		# ###

		tweets = []
		for tweet in self.exception_handler.rate_limit_handler(Cursor(self.twitter_client.user_timeline,id = twitter_username,tweet_mode='extended').items(num_tweets)):
			tweets.append(tweet)
			#print(dir(tweet))
		return tweets

	def get_friendlist_of_user(self, num_friends,twitter_username = None):
		
		# ###	
		# Function to get the friendlist of a particular user
		#
		# Parameter:
		# ---------
		#	num_friends: It is a variable containing the number of friends required to fetch
		#	twitter_username: It is a varible containing the username of the user whose tweet is required
		#	friendlist: It is a list of friends
		#
		# Raises:
		# ------
		# 	Exception:
		# 		To handle any kind of Exception
		# ###

		friendlist = []
		for friend in self.exception_handler.rate_limit_handler(Cursor(self.twitter_client.friends,id = twitter_username).items(num_friends)):
			friendlist.append(friend)
		return friendlist

class Exception_Handler():

	# ###
	# Exception Handler for RateLimit Error
	#
	# Attributes:
	# ----------
	#	cursor: it is a variable containing a cursor object
	#
	# Function:
	# --------
	#	rate_limit_handler: This function is used to handle RateLimit Exception
	# ###

	def rate_limit_handler(self, cursor):
		# ###	
		# Function to handle Exception 
		#
		# Parameter:
		# ---------
		#	cursor: It is a variable containing cursor object
		#
		# Raises:
		# ------
		# 	Exception:
		# 		To handle any kind of Exception
		# ###

		while True:
			# Check for next Available Entry
			try:
				yield next(cursor)

			# To avoid new-in-3.7 python Behavior
			except StopIteration:
				return

			# To sleep on RateLimit Exceed Error
			except tweepy.RateLimitError:
				print("Please wait for sometime")
				time.sleep(15 * 60)