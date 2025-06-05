# Order Service GraphQL Documentation

## Queries

### all_orders
Returns a list of all orders.

```graphql
query {
  all_orders {
    id
    user_id
    status
    payment_status
    order_time
  }
}
```

## Mutations

### create_order
Creates a new order.

```graphql
mutation CreateOrder($user_id: Int!, $status: String!, $payment_status: String!) {
  create_order(user_id: $user_id, status: $status, payment_status: $payment_status) {
    success
    message
    order {
      id
      user_id
      status
      payment_status
      order_time
    }
  }
}
