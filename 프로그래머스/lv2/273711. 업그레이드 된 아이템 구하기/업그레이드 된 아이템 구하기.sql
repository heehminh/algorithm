-- 코드를 작성해주세요
select ITEM_ID, ITEM_NAME, RARITY
from ITEM_INFO
where ITEM_ID in (
    select tree.ITEM_ID
    from ITEM_INFO as info join ITEM_TREE as tree
    where RARITY = 'RARE' and info.ITEM_ID = tree.PARENT_ITEM_ID
)
order by ITEM_ID desc;