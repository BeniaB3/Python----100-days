import csv

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('weather_data.csv')
data.index.name = 'day'
data.columns.name = 'temperature'
data.plot()
plt.show()

print(data)



