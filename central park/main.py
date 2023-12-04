# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for r in data:
#         if r[1] != "temp":
#             temperature.append(r[1])

import pandas

# data = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()
#
# data_list = data["temp"].tolist()
# # print(data["temp"].mean())
# # print(data["temp"].max())
#
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
#
# # print(monday.condition)
# monday_temp = monday.temp[0]
# # print(monday_temp)
#
# # Create dataframe from scratch
#
# my_dict = {"students": ["Amy", "Gosho", "Pesho"],
#            "scores": [76, 56, 65]}
#
# new_data = pandas.DataFrame(my_dict)
# # print(new_data)
# new_data.to_csv(("new_data.csv"))



data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {"Fur Color": ["Gray", "Cinnamon", "Black"],
             "Count": [gray, red, black]}

df = pandas.DataFrame(data_dict)

df.to_csv("squirrel_count.csv")