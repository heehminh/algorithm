-- 코드를 입력하세요
SELECT A.CAR_ID, A.CAR_TYPE, round(DAILY_FEE * 30 - DAILY_FEE * 30 * DISCOUNT_RATE * 0.01) as FEE
from CAR_RENTAL_COMPANY_CAR as A inner join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as C
on A.CAR_TYPE = C.CAR_TYPE
where A.CAR_TYPE in ('세단', 'SUV') 
and DAILY_FEE * 30 - DAILY_FEE * 30 * DISCOUNT_RATE * 0.01 between 500000 and 2000000
and C.DURATION_TYPE in ('30일 이상') 
and A.CAR_ID NOT IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE END_DATE >= '2022-11-01' AND START_DATE <= '2022-11-30'
)
order by fee desc, car_type asc, car_id desc 

-- 자동차 종류: ('세단', 'SUV')
-- 2022 11 01 ~ 2022 11 30 
-- 30일간의 대여 금액이 50만원이상 200만원 미만
