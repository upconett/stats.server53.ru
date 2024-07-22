from fastapi import FastAPI

from routers import main, players


app = FastAPI()

app.include_router(main)
app.include_router(players)
