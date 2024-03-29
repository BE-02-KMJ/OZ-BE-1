from typing import List, Optional

from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None


# 따로 Create Book class 생성 필요 (data validation)
# docs에 데이터 그대로 넣어진다.
class CreateBook(BaseModel):
    title: str
    author: str
    description: Optional[str] = None


class SearchBook(BaseModel):
    results: Optional[Book]


class SearchBookList(BaseModel):
    results: List[Book]
