-- List All Cities
USE hbtn_0d_usa;
SELECT cities.id, cities.name, states.name
FROM @db_name.cities AS cities, @db_name.states AS states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
