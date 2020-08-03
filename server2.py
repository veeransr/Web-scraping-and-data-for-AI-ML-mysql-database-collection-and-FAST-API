import os
import datetime
from fastapi import FastAPI
from logger import trigger_log_save
from scrape import run as scrape_runner

app = FastAPI()

@app.get("/")
def hellow_world():
    return {"hello":"world"}

@app.get("/abc")
def abc_view():
    return {"data":[1,2,3]}

@app.post("/box_office")
def boxoffice_mozo_scraper_view():
    trigger_log_save()
    scrape_runner()
    return {"data": [1,2,3,4]}