-- Write your query below
SELECT SP.name FROM sales_person SP WHERE SP.sales_id NOT IN (
    SELECT o.sales_id FROM orders o JOIN company c ON o.com_id = c.com_id 
    WHERE c.name = 'CRIMSON'
);

