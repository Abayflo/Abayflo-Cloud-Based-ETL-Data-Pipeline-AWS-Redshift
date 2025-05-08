CREATE TABLE IF NOT EXISTS sales_orders (
    order_id INT PRIMARY KEY,
    customer VARCHAR(255),
    amount DECIMAL(10,2),
    order_date TIMESTAMP
);
