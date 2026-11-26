with recursive t as (
    select 0 as h 
    union all 
    select h+1 
    from t 
    where h+1 <= 23 
)

select t.h as hour, ifnull(count(animal_id), 0) as count 
from t left outer join animal_outs as o on t.h = hour(o.datetime)
group by t.h 
order by t.h