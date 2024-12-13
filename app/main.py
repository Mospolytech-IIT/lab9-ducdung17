from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import engine, SessionLocal
from app.models import Base
from app.crud import create_user, create_post, get_users, get_posts, get_posts_by_user

app = FastAPI()


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users")
def api_create_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    return create_user(db, username, email, password)


@app.get("/users")
def api_get_users(db: Session = Depends(get_db)):
    return get_users(db)

@app.post("/posts")
def api_create_post(title: str, content: str, user_id: int, db: Session = Depends(get_db)):
    return create_post(db, title, content, user_id)


@app.get("/posts")
def api_get_posts(db: Session = Depends(get_db)):
    return get_posts(db)


@app.get("/users/{user_id}/posts")
def api_get_posts_by_user(user_id: int, db: Session = Depends(get_db)):
    return get_posts_by_user(db, user_id)
