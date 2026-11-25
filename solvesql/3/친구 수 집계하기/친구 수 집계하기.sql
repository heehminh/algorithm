select u.user_id, ifnull(num_friends, 0) as num_friends 
from users as u left join (
  select tmp1.user_a_id, count(tmp1.user_b_id) as num_friends
  from (
    select user_a_id, user_b_id
    from edges
    union all
    select user_b_id, user_a_id
    from edges
  )  as tmp1
  group by tmp1.user_a_id 
) as tmp2 on u.user_id = tmp2.user_a_id 
order by num_friends desc, user_id 
