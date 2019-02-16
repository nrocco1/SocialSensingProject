import sys
sys.path.append('..')
import tweepy
import json

 
def scrape_tweets(keywords):
    print("Scraping tweets for keywords: {}".format(' and '.join(keywords)))
    search = api.search("{}".format(" AND ".join(keywords)), count=1000)
    print("These are the tweets with the keywords [{}]: \n".format(', '.join(keywords)))
    for s in search:
        print(s.text)
    


if __name__ == '__main__':
    consumer_token = '1MWtfOwuimQck9qSlsO90d5Se'
    consumer_secret = '1LGBv0DgJm4CC1Meb9ucwe8ewtM64t5eQcdZi5wT5d3tMniAH7'
    access_token = '1092465220780462085-TdrCUuMHqcT3NCQMRwTcyUUPAMNrO9'
    access_token_secret = 'YnR50JeN5FBPshtfvT6BNkxynuqxIWhO3FDhelPV9hRGD'
    
    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth)
    
    keywords = []
    for arg in sys.argv:
        if arg == sys.argv[0]:
            continue
        else:
            keywords.append(arg)
   
    scrape_tweets(keywords) 
