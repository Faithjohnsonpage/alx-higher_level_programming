-- This script lists all records of the table second_table
-- of the database hbtn_0c_0.
-- Rows without a name value are not listed.


SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
