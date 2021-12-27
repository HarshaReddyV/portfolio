SELECT DISTINCT name FROM people,movies,stars WHERE movies.year = 2004 AND people.id = stars.person_id AND stars.person_id = movies.id ORDER BY (birth);
