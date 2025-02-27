# app/schemas.py
from pydantic import BaseModel, EmailStr, constr, field_validator
from typing import List, Dict

class UserBase(BaseModel):
    email: EmailStr
    
class UserCreate(UserBase):
    name: str
    last_name: str
    password: constr(min_length=8)

    @field_validator('password')
    def password_complexity(cls, v):
        if not any(char.isdigit() for char in v):
            raise ValueError('A senha precisa ter pelo menos um número')
        if not any(char in '!@#$%^&*(),.?":{}|<>_-+=~`[]\\;\'/' for char in v):
            raise ValueError('A senha precisa ter pelo menos um caractere especial')
        return v

class UserInDB(UserBase):
    summaries: List[str] = []

    class Config:
        orm_mode = True

class SummaryRequest(BaseModel):
    content: Dict[str, str]  

class MessageRequest(BaseModel):
    message: str
    
class SummariesResponse(BaseModel):
    summaries: List[str]

class AnalysisRequest(BaseModel):
    content: str  # Aqui armazenaremos a imagem em base64 ou um caminho para o arquivo.

class AnalysesResponse(BaseModel):
    analyses: List[str]

class LoginCredentials(BaseModel):
    email: EmailStr
    password: constr(min_length=8)

    @field_validator('password')
    def password_complexity(cls, v):
        if not any(char.isdigit() for char in v):
            raise ValueError('A senha precisa ter pelo menos um número')
        if not any(char in '!@#$%^&*(),.?":{}|<>_-+=~`[]\\;\'/' for char in v):
            raise ValueError('A senha precisa ter pelo menos um caractere especial')
        return v

class PasswordRequest (BaseModel):
    email: EmailStr
    password: constr(min_length=8)

    @field_validator('password')
    def password_complexity(cls, v):
        if not any(char.isdigit() for char in v):
            raise ValueError('A senha precisa ter pelo menos um número')
        if not any(char in '!@#$%^&*(),.?":{}|<>_-+=~`[]\\;\'/' for char in v):
            raise ValueError('A senha precisa ter pelo menos um caractere especial')
        return v
