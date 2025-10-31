select o.product_id, p.product_name, p.price * sum(o.amount) as total_sales
from food_product as p join food_order as o on p.product_id = o.product_id 
where o.PRODUCE_DATE like '2022-05%'
group by o.product_id
order by total_sales desc, o.product_id asc

-- 생산일자: 2022년 5월 