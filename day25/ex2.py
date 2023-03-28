import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('weather_data.csv')
#print(type(data))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
average_temp = sum(temp_list) / len(temp_list)
print(average_temp)

print(pandas.Series.max(data["temp"]))
print(data["temp"].max())

print(data["temp"].mean())

#Get data in columns

print(data["condition"])
print(data.condition)

#Get data in row
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)