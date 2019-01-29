#!/usr/bin/env python

#-----------------------------------------------------------------------
# twitter-trends
#  - lists the current global trending topics
#-----------------------------------------------------------------------

from twitter import *

#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
import sys
sys.path.append(".")
import config

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(auth = OAuth(config.access_key,
                  config.access_secret,
                  config.consumer_key,
                  config.consumer_secret))

#-----------------------------------------------------------------------
# retrieve global trends.
# other localised trends can be specified by looking up WOE IDs:
#   http://developer.yahoo.com/geo/geoplanet/
# twitter API docs: https://dev.twitter.com/rest/reference/get/trends/place
#-----------------------------------------------------------------------
ny_results = twitter.trends.place(_id = 2459115)

la_results = twitter.trends.place(_id = 2442047)

chicago_results = twitter.trends.place(_id = 2379574)

dallas_results = twitter.trends.place(_id = 2388929)

dc_results = twitter.trends.place(_id = 2514815)

all_results = ny_results+la_results+chicago_results+dallas_results+dc_results
# print(all_results)

# create an empty dictionary to store results without duplicates from each areas
paired_down = {}

for location in all_results:
	for trend in location ["trends"]:
		if trend["name"] not in paired_down:
			if trend["tweet_volume"] is None:
 				paired_down[trend["name"]] = ['N/A']
			else:
				paired_down[trend["name"]] = [trend["tweet_volume"]]
		else:
			if trend["tweet_volume"] is None:
				paired_down[trend["name"]].append(['N/A;])
			else:
				paired_down[trend["name"]].append([trend["tweet_volume"]])
 		# print(" - %s" % trend["name"])

topics_appear_in_each = {}
for trend in paired_down:
	if len(trend) == 5:
		topics_appear_in_each[trend]=trend
	else:
		pass
print(topics_appear_in_each) 
