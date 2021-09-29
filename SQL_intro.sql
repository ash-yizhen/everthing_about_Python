SQL Server is rational database system developed by Microsoft
T-SQL: Transact SQL - Microsoft's implementation of SQL, with addtional functionality
NULL is used to highlight missing data/filling gaps

Key word: 
SELECT
FROM 

SELECT TOP(5) artist
FROM artists;

SELECT TOP(5) PERCENT artist
FROM artists;

SELECT DISTINCT nerc_region.    #return unique combination of values
FROM grid;

SELECT *
FROM grid;     #return all the rows and columns in a table

SELECT demand_loss_mw AS lost_demand
FROM grid;      #re-name collumns

---------------------------------------------------------------
Ordering and filtering
Select TOP(10) prod_id, year_intro
FROM products
ORDER BY year_intro, product_id. #order in ascending order

Select TOP(10) prod_id, year_intro
FROM products
ORDER BY year_intro DESC, product_id. #order in descending order

SELECT customer_id, total
FROM invoice
WHERE total > 15; 

WHERE total <> 15;    #testing for non-equality 
WHERE total BETWEEN 20 AND 30; 
WHERE total NOT BETWEEN 20 AND 30; 

SELECT 
  TOP(6) total, 
  billing_state
FROM invoice
WHERE billing_state IS NULL;

WHERE billing_state IS NOT NULL;

-------------------------------------------------------
AND OR command and wrappong conditions
SELECT song 
FROM songlist 
WHERE 
  artist = 'Green Day'
  AND (
    release_year = 1994 
    OR release_year >2000
  );
  
SELECT song, artist
FROM songlist
WHERE 
  artist IN ('Van Halen', 'ZZ Top')
ORDERED BY song; 

#Search for text fields 
SELECT song 
FROM songlist
WHERE song LIKE 'a%';  #select fileds include 'a'

-------------------------------------------------------------
Aggregating date: how to use T-SQL 
SUM() - Calculate the total amount of a column value with SUM() used on specific columns
COUNT() - Calculate the number of values
MIN()
MAX()
AVG()

SELECT
  SUM(affected_customers) AS total_affected.  #provide a name for your results
  SUM(demand_loss_mw) AS total_loss
FROM grid; 

SELECT 
  COUNT(DISTINCT affected_customers) AS unique_count_affected
FROM grid; 

SELECT 
  MIN(affected_customers) AS min_count_affected
FROM grid; 

SELECT 
  MAX(affected_customers) AS max_count_affected
FROM grid;

SELECT 
  AVG(affected_customers) AS avg_count_affected
FROM grid;

------------------------------------------------------------
Strings and texts
LEN() -- return the length of the strings
LEFT() -- extract a number of characters from the beginning of a string
RIGHT() -- extract a number of characters from the end of a string
CHARINDEX() -- help extract strings with specific characters
SUBSTRING() -- parameters: column name, the number of the character to start from, the number of characters to extract 
REPLACE() -- replace the character with another character

SELECT 
  description, 
  LEN(description) AS description_length
FROM grid;

SELECT 
  description
  LEFT(description, 20) AS first_20_left
FROM grid; 

SELECT 
  description, 
  RIGHT(description, 20) AS last_20
FROM grid; 

SELECT 
  CHARINDEX ('_', url) AS char_location        --returns location of the character
  url
FROM courses; 

SELECT 
  SUBSTRING(url, 12, 12) AS target_section
  url
FROM courses; 

SELECT 
   TOP(5) REPLACE(url, '_', '-') AS replace_with_hyphen
FROM courses; 

-----------------------------------------------------------------------
GROUP BY and HAVING 
-- GROUP BY: splits the data up into combinations of one or more vcalues
-- WHERE: filters on row values 
-- HAVING: appears agter the GROUP BY clause and filters on groups or aggregates (to be used after GROUP BY)

SELECT 
  SUM(demand_loss_mw) AS lost_demand
  description
FROM grid
WHERE 
  description LIKE '%storm'
  AND demand_loss_mw IS NOT NULL
GROUP BY description             --order based on description collumn
HAVING SUM(demand_loss_mw) > 1000; 






 
