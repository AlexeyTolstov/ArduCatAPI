from pydantic import BaseModel, EmailStr, Field


class UserSignUpRequest(BaseModel):
    login: str = Field(..., min_length=3, max_length=60)
    password: str = Field(..., min_length=8, max_length=60)

    first_name: str = Field(..., min_length=3, max_length=60)
    last_name: str = Field(..., min_length=3, max_length=60)
    email: EmailStr