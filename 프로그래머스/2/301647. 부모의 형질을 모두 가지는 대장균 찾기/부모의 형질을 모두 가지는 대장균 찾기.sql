select c.id, c.genotype, p.genotype as parent_genotype 
from ecoli_data as c join ecoli_data as p on c.parent_id = p.id 
where c.genotype & p.genotype = p.genotype 
order by c.id 