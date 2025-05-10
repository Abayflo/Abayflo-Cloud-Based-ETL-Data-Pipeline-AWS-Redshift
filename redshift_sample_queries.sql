-- Create table
CREATE TABLE IF NOT EXISTS public.sales_orders (
    order_id        INT,
    customer_id     INT,
    order_date      DATE,
    product_id      INT,
    quantity        INT,
    price           DECIMAL(10, 2)
);

-- Select query
SELECT * FROM public.sales_orders LIMIT 10;

-- Aggregate query
SELECT customer_id, SUM(price * quantity) AS total_spent
FROM public.sales_orders
GROUP BY customer_id
ORDER BY total_spent DESC;