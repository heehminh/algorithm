select id, 
case when (p/cnt) * 100 <= 25 then 'CRITICAL' 
when (p/cnt) * 100 <= 50 then 'HIGH' 
when (p/cnt) * 100 <= 75 then 'MEDIUM' 
else 'LOW' end as colony_name
from (
    select id, rank() over (order by size_of_colony desc) as p
    from ecoli_data 
) as r, (select count(*) as cnt from ecoli_data) as c 
order by id 
