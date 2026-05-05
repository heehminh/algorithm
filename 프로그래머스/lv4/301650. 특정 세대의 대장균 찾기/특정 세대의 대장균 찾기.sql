select id 
from ecoli_data
where parent_id in (
    select id 
    from ecoli_data
    where parent_id in (
        select id 
        from ecoli_data
        where parent_id is null
    )
)
order by id;