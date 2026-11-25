select a.name 
from (
  select a.id, count(distinct team_id)
  from records as r join games as g on g.id = r.game_id join 
  athletes as a on r.athlete_id = a.id 
  where r.medal is not null and g.year >= 2000
  group by a.id
  having count(distinct team_id) > 1 
) as t join athletes as a on t.id = a.id
order by a.name; 