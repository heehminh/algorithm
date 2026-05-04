select substr(o.order_date,1, 7) as order_month, 
      sum(case when i.order_id not like 'C%' then i.price * i.quantity else 0 end) as ordered_amount,
      sum(case when i.order_id like 'C%' then i.price * i.quantity else 0 end) as canceled_amount,
      sum(i.price * i.quantity) as total_amount
from order_items as i left join orders as o on i.order_id = o.order_id
group by 1
order by 1;