from dotenv import load_dotenv

# load .env file into os.environ
load_dotenv()
from fastapi import FastAPI
from .routers import users
from .routers import auth
from .routers import note

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(note.router)
@app.get('/')
async def root():
    return {'message': 'hello world'}