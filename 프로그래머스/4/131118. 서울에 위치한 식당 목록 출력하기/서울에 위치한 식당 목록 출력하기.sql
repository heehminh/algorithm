-- 코드를 입력하세요
select info.rest_id as REST_ID, info.rest_name as REST_NAME, info.food_type as FOOD_TYPE, 
        FAVORITES, ADDRESS, round(avg(REVIEW_SCORE),2) as score 
from rest_info as info join REST_REVIEW as review on info.rest_id = review.rest_id 
where address like '서울%'
group by rest_id
order by score desc, FAVORITES desc;