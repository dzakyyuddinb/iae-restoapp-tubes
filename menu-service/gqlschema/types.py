import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Menu

class MenuType(SQLAlchemyObjectType):
    class Meta:
        model = Menu
        interfaces = (graphene.relay.Node,)
