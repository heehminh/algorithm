-- 코드를 작성해주세요
select 
case 
    when month(DIFFERENTIATION_DATE) < 4 then '1Q'
    when month(DIFFERENTIATION_DATE) < 7 then '2Q'
    when month(DIFFERENTIATION_DATE) < 10 then '3Q'
    else '4Q' end as QUARTER,
count(id) as ECOLI_COUNT
from ECOLI_DATA
group by QUARTER
order by QUARTER

