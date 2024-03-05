-- This script lists all the cities of California that can be found
-- in the database hbtn_0d_usa.

SELECT cities.id, cities.name
  FROM cities AS c, states AS s
 WHERE c.state_id = California
   AND c.state_id = s.state_id
