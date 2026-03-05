select case when mod(customer_id, 10) = 0 then 'A' else 'B' end as bucket,
count(distinct customer_id) as user_count, 
round(count(*) / count(DISTINCT customer_id), 2) as avg_orders, 
round(sum(total_price) / count(DISTINCT customer_id), 2) as avg_revenue
from transactions
where is_returned = 0
group by bucket;