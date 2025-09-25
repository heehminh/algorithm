-- 코드를 입력하세요
select i.food_type, i.rest_id, i.rest_name, i.FAVORITES
from rest_info as i join
(
    select food_type, max(FAVORITES) as max_favorite 
    from REST_INFO
    group by food_type 
) as t on i.food_type = t.food_type and i.FAVORITES = t.max_favorite
order by food_type desc
