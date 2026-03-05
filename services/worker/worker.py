import time
import requests
import redis
import os

redis_host = os.getenv("REDIS_HOST", "redis")

r = redis.Redis(
    host=redis_host,
    port=6379,
    decode_responses=True
)

API = "https://api.exchangerate-api.com/v4/latest/USD"

while True:
    try:
        data = requests.get(API).json()
        rate = data["rates"]["ILS"]

        r.set("usd_rate", rate)

        print("rate updated:", rate)

    except Exception as e:
        print("error:", e)

    time.sleep(60)