-- 코드를 입력하세요
select flavor 
from (
    select t1.flavor, t1.total_order + t2.total_order as total_order 
    from (
        select flavor, sum(total_order) as total_order
        from first_half
        group by FLAVOR 
    ) as t1 join 
    (
    select flavor, sum(total_order) as total_order
    from july
    group by flavor 
    ) as t2 on t1.flavor = t2.flavor
) as t 
order by t.total_order desc
limit 3 