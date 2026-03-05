from fastapi import FastAPI
import redis
import os

app = FastAPI()

redis_host = os.getenv("REDIS_HOST", "redis")

r = redis.Redis(
    host=redis_host,
    port=6379,
    decode_responses=True
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/usd-rate")
def usd_rate():
    rate = r.get("usd_rate")
    return {"usd_rate": rate}