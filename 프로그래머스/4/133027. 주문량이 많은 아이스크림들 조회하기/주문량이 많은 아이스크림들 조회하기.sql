with t1 as (
    select *
    from first_half 
    union all
    select *
    from july
)
select flavor
from t1 
group by flavor 
order by sum(total_order) desc 
limit 3;