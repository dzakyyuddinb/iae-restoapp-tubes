import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Order

class OrderType(SQLAlchemyObjectType):
    class Meta:
        model = Order
        interfaces = (graphene.relay.Node,)