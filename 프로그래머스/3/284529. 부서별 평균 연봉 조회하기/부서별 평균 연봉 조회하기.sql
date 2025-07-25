-- 코드를 작성해주세요
select d.dept_id, d.dept_name_en, round(sum(e.sal) / count(d.dept_id),0) as avg_sal
from hr_department as d join hr_employees as e on d.dept_id = e.dept_id
group by d.dept_id
order by avg_sal desc