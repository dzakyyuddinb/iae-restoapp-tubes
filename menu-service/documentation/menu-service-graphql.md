# Menu Service GraphQL Documentation

## Queries

### all_menus
Returns a list of all menu items.

```graphql
query {
  all_menus {
    id
    name
    description
    price
    stock
  }
}
```

## Mutations

### create_menu
Creates a new menu item.

```graphql
mutation{
  createMenu(name: "Nasi Goreng", description: "Makanan", price: 20000, stock: 20) {
    ok
    menu {
      id
      name
      description
      price
      stock
    }
  }
}
