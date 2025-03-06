import os
import redis

REDIS_HOST = os.getenv("REDIS_HOST", "localhost") 

cache = redis.StrictRedis(host=REDIS_HOST, port=6379, db=0)

def set_cache(key, value):
    cache.setex(key, 3600, value)

def get_cache(key):
    return cache.get(key)
