from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from db_engine import engine as engine


class Base(DeclarativeBase):
    """SQLAlchemy's DeclarativeBase class for mapping"""
    pass


class ZA4BlogBase(Base):
    """Maps the Blog table's columns for use by Base to create the table and columns in the database"""
    __tablename__ = "za4_blog"

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[str]
    author: Mapped[str]
    title: Mapped[str] = mapped_column(unique=True)
    subtitle: Mapped[str]
    img_url: Mapped[str]
    body: Mapped[str]


# Connects to database and creates the Weapons table and columns
Base.metadata.create_all(engine)
