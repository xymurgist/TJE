from datetime import date

from sqlalchemy import insert
from sqlalchemy.orm import Session

from db_engine import engine as engine
from db_schema_za4_blog import ZA4BlogBase as ZA4BlogBase


today = date.today()
full_today = today.strftime("%B %d, %Y")


class ZA4BlogObj:
    def __init__(self, **kw):
        self.date = kw.get('date', f'{full_today}')
        self.author = kw.get('author', 'n/a')
        self.title = kw.get('title', 'n/a')
        self.subtitle = kw.get('subtitle', 'n/a')
        self.img_url = kw.get('img_url', 'n/a')
        self.body = kw.get('body', 'n/a')
        

#     def set_blog_props():
#         with open('blog-data.json', 'r') as file:
#             blog_posts = json.load(file)
#         for key in blog_posts:
#             props = blog_posts[key]
#             yield ZA4_Blog(**props)

    def insert_post(self, form):
        with Session(engine) as session:
            for key in form:
                blog_post = ZA4BlogObj(
                    date=full_today,
                    author=form["author"],
                    title=form["title"],
                    subtitle=form["subtitle"],
                    img_url=form["img_url"],
                    body=form["body"],
                )

                # session.execute(insert(blog_post))
                session.add_all([blog_post])
                session.commit()
