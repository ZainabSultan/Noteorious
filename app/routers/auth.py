
from fastapi import APIRouter, Depends, status
# create user, post, save in db
import os
from fastapi import HTTPException
import jwt
from typing import Annotated
from ..models.auth import Token
from supabase._sync.client import SyncClient
from ..dependencies.database import connect_db
from ..utils.auth_utils import TokenService
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
token_service = TokenService(secret = os.environ['key'], algorithm = 'HS256')

router = APIRouter()


@router.post('/token', tags = ['auth'])
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db_client: Annotated[SyncClient, Depends(connect_db)]):
    email = form_data.username
    password = form_data.password
    # TODO add BCrypt hashing
    result = (db_client.table('users').select('password').eq('email', email).execute())
    users = result.data  # this is a list of dicts
    if not users:  # no user found
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No account, are you registered?")

    # Supabase returns a list, take the first row
    stored_password = users[0]['password'].strip()
    print(stored_password, password)
    # TODO: use bcrypt.checkpw here instead of plain comparison
    if stored_password != password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Wrong username or password")
    
    token = token_service.create(subject=email)
    return {"access_token": token, "token_type": "bearer"}






    

    