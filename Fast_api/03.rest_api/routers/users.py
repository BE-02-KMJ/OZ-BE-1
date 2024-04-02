from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from schemas import UserCreate, UserUpdate
from typing import Union
import crud

router = APIRouter()


# CRUD
@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user)
    return db_user


# api/v1/users/{user_id}
@router.get("/{user_data}")  # user_id 문자와 숫자 어떤거든 입력하여 검색 가능하도록
def get_user(user_data: Union[int, str], db: Session = Depends(get_db)):
    try:  # user_data type이 int인 경우
        user_data = int(user_data)
        db_user = crud.get_user_id(db, user_data)
    except:  # user_data type이 str인 경우
        db_user = crud.get_user_email(db, user_data)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    return db_user


# api/v1/users/
@router.get("/")
def get_users(skip: int, limit: int, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)


# api/v1/users/{user_id}
@router.put("/{user_id}")
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    updated_user = crud.update_user(db, user_id, user)

    if updated_user is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    return updated_user


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = crud.delete_user(db, user_id)

    if delete_user is None:
        raise HTTPException(status_code=404, detail="User Not Found")
    return deleted_user
