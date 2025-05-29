import graphene
from .types import PaymentType
from models import Payment

class Query(graphene.ObjectType):
    all_payments = graphene.List(PaymentType)

    def resolve_all_payments(root, info):
        return Payment.query.all()