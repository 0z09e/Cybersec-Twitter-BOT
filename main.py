import tweepy
from datetime import date
import time

def time1(): #returns current time
	from datetime import datetime

	# datetime object containing current date and time
	now = datetime.now()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	return dt_string


def whole_data(hashtags): #returns 
	arr = []
	try:
		for tweet in tweepy.Cursor(api.search, q=hashtags, rpp=100,exclude_replies=True,lang='en').items(): #Searching for hashtags related to given parameter 
		#print(tweet.text)
			date1 = str(tweet.created_at) # Checking the date of that tweet
			dates = list(map(str , date1.split()))
			if dates[0] == str(date.today()): #Matches it with the current date
				arr.append(tweet)
			return arr
	except:
		print("[ " + str(time1()) + " ] Some crappy errors again.." ) 
		return arr

			

def twitter():
	API_key = '' #Insert API key here
	API_key_secret = '' #Insert API key Secret here
	Bearer_token = '' #Insert Bearer token here
	access_token = '' #Insert Access token here
	access_token_secret = '' #Insert access token secret here
	auth = tweepy.OAuthHandler(API_key, API_key_secret)
	auth.set_access_token(access_token, access_token_secret)
	global api 
	api = tweepy.API(auth, wait_on_rate_limit=True) #Authentication with wait_on_rate_limit turned beacause twiiter API takes 300 request per 15 minute after that it stops responding for some time.wait_on_rate_limit will waits until it responds back
	print("[ " + str(time1()) + " ] Connected to twitter") 

	while True:
		print("[ " + str(time1()) + " ] searching for tweets.....")
		
		hashtags = ['#databreach', '#activedirectory', '#exploit', '#0day', '#infosec','#malware', '#cve', '#cyberattack', '#cybersecurity', '#cybersec','#zeroday', '#privilageescalation', '#privesc', '#bufferoverflow','#heapoverflow', '#ctf', '#rce', '#remotecommandexecution', '#xss','#owasp', '#rapid7', '#exploitdb', '#csrf'] #Hashtags, change this according to your need
		print("[ " + str(time1()) + " ] fewwww....Let me wake up")
		time.sleep(10)
		for tags in hashtags:
			big_data = whole_data(tags)
			try:
				for data in big_data:
					print("[ " +time1() + " ] retweeting.....")
					try:
						api.retweet(data.id)
						print("[ " + time1() + " ] retweet done.finding more to retweet")
					except:
						print("[ " + str(time1()) + " ] ehhhhh.....you have retweeted that")
						continue
			except:
				print(  "[ "+str(time1())+" ] ouchh....got some crappy error,i have to sleep for  a while")
				time.sleep(60)
				continue
		print("[ " + str(time1()) + " ] no more tweet found,going for a nap...zzzzzz")
		time.sleep(60)
