#Get text from tweet
import json


tweets_filename = 'td1.txt'
tweets_file = open(tweets_filename, "r")

for line in tweets_file:
    try:
        # Read in one line of the file, convert it into a json object 
        tweet = json.loads(line.strip())
        if 'text' in tweet and tweet['lang']=='en': # only messages contains 'text' field is a tweet
        	print tweet['text'] # content of the tweet

    except:
        # read in a line is not in JSON format (sometimes error occured)
        continue