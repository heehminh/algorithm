select day, time, sex, total_bill
from (
  select day, time, sex, total_bill, dense_rank() over (partition by day order by total_bill desc) as ranking
  from tips
) as t1 
where t1.ranking < 4;