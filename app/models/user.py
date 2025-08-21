
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    firstname: str
    lastname : str
    email: EmailStr    

class User(UserBase):
    password: str
    id: str

