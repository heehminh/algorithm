-- 코드를 입력하세요
SELECT r.food_type, r.rest_id, r.rest_name, r.favorites
from rest_info as r join (
    select food_type, max(favorites) as favorites
    from rest_info
    group by food_type
) as t 
where r.favorites = t.favorites and r.food_type = t.food_type
order by r.food_type desc
