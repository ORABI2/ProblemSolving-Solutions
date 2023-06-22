select
    h.hacker_id , h.name
from submissions s
    join challenges cha 
        on s.challenge_id = cha.challenge_id
    join difficulty d 
        on cha.difficulty_level = d.difficulty_level
    join hackers h
        on h.hacker_id = s.hacker_id
where s.score = d.score 
group by s.hacker_id , h.name
having count(s.hacker_id) > 1
order by count(s.hacker_id) desc, s.hacker_id
