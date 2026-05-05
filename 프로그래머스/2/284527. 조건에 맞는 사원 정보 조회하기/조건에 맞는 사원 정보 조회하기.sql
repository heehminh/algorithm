-- 코드를 작성해주세요
with t1 as (
    select emp_no, sum(score) as score
    from hr_grade
    where year = 2022 
    group by emp_no
)
select t1.score, e.emp_no, e.emp_name, e.position, e.email
from hr_employees as e join t1 on e.emp_no = t1.emp_no 
where t1.score = (select max(score) from t1)