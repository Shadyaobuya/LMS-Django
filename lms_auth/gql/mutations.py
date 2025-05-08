import traceback
import strawberry
import typing
from .input import AddUserInput
from lms_auth.models import CustomUser  # Import CustomUser from the appropriate module
from lms_auth.gql.types import UserType  # Import UserType from the appropriate module


@strawberry.type
class AddUserMutation:
    message: str = strawberry.field(
        description="Message indicating the result of the operation"
    )
    user: UserType = strawberry.field(description="The created user object")

    @strawberry.mutation
    def add_user(self, input: AddUserInput) -> typing.Optional[UserType]:
        """
        Add a new user to the system.
        """
        try:
            # Check if the user already exists
            existing_user = CustomUser.objects.filter(email=input.email).first()
            if existing_user:
                raise ValueError("User with this email already exists.")
            email = input.email
            username = input.username
            password = input.password
            role = input.role
            user = CustomUser.objects.create_user(
                email=email, username=username, password=password, role=role
            )
            return UserType(
                username=user.username,
                email=user.email,
                role=user.role,
            )
        except Exception as e:
            traceback.print_exc()
            raise ValueError(f"An error occurred while creating the user: {str(e)}")


@strawberry.type
class LoginMutation:
    message: str = strawberry.field(
        description="Message indicating the result of the operation"
    )
    user: UserType = strawberry.field(description="The logged user object")

    @strawberry.mutation
    def add_user(self, input: AddUserInput) -> typing.Optional[UserType]:
        """
        login to the system.
        """
        try:
            # Check if the user already exists
            existing_user = CustomUser.objects.filter(email=input.email).first()
            if existing_user:
                raise ValueError("User with this email already exists.")
            email = input.email
            username = input.username
            password = input.password
            role = input.role
            user = CustomUser.objects.create_user(
                email=email, username=username, password=password, role=role
            )
            return UserType(
                username=user.username,
                email=user.email,
                role=user.role,
            )
        except Exception as e:
            traceback.print_exc()
            raise ValueError(f"An error occurred while creating the user: {str(e)}")
