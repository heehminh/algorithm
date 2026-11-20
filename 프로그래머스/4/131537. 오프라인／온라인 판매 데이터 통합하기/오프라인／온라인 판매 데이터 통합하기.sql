select sales_date, product_id, user_id, sales_amount 
from (
    select sales_date, product_id, user_id, sales_amount 
    from online_sale
    union
    select sales_date, product_id, NULL, sales_amount  
    from offline_sale
) as tmp
where sales_date like '2022-03%'
order by sales_date, product_id, user_id 

