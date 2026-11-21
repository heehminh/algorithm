select item_id, item_name 
from item_info 
where item_id in (
    select item_id 
    from item_tree 
    where parent_item_id is null 
)
order by item_id 