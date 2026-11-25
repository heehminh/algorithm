-- 코드를 입력하세요
select category, sum(s.sales) as TOTAL_SALES
from book as b join book_sales as s on b.book_id = s.book_id
where sales_date like '2022-01%'
group by category
order by category