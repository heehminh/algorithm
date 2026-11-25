-- 코드를 입력하세요
select book_id, author_name, published_date 
from book as b join author as a on b.author_id = a.author_id 
where category = '경제'
order by published_date