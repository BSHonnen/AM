from twitter import *

from pois import PoI

import sys
sys.path.append(".")
import config

class TwitterTrendPoller:

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