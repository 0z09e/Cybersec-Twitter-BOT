import tweepy
from datetime import date
import time


def time1():
	from datetime import datetime

	# datetime object containing current date and time
	now = datetime.now()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	return dt_string


API_key = ''
API_key_secret = ''
Bearer_token = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(API_key, API_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
print("[ " + str(time1()) + " ] Connected to twitter")
def whole_data(hashtags):
	arr = []
	try:
		for tweet in tweepy.Cursor(api.search, q=hashtags + " exclude:replies exclude:retweets", rpp=100,exclude_replies=False,lang='en').items():
			date1 = str(tweet.created_at)
			dates = list(map(str , date1.split()))
			text = tweet.text
			if dates[0] == str(date.today()) and "RT @" not in text:
				arr.append(tweet)
			return arr
	except:
		print("[ " + str(time1()) + " ] Some crappy errors again.." ) 
		return arr

			

def twitter():
	while True:
		print("[ " + str(time1()) + " ] searching for tweets.....")
		
		hashtags = ['databreach', 'activedirectory', '0day', 'infosec','malware', 'cyberattack', 'cybersecurity','zeroday', 'bufferoverflow','heapoverflow' , 'stackoverflow' , 'capturetheflag', 'remotecommandexecution', 'crosssitescripting', 'rapid7', 'exploitdb' , 'crosssiterequestforgery ' , 'bugbounty' , 'bughunting' , 'bugfinder']
		print("[ " + str(time1()) + " ] fewwww....Let me wake up")
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
				time.sleep(10)
				continue
		print("[ " + str(time1()) + " ] no more tweet found,going for a nap...zzzzzz")
		time.sleep(30)


