from sqlalchemy import select
from sqlalchemy.orm import Session
from db_engine import engine as engine
from db_schema_za4_blog import Blog as Blog

session = Session(engine)
stmt = select(Blog)
data_obj = session.scalars(stmt).all()
