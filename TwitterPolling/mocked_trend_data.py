import json

class MockedTrendData:

    def __init__(self):
        pass

    def poll(self):
        with open('poll_data.json') as file:
            data = json.load(file)
            return data