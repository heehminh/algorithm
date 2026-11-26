with recursive ge as (
    select id, 1 as generation 
    from ecoli_data
    where parent_id is null 
    
    union all 
    
    select e.id, ge.generation + 1 
    from ecoli_data as e join ge on e.parent_id = ge.id 
)

select count(*) as count, ge.generation 
from ecoli_data as e join ge on e.id = ge.id 
where not exists (
    select 1 
    from ecoli_data as c 
    where c.parent_id = e.id 
)
group by ge.generation 
order by ge.generation 