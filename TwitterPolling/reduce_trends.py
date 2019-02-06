from trend_data import TrendData

class ReduceTrends:

    def __init__(self):
        pass

    def reduce(self, top_trends):
        print()
        paired_down = {}
        no_tweet_volume = "N/A"
        for trend in top_trends:
            trend_name = trend['name']
            tweet_volume = trend['tweet_volume']
            promoted_content = trend['promoted_content']
            if trend_name not in paired_down:
                paired_down[trend_name] = TrendData(
                    trend_name, 1, tweet_volume, promoted_content)
            else:
                paired_down[trend_name].increment_num_cities()
        topics_appear_in_each = []
        for trend in paired_down:
            num_cities = paired_down[trend].get_num_cities()
            if num_cities >= 2:
                topics_appear_in_each.append(paired_down[trend])
        return topics_appear_in_each
