select id,
    case when size_of_colony > 1000 then 'HIGH'
    when size_of_colony > 100 then 'MEDIUM'
    else 'LOW' end as size 
from ecoli_data 
order by id 