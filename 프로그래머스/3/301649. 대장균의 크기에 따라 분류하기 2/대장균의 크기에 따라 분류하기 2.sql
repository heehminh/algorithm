select id, 
case when ranking/cnt <= 0.25 then 'CRITICAL'
when ranking/cnt <= 0.5 then 'HIGH'
when ranking/cnt <= 0.75 then 'MEDIUM'
else 'LOW' end as colony_name
from (
    select *, row_number() over (order by size_of_colony desc) as ranking
    from ecoli_data join (
    select count(*) as cnt
    from ecoli_data
    ) as t1
) as t2 
order by id asc