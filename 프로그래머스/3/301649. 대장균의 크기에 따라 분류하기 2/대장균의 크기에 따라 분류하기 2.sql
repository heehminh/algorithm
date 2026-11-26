select id,
case when n = 1 then 'CRITICAL' 
when n = 2 then 'HIGH'
when n = 3 then 'MEDIUM'
else 'LOW' end as colony_name 
from (
    select id, ntile(4) over (order by size_of_colony desc) as n 
    from ecoli_data 
) as tmp 
order by id 