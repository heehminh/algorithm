select year(o.sales_date) as year, month(o.sales_date) as month,
count(distinct u.user_id) as purchased_users,
round(count(distinct u.user_id) / 
      (select count(*)
      from user_info
      where year(joined) = '2021')
      ,1) as purchased_ratio
from user_info as u join online_sale as o on u.user_id = o.user_id
where year(u.joined) = '2021'
group by year, month
order by year, month