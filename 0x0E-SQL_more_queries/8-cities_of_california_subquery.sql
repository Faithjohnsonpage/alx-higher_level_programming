-- This script lists all the cities of California that can be found
-- in the database hbtn_0d_usa.

SELECT cities.id, cities.name
  FROM cities AS c
 WHERE c.state_id = 1
