# Menu Service SQL Seed and Queries

## SQL Table Creation

```sql
CREATE TABLE menus (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    description VARCHAR(255),
    price DECIMAL(10, 2),
    stock INT
);

INSERT INTO menus (name, description, price, stock) VALUES 
('Nasi Goreng', 'Fried rice with chicken', 15000.00, 10),
('Mie Ayam', 'Chicken noodles', 12000.00, 15),
('Es Teh Manis', 'Sweet iced tea', 5000.00, 20);
```



