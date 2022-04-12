# import csv
# with open("weather-data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)

# import pandas
# data = pandas.read_csv("weather-data.csv")
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
# # get data in column
#
# print(data["temp"])
# print(data.temp)

# get data in row

# print(data[data.temp == data.temp.max()])

import pandas
data = pandas.read_csv("227 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
grey = len(data[data["Primary Fur Color"] == "Gray"])
print(grey)
black = len(data[data["Primary Fur Color"] == "Black"])
print(black)
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(cinnamon)

data_dict = {
    "fur color": ["Grey", "black", "cinnamon"],
    "count": [grey, black, cinnamon]
}

df = pandas.DataFrame(data_dict)
df.to_csv("fur color.csv")
