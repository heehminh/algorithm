-- 코드를 입력하세요
(select date_format(sales_date, '%Y-%m-%d') as sales_date, product_id, user_id, sales_amount
from online_sale 
where sales_date like '2022-03%')
union
(select date_format(sales_date, '%Y-%m-%d') as sales_date, product_id, null as user_id, sales_amount
from offline_sale 
where sales_date like '2022-03%')
order by sales_date asc, product_id asc, user_id asc

-- 2022년 3월 
-- 오프라인은 user_id null 