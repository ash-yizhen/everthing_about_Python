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








 
