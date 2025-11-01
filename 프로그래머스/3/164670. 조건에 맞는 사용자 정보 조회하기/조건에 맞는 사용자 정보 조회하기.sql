-- 코드를 입력하세요
select u.user_id as user_id, u.nickname, concat(city, ' ', street_address1, ' ', street_address2) as '전체주소', concat(substr(tlno, 1, 3), '-', substr(tlno, 4, 4), '-', substr(tlno, 8, 4)) as '전화번호'
from USED_GOODS_BOARD as b join USED_GOODS_USER as u on b.writer_id = u.user_id 
group by u.user_id 
having count(u.user_id) >= 3
order by u.user_id desc