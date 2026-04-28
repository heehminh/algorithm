select m.artist_id, m.name 
from artists as m left join artworks_artists as a on m.artist_id = a.artist_id
where m.death_year is not null and a.artist_id is null;