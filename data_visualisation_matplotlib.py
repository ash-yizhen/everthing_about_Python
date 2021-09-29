#BAr chart shows the categorical data 
#Histgram shows the distribution of the data
#Error bars indicates the dsitribution of the data in one number, such as the standard deviation of the values
#Box plot shows the standard deviation and outliers

import matplotlib.pyplot as plt 
fig, ax = plt.subplots() #fig object is container that holds everything you see on page; ax is part of the page hold the data
plt.show()

ax.plot(seattle_weather["MONTH", seattle_weather["MLY-TAVG-NORMAL"])
plt.show()

#Example
fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()

#Customise your plot   
#marker - change the marker in the plot
#linestyle -- change the line style in the plot
#color -- changet the line of the color
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"], marker = "v", linestyle="--", color="r")
#maker is v shape, line is dashed, line color is red
ax.set_xlabel("Time(months)")
ax.set_ylabel("Average temperature (Fahrenheit degrees)")                 
ax.set_title("Weather in Seattle")

#adding data
#small multiples -- arrange on the page as a grid with rows and columns
fig, ax = plt.subplots(). #returns 1 small subplot
fig, ax = plt.subplots(3,2) #returns 3 rows and 2 collumns of small subplots
plt.show()
ax.shape  #return result (3,2) 
#add data in the little subplot [0,0]
ax[0,0].plot(seattle_weather["MONTH"], seattle_weather["MLK-PRCP-NORMAL"], color = 'b')
plt.show()

fig, ax = plt.subplots(2,1)
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color ='b')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"], linestyle='--', color ='b')
ax[0].plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-75PCTL"], linestyle='--', color ='b')
ax[1].plot(austin_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color ='r')
ax[1].plot(austin_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"], linestyle='--', color ='r')
ax[1].plot(austin_weather["MONTH"], seattle_weather["MLY-PRCP-75PCTL"], linestyle='--', color ='r')
ax[0].set_ystyle("Precipitation (inches)")
ax[1].set_ystyle("Precipitation (inches)")                        
fig, ax = plt.subplots(2,1, sharey = True)   #to make sure that all the subplots have the same range of y-axis values
                        
#plotting time-series data
#slicing date data
sixties = climate_change["1960-01-01":"1969-12-31"]  #slicing dat/zoom in dateax.plot 
fig, ax = plt.subplots
ax.plot(sixties.index, sixties['co2'])
ax.set_xlable('Time')
ax.set_ylable('CO2(ppm)')                        
plt.show()
                        
#plotting wo time-series together 
fig, ax = plt.subplots()
ax.plot(climate_change.index, climate_change["co2"], color = 'blue')
ax.set_xlabel('Time')
ax.set_ylabel('CO2 (ppm)', color = 'blue') 
ax.tick_params('y', colors = 'blue')       #modifying the prarameters of the y-axis ticks and tick labels
ax2 = ax.twinx()                           #this means the two axes share the same x-axis, but the y-axes are separate
ax2.plot(climate_change.index, climate_change["relative_temp"], color = 'red')
ax2.set_ylabel('Relative temperature (Celsius)', color = 'red')
ax2.tick_params('y', colors = 'red')       #modifying the prarameters of the y-axis ticks and tick labels
plt.show()

#a function that plots time-series
def plot_timeseries(axes, x, y, color, xlabel, ylabel)
  axes.plot(x, y, color = color)
  axes.set_xlabel(xlabel)
  axes.set_ylabel(ylabel, color = color)
  axes.tick_params('y', colors = color)        
                        
fig, ax = plot.subplots()
plot_timeseries(ax, climate_change.index, climate_chnage['co2'], 'blue', 'Time', 'CO2 (ppm)')

#Annotating time-series data
ax2.annotate(">1 degree", xy =(pd.TimeStamp("2015-10-06"), 1), xytext=(pd.TimeStamp('2008-10-06'), -0.2), arrowprops = {"arrowstyle" : "->", "color": "gray"})
                        
-----------------------------------------------------------
#Quantative comparsion: bar charts
                        
fig,ax = plt.subplots
ax.bar(medals.index, medals["Gold"], label="Gold")
ax.bar(madels.index, medals["Silver"], bottom=medals["Gold"], label="Silver") 
ax.bar(madels.index, medals["Bronze"], bottom=medals["Gold"] + meadls["Silver"], label="Bronze")
ax.set_xticklabels(medals.index, rotation = 90)                   #roate x-axis label to be able to display completely
ax.set_ylabel("Number of medals")                            
ax.legend()                                                       #display different colors for different medals
plt.show()
                        
ax.hist(men_rowing["Height], label = "Rowing", bins=[150, 160. 170, 180, 190, 200. 210], histtype="step")
ax.hist(men_gymnastic["Height], label = "Gymnastics", bins=[150, 160. 170, 180, 190, 200. 210], histtype="step")   # histtype = "step" to get rid of the innerline to make it look like steos
ax.set_xlabel("Height (cm)")                 
ax.set_ylabel("# of observations")
ax.legend()
plt.show()
                      
fig, ax =plt.subplots()
ax.boxlot([mens_rowing["Height"], mens_gymnastics["Height"]])
ax.set_xticklabels(["Rowing", "Gymnastics"])
 ax.set_ylabel("Height (cm)")
plt.show()
 
