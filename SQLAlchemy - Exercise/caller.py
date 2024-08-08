from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:password@localhost/sqlalchemy_db")
Session = sessionmaker(engine=engine)

session = Session()
