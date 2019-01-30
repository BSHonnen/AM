#-----------------------------------------------------------------------
#
# Polls Twitter for top 50 trends in top 5 US cities, pairs them down
# into a nested dictionary, and removes duplicates
#
#-----------------------------------------------------------------------


from twitter import *
from pois import PoI

import sys
sys.path.append(".")
import config


class Poller:

    def __init__(self):
        self.twitter = Twitter(auth=OAuth(config.access_key,
                                          config.access_secret,
                                          config.consumer_key,
                                          config.consumer_secret))

    def poll(self):
        top_trends = []

        for woe_ID in PoI:
            raw_poll_data = self.twitter.trends.place(_id=woe_ID.value)
            top_trends.extend(raw_poll_data[0]['trends'])

        return top_trends


# [{}, {} ]
# [ { trendsL[{}]}]
#
#-----------------------------------------------------------------------
# Create an empty dictionary to store results without duplicates from each areas
# and variables for clarity
#-----------------------------------------------------------------------

top_trends = Poller().poll()
paired_down = {}
no_tweet_volume = "N/A"


#-----------------------------------------------------------------------
# Removes duplicate names and notes the tweet volume from each trend
#-----------------------------------------------------------------------
for trend in top_trends:
    trend_name = trend['name']
    tweet_volume = trend['tweet_volume']
    promoted_content = trend['promoted_content']
    if trend_name not in paired_down:
        paired_down[trend_name] = {
            'count': 1, 'tweet_volume': tweet_volume, 'promoted_content': promoted_content}
    else:
        paired_down[trend_name]['count'] += 1
# [{'Fa},{}]
#
# Trend(Count, Tweet Volume)
#

#-----------------------------------------------------------------------
# Only show trends that appear in all 5 localesß
#-----------------------------------------------------------------------

topics_appear_in_each = []
counter = 0
for trend in paired_down:
    count = paired_down[trend]['count']
    if count >= 2:
        topics_appear_in_each.append(
            (trend, count, paired_down[trend]['tweet_volume'], paired_down[trend]['promoted_content']))
print(topics_appear_in_each)
