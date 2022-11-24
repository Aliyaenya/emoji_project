from db import Base, engine


def create_tables():   # создает все таблицы в базе 
    Base.metadata.create_all(engine, checkfirst=True)
    