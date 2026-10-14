select i.rest_id, rest_name, food_type, favorites, address, round(avg(review_score),2) as score
from rest_info as i join rest_review as r on i.rest_id = r.rest_id
where address like '서울%'
group by i.rest_id 
order by avg(review_score) desc, favorites desc