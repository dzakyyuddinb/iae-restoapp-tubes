# User Service SQL Seed and Queries

## SQL Table Creation

```sql
CREATE TABLE iae_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    payment_status VARCHAR(20)
);
```

## SQL Queries

### Select all users
```sql
SELECT * FROM iae_users;
```

### Insert new user (dummy data)
```sql
INSERT INTO iae_users (name, phone, payment_status) VALUES 
('John Doe', '08123456789', 'pending'),
('Jane Smith', '08987654321', 'paid'),
('Alice Johnson', '08223344556', 'failed');
