from pydantic import BaseModel, EmailStr


class FullName(BaseModel):
    first: str
    last: str


class UserBase(BaseModel):
    name: FullName
    email: EmailStr


class UserCreate(UserBase):
    slug: str


class User(UserBase):
    user_id: str
    slug: str

    class Config:
        fields = {"user_id": "id_user"}
