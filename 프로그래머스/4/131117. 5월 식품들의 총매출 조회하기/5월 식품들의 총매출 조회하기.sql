-- 코드를 입력하세요
SELECT p.product_id, product_name, price*sum(amount) as total_sales 
from food_product as p join food_order as o on p.product_id = o.product_id
where date_format(produce_date, '%Y-%m') = '2022-05'
group by p.product_id 
order by total_sales desc, product_id asc

-- 생산일자 2022년 5월 