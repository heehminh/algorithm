-- 코드를 작성해주세요
select id, email, first_name, last_name
from developers
where skill_code in (
    select d.skill_code
    from developers as d, skillcodes as s 
    where s.category = 'Front End' and d.skill_code & s.code > 0 
)
order by id asc;