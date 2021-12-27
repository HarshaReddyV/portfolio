SELECT Avg(energy) FROM songs WHERE id=(SELECT id FROM artists WHERE name LIKE "%drake%");
