select name, count(name) as count 
from animal_ins 
group by name
having count > 1
order by name;