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
        
class UpdateOrder(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        user_id = graphene.Int()
        status = graphene.String()
        payment_status = graphene.String()

    order = graphene.Field(lambda: OrderType)
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, id, user_id=None, status=None, payment_status=None):
        order = Order.query.get(id)
        if not order:
            return UpdateOrder(success=False, message="Order not found")

        if status:
            valid_status = ['created', 'processed', 'completed', 'delivered', 'cancelled']
            # Tambahkan status baru sesuai kebutuhan
            if status not in valid_status:
                return UpdateOrder(success=False, message=f"Invalid status: {status}")
            order.status = status

        if payment_status:
            valid_payment_status = ['pending', 'paid', 'failed']
            if payment_status not in valid_payment_status:
                return UpdateOrder(success=False, message=f"Invalid payment status: {payment_status}")
            order.payment_status = payment_status

        if user_id:
            order.user_id = user_id

        try:
            db.session.commit()
            return UpdateOrder(order=order, success=True, message="Order updated successfully")
        except Exception:
            db.session.rollback()
            return UpdateOrder(success=False, message="Failed to update order")

class UpdateOrderStatus(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        status = graphene.String(required=True)

    order = graphene.Field(lambda: OrderType)
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, id, status):
        order = Order.query.get(id)
        if not order:
            return UpdateOrderStatus(success=False, message="Order not found")

        valid_status = ['created', 'processed', 'completed']
        if status not in valid_status:
            return UpdateOrderStatus(success=False, message=f"Invalid status: {status}")

        order.status = status
        try:
            db.session.commit()
            return UpdateOrderStatus(order=order, success=True, message="Order status updated")
        except Exception:
            db.session.rollback()
            return UpdateOrderStatus(success=False, message="Failed to update status")

class DeleteOrder(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, id):
        order = Order.query.get(id)
        if not order:
            return DeleteOrder(success=False, message="Order not found")
        try:
            db.session.delete(order)
            db.session.commit()
            return DeleteOrder(success=True, message="Order deleted")
        except Exception:
            db.session.rollback()
            return DeleteOrder(success=False, message="Failed to delete order")
        
class Mutation(graphene.ObjectType):
    create_order = CreateOrder.Field()
    update_order = UpdateOrder.Field()
    update_order_status = UpdateOrderStatus.Field()
    delete_order = DeleteOrder.Field()