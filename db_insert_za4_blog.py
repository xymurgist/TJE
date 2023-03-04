from sqlalchemy import insert
from sqlalchemy.orm import Session
from db_engine import engine as engine
from db_schema_za4_blog import ZA4BlogBase as ZA4BlogBase

from datetime import date

today = date.today()
full_today = today.strftime("%B %d, %Y")


def insert_post(form):
    with Session(engine) as session:
        for key in form:
            blog_post = {
                'date': full_today,
                'author': form["author"],
                'title': form["title"],
                'subtitle': form["subtitle"],
                'img_url': form["img_url"],
                'body': form["body"],
            }
        session.execute(insert(ZA4BlogBase), blog_post)
        session.commit()
