from flask import Flask
from scrape import run as scrape_runner
from logger import trigger_log_save
app = Flask(__name__)

@app.route("/", methods= ['GET'])
def hellow_world():
    return "Hello World This is Flask"

@app.route("/abc", methods= ['GET'])
def abc_view():
    return "Hello World This is abc and I am different"

@app.route("/box_office", methods= ['POST'])
def boxoffice_mozo_scraper_view():
    trigger_log_save()
    scrape_runner()
    return {"data": [1,2,3]}
