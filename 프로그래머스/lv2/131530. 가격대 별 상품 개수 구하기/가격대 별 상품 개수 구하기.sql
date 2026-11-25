-- 코드를 입력하세요
select price * 10000 as price_group, count(distinct product_id) as products 
from (
    select product_id, floor(price / 10000) as price 
    from product 
) as t1 
group by price 
order by 1