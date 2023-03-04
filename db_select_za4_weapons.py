from sqlalchemy import select
from sqlalchemy.orm import Session
from db_engine import engine as engine
from db_schema_za4_weapons import Weapons as Weapons

session = Session(engine)
stmt = select(Weapons)
data_obj = session.scalars(stmt).all()
