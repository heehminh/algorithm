select car_id, 
case when sum(avail) > 0 then '대여중' else '대여 가능' end as availability
from (
    select car_id, 
    case when start_date = '2022-10-16' then '1'
    when start_date < '2022-10-16' and end_date >= '2022-10-16' then '1'
    else 0 end as avail 
    from car_rental_company_rental_history 
) as tmp 
group by car_id
order by car_id desc 