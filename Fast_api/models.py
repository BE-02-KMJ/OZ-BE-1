from pydantic import BaseModel
from typing import Optional, List

class Book(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None

# 따로 Create Book class 생성 필요 (data validation)
class CreateBook(BaseModel):
    title: str
    author: str
    description: Optional[str] = None

class SearchBook(BaseModel):
    results: Optional[Book]

class SearchBookList(BaseModel):
    results: List[Book]