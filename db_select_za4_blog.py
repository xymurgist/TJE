from sqlalchemy import select
from sqlalchemy.orm import Session
from db_engine import engine as engine
from db_schema_za4_blog import ZA4BlogBase as ZA4BlogBase


def select_za4_blog():
    with Session(engine) as session:
        stmt = select(ZA4BlogBase).execution_options(populate_existing=True)
        data_obj = session.scalars(stmt).all()
        return data_obj
