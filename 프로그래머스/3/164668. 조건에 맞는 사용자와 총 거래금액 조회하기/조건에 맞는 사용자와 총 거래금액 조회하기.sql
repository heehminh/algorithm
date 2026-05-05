select u.user_id, u.nickname, sum(price) as total_sales 
from used_goods_board as b join used_goods_user as u on b.writer_id = u.user_id  
where status = 'DONE'
group by u.user_id, u.nickname 
having sum(price) >= 700000
order by sum(price)