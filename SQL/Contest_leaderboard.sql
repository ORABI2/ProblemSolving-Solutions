select
    h.hacker_id, h.name, sum(score)
from hackers h join
    (
      select hacker_id, max(score) score from submissions group by challenge_id, hacker_id
    ) as s
    on h.hacker_id = s.hacker_id
group by h.hacker_id, h.name
having sum(s.score) > 0
order by sum(s.score) desc, h.hacker_id
