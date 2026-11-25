-- 코드를 작성해주세요
select count(*) as fish_count, fish_name 
from fish_info as i join fish_name_info as n on i.fish_type = n.fish_type 
group by n.fish_name 
order by 1 desc