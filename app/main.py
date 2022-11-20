from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

print(settings.database_username)

# This is the command that tells sqlalchemy to run the create statements to generate tables when it is starting up
# models.Base.metadata.create_all(bind=engine)

# To create a txt file containing the libraries install or used for this project without having to upload the venv folder to git
# pip freeze > requirements.txt

# To automatically install the libraries inside the requirements.txt file
# pip install -r requirements.txt

# Creating a virtual environment
# py -3 -m venv venv

# Running on virtual environment interpreter instead of global interpreter
# venv\Scripts\activate.bat

# Running the server
# uvicorn app.main:app --reload

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# my_post = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
# {"title": "favorite food", "content": "I like pizza", "id": 2}]

# def find_post(id: int):
#     for p in my_post:
#         if p["id"] == id:
#             return p

# def find_index_post(id: int):
#     for i, p in enumerate(my_post):
#         if p['id'] == id:
#             return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return { "message" : "Hello World!"}

# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return posts