import strawberry
from .mutations import AddUserMutation
from .queries import Query
schema = strawberry.Schema(mutation=AddUserMutation, query=Query)