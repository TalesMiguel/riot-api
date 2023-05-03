from fastapi import FastAPI
from routers import matches, summoner

app = FastAPI()

app.include_router(summoner.router)
app.include_router(matches.router)
