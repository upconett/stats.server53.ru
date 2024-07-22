from fastapi import APIRouter, Body, Request
from fastapi.responses import JSONResponse, Response
import logging
from pydantic import BaseModel

from typing import Union

from database import redis

router = APIRouter(
    prefix='/players'
)


@router.get('/')
async def get_online():
    all_ = await redis.lrange('logged_all', 0, -1)
    plen = await redis.llen('logged_pending')
    pending = await redis.lpop('logged_pending', plen)
    
    return JSONResponse(
        content={
            'all': all_,
            'pending': pending
        },
        status_code=200
    )



class PlayersPost(BaseModel):
    all_: list[str]
    in_: Union[str | None]
    out_: Union[str | None]


@router.post('/')
async def post_online(data: PlayersPost):
    await redis.delete('logged_all')
    await redis.lpush('logged_all', *data.all_)

    pending = []
    if data.in_:
        if f'in_{data.in_}' not in pending: 
            pending.append(f'in_{data.in_}')
    if data.out_:
        if f'out_{data.in_}' not in pending: 
            pending.append(f'out_{data.out_}')

    await redis.rpush('logged_pending', *pending)

    logging.info('Got updates on players')
    return Response(status_code=202)
