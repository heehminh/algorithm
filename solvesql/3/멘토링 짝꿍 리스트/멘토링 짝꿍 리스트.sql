select e.employee_id as mentee_id, e.name as mentee_name, o.employee_id as mentor_id, o.name as mentor_name
from (
  select employee_id, name, department
  from employees
  where join_date > date_sub('2021-12-31', interval 3 month) and join_date <= '2021-12-31'
) as e left join
( 
  select employee_id, name, department
  from employees
  where join_date <= date_sub('2021-12-31', interval 2 year)
) as o on e.department <> o.department
order by mentee_id, mentor_id;