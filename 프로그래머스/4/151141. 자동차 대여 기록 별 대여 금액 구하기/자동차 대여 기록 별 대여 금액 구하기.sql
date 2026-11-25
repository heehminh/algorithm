select history_id, (daily_fee * (datediff(end_date, start_date)+1) * (100 - t1.discount_rate) / 100) as fee 
from (
    select h.history_id, c.daily_fee, end_date, start_date, 
    case when datediff(end_date, start_date)+1 >= 90 then (select discount_rate from car_rental_company_discount_plan where car_type = '트럭' and duration_type = '90일 이상') 
    when datediff(end_date, start_date)+1 >= 30 then (select discount_rate from car_rental_company_discount_plan where car_type = '트럭' and duration_type = '30일 이상') 
    when datediff(end_date, start_date)+1 >= 7 then (select discount_rate from car_rental_company_discount_plan where car_type = '트럭' and duration_type = '7일 이상') 
    else 0
    end as discount_rate 
    from car_rental_company_car as c join car_rental_company_rental_history as h on c.car_id = h.car_id 
    where car_type = '트럭'
) as t1 
order by 2 desc, 1 desc
