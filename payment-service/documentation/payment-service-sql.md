# Payment Service SQL Seed and Queries

## SQL Table Creation

```sql
CREATE TABLE iae_payments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    user_id INT,
    amount DECIMAL(10, 2),
    status ENUM('pending', 'paid', 'failed'),
    payment_method VARCHAR(50),
    payment_time DATETIME
);
```

## SQL Queries

### Select all payments
```sql
SELECT * FROM iae_payments;
```

### Insert new payment (dummy data)
```sql
INSERT INTO iae_payments (order_id, user_id, amount, status, payment_method, payment_time) VALUES 
(1, 1, 50000.00, 'pending', 'credit_card', '2025-06-05 08:30:00'),
(2, 2, 120000.00, 'paid', 'bank_transfer', '2025-06-05 09:30:00'),
(3, 3, 75000.00, 'failed', 'cash', '2025-06-05 10:30:00');
```

### Update payment status
```sql
UPDATE iae_payments SET status = ? WHERE id = ?;
