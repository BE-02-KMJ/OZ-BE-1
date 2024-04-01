from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from schemas import ItemCreate, ItemUpdate
from typing import Union
import crud

router = APIRouter()

# CRUD
@router.post('/')
def create_item(item: ItemCreate, owner_id: int, db: Session = Depends(get_db)):
    db_item = crud.create_item(db, item, owner_id)
    return db_item

# api/v1/users/{item_id}
@router.get('/{item_id}')
def get_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id)

    if db_item is None:
        raise HTTPException(status_code=404, detail="Item Not Found")
    return db_item

@router.get('/')
def get_items(skip: int, limit: int, db: Session = Depends(get_db)):
    return crud.get_items(db, skip, limit)

@router.put('/{item_id}')
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    updated_item = crud.update_item(db, item_id, item)

    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item Not Found")
    return updated_item

@router.delete('/{item_id}')
def delete_item(item_id: int, db: Session = Depends(get_db)):
    deleted_item = crud.delete_item(db, item_id)

    if delete_item is None:
        raise HTTPException(status_code=404, detail="Item Not Found")
    return deleted_item