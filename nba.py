import sys
sys.path.append('..')
import tweepy
import json
from textblob import TextBlob
import operator
def scrape_tweets(keyword):
	search = api.search(keyword, count=100, tweet_mode="extended")
	return search

    


if __name__ == '__main__':

	#including two sets of tokens in case of running into twitter search limit
	
	consumer_token = '1MWtfOwuimQck9qSlsO90d5Se'
	consumer_secret = '1LGBv0DgJm4CC1Meb9ucwe8ewtM64t5eQcdZi5wT5d3tMniAH7'
    	access_token = '1092465220780462085-TdrCUuMHqcT3NCQMRwTcyUUPAMNrO9'
    	access_token_secret = 'YnR50JeN5FBPshtfvT6BNkxynuqxIWhO3FDhelPV9hRGD'
	
	'''
	consumer_token = "d6Zg5kGVouqPKp3WpYWA5OsMG"
	consumer_secret = "wMHxkCdWpUABPR2rrc2hOxkclowBoIo3NjADvxpu1QfNTKmecT"
	access_token = "4385868237-3PtN5Tv5Ufe1ERJW3T6Omn1BKbhlTANjAqxZMZd"
	access_token_secret = "VFonx25Qx91yNKFH2df88BOKINgpFbWgGKuxlZD0z3ajX"    
	'''
    	auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    	auth.set_access_token(access_token, access_token_secret)
    
    	api = tweepy.API(auth)
    	keywords = []
    	hashtags = {
		"Hawks" : ["#TrueToAtlanta", "Hawks"],
		"Nets" : ["#WeGoHard", "Nets"],
		"Celtics" : ["#CUsRise", "Celtics"],
		"Hornets" : ["#Hornets30", "Hornets"],
		"Bulls" : ["#BullsNation", "Bulls"],
		"Cavaliers" : ["#BeTheFight", "Cavs"],
		"Mavericks" : ["#MFFL", "#Mavericks", "Mavs"],
		"Nuggets" : ["#MileHighBasketball", "Nuggets"],
		"Pistons" : ["#DetriotBasketball", "Pistons"],
		"Warriors" : ["#DubNation", "Warriors", "#GSW"],
		"Rockets" : ["#Rockets", "#HoustonRockets"],
		"Pacers" : ["#Pacers", "#IndianaPacers"],
		"Clippers" : ["#ClipperNation", "Clippers", "#LAC"],
		"Lakers" : ["#LakeShow", "Lakers", "#LAL"],
		"Grizzlies" : ["#GrindCity", "#Grizzlies"],
		"Heat" : ["#HeatCulture", "#Heat"],
		"Bucks" : ["#FearTheDear", "#Bucks"],
		"Timberwolves" : ["#AllEyesNorth", "TWolves", "Timberwolves"],
		"Pelicans" : ["#DoItBig", "Pelicans"],
		"Knicks" : ["#NewYorkForever", "Knicks", "#NYK"],
		"Thunder" : ["#ThunderUp", "#Thunder"],
		"Magic" : ["#PureMagic", "#OrlandoMagic"],
		"76ers" : ["#HereTheyCome", "76ers", "6ers"],
		"Suns" : ["#TimeToRise", "#Suns"],
		"Trail Blazers" : ["#RipCity", "#Blazers", "Trail Blazers"],
		"Kings" : ["#SacramentoProud", "#SACKings"],
		"Spurs" : ["#GoSpursGo", "#Spurs", "#SAS"],
		"Raptors" : ["#WeTheNorth", "Raptors"],
		"Jazz" : ["#TeamIsEverything", "Jazz"],
		"Wizards" : ["#DCFamily", "#Wizards"]
    	}	

	tweets = {} # tweets dict has key, val pair of "team name" : ["tweet object", "tweet object", ...]
	scores = {} # sentiment analysis scores
	avg = {}
	for key in hashtags:
		scores[key] = []
			
    	for key, values in hashtags.items(): #iterate through hashtag dict
		for i in range(len(values)):
			out = scrape_tweets(str(values[i]))
			for j in range(len(out)):
				if hasattr(out[j], "retweeted_status") == False: # filter out retweets
					if key not in tweets:
						tweets[key] = [out[j].full_text]
					else:
						tweets[key].append(out[j].full_text)
		print "Tweets per team " + str(key) + ": " + str(len(tweets[key]))

	for key, values in tweets.items():
		print "Examining sentiments of " + str(key)
		for i in range(len(values)):
			sent = TextBlob(values[i]).sentiment.polarity
			scores[key].append(float(sent))

	for key, values in scores.items():
		score = float(sum(values)) / float(len(values))
		avg[key] = score

	for key, values in avg.items():
		print str(key) + ": " + str(values) 
		
