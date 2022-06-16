from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from configuration import settings

CONNECTION = f"postgresql://{settings.databaseusername}:{settings.databasepassword}@{settings.host}/{settings.database}"
server = create_engine(CONNECTION)
Session = sessionmaker(bind=server, autoflush=False, autocommit=True)
Base = declarative_base(server)
