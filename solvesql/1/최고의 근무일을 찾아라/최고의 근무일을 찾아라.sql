select day, round(sum(tip),2) as tip_daily
from tips 
group by day
order by tip_daily desc
limit 1;