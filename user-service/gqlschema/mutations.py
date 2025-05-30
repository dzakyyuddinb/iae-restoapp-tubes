import graphene
from models import db, User
from .types import UserType

class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        phone = graphene.String(required=True)
        payment_status = graphene.String(required=True)

    user = graphene.Field(lambda: UserType)

    def mutate(self, info, name, phone, payment_status):
        new_user = User(name=name, phone=phone, payment_status=payment_status)
        db.session.add(new_user)
        db.session.commit()
        return CreateUser(user=new_user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()