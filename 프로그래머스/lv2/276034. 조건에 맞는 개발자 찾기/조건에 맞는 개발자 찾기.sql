select id, email, first_name, last_name
from DEVELOPERS
where SKILL_CODE & (
    select code 
    from SKILLCODES
    where name = 'Python'
) > 0
or SKILL_CODE & (
    select code 
    from SKILLCODES
    where name = 'C#'
) > 0
order by id;