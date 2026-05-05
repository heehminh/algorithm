select distinct game_name as name 
from (
  select g.name as game_name,
  case when p.name in ('PS3', 'PS4', 'PSP', 'PSV') then 1 else 0 end as Sony,
  case when p.name in ('Wii', 'WiiU', 'DS', '3DS') then 1 else 0 end as Nintendo,
  case when p.name in ('X360', 'XONE') then 1 else 0 end as Microsoft
  from games as g join platforms as p on g.platform_id = p.platform_id
  where year >= 2012
) as t1 
group by game_name 
having (sum(Sony) > 0 and sum(Nintendo) > 0) or (sum(Sony) > 0 and sum(Microsoft) > 0) or (sum(Nintendo) > 0 and sum(Microsoft) > 0) 