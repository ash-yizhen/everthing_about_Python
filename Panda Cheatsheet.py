#Panada is a powerful tool to deal with tableau data
#Transforming dataFrames
____.head() #first few rows of the table
____.info() #name of columns and data contained 
____.shape() #number of row and number of columns 
____.discribe() #statistic summaries of the columns such as count, mean, std, min, max overview of table 
____.vaues  #contains datas 
____.columns #contained columns
____.index #row numbers 
#sorting and subsetting
____.sort_values("columnname", ascending = True/False)
#more than one variables 
____.sort_values(["____", "____"], ascending =[____, _____])
#subsetting
____.["____"]
____.[["___", "____"]]
dogs[dogs["height_cm">50]]
dogs[dogs["breed"]=="Labrador"]
#isin method
_____=dogs["color"].isin(["Black", "Brown"]). #work the same as a filter
#new columns
____["newcollumnname"] = ____["column"]/100

#Summary statistics
____["____"].mean
____["____"].max
____["____"].min
____["____"].var
____["____"].median
____["____"].mode
____["____"].sum
____["____"].quantile
#summary on more than one columns
____[["____", "____"]].mean
#agg() functions more than one element
____[["____", "____"]].agg([____, ____])
#cumulative sum and other statistics 
____.["____"].cumsum()
____.["____"].cummin()
____.["____"].cummax()
____.["____"].cumprod()


#Counting: Dropping dupliacted elements, subset is the column name to remove duplicates from
____.drop_duplicates(subset ="_____")
#Droppinh duplicated pairs, only remove duplicates when two columns elements are the same
____.drop_duplicates(subset = ["____", "____"])
#counting the column element 
____["_____"].value_counts()
#sort the elements from bigger counts to smalled counts
____["_____"].value_counts(sort = True)
#Normalise arguements can turn the counts to proportions
____["_____"].value_counts(normalize = True)

#GRoup summary statistics
____.groupby("groupbyelement")["valuelelment"].mean() 
#When group by multiple variables/multiple columns
____.groupby(["____", "____"])[["______","_____",...]].mean()
#multiple grouped summaries
____.groupby("____")["____"].aggfun([min, max, sum])

#Working with Pivot Tables: Calculate group summary statistics
___.pivot_table(values=_____, index= _____, aggfunc = _____)
#pivot on two variables/more functions: min, max, mean, median (mean and median are numpy functions -- np.mean, np.median; import numpy as np needs to be done)
____.pivot_table(values=____, index=____, columns =_____, aggfunc = [____,____,...])
#pivot filling missing values
____.pivot_table(values=____, index=____, columns =_____, fill_value=0)
#Summing with Pivot
____.pivot_table(values=____, index=____, columns =_____, fill_value=0, margins= True)

------------------------------------------------------------------------------------------------------------
#Slicing and Indexing dataframe
#set a column as index & multiple indexes
____.set_index("____")
____.set_index(["____", "____"]) #multi-level indexes, hierarchical indexes
#undo/remove the index 
____.reset_index()
#discard the index
____.reset_index(drop = True)
#index makes subsetting simpler, the elements in the brackets are from index column
____.loc[["____", "____"]] #same as ____[____["____"].isin(["____", "____"])]
#subset multi-level indexes data frame
# subset outer level with a lsit
____.loc[["outer index1", "outer index2"]]
#subset inmer levels with a list of tuples 
____.loc[[("outer index1", "inner index1"), ("outer index2", "inner index2")]]
#sort index
____.sort_index()
____.sort_index(level=["index colmun1", "index column2"], ascending = [True, False])

---------------------------------------------------------------------------------------------------------------
#Slicing and subsetting with loc. and iloc
#1. Sort index before slicing 
____.set_index(["____", "____"]).sort_index()
#2. Slicing outer index level
____.loc["____":"____"]   #the final value is included 
#3. Slicing inner index level 
____.loc[("outer1", "inner1"):("outer2", "inner2")]
#Slicing columns 
____.loc[:, "____":"____"]
#Slicing both rows and colums
____.loc[("outer1", "inner1"):("outer2", "inner2"), "____":"____"]
____.iloc[2:5, 1:4]
----------------------------------------------------------------------------------------------------------------
#Pivot Tables
____.pivot_table("____", index = "____", columns = "____") 
____.mean(axis="____").  #calculate mean across "____" could be "index" or "columns"#
____.mean() / ____.mean(axis="columns")

---------------------------------------------------------------------------------------------------------------
#Visualise your data 
#import the pack
import matplotlib.pyplot as plt
____["____"].hist()  #x-axis represent the elemenst in the brackets. the y-axis represent the number of the corresponding elements 
plt.show()
#adjuts the number of bars using bin arguement
_____["_____"].hist(bins=20)
#Bar plot example: 
avg_weight_by_weight = dog_pack.groupby("breed")["weight_kg"].mean()
print(avg_weight_by_weight)
avg_weight_by_weight.plot(kind ="bar")  #show the plot with bar kind
plt.show() 
avg_weight_by_weight.plot(kind="bar", title="Mean weight by Dog Breed") #add title arguement
plt.show()
#Line plot example:
sully.head()  #show summary of the dataframe/table first few rows of the data
sully.plot(x="date", y="weight_kg", kind="line") #more arguements
plot.show()
sully.plot(x="date", y="weight_kg", kind="line", rot=45) #rotate the x-axis with 45 degrees so it is easy to read 
#Scatter plot
_____.plot(x="____", y="_____", kind="scatter")
plt.show()
#layer plot example
dog_pack[dog_pack["sex"]=="F"]["height_cm"].hist(alpha=0.7) #alpha arguement is to make the bar chart translucent: 0 - completely transparent, 1 - completely solid
dog_pack[dog_pack["sex"]=="M"]["height_cm"].hist(alpha=0.7) #layering Male on top of the Female
plt.legend(["F", "M"]).        #Pass lables to distinguish two categories
plt.show()
-----------------------------------------------------------------------------------------------------------

#handle data with missing values
#1. Detecting missing values
____.isna(). #detect any missing data from the whole data frame -- show as True and False, True means there is missing data, False means no missing data
____.isna().any() #reflect each column for each variable tells us if there is any missing value in that column
____.isna().sum() #counting the missing values 
#visualise missing data by plot 
import matplotlib.pyplot as plt
____.isna().sum().plot(kind="bar')
plt.show()
#2. remove data containes missing values
____.dropna()
#replace missing values with another value such as 0
____.fillna(0)

-------------------------------------------------------------------------------------------------------------
#create data frame from scratch 
#create data frame from list of dictionary by rows 
list_of_dicts =[
  {"key1": "value1", "key2": "values2", "key3":"value3","key4":"value4"}.    #key = column name; value = list of column values
  {"key1": "value1", "key2": "values2", "key3":"value3","key4":"value4"}
]
dataframename = pd.DataFrame(list_of_dicts)
#create data frame from dic of list by columns
dic_of_lists = {
  "key1": ["value1", "value2"...],
  "key2": ["value1", "value2"...],
  "key3": ["value1", "value2"...],
  ...
}
dataframename=pd.DataFrame(dic_of_lists)
---------------------------------------------------------------------------------------------------------------
#Read and write CSVs
#CSV = Comma-separated values, deisgned for dataFrame-like data
import pandas as pd
_____=pd.read_csv("____")
#share and convert updated csv file 
____.to_csv("_____")

                
