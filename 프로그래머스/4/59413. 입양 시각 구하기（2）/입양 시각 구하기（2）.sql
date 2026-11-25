with recursive t as (
    select 0 as h 
    union all 
    select h+1
    from t 
    where h+1 <= 23 
)

select t.h as hour, ifnull(count(distinct animal_id),0) as count 
from t left outer join animal_outs as a on t.h = hour(a.datetime)
group by t.h
order by t.h