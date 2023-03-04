from sqlalchemy import select
from sqlalchemy.orm import Session
from db_engine import engine as engine
from db_schema_za4_weapons import Weapons as Weapons


def select_za4_weapons():
    with Session(engine) as session:
        stmt = select(Weapons).execution_options(populate_existing=True)
        data_obj = session.scalars(stmt).all()
        return data_obj
