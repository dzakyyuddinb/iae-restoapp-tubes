# Order Service SQL Seed and Queries

## SQL Table Creation

```sql
CREATE TABLE iae_orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    status ENUM('created', 'processed', 'completed'),
    payment_status ENUM('pending', 'paid', 'failed'),
    order_time DATETIME
);
```

## SQL Queries

### Select all orders
```sql
SELECT * FROM iae_orders;
```

### Insert new order (dummy data)
```sql
INSERT INTO iae_orders (user_id, status, payment_status, order_time) VALUES 
(1, 'created', 'pending', '2025-06-05 08:00:00'),
(2, 'processed', 'paid', '2025-06-05 09:00:00'),
(3, 'completed', 'paid', '2025-06-05 10:00:00');
