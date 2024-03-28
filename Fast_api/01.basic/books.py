from fastapi import APIRouter, FastAPI

BOOKS = [
    {"id": 1, "title": "수도꼭지가 쏴아아", "author": "채은혜", "url": "https://www.yes24.com/수도꼭지"},
]

app = FastAPI()
router = APIRouter()


@router.get("/", status_code=200)
def main():
    return {"Message": "Welcome to the Book World~!"}  # Template Code


# 전체 책 데이터 조회
@router.get("/api/v1/books", status_code=200)
def get_all_books() -> list:
    return BOOKS


# 특정 책 데이터 조회
@router.get("/api/v1/books/{book_id}", status_code=200)
def get_book(book_id: int):

    # for book in BOOKS:
    #     if book["id"] == book_id:
    #         book
    #         break

    # 위 코드를 아래 코드 한 줄로 표현.
    book = next((book for book in BOOKS if book["id"] == book_id), None)
    # next는 data 하나를 찾고 나서 break
    if book:
        return book
    return {"error": f"book not found, ID: {book_id}"}


# 책 생성
@router.post("/api/v1/books")
def create_book(book: dict):
    BOOKS.append(book)
    return book


# 특정 책 수정
@router.put("/api/v1/books/{book_id}")
def update_book(book_id: int, book_update: dict):
    # 수정할 book data 가져오기
    book = next((book for book in BOOKS if book["id"] == book_id), None)

    for key, value in book_update.items():
        if key in book:
            book[key] = value
    return book


# 특정 책 삭제
@router.delete("/api/v1/books/{book_id}")
def delete_book(book_id: int):
    global BOOKS

    # for item in BOOKS:
    #     if item['id'] != book_id:
    #         item

    # 위 코드를 아래 코드 한 줄로 표현.
    BOOKS = [item for item in BOOKS if item["id"] != book_id]

    return {"Message": f"Book {book_id} deleted successfully"}


app.include_router(router)

# books data만 따로 부르기.
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("books:app", port=8001, reload=True)
