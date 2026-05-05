select d.dept_id, d.dept_name_en, round(avg(e.sal)) as avg_sal
from HR_DEPARTMENT as d join HR_EMPLOYEES as e on d.dept_id = e.dept_id
group by d.dept_id 
order by avg_sal desc