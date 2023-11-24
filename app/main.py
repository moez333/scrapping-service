from fastapi import FastAPI
from scraper import scrape_and_save_to_db


app = FastAPI()

@app.get("/scrape")
def trigger_scrape():
    result = scrape_and_save_to_db()
    return result
