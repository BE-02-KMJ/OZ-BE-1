import uvicorn
from fastapi import FastAPI
from items import router as items_router  # as는 추후 다른 model에서의 router와 비교하기 위해.
from users import router as users_router

app = FastAPI()

app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


# http://127.0.0.1:8000/items/123?q=hi

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")
