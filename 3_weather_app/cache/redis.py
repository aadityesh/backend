import redis


def connect_to_cache():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    r.ping()
    yield r
