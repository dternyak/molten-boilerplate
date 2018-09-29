from molten.contrib.sqlalchemy import (
    EngineData
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def init_db(engine_data: EngineData):
    Base.metadata.create_all(engine_data.engine)


def setup_db(app):
    # Initialize the DB by injecting EngineData into initdb and calling it.
    resolver = app.injector.get_resolver()
    resolver.resolve(init_db)()
