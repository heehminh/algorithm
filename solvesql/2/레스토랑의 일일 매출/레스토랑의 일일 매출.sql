select day, sum(total_bill) as revenue_daily
from tips
group by day
having revenue_daily >= 1000 
order by revenue_daily desc 