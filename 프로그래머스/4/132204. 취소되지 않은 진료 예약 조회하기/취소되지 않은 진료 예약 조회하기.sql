select a.apnt_no, p.pt_name, p.pt_no, a.mcdp_cd, d.dr_name, a.apnt_ymd
from patient as p join appointment as a on p.pt_no = a.pt_no join doctor as d on a.mddr_id = d.dr_id 
where d.mcdp_cd = 'CS' and a.apnt_ymd like '2022-04-13%' and a.apnt_cncl_yn = 'N'
order by a.apnt_ymd;