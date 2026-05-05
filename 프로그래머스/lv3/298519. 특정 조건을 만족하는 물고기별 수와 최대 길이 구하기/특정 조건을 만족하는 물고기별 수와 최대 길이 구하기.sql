select count(*) as fish_count, max(length) as max_length, fish_type
from (select fish_type, ifnull(length, 10) as length 
from fish_info) as t 
group by fish_type 
having sum(length) / count(length) >= 33 
order by fish_type;