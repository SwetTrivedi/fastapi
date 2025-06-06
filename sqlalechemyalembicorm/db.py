from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
DATABASE_URL = "sqlite+aiosqlite:///./sqlite.db"


engine=create_async_engine(DATABASE_URL,echo=True)

async_session=async_sessionmaker(bind=engine,expire_on_commit=False)








# Today I Learned about :-

# 1. Async SqlAlchemy Core and also Async sqlalchemy core with alembic used his topic performed the CRUD .

# 2. Async SqlAlchemy ORM and also Async sqlalchemy ORM  with alembic used his topic performed the CRUD .

# 3. Setup and Configured fastapi with sync sqlalchemy and Alembic and also created a models .

# 4. Insert and Read the data using fastapi (Swagger Ui ) and sync sqlalchemy