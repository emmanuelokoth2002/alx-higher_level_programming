--  lists all the cities of California that can be found in the database hbtn_0d_usa
SET @db_name = 'hbtn_0d_usa';
SELECT id INTO @state_id FROM @db_name.states WHERE name = 'California';
SELECT cities.* FROM @db_name.cities AS cities, @db_name.states AS states
WHERE cities.state_id = states.id AND states.name = 'California'
ORDER BY cities.id ASC;
