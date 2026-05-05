-- 코드를 작성해주세요

select year(A.differentiation_date) as year, (B.size_of_colony - A.size_of_colony) as year_dev, id 
from ecoli_data as A inner join (
    select year(differentiation_date) as year, max(size_of_colony) as size_of_colony
    from ecoli_data
    group by year(differentiation_date)
) as B 
on year(A.differentiation_date) = B.year 
order by year, year_dev