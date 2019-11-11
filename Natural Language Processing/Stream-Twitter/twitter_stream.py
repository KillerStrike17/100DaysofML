# Loading Credentials to access Twitter API
from twitter_credentials import *
from tweepy import OAuthHandler, Stream, Cursor, API
from tweepy.streaming import StreamListener
import pandas as pd
import numpy as np
import json


# ###
# Class to Authenticate user to Twitter API
# ###
class Authenticate_Twitter():

	# This function is used for authentication
	def authenticate_twitter_api(self):

		try:
			auth = OAuthHandler(consumer_key,consumer_secret)
			auth.set_access_token(access_token, access_secret)
			return auth

		except Exception as e:
			print("Exception at Authenticate_Twitter Class: ",e)

# ###
# Class to convert the incoming data to a clean format
# ###
class Clean_Data():

	def convert_to_df(self,data):
		data = json.loads(data)
		df = pd.DataFrame(data = [data['text']],columns  = ['Tweets'])
		return df


# ###
# Twitter Listener Class inherting StreamListener Class.
# This class is used to get the data
# ###
class Twitter_Listener(StreamListener):
	def __init__(self):
		self.clean_data = Clean_Data()
	
	def on_data(self,data):

		try:
			#print(data)
			tweet = self.clean_data.convert_to_df(data)
			print(tweet)

		except Exception as e:
			print("Exception at on_data function: ",e)

		return True

	#on error function is an overriden function to trigger on geting the error
	def on_error(self,status):
		#returning false on datamethod incase rate limit occurs
		if status == 420:
			return False
		print(status)


# ###
# Stream Tweet Class is used to authenticate and stream the data
# ###
class Stream_Tweets():

	# Constructor to create Authenticate_Twitter Class object
	def __init__(self):
		self.auth_twitter = Authenticate_Twitter()

	# Function to steam the filtered data
	def stream_data(self,hashed_list):

		try:
			twitter_listener = Twitter_Listener()
			auth = self.auth_twitter.authenticate_twitter_api()
			stream=Stream(auth,twitter_listener)
			stream.filter(track =hashed_list)

		except Exception as e:
			print("Exception at Stream_Tweet Class: ",e)


if __name__ == "__main__":
	hashed_list = ['Trump','USA']
	twitter_streamer = Stream_Tweets()
	twitter_streamer.stream_data(hashed_list)

