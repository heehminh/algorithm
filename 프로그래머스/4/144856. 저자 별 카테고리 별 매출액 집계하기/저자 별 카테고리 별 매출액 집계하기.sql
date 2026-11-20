select a.author_id, a.author_name, tmp1.category, sum(tmp1.bs) as total_sales 
from (
    select b.author_id, b.category, b.book_id, (b.price * s.sales) as bs
    from book as b join book_sales as s on b.book_id = s.book_id 
    where sales_date like '2022-01%'
) as tmp1 join author as a on tmp1.author_id = a.author_id 
group by a.author_id, tmp1.category
order by a.author_id, tmp1.category desc