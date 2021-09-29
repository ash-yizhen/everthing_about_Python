JOING DATA with SQL 
Primary Key: uniquely identify each row in a table
FOREIGN KEYs 
-- INNER JOIN: only returns matching rows
-- LEFT/RIGHT JOIN: All rows from the main table plus matches from the joining table (RIGHT JOIN AND RIGHT JOIN CAN BE INTERCHANGABLE)
-- NULL displays of no match is found

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





