# User Service GraphQL Documentation

## Queries

### all_users
Returns a list of all users.

```graphql
query {
  all_users {
    id
    name
    phone
    payment_status
  }
}
```

## Mutations

### create_user
Creates a new user.

```graphql
mutation {
  createUser(name: "nama", phone: "0888888", paymentStatus: "PAID") {
    user {
      id
      name
      phone
      paymentStatus
    }
  }
}
