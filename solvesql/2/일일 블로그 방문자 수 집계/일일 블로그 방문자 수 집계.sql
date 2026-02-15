select event_date_kst as dt, count(*) as users 
from 
(
  select event_date_kst, count(*) as users
  from ga 
  group by event_date_kst, user_pseudo_id
) as t 
where event_date_kst between '2021-08-02' and '2021-08-09' 
group by dt 
order by dt 