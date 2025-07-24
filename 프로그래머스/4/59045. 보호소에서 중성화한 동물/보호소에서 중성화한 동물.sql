-- 코드를 입력하세요
SELECT ins.animal_id, ins.animal_type, ins.name
from animal_ins as ins join animal_outs as outs 
on ins.animal_id = outs.animal_id 
where ins.sex_upon_intake like 'Intact%' and 
(outs.sex_upon_outcome = 'Spayed Female' or outs.sex_upon_outcome = 'Neutered Male')
order by ins.animal_id 