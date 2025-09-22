from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQL_URL_SQLITE = 'sqlite:///./blog.db'
engine = create_engine(
sessionlocal=sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

Base=declarative_base()


def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()
