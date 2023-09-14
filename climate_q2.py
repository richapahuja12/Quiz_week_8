import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('climate.csv')

years = data['Year']
co2 = data['CO2']
temp = ['Temperature']

plt.figure(figsize=(10,6))

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("CO2 Levels Over Time") 
plt.ylabel("CO2") 
plt.xlabel("Year") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.title("Temperature change over time")
plt.ylabel("Temperature (C)") 
plt.xlabel("Year") 

plt.tight_layout()

plt.savefig("co2_temp_2.png")

plt.show() 

