with recursive ge as (
    select id, 1 as generation
    from ecoli_data
    where parent_id is null
    
    union all
    
    select a.id, b.generation + 1 as generation
    from ecoli_data as a, ge as b 
    where a.parent_id = b.id 
)

select count(*) as count, generation
from ge 
where not exists (
    select 1 
    from ecoli_data as child
    where ge.id = child.parent_id
)
group by generation
order by generation