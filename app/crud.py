from sqlalchemy.orm import Session
from app.models import User, Post


def create_user(db: Session, username: str, email: str, password: str):
    user = User(username=username, email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def create_post(db: Session, title: str, content: str, user_id: int):
    post = Post(title=title, content=content, user_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_users(db: Session):
    return db.query(User).all()

def get_posts(db: Session):
    return db.query(Post).all()


def get_posts_by_user(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()
