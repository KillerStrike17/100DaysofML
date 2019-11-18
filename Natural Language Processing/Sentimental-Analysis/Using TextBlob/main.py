# Importing the libraries
import sys
sys.path.append(r'D:\Github\100DaysofML\Natural Language Processing\Stream_Twitter')
from twitter_stream import *
from sentiment_analysis import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def check(sentiment):
    #print(sentiment)
    if sentiment == "Positive":
        return 1
    elif sentiment == "Negative":
        return -1
    else:
        return 0

# Stream of Hashed words
# hashed_list = ['Trump','USA']
# twitter_streamer = Stream_Tweets()
# twitter_streamer.stream_data(hashed_list)

# Stream of Users Tweets
a = Analyze_Tweet()

twitter_client = User_Tweets()
tweets = twitter_client.get_user_timeline_tweet(2000,"realDonaldTrump")
clean_data = Clean_Data()
clean_data.tweets_to_df(tweets)
df = pd.read_csv('user_tweets.csv')
# for index, row in df.iterrows() :
#     print(a.Analyze_Sentiment(row[0]))
df['sentiments'] = np.array([a.Analyze_Sentiment(row[0]) for index,row in df.iterrows()])
#print(df.columns)
df2 = df.filter(['sentiments'],axis = 1)
#print(df2)
counter_variable = 0
y = []
# df2['sentiments_label'] = np.array([counter_variable  = counter_variable + check(row[0]) for index,row in df2.iterrows()])
for index,row in df2.iterrows():
    counter_variable  = counter_variable + check(row[0])
    y.append(counter_variable)

print(len(df2))
x= range(len(df2))
#y = df2['sentiments_label']
plt.plot(x,y)
plt.show()
#np.array([check(row[0]) 
# for index,row in df2.iterrows():
#     print(check(row[0]))
# ax = plt.gca()
# df.plot()



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
