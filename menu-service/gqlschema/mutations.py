import graphene
from models import db, Menu  
from .types import MenuType

class CreateMenu(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()
        price = graphene.Float(required=True)
        stock = graphene.Int()

    ok = graphene.Boolean()
    menu = graphene.Field(lambda: MenuType)

    def mutate(self, info, name, description=None, price=0.0, stock=None):
        menu = Menu(name=name, description=description, price=price, stock=stock)
        db.session.add(menu)
        db.session.commit()
        return CreateMenu(menu=menu, ok=True)

class Mutation(graphene.ObjectType):
    create_menu = CreateMenu.Field()