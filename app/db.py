from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from contextlib import contextmanager
from sqlalchemy.sql.expression import text
import gns
from app import model

database_url = gns.config.db.connection_string.format(
        username=gns.config.db.username,
        password=gns.config.db.password,
        port=gns.config.db.port,
        host=gns.config.db.host,
        database=gns.config.db.database
    )
print(database_url)


@contextmanager
def DBSession():
    session = session_maker()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


engine =  create_engine(database_url, max_overflow=0, pool_size=100, echo=False)
session_maker = sessionmaker(
    bind=engine,
    expire_on_commit=False
    )

metadata = model.metadata
execute = engine.execute

metadata.create_all(engine)  # creates the database tables and things for us


def get_table_list_from_db():
    """
    return a list of table names from the current
    databases public schema
    """
    sql="select table_name from information_schema.tables "\
        "where table_schema='public'"
    return [name for (name, ) in execute(text(sql))]


def get_seq_list_from_db():
    """return a list of the sequence names from the current
       databases public schema
    """
    sql="select sequence_name from information_schema.sequences "\
        "where sequence_schema='public'"
    return [name for (name, ) in execute(text(sql))]


def drop_all_tables_and_sequences():
    for table in get_table_list_from_db():
        try:
            execute(text("DROP TABLE %s CASCADE" % table))
        except (SQLAlchemyError, e):
            print(e)

    for seq in get_seq_list_from_db():
        try:
            execute(text("DROP SEQUENCE %s CASCADE" % table))
        except (SQLAlchemyError, e):
            print(e)
