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
fig, ax = plt.subplots()
fig, ax = plt.subplots(3,2)
plt.show()
ax.shape  #return result (3,2) 
#add data in the little subplot [0,0]
ax[0,0].plot(seattle_weather["MONTH"], seattle_weather["MLK-PRCP-NORMAL"], color = 'b')
plt.show()
                        
                        


                        
                        
