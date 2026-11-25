select m.member_name, r.review_text, date_format(r.review_date, '%Y-%m-%d') as review_date 
from member_profile as m join rest_review as r on m.member_id = r.member_id 
join (
    select member_id 
    from rest_review
    group by member_id
    having count(*) = (
        select max(cnt) 
        from (
            select member_id, count(*) as cnt 
            from rest_review
            group by member_id 
        ) as tmp1
    )
) as tmp2 on m.member_id = tmp2.member_id 
order by review_date, review_text