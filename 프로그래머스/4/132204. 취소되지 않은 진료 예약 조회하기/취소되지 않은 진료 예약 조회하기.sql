-- 코드를 입력하세요
SELECT a.APNT_NO, p.pt_name, p.pt_no, a.mcdp_cd, d.dr_name, a.apnt_ymd
from APPOINTMENT as a join PATIENT as p on a.pt_no = p.pt_no
join DOCTOR as d on a.MDDR_ID = d.dr_id
where a.APNT_CNCL_YN = 'N' 
and date_format(a.apnt_ymd, '%Y-%m-%d') = '2022-04-13'
and a.mcdp_cd = 'CS'
order by a.APNT_YMD 