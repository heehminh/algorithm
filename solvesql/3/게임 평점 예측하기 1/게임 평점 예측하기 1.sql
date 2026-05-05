select games.game_id, name,
      ifnull(critic_score,t1.t_critic_score) as critic_score,
      ifnull(critic_count, t1.t_critic_count) as critic_count,
      ifnull(user_score,t1.t_user_score) as user_score,
      ifnull(user_count, t1.t_user_count) as user_count
from games join 
  (select genre_id,
  round(avg(critic_score),3) as t_critic_score,
  ceil(avg(critic_count)) as t_critic_count,
  round(avg(user_score),3) as t_user_score,
  ceil(avg(user_count)) as t_user_count
  from games 
  group by genre_id
) as t1 on games.genre_id = t1.genre_id
where games.year >= 2015 
and (games.critic_score is null or games.critic_count is null 
or games.user_score is null or games.user_count is null)