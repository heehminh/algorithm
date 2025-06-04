-- 코드를 입력하세요
SELECT ins.ANIMAL_ID as ANIMAL_ID, ins.NAME as NAME
from ANIMAL_INS as ins inner join ANIMAL_OUTS as outs on ins.ANIMAL_ID = outs.ANIMAL_ID
order by timestampdiff(day, ins.DATETIME, outs.DATETIME) desc 
limit 2;