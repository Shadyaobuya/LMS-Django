import typing

import strawberry

from lms_auth.models import CustomUser


@strawberry.type
class UserType:
    username: str
    email: str
    role: str
   