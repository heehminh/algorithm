select date_format(order_purchase_timestamp, '%Y-%m-%d') as purchase_date,
ifnull(sum(success),0) as success, ifnull(sum(fail),0) as fail 
from (
  select order_purchase_timestamp,
  case when order_estimated_delivery_date >= order_delivered_customer_date then 1 end as success,
  case when order_estimated_delivery_date < order_delivered_customer_date then 1 end as fail
  from olist_orders_dataset
  where order_purchase_timestamp like '2017-01%'
) as t
group by date_format(order_purchase_timestamp, '%Y-%m-%d')
order by date_format(order_purchase_timestamp, '%Y-%m-%d') 