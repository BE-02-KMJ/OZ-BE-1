from sqlalchemy.orm import Session
from models import User, Item
from schemas import UserCreate, UserUpdate, ItemCreate, ItemUpdate
import bcrypt

# User - CRUD
def create_user(db: Session, user:UserCreate):
    hashed_password = bcrypt.hashpw(user.password)

    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()

    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int=0, limit: int=10):
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

def delete_user():
    pass

# Item - CRUD

# FastAPI - Django(main) + FastAPI(MSA) - chatting // 비동기(ASGI)