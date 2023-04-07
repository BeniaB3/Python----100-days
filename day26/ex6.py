weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

def convert_temp(temp):
    return (temp * 9/5) + 32


weather_f = {day: convert_temp(temp) for (day, temp) in weather_c.items()}


# Write your code 👇 below:



print(weather_f)


