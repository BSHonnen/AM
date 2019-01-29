#-----------------------------------------------------------------------
#
# Polls Twitter for top 50 trends in top 5 US cities, pairs them down 
# into a nested dictionary, and removes duplicates
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#  import all the things
#-----------------------------------------------------------------------

from twitter import *



#-----------------------------------------------------------------------
# load our API credentials and import sys... and append a "." ... 'cause
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
# Where on Earth (WOE) IDs for:
# 0 - New York, 1 - LA, 2 - Chicago, 3 - Dallas, 4 - DC
# NOTE: List can be expanded but API limit is 75 requests every 15 minutes
#-----------------------------------------------------------------------

top_USA_cities_by_capita = [2459115, 2442047, 2379574, 2388929, 2514815]



#-----------------------------------------------------------------------
# Pull each city's top 50 trends in this data structure: https://developer.twitter.com/en/docs/trends/trends-for-location/api-reference/get-trends-place
#-----------------------------------------------------------------------

top_trends = []

for city in top_USA_cities_by_capita:
 top_trends.append(twitter.trends.place(_id = city))



#-----------------------------------------------------------------------
# Create an empty dictionary to store results without duplicates from each areas and variables for clarity
#-----------------------------------------------------------------------

paired_down = {}
no_tweet_volume = "N/A"



#-----------------------------------------------------------------------
# Removes duplicate names and notes the tweet volume from each trend
#-----------------------------------------------------------------------

for each_city in top_trends:
 for location in each_city:
  for trend in location["trends"]:
   trend_name = trend["name"]
   tweet_volume = trend["tweet_volume"]
   if trend_name not in paired_down:
    if tweet_volume is None:
     paired_down[trend_name] = [no_tweet_volume]
    else:
     paired_down[trend_name] = [tweet_volume]
   else:
    if tweet_volume is None:
     paired_down[trend_name].append([no_tweet_volume])
    else:
     paired_down[trend_name].append(tweet_volume)



#-----------------------------------------------------------------------
# Only show trends that appear in all 5 locales
#-----------------------------------------------------------------------

topics_appear_in_each = {}
for trend in paired_down:
 if len(trend) == 5:
  topics_appear_in_each[trend]=trend
print(topics_appear_in_each)