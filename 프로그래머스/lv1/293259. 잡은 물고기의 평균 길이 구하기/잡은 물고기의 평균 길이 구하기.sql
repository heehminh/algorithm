-- 코드를 작성해주세요
select round(avg(t.length),2) as average_length
from (
    select ifnull(length, 10) as length
    from fish_info
) as t