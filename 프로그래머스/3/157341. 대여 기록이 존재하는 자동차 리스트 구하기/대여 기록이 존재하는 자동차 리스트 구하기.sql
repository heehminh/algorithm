-- 코드를 입력하세요
select distinct c.car_id 
from car_rental_company_car as c join car_rental_company_rental_history as h on c.car_id = h.car_id 
where month(start_date) = 10 and car_type = '세단'
order by c.car_id desc 