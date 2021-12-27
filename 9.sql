SELECT DISTINCT name FROM people,movies WHERE year = 2004 AND people.id = movies.id ORDER BY (birth);
