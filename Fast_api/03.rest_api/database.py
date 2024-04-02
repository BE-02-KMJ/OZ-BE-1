from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# (1) 비동기 방식 - Starlette
# (2) 데이터 검증 - pydantic

# 동기용 데이터 베이스 설정 (pymysql)
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:alswjd6984!@localhost/oz_fastapi"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# 비동기용 데이터 베이스 설정 (aiomysql)
# - 무거운 I/O 요청(5초)이 먼저 와도, 뒤에 가벼운 I/O 작업 요청(1초)이 들어오면 더 빨리 끝나는 것이 응답된다.
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

ASYNC_SQLALCHEMY_DATABASE_URL = "mysql+aiomysql://root:alswjd6984!@localhost/oz_fastapi"
async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)
AsyncSessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
