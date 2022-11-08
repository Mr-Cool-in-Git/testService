from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from .api import router
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory=os.getcwd()+"/workshop/static"), name="static")
app.include_router(router)


