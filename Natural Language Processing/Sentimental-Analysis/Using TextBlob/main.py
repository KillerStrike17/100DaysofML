# Importing the libraries
import sys
sys.path.append(r'D:\Github\100DaysofML\Natural Language Processing\Stream_Twitter')
from twitter_stream import *
from sentiment_analysis import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ###
# Function to convert Sentiments to values
# 
# Parameter:
# ---------
# 	Sentiment -  it is a variable that contains sentiment of a text. 
# ###
def check(sentiment):
    #print(sentiment)
    if sentiment == "Positive":
        return 1
    elif sentiment == "Negative":
        return -1
    else:
        return 0

# Stream of Users Tweets
twitter_client = User_Tweets()
tweets = twitter_client.get_user_timeline_tweet(2000,"realDonaldTrump")
clean_data = Clean_Data()
clean_data.tweets_to_df(tweets)
df = pd.read_csv('user_tweets.csv')

# Analyzing Sentiments
a = Analyze_Tweet()
df['sentiments'] = np.array([a.Analyze_Sentiment(row[0]) for index,row in df.iterrows()])
df2 = df.filter(['sentiments'],axis = 1)

# Plotting Graph
counter_variable = 0
y = []
for index,row in df2.iterrows():
    counter_variable  = counter_variable + check(row[0])
    y.append(counter_variable)

print(len(df2))
x = range(len(df2))
plt.plot(x,y)
plt.show()



# # Stream of User Friendlist Tweets
# friendlist = twitter_client.get_friendlist_of_user(10,"killerstrike17")
# clean_data.friends_to_df(friendlist)

# twitter_client = User_Tweets()
	
# tweets = twitter_client.get_user_timeline_tweet(100,"realDonaldTrump")

# friendlist = twitter_client.get_friendlist_of_user(10)
# # print(friendlist)
# clean_data = Clean_Data()
# df = clean_data.friends_to_df(friendlist)
# #df = clean_data.tweets_to_df(tweets)
