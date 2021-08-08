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
____.groupby("____")["_____"].mean()
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

