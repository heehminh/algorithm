select distinct athlete_id 
from records
where event_id in (select id from events where sport = 'Golf')