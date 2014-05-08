import redis
import json

class PubSub(object):
    def __init__(self):
        self.redis = redis.Redis()

    def publish(self, channel, data):
        self.redis.publish(channel, json.dumps(data))
 
    def subscribe(self, channel, handler):
        redis = self.redis.pubsub()
        redis.psubscribe(channel)
        for data_raw in redis.listen():
            data = data_raw["data"]
            if isinstance(data, long):
                continue
            data = json.loads(data)
            sender = data_raw["channel"]
            handler(sender, data)
