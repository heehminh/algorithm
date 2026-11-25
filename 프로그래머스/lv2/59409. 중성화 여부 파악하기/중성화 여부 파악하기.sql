select ANIMAL_ID, NAME, 
CASE 
    when SEX_UPON_INTAKE like 'Neutered%' then 'O'
    when SEX_UPON_INTAKE like 'Spayed%' then 'O'
    else 'X'
end as "중성화"
from ANIMAL_INS