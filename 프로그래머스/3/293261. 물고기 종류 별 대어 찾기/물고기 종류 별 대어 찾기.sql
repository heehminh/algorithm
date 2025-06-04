-- 코드를 작성해주세요
select ID, A.FISH_NAME, A.LENGTH
from (
    select name.FISH_NAME, name.FISH_TYPE, MAX(info.LENGTH) as LENGTH 
    from FISH_INFO as info inner join FISH_NAME_INFO as name 
    on info.FISH_TYPE = name.FISH_TYPE
    group by name.FISH_NAME, name.FISH_TYPE
) as A inner join FISH_INFO as B
on A.FISH_TYPE = B.FISH_TYPE and A.LENGTH = B.LENGTH
