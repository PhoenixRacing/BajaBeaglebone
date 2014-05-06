import redis
import json

class PubSub(object):
    """
    Very simple Pub/Sub pattern wrapper
    using simplified Redis Pub/Sub functionality.
 
    Usage (publisher)::
 
        import redis
 
        r = redis.Redis()
 
        q = PubSub(r, "channel")
        q.publish("test data")
 
 
    Usage (listener)::
 
        import redis
 
        r = redis.Redis()
        q = PubSub(r, "channel")
 
        def handler(data):
            print "Data received: %r" % data
 
        q.subscribe(handler)
 
    """
    def __init__(self, channel="default"):
        self.redis = redis.Redis()
        self.channel = channel
 
    def publish(self, data):
        self.redis.publish(self.channel, data)
 
    def subscribe(self, handler):
        redis = self.redis.pubsub()
        redis.psubscribe(self.channel)
 
        for data_raw in redis.listen():
            data = data_raw["data"]
            sender = data_raw["channel"]
            handler(sender, data)
