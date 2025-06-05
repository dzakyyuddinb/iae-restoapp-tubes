# Payment Service GraphQL Documentation

## Queries

### all_payments
Returns a list of all payments.

```graphql
query {
  all_payments {
    id
    order_id
    user_id
    amount
    status
    payment_method
    payment_time
  }
}
```

## Mutations

### create_payment
Creates a new payment.

```graphql
mutation{
  createPayment(order_id: $order_id, user_id: $user_id, amount: $amount, status: $status, payment_method: $payment_method) {
    payment {
      id
      order_id
      user_id
      amount
      status
      payment_method
      payment_time
    }
  }
}
```

### update_payment_status
Updates the status of an existing payment.

```graphql
mutation UpdatePaymentStatus($id: Int!, $status: String!) {
  update_payment_status(id: $id, status: $status) {
    payment {
      id
      status
    }
  }
}
