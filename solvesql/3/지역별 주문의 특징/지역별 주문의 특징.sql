select region as Region,
  count(distinct(case when category = 'Furniture' then order_id end)) as Furniture,
  count(distinct(case when category = 'Office Supplies' then order_id end)) as "Office Supplies",
  count(distinct(case when category = 'Technology' then order_id end)) as Technology
from records
group by region
order by region;

#################################################

select Region, sum(f) as Furniture, sum(o) as 'Office Supplies', sum(t) as Technology
from (
  select Region, 
  case when category = 'Furniture' then cnt end as 'f',
  case when category = 'Office Supplies' then cnt end as 'o',
  case when category = 'Technology' then cnt end as 't'
  from (
    select region, category, count(distinct order_id) as cnt 
    from records
    group by region, category 
  ) as t1 
) as t2
group by Region
order by Region
