from fastapi import APIRouter
from typing import List, Optional
from .models import Book, CreateBook, SearchBookList

route = APIRouter()

books: List[Book] = []

@route.post('/')
def create_book(book: CreateBook) -> Book:
    book = Book(id=len(books)+1, **book.model_dump())
    books.append(book)

    return book

@route.get('/search/')
# 1개의 책만 조회
# def search_book() -> SearchBook:
#     pass

# 여러개 책 조회
def search_book_list(keyword: Optional[str], max_results: int=10) -> SearchBookList:
    # 이 코드를
    # for book in books:
    #     if keyword in book.title:
    #         book

    # 이렇게 한 줄로 표시
    search_result = [book for book in books if keyword in book.title] if keyword else books
    return SearchBookList(results=search_result[:max_results])