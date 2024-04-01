from fastapi import FastAPI
from routers.users import router as user_router
from routers.items import router as item_router

app = FastAPI()

app.include_router(user_router, prefix='/api/v1/users', tags=['User'])
app.include_router(item_router, prefix='/api/v1/items', tags=['Item'])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)