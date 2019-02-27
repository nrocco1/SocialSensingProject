import sys
sys.path.append('..')
import tweepy
import json

 
def scrape_tweets(keyword):
	search = api.search(keyword, count=100)
	return search

    


if __name__ == '__main__':
	consumer_token = '1MWtfOwuimQck9qSlsO90d5Se'
	consumer_secret = '1LGBv0DgJm4CC1Meb9ucwe8ewtM64t5eQcdZi5wT5d3tMniAH7'
    	access_token = '1092465220780462085-TdrCUuMHqcT3NCQMRwTcyUUPAMNrO9'
    	access_token_secret = 'YnR50JeN5FBPshtfvT6BNkxynuqxIWhO3FDhelPV9hRGD'
    
    	auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    	auth.set_access_token(access_token, access_token_secret)
    
    	api = tweepy.API(auth)
    	keywords = []
    	hashtags = {
		"Hawks" : ["#TrueToAtlanta", "#Hawks"],
		"Nets" : ["#WeGoHard", "#Nets"],
		"Celtics" : ["#CUsRise", "#Celtics"],
		"Hornets" : ["#Hornets30", "#Hornets"],
		"Bulls" : ["#BullsNation", "#Bulls"],
		"Cavaliers" : ["#BeTheFight", "#Cavs"],
		"Mavericks" : ["#MFFL", "#Mavericks", "#Mavs"],
		"Nuggets" : ["#MileHighBasketball", "#Nuggets"],
		"Pistons" : ["#DetriotBasketball", "#Pistons"],
		"Warriors" : ["#DubNation", "#Warriors"],
		"Rockets" : ["#Rockets"],
		"Pacers" : ["#Pacers"],
		"Clippers" : ["#ClipperNation", "#Clippers"],
		"Lakers" : ["#LakeShow", "#Lakers"],
		"Grizzlies" : ["#GrindCity", "#Grizzlies"],
		"Heat" : ["#HeatCulture", "#Heat"],
		"Bucks" : ["#FearTheDear", "#Bucks"],
		"Timberwolves" : ["#AllEyesNorth", "#TWolves", "#Timberwolves"],
		"Pelicans" : ["#DoItBig", "#Pelicans"],
		"Knicks" : ["#NewYorkForever", "#Knicks"],
		"Thunder" : ["#ThunderUp", "#Thunder"],
		"Magic" : ["#PureMagic"],
		"76ers" : ["#HereTheyCome", "#76ers"],
		"Suns" : ["#TimeToRise", "#Suns"],
		"Trail Blazers" : ["#RipCity", "#Blazers", "#TrailBlazers"],
		"Kings" : ["#SacramentoProud", "#SACKings"],
		"Spurs" : ["#GoSpursGo", "#Spurs"],
		"Raptors" : ["#WeTheNorth", "#Raptors"],
		"Jazz" : ["#TeamIsEverything", "#Jazz"],
		"Wizards" : ["#DCFamily", "#Wizards"]
    	}	

	tweets = {} # tweets dict has key, val pair of "team name" : ["tweet object", "tweet object", ...]


			
    	for key, values in hashtags.items(): #iterate through hashtag dict
		for i in range(len(values)):
			out = scrape_tweets(str(values[i]))
			for j in range(len(out)):
				if not hasattr(out[j], "retweeted_status"): # filter out retweets
					if key not in tweets:
						tweets[key] = [out[j]]
					else:
						tweets[key].append(out[j])
		print "Tweets per team " + str(key) + ": " + str(len(tweets[key]))
