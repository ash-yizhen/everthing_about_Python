JOING DATA with SQL 
Primary Key: uniquely identify each row in a table
FOREIGN KEYs 
-- INNER JOIN: only returns matching rows
-- LEFT/RIGHT JOIN: All rows from the main table plus matches from the joining table (RIGHT JOIN AND RIGHT JOIN CAN BE INTERCHANGABLE)
-- NULL displays of no match is found
-- Combines queries from the same tabk=le or different tables 
-- UNION: exclude duplicated rows, slower to run 
-- UNION ALL: include duplicated rows, run faster
-- pay attention: select the same number of columns in the same order
-- columns should habe the same data types


SELECT 
  album_id, 
  title,
  album.artist_id, 
  name AS artist_name
FROM album 
INNER JOIN artist ON artist.artist_id = album.artist_id
WHERE album.artist_id = 1; 

SELECT 
  table_A.columnX, 
  table_A.columnY,
  table_B.columnZ, table_C.columnW
FROM table_A
INNER JOIN table_B ON table_B.foreign_key = table_A.primary_key
INNER JOIN table_C ON table_C.foreign_key = table_B.primary_key

--LEFT JOIN: 
--RIGHT JOIN: 

SELECT 
  admitted.patient_ID, 
  admitted,
  discharged
FROM admitted
LEFT JOIN discharged ON discharged.patient.ID = admitted.patient_ID

SELECT 
  admitted.patient_ID, 
  admitted,
  discharged
FROM dischaged
RIGHT JOIN admitted ON admitted.patient_ID = dischaged.patient_ID

----------------------------------------------------------------
-- clear and update tables
-- CRUD: CREATE, READ, UPDATE, DELETE 
-- CREATE: databases, tables or views; users, permissions mad security groups
-- READ: SELECT
-- UPDATE: Amend existing database records
-- DELETE
--INSERT INTO 
--DECLARE yourself: use declare to create variables
-- CREATE temporary table

-- CREATE TABLE (column name, data type, size)
CREATE TABLE test_table(
  test_date date, 
  test_name varchar(20)
  test_int int
)

INSERT INTO table_name (col1, col2, col3)
VALUES 
  ('value1', 'value2', value3)

INSERT INTO table_name (col1, col2, col3)
SELECT 
  column1, 
  column2,
  column3
FROM other_table
WHERE 
 -- conditions apply;
 
UPDATE table
SET 
 column1 = value1,
 column2 = value2
WHERE 
--conditions apply; 
 
DELETE
FROM table
WHERE 
 -- condtions apply

TRUNCATE TABLE table_name.  -- clear all table at once

DECLARE @my_artist varchar(100)
DECLARE @my_album varchar(300)

SET @my_artist = 'AC/DC'
SET @my_album = 'Let There Be Rock'

SELECT -- 
FROM -- 
WHERE artist = @my_artist
AND album = @my_album

SELECT 
  col1,
  col2,
  col3 INTO #my_temp_table
FROM my_existing_tale
WHERE 
  -- conditions 
  
-- Remove tem table
DROP TABLE #my_temp_table 
 




