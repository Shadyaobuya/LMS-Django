import strawberry


@strawberry.type
class UserType:
    username: str
    email: str
    role: str
