select i.animal_id, i.name 
from animal_ins as i join animal_outs as o on i.animal_id = o.animal_id 
where i.datetime > o.datetime 
order by i.datetime 