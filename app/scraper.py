
from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from datetime import datetime
from db import *
import requests

class FacebookPageData(Base):
    __tablename__ = 'facebook_page_data'

    id           = Column(Integer, primary_key=True, autoincrement=True)
    page_id      = Column(String)
    page_name    = Column(String)
    about        = Column(Text)
    post_content = Column(JSON)
    timestamp    = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

def save_to_database(session, page_id, page_name, about, post_content):
    entry = FacebookPageData(
        page_id     =page_id,
        page_name   =page_name,
        about       =about,
        post_content=post_content
    )
    session.add(entry)
    session.commit()

def scrape_facebook_page(page_id: str, access_token: str):
    graph_api_url = f"https://graph.facebook.com/v18.0/{page_id}?fields=id,name,about,posts{{id,message,created_time,reactions.summary(total_count),comments.summary(total_count)}}&access_token={access_token}"

    response = requests.get(graph_api_url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None
    
#If we want to Exclude the "paging" field from the "page", "reactions" and "comments" sections
"""def process_data(data):
    del data['posts']['paging']
    for post in data.get('posts', {}).get('data', []):
        reactions = post.get('reactions', {})
        reactions.pop('paging', None)
        comments  = post.get('comments', {})
        comments.pop('paging', None)

    return data
"""

def scrape_and_save_to_db():

    access_token = os.getenv("ACCESS_TOKEN")
    page_id      = os.getenv("PAGE_ID")
    data         = scrape_facebook_page(page_id, access_token)

    if data:
        #data = process_data(data)
        session = Session()
        save_to_database(session, data['id'], data['name'], data.get('about', ''), data.get('posts', {}).get('data', ''))
        session.close()
        return {"data": data, "message": "Scraped data saved to the database."}
    else:
        return {"message": "Error scraping data."}
