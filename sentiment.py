from textblob import TextBlob

if __name__ == '__main__':
    with open("UTvsKU.txt") as f:
        tweets = f.read().split('\n')
        print(tweets)
        for tweet in tweets:
            t = TextBlob(tweet)
            print(t.sentiment.polarity)
        
