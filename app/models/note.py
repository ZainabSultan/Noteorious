from pydantic import BaseModel
from datetime import datetime
class NoteBase(BaseModel):
    content: str

class Note(NoteBase):
    date_created: str
    date_updated: str
    user_id: int

class Summary(Note):
    summary: str
