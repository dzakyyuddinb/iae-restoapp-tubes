import graphene
from .types import UserType
from models import User

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)

    def resolve_all_users(self, info):
        return User.query.all()
