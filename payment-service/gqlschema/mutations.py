import graphene
from models import db, Payment
from .types import PaymentType
from datetime import datetime
from pytz import timezone


jakarta_tz = timezone('Asia/Jakarta')
payment_time = datetime.now(jakarta_tz)


class CreatePayment(graphene.Mutation):
    class Arguments:
        order_id = graphene.Int(required=True)
        user_id = graphene.Int(required=True)
        amount = graphene.Float(required=True)
        status = graphene.String(required=True)
        payment_method = graphene.String(required=True)

    payment = graphene.Field(lambda: PaymentType)

    def mutate(self, info, order_id, user_id, amount, status, payment_method):
        payment = Payment(
            order_id=order_id,
            user_id=user_id,
            amount=amount,
            status=status,
            payment_method=payment_method,
            payment_time=payment_time
        )
        db.session.add(payment)
        db.session.commit()
        return CreatePayment(payment=payment)

class UpdatePaymentStatus(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        status = graphene.String(required=True)

    payment = graphene.Field(lambda: PaymentType)

    def mutate(self, info, id, status):
        payment = Payment.query.get(id)
        if not payment:
            raise Exception("Payment not found")
        payment.status = status
        db.session.commit()
        return UpdatePaymentStatus(payment=payment)

class Mutation(graphene.ObjectType):
    create_payment = CreatePayment.Field()
    update_payment_status = UpdatePaymentStatus.Field()