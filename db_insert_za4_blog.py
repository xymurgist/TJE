from sqlalchemy.orm import Session
from db_engine import engine as engine
from db_schema_za4_blog import Blog as Blog
from za4_blog_class import Blog as blog_props


# Insert data into table
with Session(engine) as session:
    for prop in blog_props.set_blog_props():
        blog_posts = Blog(
            date=prop.date,
            author=prop.author,
            title = prop.title,
            subtitle=prop.subtitle,
            img_url = prop.img_url,
            body=prop.body,
        )

        session.add_all([blog_posts])
        session.commit()


# might need to switch to this to insert from forms
# from sqlalchemy import insert
    # session.execute()