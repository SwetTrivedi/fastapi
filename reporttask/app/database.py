from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# DATABASE_URL = "postgresql+psycopg2://swet:swet1234@localhost:5432/fastapitask"


# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

