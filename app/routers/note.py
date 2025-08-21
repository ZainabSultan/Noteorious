from typing import Annotated
from fastapi import APIRouter, Depends
from ..dependencies.auth import get_active_user
from ..models.note import NoteBase, Note
from supabase._sync.client import SyncClient
from ..dependencies.database import connect_db
from datetime import datetime
from google import genai

router = APIRouter()

@router.post('/create', tags=['notes'])
async def create_note(note: NoteBase, username: Annotated[str, Depends(get_active_user)], 
                      db_client: Annotated[SyncClient, Depends(connect_db)]):
    # retrieve id 
    data = db_client.table('users').select('id').eq('email', username).execute().data
    user_id = data[0]['id']
    date = datetime.now().isoformat()
    note_entry = {'user_id' : user_id, 'content': note.content, 'date_created' : date,  'date_updated' : date}
    response = db_client.table('notes').insert(note_entry).execute()
    print(response)
    return Note(**note_entry)


# @router.post('/summarise', tags= ['notes'])
# async def summarise_note(note_id: int, username: Annotated[str, Depends(get_active_user)], db_client: Annotated[SyncClient, Depends(connect_db)]):
#     data = db_client.table('users').select('id').eq('email', username).execute().data
#     user_id = data[0]['id']
#     data = db_client.tables('notes').select('content').eq('note_id', note_id, 'user_id', user_id).execute().data
#     note = data[0]['content']
#     client = genai.Client()
#     response = client.models.generate_content(
#         model="gemini-2.5-flash", contents=f"Summarise this text: {note}"
#     )
#     print(response)




