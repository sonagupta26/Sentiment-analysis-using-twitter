from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s


#consumer key, consumer secret, access token, access secret.
ckey="DzWqrdtS4cATc9OLYw157ggr5"
csecret="MkdBpCtV2Zfq9EfzVjQuOT4rf5g1c50XXVIKJ885TWANS3KNnM"
atoken="840088269748486148-d3Qi8X5UDlkL1rlO76gLsr0I4o1PUsq"
asecret="VchJjVyEkqkgOsdT4ifuPSrAeK4wIrt01Wfg4IRYiRWS6"

class listener(StreamListener):

    def on_data(self, data):
        try: 
            all_data = json.loads(data)
            
            tweet = all_data["text"]

            sentiment_value, confidence = s.sentiment(tweet)
            print(tweet, sentiment_value, str(confidence*100)+"%")

            if confidence*100 >= 80:
                output = open("twitter-out.txt","a")
                output.write(sentiment_value)
                output.write('\n')
                output.close()
            
            return True
        except:
            return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["shahrukhkhan"])
