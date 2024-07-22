from redis.asyncio import Redis
import asyncio, logging

import config as cfg


redis = Redis(
    host=cfg.REDIS_HOST,
    port=cfg.REDIS_PORT,
    db=cfg.REDIS_DB,
    password=cfg.REDIS_PASSWORD,
    decode_responses=True
)
