-- 코드를 입력하세요
SELECT outs.ANIMAL_ID, outs.NAME 
from ANIMAL_OUTS as outs left join ANIMAL_INS as ins 
on outs.ANIMAL_ID = ins.ANIMAL_ID 
where ins.ANIMAL_ID is null 
order by  outs.ANIMAL_ID, outs.NAME 