# import csv
# with open("225 weather-data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)
import pandas
data = pandas.read_csv("225 weather-data.csv")
print(data["temp"])
