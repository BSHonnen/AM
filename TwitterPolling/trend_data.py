class TrendData:

    def __init__(self, trend_name, num_cities, tweet_volume, promoted_content):
        self.trend_name = trend_name
        self.num_cities = num_cities
        self.tweet_volume = tweet_volume
        self.promoted_content = promoted_content

    def increment_num_cities(self):
        self.num_cities += 1

    def printSelf(self):
        return "<{}, {}, {}, {} >".format(self.trend_name, str(self.num_cities), str(self.tweet_volume), str(self.promoted_content))

    def __str__(self):
        return self.printSelf()

    def __repr__(self):
        return self.printSelf()

    def get_num_cities(self):
        return self.num_cities

    def csv_format(self):
          return '"{}",{},{},{}\n'.format(self.trend_name, str(self.num_cities), str(self.tweet_volume), str(self.promoted_content))