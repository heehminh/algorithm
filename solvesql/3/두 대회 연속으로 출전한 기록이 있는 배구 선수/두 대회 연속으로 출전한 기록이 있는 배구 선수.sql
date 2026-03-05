select distinct t1.athlete_id as id, t1.name as name
from (
  select distinct a.id as athlete_id, a.name, g.year as game_year
  from records as r join events as e on r.event_id = e.id
  join teams as t on r.team_id = t.id
  join games as g on r.game_id = g.id 
  join athletes as a on r.athlete_id = a.id 
  where e.event = 'Volleyball Women''s Volleyball' 
  and t.team = 'KOR' and g.year <= 2016 
  group by a.id, a.name, g.year
) as t1 join 
(
  select distinct a.id as athlete_id, a.name, g.year as game_year
  from records as r join events as e on r.event_id = e.id
  join teams as t on r.team_id = t.id
  join games as g on r.game_id = g.id 
  join athletes as a on r.athlete_id = a.id 
  where e.event = 'Volleyball Women''s Volleyball' 
  and t.team = 'KOR' and g.year <= 2016 
  group by a.id, a.name, g.year
) as t2 on t1.athlete_id = t2.athlete_id and t1.game_year = t2.game_year+4
