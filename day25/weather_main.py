# with open("weather_data.csv", mode="r") as file:
#     weather = file.readlines()
# print(weather)

# import csv
#
# with open("weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file, delimiter=',')
#     temperature = []
#     for row in data:
#         if row[1].isdigit():
#             temperature.append(int(row[1]))
#
#     print(temperature)

import pandas
from numpy.ma.extras import average

data = pandas.read_csv("weather_data.csv")
avg_tmp = data["temp"].tolist()

print(average(avg_tmp))
print(data["temp"].mean())
print(data["temp"].max())

print(data[data.day == "Monday"])

print(data[data.temp == data["temp"].max()])






