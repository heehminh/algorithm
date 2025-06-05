-- 코드를 작성해주세요

select count(id) as count 
from ecoli_data
where (genotype & 1 or genotype & 4 ) and not genotype & 2