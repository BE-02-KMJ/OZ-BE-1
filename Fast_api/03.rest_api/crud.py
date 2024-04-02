from sqlalchemy.orm import Session
from models import User, Item
from schemas import UserCreate, UserUpdate, ItemCreate, ItemUpdate
import bcrypt


# User - CRUD
def create_user(db: Session, user: UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())  # bite 형태라 encode 필요!

    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()

    return db_user


def get_user_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_email(db: Session, user_email: str):
    return db.query(User).filter(User.email == user_email).first()


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, user_update: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None

    user_data = user_update.dict()

    for key, value in user_data.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None

    db.delete(db_user)
    db.commit()

    return db_user


# Item - CRUD
def create_item(db: Session, item: ItemCreate, owner_id: int):
    db_item = Item(**item.dict(), owner_id=owner_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()


def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()
    # 순서 관련 (order by) - 오름차순_기본
    # 내림차순 ex) db.query(Item).order_by(Item.id.desc()).offset(skip).limit(limit).all()


def update_item(db: Session, item_id: int, item_update: ItemUpdate):
    db_item = db.query(Item).filter(Item.id == item_id).first()

    if not db_item:
        return None

    for key, value in item_update.dict().items():
        setattr(db_item, key, value)

    db.commit()
    db.refresh(db_item)

    return db_item


def delete_item(db: Session, item_id: int):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        return None

    db.delete(db_item)
    db.commit()

    return db_item


# FastAPI - Django(main) + FastAPI(MSA) - chatting // 비동기(ASGI)
