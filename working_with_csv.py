# import csv
# with open("weather-data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)

import pandas
data = pandas.read_csv("weather-data.csv")
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
# # get data in column
#
# print(data["temp"])
# print(data.temp)

# get data in row

print(data[data.temp == data.temp.max()])
