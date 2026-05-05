-- 코드를 입력하세요
SELECT A.author_id as author_id, author_name, category, sum(A.price * C.sales) as total_sales
from book as A inner join author as B on A.author_id = B.author_id 
inner join book_sales as C on A.book_id = C.book_id
where year(C.sales_date) = 2022 and month(C.sales_date) = 1 
group by A.author_id, A.category
order by author_id asc, category desc

-- book_sales (sales_date) 2022년 1월 
-- book(price) * book_sales(sales) = total_sales 
-- group by (author_id, cateogry)