--Date Type
varchar(n)
INT
DDECIMAL(p,s) / NUMERIC(p,s) --p: total number of the decial digits; s: number of decimal digits that will be sorted to the right of the decimal points

--Decalring variables in T-SQL 
DECLARE @variablename date_type

-- Assignin values to variables
DECLARE @Snack VARCHAR(10)         -- Declare the variable
SET @Snack = 'Cookies'             -- Use SET a value to the variable
SELECT @Snack                      -- Show the value


-- CASE statement: CASE, WHEN, THEN, ELSE(optional), END
--Create a new collumn called NewContinent and the value is Eurasia if the corresponding row in Continent is either Europe or Asia, otherwise continent doesn'y change
SELECT Continent, 
CASE WHEN Continent = 'Europe' Or Continent = 'Asia' THEN 'Eurasia'
  ELSE Continent
  END AS NewContinent
FROM EconomicIndicators;

-- DATEPART: is sued to determine what part of the date you want to calculate. some of common abbreviations are: DD MM YY HH 
-- DATEADD(DATEPART, number, date): Add or substract datetime values, always returns a date
----DATEPART: unit of measurement 
----number: An integar value to add.   #can use negative number to see date in the past
----date: a datetie value

-- DATEDIFF(datepart, startdate, endate): Obtain the difference between two datetime values, always return a number
----datepart: unit of measurement (DD, MM etc.)
----startdate: the starting date value
----enddate: an ending datetime value

--Rounding and Truncating numbers
ROUND(number, length)
-- number: the number to be rounded 
--length: the number of places the number should be rounded
----if the length specified is negative the number is on left side of the decimal, the whole numbers are rounded 
----if the length specified is positive, the number on the right side of the decimal, the decimal numbers are rounde d 

--Truncating numbers instead of rounding down
--truncate 17.85 -- 17.      round 17.85 -- 18
--ROUND() function can be used to truncate values when you specify the third argument 
ROUND(number, length, _____)       -- set the thrid arguement to a non-zero number 
**Truncating just cuts all numbers off after the specified digit

ROUND(Cost, 0, 1). -- Truncate cost values to the nearest whole value

--Absolute value: retuen non-negative values
ABS(number)

--Square and square roots in T-SQL
SQRT(number)  -- suqare root 
SQUARE(number)  --square 

--Logs function: returns the natural logarithm
LOG(number, Base)    if base is not set its 2.718281828

--WHILE Loops: Modifying data by using WHILE Loops
--WHILE evaluates a true or false cindition 
-- After the WHILE, there should be a line with the keyword BEGIN 
-- Next invlude code to run until the condition in the WHILE loop is true
-- After the code add END 
--BREAK will cause an exit out of the loop 
--CONTINUE will cause the loop to continue

DECLARE @ctr INT 
SET @ctr = 1
WHILE @ctr <10
  BEGIN 
    SET @ctr = @ctr + 1
  END 
SELECT @ctr

SET @ctr = 1
WHILE @ctr <10
  BEGIN 
    SET @ctr = @ctr + 1
    IF @ctr =4
      BREAK
  END
SELECT @ctr

-- Derived tabels: query acting as a table and are commonly used ot do aggregations in T-SQL
SELECT * 
FROM Kidney a
JOIN(SELECT age, MAX(BloodPressure) AS MaxBloodPressure FROM Kidney GROUP BY Age) b
ON a.BloodPressure = b.MaxBloodPressure
AND a.Age = b.Age;

--CET: Common Table expressions: another type od derived table
--CETs can be used multiple times in a query and are defined like a table and can be used multiple times
WITH CTEName (Col1, Col2)
AS 
(
  SELECT COl1, COl2 
  FROM TableName
)

-- Windowing Function 
-- Using windowing function, data within a table is proccesed as a group, allowing each group to be evaluated separately
OVER(PARTITION BY SalesYear ORDERED BY SalesYear)
-- Ceate window with OVER 
-- PARTITION BY creates the frame.  -- each window is based on the value after PARTITION BY, then they are separated frames
-- ORDER BY to arrange results

SELECT Salesperson, SalesYear, CurrentQuota,
  SUM(CurrentQuota)
  OVER (PARTITION BY SalesYear) AS YearlyTotal, 
  ModifiedDate AS ModDate
FROM SaleGoal

--Common Windowing functions
FIRST_VALUE()
LAST_VALUE()

-- Select the columns
SELECT SalesPerson, SalesYear, CurrentQuota, 
-- First value from every window
  FIRST_VALUE(CurrentQuota) 
  OVER (PARTITIONBY SalesYear ORDERBY ModifiedDate) AS StartQuota, 
  -- Last value from every window 
  LAST_VALUE(CurrentQuota) 
  OVER (PARTITIONBY SalesYear ORDERBY ModifiedDate) AS EndQuota,       
  ModifiedDate as ModDate
FROM SaleGoal

-- LEAD(): Create a window function to get the calues from the next row
SELECT SalesPerson, SalesYear, CurrentQuota, 
-- Create a window function to get the values from the next row
  LEAD(CurrentQuota) 
  OVER (PARTITIONBY SalesYear ORDERBY ModifiedDate) AS NextQuota,        
  ModifiedDate AS ModDate
FROM SaleGoal

--LAG(): query the value from the previous row
SELECT SalesPerson, SalesYear, CurrentQuota, 
-- Create a window function to get the values from the previous row       
  LAG(CurrentQuota) 
  OVER (PARTITIONBY SalesYear ORDERBY ModifiedDate) AS PreviousQuota,        
  ModifiedDate AS ModDate
FROM SaleGoal

--Increasing window complexity 
--Adding row numbers in T-SQL 
SELECT SalesPerson, SalesYear, CurrentQuota, 
  ROW_NUMBER() 
  OVER (PARTITIONBY SalesPerson ORDERBY SalesYear) AS QuotabySalesPerson       
FROM SaleGoal

--Using Windows for statistical functions
--STDEV()
SELECT SalesPerson, SalesYear, CurrentQuota,  
  STDEV(CurrentQuota) 
  OVER (PARTITIONBY SalesYear ORDERBY SalesYear) AS StDev,        -- Calculating the standard deviation for each partition 
  ModifiedDate AS ModDate
FROM SaleGoal

SELECT SalesPerson, SalesYear, CurrentQuota,  
  STDEV(CurrentQuota) 
  OVER () AS StDev,        -- Calculating the standard deviation for the entire table
  ModifiedDate AS ModDate
FROM SaleGoal

-- Calculate Mode: the most appears values
--USE CTE
WITH QuotaCount AS (
SELECT SalesPerson, SalesYear, CurrentQuota,        
  ROW_NUMBER() 
  OVER (PARTITIONBY CurrentQuota ORDERBY CurrentQuota) AS QuotaList
FROM SaleGoal 
)

SELECT CurrentQuota, QuotaList AS Mode
FROM QuotaCount 
WHERE QuotaList IN (SELECTMAX(QuotaList) FROM QuotaCount)

