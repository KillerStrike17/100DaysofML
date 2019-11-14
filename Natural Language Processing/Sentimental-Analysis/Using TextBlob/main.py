# Importing the libraries
import sys
sys.path.append(r'D:\Github\100DaysofML\Natural Language Processing\Stream_Twitter')
from twitter_stream import *
from sentiment_analysis import *
import pandas as pd
import numpy as np


# Stream of Hashed words
# hashed_list = ['Trump','USA']
# twitter_streamer = Stream_Tweets()
# twitter_streamer.stream_data(hashed_list)

# Stream of Users Tweets
a = Analyze_Tweet()

# twitter_client = User_Tweets()
# tweets = twitter_client.get_user_timeline_tweet(10,"realDonaldTrump")
# clean_data = Clean_Data()
# clean_data.tweets_to_df(tweets)
df = pd.read_csv('user_tweets.csv')
# for index, row in df.iterrows() :
#     print(a.Analyze_Sentiment(row[0]))
df['sentiments'] = np.array([a.Analyze_Sentiment(row[0]) for index,row in df.iterrows()])
print(df.columns)
df2 = df.filter(['Tweet','sentiments'],axis = 1)
print(df2)


# # Stream of User Friendlist Tweets
# friendlist = twitter_client.get_friendlist_of_user(10,"killerstrike17")
# clean_data.friends_to_df(friendlist)

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
