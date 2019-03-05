# this tool queries the score dict to determine who will win based on teams passed in on the command line. Run the program by typing: python predict.py team1 team2
# For example: python predict.py Lakers Celtics

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
                score = float(sum(values)) / float(len(values))
                avg[key] = score

	team1 = sys.argv[1]
	team2 = sys.argv[2]

        if team1 and team2 in scores.keys():
		print str(team1) + " score " + str(avg[team1])
		print str(team2) + " score " + str(avg[team2])
		if avg[team1] > avg[team2]:
			print "Based on popular sentiment, we predict that " + str(team1) + " will win."
		elif avg[team1] < avg[team2]:
			print "Based on popular sentiment, we predict that " + str(team2) + " will win."
	else:
		print "Incorrect team names. Try again."
