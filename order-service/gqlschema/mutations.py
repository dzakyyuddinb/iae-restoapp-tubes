import graphene
from models import db, Order
from .types import OrderType
from datetime import datetime

class CreateOrder(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int(required=True)
        status = graphene.String(required=True)
        payment_status = graphene.String(required=True)

    order = graphene.Field(lambda: OrderType)
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, user_id, status, payment_status):
        # Validasi enum untuk status dan payment_status
        valid_status = ['created', 'processed', 'completed']
        valid_payment_status = ['pending', 'paid', 'failed']

        if status not in valid_status:
            return CreateOrder(success=False, message=f"Invalid status: {status}. Must be one of {valid_status}")

        if payment_status not in valid_payment_status:
            return CreateOrder(success=False, message=f"Invalid payment status: {payment_status}. Must be one of {valid_payment_status}")

        try:
            new_order = Order(
                user_id=user_id,
                status=status,
                payment_status=payment_status,
                order_time=datetime.utcnow()
            )
            db.session.add(new_order)
            print("Sebelum commit")
            db.session.commit()
            print("Setelah commit")
            print("Order berhasil disimpan:", new_order.id)
            return CreateOrder(order=new_order, success=True, message="Order created successfully")
        except Exception as e:
            db.session.rollback()
            print("Error saat menyimpan order:", str(e))
            return CreateOrder(success=False, message="Failed to create order")

class Mutation(graphene.ObjectType):
    create_order = CreateOrder.Field()