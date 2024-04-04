from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @field_validator("account_id")
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f"account_id must be positive: {value}")
        return value


user = User(
    name = "Victor",
    email = "vic@vic.dev",
    account_id = 1234
    )
json_str = {'name':'john', 'email':'john@dev.com','account_id':2334}

user_2 = User(**json_str)
print(user.name, user_2.name)
print(type(user.model_dump()))
print(type(user.model_dump_json()))
