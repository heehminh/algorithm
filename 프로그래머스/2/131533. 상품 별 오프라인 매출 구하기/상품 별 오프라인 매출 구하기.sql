-- 코드를 입력하세요
select product_code, price * sum(sales_amount) as sales 
from product as p join offline_sale as o on p.product_id = o.product_id 
group by product_code 
order by 2 desc, 1