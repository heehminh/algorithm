select item_id, item_name, rarity
from item_info as i
where item_id not in (
    select parent_item_id
    from item_tree
    where parent_item_id is not null 
)
order by item_id desc;