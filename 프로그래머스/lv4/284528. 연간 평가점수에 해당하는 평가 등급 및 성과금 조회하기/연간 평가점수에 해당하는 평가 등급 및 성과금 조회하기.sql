select e.emp_no, e.emp_name, 
case when sum(score)/2  >= 96 then 'S' 
when sum(score)/2  >= 90 then 'A' 
when sum(score)/2 >= 80 then 'B' else 'C' end as grade,
case when sum(score)/2  >= 96 then sal * 0.2  
when sum(score)/2  >= 90 then sal * 0.15  
when sum(score)/2 >= 80 then sal * 0.1 else 0 end as bonus
from hr_employees as e join hr_grade as g on e.emp_no = g.emp_no 
group by e.emp_no
order by 1