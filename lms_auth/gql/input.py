import typing

import strawberry

from lms_auth.models import CustomUser



@strawberry.input
class AddUserInput:
    username: str= strawberry.field(description="Username of the user")
    email: str = strawberry.field(description="Email of the user")
    password: str = strawberry.field(description="Password of the user")
    role: str = strawberry.field(description="Role of the user")
