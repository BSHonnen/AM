#-----------------------------------------------------------------------
#
# Polls Twitter for top 50 trends in top 5 US cities, pairs them down
# into a nested dictionary, and removes duplicates
#
#-----------------------------------------------------------------------

from reduce_trends import ReduceTrends
from twitter_trend_poller import TwitterTrendPoller
from mocked_trend_data import MockedTrendData




top_trends = MockedTrendData().poll()
#top_trends = TwitterTrendPoller().poll()


topics_appear_in_each = ReduceTrends().reduce(top_trends)


print(topics_appear_in_each)
