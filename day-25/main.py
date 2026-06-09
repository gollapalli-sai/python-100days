

#with open("weather_data.csv") as data_file:
#    data=data_file.readlines()
#    print(data)
#


#import csv
#with open("weather_data.csv") as data_file:
#    data =csv.reader(data_file)
#    temperatures=[]
#    for row in data:
#        if row[1]!="temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)

#import pandas
#data=pandas.read_csv("weather_data.csv")
##print(data["temp"])
#
#data_dict=data.to_dict()
#print(data_dict)
#print(data["condition"])
#print(data[data.day=="Monday"])
#print(data["temp"].max())

import pandas
from reportlab.lib.colors import black

#data_frame={
#    "students":["sai","teja"],
#    "scores":[56,78]
#}
#data=pandas.DataFrame(data_frame)
#data.to_csv("new_data.csv")

data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squrreils=len(data[data["Primary Fur Color"]=="Gray"])
print(gray_squrreils)

#data_dict={
#    "Fur Color":["Gray","Red","Black"],
#    "Count":[gray_squrreils,red_squrreis_count,black_squrreils_count]
#}
#df=pandas.DataFrame(data_dict)
#df.to_csv("squirrel_count.csv")