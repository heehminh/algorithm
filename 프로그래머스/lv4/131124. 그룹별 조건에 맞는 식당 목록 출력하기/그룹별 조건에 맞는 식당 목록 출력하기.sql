select m.member_name, r.review_text, date_format(r.review_date, '%Y-%m-%d') as review_date
from member_profile as m join rest_review as r on m.member_id = r.member_id
where m.member_id = (
    select member_id
    from rest_review
    group by member_id
    order by count(*) desc
    limit 1
)
order by r.review_date, r.review_text