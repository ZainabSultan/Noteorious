
from fastapi import APIRouter, Depends
# create user, post, save in db
from typing import Annotated
from ..models.user import UserBase
from supabase._sync.client import SyncClient
from ..dependencies.database import connect_db
from ..dependencies.auth import get_active_user

router = APIRouter(dependencies=[Depends(get_active_user)])

@router.get('/users', tags = ['users'], response_model=list[UserBase])
async def read_users(db_client : Annotated[SyncClient, Depends(connect_db)]):
    response = (
    db_client.table("users")
    .select("*")
    .execute()
    ).data
    print(response)
    return response






    

    