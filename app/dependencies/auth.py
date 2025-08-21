from app.routers.auth import oauth2_scheme, token_service

from fastapi import Depends, status, HTTPException
# create user, post, save in db
from typing import Annotated


async def get_active_user(token: Annotated[str, Depends(oauth2_scheme)]):
    #try:
    print(token)
    username = token_service.decode(token)
    assert username is not None
    print(username)
    # except:
    #     raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = 'Inactive user')
    return username



  