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

 
