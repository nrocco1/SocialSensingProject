# outputs the total sentiment of all teams

import sys
sys.path.append('..')
import tweepy
import json
from textblob import TextBlob
from operator import itemgetter
import pickle
import os

if __name__ == '__main__':

	scores = {} # sentiment analysis scores
        avg = {}

        # load in dictionary containing previous scores for appending data
        scores = pickle.load(open("curDict_dict.pkl", "rb"))

	for key, values in scores.items():
                print "Total tweets for " + str(key) + " is " + str(len(values))
                score = float(sum(values)) / float(len(values))
                avg[key] = score

        print "\nScores:"
        for k, v in sorted(avg.items(), key=itemgetter(1)):
                print str(k) + ": " + str(v)
