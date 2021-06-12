import tweepy
from datetime import date
import time
from datetime import datetime


API_key = '' # Change this 
API_key_secret = '' # Change this
Bearer_token = '' # Change this
access_token = '' # Change this
access_token_secret = '' # Change this
hashtags = ['databreach', 'activedirectory', '0day', 'infosec', 'malware','cyberattack', 'cybersecurity', 'zeroday', 'bufferoverflow','heapoverflow', 'capturetheflag', 'remotecommandexecution','crosssitescripting', 'rapid7', 'exploitdb','crosssiterequestforgery ', 'bugbounty', 'bughunting', 'bugfinder','pentesting', 'infosecjobs'] # Change this

#<==========================================================================================>
# This function returns the current date in a structured format
#<==========================================================================================>
def time1():
	now = datetime.now()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	return dt_string


#<==========================================================================================>
# This function returns all the tweets which contains the given hashtag
#<==========================================================================================>

def finder(hashtags):
	arr = []
	try:
		for tweet in tweepy.Cursor(api.search, q=hashtags + " exclude:replies exclude:retweets", rpp=100,exclude_replies=False,lang='en').items(): #here we exclude replies and retweets unless it will retweet literally everything
			date1 = str(tweet.created_at)
			dates = list(map(str , date1.split()))
			text = tweet.text
			# Here we check if the tweet is fresh by matching the tweet date with today's date
			if dates[0] == str(date.today()) and "RT @" not in text: 
				arr.append(tweet.id)
			return arr
	except:
		print("[ " + str(time1()) + " ] Some crappy errors again.." ) 
		return arr

#<==========================================================================================>
# This function process all the tweets returned by finder function
#<==========================================================================================>
def twitter():
	while True:
		print("[ " + str(time1()) + " ] searching for tweets.....")
		for tags in hashtags:
			big_data = finder(tags)
			try:
				for data in big_data:
					print("[ " +time1() + " ] retweeting.....")
					try:
						api.retweet(data) # retweeting the tweets provided by big_data
						print("[ " + time1() + " ] retweet done.finding more to retweet")
					except:
						print("[ " + str(time1()) + " ] ehhhhh.....you have retweeted that")
						continue
			except:
				print(  "[ "+str(time1())+" ] ouchh....got some crappy error,i have to sleep for  a while")
				time.sleep(10)
				continue
		print("[ " + str(time1()) + " ] no more tweet found,going for a nap...zzzzzz")
		time.sleep(30)


auth = tweepy.OAuthHandler(API_key, API_key_secret) 
auth.set_access_token(access_token, access_token_secret) # setting access token
api = tweepy.API(auth, wait_on_rate_limit=True) #Authenticating with the API
print("[ " + str(time1()) + " ] Connected to twitter")
twitter()