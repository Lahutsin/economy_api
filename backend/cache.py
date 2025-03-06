import os
import redis

# Получаем переменную окружения для хоста Redis
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")  # "localhost" - значение по умолчанию

# Подключение к Redis
cache = redis.StrictRedis(host=REDIS_HOST, port=6379, db=0)

def set_cache(key, value):
    cache.setex(key, 3600, value)  # Сохраняем в Redis на 1 час

def get_cache(key):
    return cache.get(key)
