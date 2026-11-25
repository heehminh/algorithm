select c.id, c.genotype, p.genotype 
from ecoli_data as c join ecoli_data as p on c.parent_id = p.id 
where p.genotype & c.genotype = p.genotype 
order by c.id