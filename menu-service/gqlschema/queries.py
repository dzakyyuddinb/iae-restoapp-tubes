import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField
from .types import MenuType
from models import Menu

class Query(graphene.ObjectType):
    all_menus = graphene.List(MenuType)

    def resolve_all_menus(root, info):
        return Menu.query.all()