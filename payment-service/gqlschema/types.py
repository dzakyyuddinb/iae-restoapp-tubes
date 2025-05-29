import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Payment

class PaymentType(SQLAlchemyObjectType):
    class Meta:
        model = Payment
        interfaces = (graphene.relay.Node,)