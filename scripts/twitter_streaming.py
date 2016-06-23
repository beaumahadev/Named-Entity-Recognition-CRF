#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import matplotlib.pyplot as plt

#Variables that contains the user credentials to access Twitter API 
access_token = "719949625390706689-kJuCtuQyF9fCnVNE5mpIY17I9W1kTUx"
access_token_secret = "j3TBKTLPYTuUlISaBZeALyIDfUgUWcbX7QRAlezEVCdbw"
consumer_key = "FXe80pBUHHYo2Wuj0J8YZOfJv"
consumer_secret = "i0QRBi8NR0sighfu7z0t8GKuphxH6drGFvIEVFRa8wztbIoSiJ"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        #start=data.index('text')
        #end=data.index('source:')
        tweet=json.loads(data)
        #Transforms into dictionary type python object 
        try:
            text=tweet["text"]
        except KeyError:
            text=''
        
        print text.encode('utf-8')
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['a '],languages=['en'])