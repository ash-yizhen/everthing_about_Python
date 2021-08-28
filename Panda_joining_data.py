#Inner Join: only return rows with matching values
____=dataframe1.merge(dataframe2, on='column')
____=dataframe1.merge(dataframe2, on='column', suffixes = ('_ward', '_cen')) #differentiate columns with suffxies from 2 tables

#One-to-one and one-to-many
#One to one:Every row in thr left is related to only one row in the right 
#One-to-many: Every row in thr left is related to many rows in the right 
df1.merge(df2, on='')\
  .merge(df3, on='')\
  .merge(df4, on='')

#Left Join -- returns all the rows from left table and only rows from right table that key collumns match 
df3 = df1.merge(df1, on ='id', how='left')

# Other join
#Right join
df3 = df1.merge(df2, how='right', left_on = '___', right_on='____') #left_on and right_on refers to which keys merge in from which tables
#Outer join -- every row returns from both tables
df3 = df1.merge(df2, on ='____', how='outer', suffixes=('____', '_____'))

------------------------------------------------------------------------------------------------
#Merging a table to itself
df2 = df1.merge(df1, left_on ='____', right_on='____', suffixes=('____', '_____'))
#When to merge at table to itself
#- hierarchical relationships
#- Sequential relationships
#- Graph data

#Merge on indexes
df1 = pd.read_csv('_____', index_col=['____', '____'])
df2 = pd.read_csv('_____', index_col=['____', '____'])
df3 = df1.merge(df2, left_on='__', left_index= True, right_on='____', right_index=True)

#Filtering joins
#Difference between filtering joins and mutating joins
#Mutatiing joins: conbines data from two tables based on matching observations in both tables
#Filtering joins: Filter observations from table based on whether or not they maych an observation in another table 

#Semi-join: returns the intersction, similar to an inner join; returns only columns from the left table and not the right; no duplicates
#Step 1: inner join - returns values both tables have
genres_tracks=genres.merge(top_tracks, on='gid')
#step 2: 
genres['grid'].isin(genres_tracks['grid']) #returns True/False
#step 3:
top_genres=genres[enres['grid'].isin(genres_tracks['grid'])] #returns values

#Anti-join: retuns the left table, excluding the intersection; returns only columns from the left table and not the right 
#step1: 
genres_tracks=genres.merge(top_tracks, on='gid', how ='left', indicator=True)
#Step2: 
gid_list=genres_tracks.loc[genres_tracks['_merge']=='left_only', 'gid'] #choose the rows that only shows in left table 
#Step 3: 
non_top_genres=genres[genres['gid'].isin(gid_list)]]

-------------------------------------------------------------------------------------------------
#concatenation: link together in a chain or series
#concatenate two tables vertically 
#3 different tables; same column names; table variable names: inv_jan, inv_feb, inv_mar
pd.concat([inv_jan, inv_feb, inv_mar], ignore_index=True) #to make sure index is continuing
pd.concat([inv_jan, inv_feb, inv_mar], ignore_index=False, keys=['jan', 'feb', 'mar']) #make sure there will be multi indexes: with lable: jan, feb, mar

#Concat table with different cloumn names
pd.concat([inv_jan, inv_feb], sort=True) #include all columns from 2 tables
pd.concat([inv_jan, inv_feb], join='inner')
#.append() method: simplified version of the .concat() method; support ingore_index and sort argurments; DOES not support keys and join: join=outer
inv_jan.append([inv_feb, inv_mar], ignore_index=True, sort=True)

#Verify integrity
#when concatenating data: duplicate records possibly unintentionally introduced
df1.merge(df2, on='__', validate='one_to_one') #if there is error, that means it is not one to one merge 
df3.merge(df3, on='___', validate='one_to_many') #if no error is raised that means it is one to mant merge

#varifying concatenations
.concat(verfify_integrity = False) #check whether the new concatenated index contains duplicates; default calue is False

pd.concat([inv_feb, inv_mar], verify_integrity =True) #retrun calues when there is overlapping values 
pd.concat([inv_feb, inv_mar], verify_integrity =False) #returns table with duplicated values

------------------------------------------------------------------------------------
#merge_ordered() method: 
#realtionship between .merge() & .merge_ordered()
#both can do on, left_on, right_on 
#both can do left join, right join, inner join and outer join. .merge() default join is inner join, .merge_ordered() default join is outer
#both support suffixes
#calling .merge(): df1.merge(df2); calling .merge_ordered: pd.merge_ordered(df1, df2)
import pandas as pd
pd.merge_ordered(df1, df2, on='__', suffixes=('___', '____'))
#forward fill: filling missing values with the previous value
pd.merge_ordered(df1, df2, on='__', suffixes=('___', '____'), fill_method='ffill')
#when to use merge_ordered() method:
#- ordered data/time series
#- filling in missing values
-------------------------------------------------------------------------------------
#merge_asof()
#-similar as merge_order() left join 
#-match on the neareast key column and not exact matches 
#-merged on columns must be sorted
# Merge value is the closest value in the right table that is still less than or equal to the table from the left table
pd.merge_asof(df1, df2, on='date_time', suffixes=('_ ___', '_ ____'))
pd.merge_asof(df1, df2, on='date_time', suffixes=('_ ___', '_ ____'), direction='forward') #set the nearest row in the right table as forward/backwrd/nearest
#When to use it
# - DAta sampled from a process 
# - developing a training set (no data leakage)

---------------------------------------------------------------------------------------
#select data: .query()
#input string used to determine what rows are returned 
#input string similar to statement after WHERE clause in SQL statement
df.query('___ and ____' )
df.query('___ or ____')
stock_long.query('stock =="disney" or (stock=="nike" and close<90)')

-----------------------------------------------------------------------------------------
#reshape data: .melt(): make a computer-friendly format
social_fin_tall=socail_fin.melt(id_vars=['financial', 'company']) #id-vars are the columns you dont want to change
social_fin_tall=socail_fin.melt(id_vars=['financial', 'company'], value_vars=['2018', '2017']) #value_vars to unpivot columns
social_fin_tall=socail_fin.melt(id_vars=['financial', 'company'], value_vars=['2018', '2017'], var_name=['year'], value_name='dollars') #rename columns 







 









 
