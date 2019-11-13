# Importing the libraries
import sys
sys.path.append(r'D:\Github\100DaysofML\Natural Language Processing\Stream_Twitter')
from twitter_stream import *
from sentiment_analysis import *


# Stream of Hashed words
# hashed_list = ['Trump','USA']
# twitter_streamer = Stream_Tweets()
# twitter_streamer.stream_data(hashed_list)

# Stream of Users
twitter_client = User_Tweets()
tweets = twitter_client.get_user_timeline_tweet(10,"realDonaldTrump")
clean_data = Clean_Data()
clean_data.tweets_to_df(tweets)



# Sentimental Analysis of Batches 

# Live Plotting of Sentiments

#
# twitter_client = User_Tweets()
	
# tweets = twitter_client.get_user_timeline_tweet(10,"killerstrike17")

# friendlist = twitter_client.get_friendlist_of_user(10)
# # print(friendlist)
# clean_data = Clean_Data()
# df = clean_data.friends_to_df(friendlist)
# #df = clean_data.tweets_to_df(tweets)

# print(df)
