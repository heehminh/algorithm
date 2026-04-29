select a.car_id, a.car_type, round(daily_fee * 30 - daily_fee * 30 * discount_rate * 0.01) as fee
from CAR_RENTAL_COMPANY_CAR as a inner join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as c
on a.car_type = c.car_type
where a.car_type in ('세단', 'SUV') 
and daily_fee * 30 - daily_fee * 30 * discount_rate * 0.01 between 500000 and 2000000
and c.duration_type in ('30일 이상') 
and a.car_id not in (
    select car_id
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where end_date >= '2022-11-01' and start_date <= '2022-11-30'
)
order by fee desc, car_type asc, car_id desc 