from textblob import TextBlob 

class Analyze_Tweet():
    
    # ###
    # This class is used to analyze the tweet over the sentiment and return the sentiment.
    #
    # Attributes:
    # ----------
    #   tweet: A variable of type strnig containing the tweet
    #   analysis_result: An object of TextBLob class
    # 
    # Function:
    # --------
    #   Analyze_Sentiment: This function has to task to analyze tweet and return the sentiment
    # ###

    def Analyze_Sentiment(self,tweet):

        # ###
        # This is a function to return sentiment of a tweet
        #
        # Parameters:
        # ----------
        #   tweet: It is a text varibale containing tweet.
        #
        # Raises:
        # ------
		# 	Exception:
		# 		To handle any kind of Exception
        # ###

        try:
            analysis_result = TextBlob(tweet)
            if analysis_result.sentiment.polarity > 0:
                return "Positive"
            elif analysis_result.sentiment.polarity == 0:
                return "Neutral"
            else:
                return "Negative"
                
        except Exception as e:
            print("Exception as Analyze_Tweet Class on function Analyze_Sentiment: ",e)
            return "Nil"
        
a = Analyze_Tweet()
print("you are awesome:- ",a.Analyze_Sentiment("you are awesome"))
print("you are bad:- ",a.Analyze_Sentiment("you are bad"))
print("hi, how are you:- ", a.Analyze_Sentiment("hi, how are you"))