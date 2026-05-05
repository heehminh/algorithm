select 
case when weekday = 0 then '월요일'
     when weekday = 1 then '화요일'
     when weekday = 2 then '수요일'
     when weekday = 3 then '목요일'
     when weekday = 4 then '금요일'
     when weekday = 5 then '토요일'
     when weekday = 6 then '일요일'
    end as weekday, no2, o3, co, so2, pm10, pm2_5
from (
  select 
    weekday(measured_at) as weekday, 
    round(avg(no2),4) as no2, round(avg(o3),4) as o3,
    round(avg(co),4) as co, round(avg(so2),4) as so2,
    round(avg(pm10),4) as pm10, round(avg(pm2_5),4) as pm2_5
  from measurements
  group by 1
  order by 1
) as t1 
