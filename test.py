import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

health_data = pd.read_csv("data.csv", header=0, sep=",")

print(health_data.head())
print(health_data)

# data cleaning
# remove the NaNs. axis=0 means that we want to remove all rows that have a NaN value
health_data.dropna(axis=0, inplace = True)

print(health_data.info())     #list data types
print(health_data.describe()) #analyze data


# linear function
 

health_data.plot(x="Average_Pulse", y="Calorie_Burnage", kind="line")
# health_data.plot(x="Max_Pulse" ,y="Calorie_Burnage", kind="line")
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.show()


#Mathematically, Slope is Defined as:
#Slope = f(x2) - f(x1) / x2-x1
#f(x2) = Second observation of Calorie_Burnage = 260
#f(x1) = First observation of Calorie_Burnage = 240
#x2 = Second observation of Average_Pulse = 90
#x1 = First observation of Average_Pulse = 80

def slope(x1, y1, x2, y2):
  s = (y2-y1)/(x2-x1)
  return s

print (slope(80,240,90,260))

# The intercept is the value of y, when x = 0.
# intercept is 80.



x = health_data["Average_Pulse"]
y = health_data["Calorie_Burnage"]
slope_intercept = np.polyfit(x,y,1)
print(slope_intercept)

# standard deviation
print("######## Standard Deviation #######")
std = np.std(health_data)
print(std)

# Coefficient of Variation = Standard Deviation / Mean
print("######## Coefficient of Variation #######")
cv = np.std(health_data) / np.mean(health_data)
print(cv)

# Variance of Full Data Set 
print("######## Variance #######")
var = np.var(health_data)     # var = std * std
print(var)
