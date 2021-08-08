#Working with Pivot Tables: Calculate group summary statistics
___.pivot_table(values=_____, index= _____, aggfunc = _____)
#pivot on two variables/more functions: min, max, mean, median (mean and median are numpy functions -- np.mean, np.median; import numpy as np needs to be done)
____.pivot_table(values=____, index=____, columns =_____, aggfunc = [____,____,...])
#pivot filling missing values
____.pivot_table(values=____, index=____, columns =_____, fill_value=0)
#Summing with Pivot
____.pivot_table(values=____, index=____, columns =_____, fill_value=0, margins= True)

#GRoup by
____.groupby("____")["_____"].mean()
#When group by two variables
____.groupby(["____", "____"])["______"].mean()
