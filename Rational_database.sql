-- CRETAE A NEW TABLE
CREATE TABLE table_name (
  columns_a date_type,
  columns_b data_type,
  columns_c data_type
);

-- Date Type: 
text: character strings of any length 
varchar [(x)]: a maximum of n characters
char [(x)]: a fixed-length strings of n characters
boolean: can only take three states, e.g. TRUE FAKSE NULL 
date, time, timestamp: various format for date and time calculations
numeric: arbitrary precision numbers, e.g. 3.145    numberic(3,2 )  5.54
integer: whole numbers in the range of -2147483648 and +2147483648

-- DELECT TABLES
DROP TABLE table_name; 


-- ADD A COLUMN TO A TABLE
ALTER TABLE table_name
ADD COLUMN column_name date_type; 

-- RENAME COLUMNS 
ALTER TABLE table_name
RENAME COLUMN old_name TO new_name; 

--ALTER DATA TYPE 
ALTER TABLE students
ALTER COLUMN name
TYPE varchar(128);

ALTER TABLE students
ALTER COLUMN average_grade
TYPE integar
USING ROUND (average_grade);

-- SET NOT NULL CONSTRAINTS 
ALTER TABLE students
ALTER COLUMN home_phone
SET NOT NULL; 

--ALTER PRIMARY KEY
ALTER TABLE table_name
ADD CONSTRAINT some_name PRIMARY KEY (column name)

ALTER TABLE students
ALTER COLUMN 
DROP NOT NULL; 

-- DELETE A COLUMN 
ALTER TABLE table_name
DROP COLUMN column_name; 

-- MIGRATE DATA TO TABLES
INSERT INTO organisations
SELECT DISTINCT organisation,
  organisation_sector
FROM university_professors; 

-- INSERT DATA MANUALLY
INSERT INTO table_name (column_a, column_b)
VALUES ("value_a", "value_b"); 

------------------------------------------------------------------------------------------
--BETTER DATA QUALITY WITH DATA CONTRAINTS
-- INTEGRATY CONSTRAINTS
-- 1. Attribute constraints e.g. data types on columns 
-- 2. Key constraints e.g. primary keys
-- 3. Referrential integrity constraints eg. enforced through foreign keys
-- Constraints give the data structures
-- constraints help with consistency, thus data quality 
-- data quality is a business advantage/data science prerequisite
-- enforcing is difficult, but PostgreSQL helps

-- DEALING WITH DATA TYPES (casting)
CREATE TABLE weather (
  temperature interger, 
  wind_spead text);
SELECT temperature * CAST(wind_speed AS integer) AS wind_chill
FROM weather; 

--NOT NULL constraints 
CREATE TABLE students (
  ssn integar not null, 
  lastname cachar(64) not null, 
  home_phone integar,
  office_phoen integar
); 

-- UNIQUE COLUMN 
CREATE TABLE table_name(
clumn_name UNIQUE
);

ALTER TABLE table_name
ADD CONSTRAINT some_name UNIQUE (column_name); 

---------------------------------------------------------------------------------
-- Key and Superkeys
-- Primary key: every table should have primary key, choosen from candidate key
CREATE TABLE products (
  product_no integer UNIQUE NOT NULL, 
  name text, 
  proce numeric
);

CREATE TABLE products (
  product_no integer PRIMARY KEY, 
  name text, 
  price numeric
);

CREATE TABLE example (
  a integer,
  b integer,
  c integer,
  PRIMARY KEY (a,c)
);


-- Surrogate key: artificial primary key
-- Primary should never change throughout the time.
ALTER TABLE cars 
ADD COLUMN id serial PRIMARY KEY;
INSERT INTO cars 
Values ('Volkswagen', 'Blitz', 'black')

ALTER TABLE table_name
ADD COLUMN column_c varchar(256)

UPDATE table_name
SET column_c = CONCAT(column_a, column_b)
ALTER TABLE table_name
ADD CONSTRAINT pk PRIMARY KEY (column c);

----------------------------------------------------------------
--Foreign keys
-- A foreign key points to the primary key of another table
-- domain of foreign key must be euqal to domain of primary key
--- duplicates are allowed and foreign key is not actual key 
ALTER TABLE a 
ADD CONSTRAINT a_fkey FOREIGN KEY (b_id) REFERENCE b (id); 

--HOW TO implement N:M-relationship
-- CRETAE A TABLE 
-- ADD FOREIGN KEYS FOR EVERY CONNECTED TABLE 
-- ADD ADDTIONAL ATTRIBUTES 

--REFERENCETIAL INTEGRITY 
-- A record in table A can not reference to record in table b that not exist







