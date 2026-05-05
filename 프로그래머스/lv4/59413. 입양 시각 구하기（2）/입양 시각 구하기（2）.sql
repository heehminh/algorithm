with recursive t1 as (
    select 0 as num
    union all
    select num+1 
    from t1 
    where num < 23
)

select t1.num as hour, ifnull(t2.count, 0) as count
from t1 left join (
    select hour(datetime) as hour, count(*) as count
    from animal_outs 
    group by hour
) as t2 on t1.num = t2.hour