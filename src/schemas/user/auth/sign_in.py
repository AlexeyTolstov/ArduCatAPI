from pydantic import BaseModel, field_validator, EmailStr, Field


class UserSignInRequest(BaseModel):
    login: str | None = Field(None, min_length=3, max_length=60)
    email: EmailStr | None = None
    password: str

    @field_validator('login', 'email', mode='before')
    def validate_at_least_one_field(cls, v, values, **kwargs):
        if v is None and not any(values.get(f) for f in ['login', 'email']):
            raise ValueError('At least one of login or email must be provided')
        return v