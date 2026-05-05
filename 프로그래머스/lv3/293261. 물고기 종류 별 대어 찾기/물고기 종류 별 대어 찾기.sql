-- 코드를 작성해주세요
select f.ID, t.FISH_NAME, t.LENGTH
from FISH_INFO as f join (
    select n.FISH_TYPE, n.FISH_NAME, max(f.LENGTH) as LENGTH
    from FISH_INFO as f join FISH_NAME_INFO as n on f.FISH_TYPE = n.FISH_TYPE
    group by n.FISH_TYPE, n.FISH_NAME
) as t on f.FISH_TYPE = t.FISH_TYPE and f.LENGTH = t.LENGTH
order by f.ID