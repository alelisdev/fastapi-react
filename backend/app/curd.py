# need for only SQL Database
from sqlalchemy.orm import Session
import app.schema  as schema
import app.model  as model


def get_user_by_email(db: Session, email: str):
    return db.query(model.User).filter(model.User.email == email).first()

def create_user(db: Session, user: schema.UserCreate):
    db_user = model.User(fullname=user['fullname'], email=user['email'], password=user['password'])
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user