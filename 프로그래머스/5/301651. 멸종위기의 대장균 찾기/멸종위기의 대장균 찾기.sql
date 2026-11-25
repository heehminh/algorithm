with recursive ge as (
    select id, 1 as generation
    from ecoli_data
    where parent_id is null 
    
    union all 
    
    select e.id, ge.generation + 1
    from ecoli_data as e join ge on e.parent_id = ge.id 
)

select count(*) as count, generation
from ge
where not exists (
    select 1 
    from ecoli_data
    where ge.id = ecoli_data.parent_id 
)
group by generation
order by generation 