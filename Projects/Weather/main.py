# with open("weather_data.csv") as data_file:
#     data=data_file.readlines()
#     print(data)


# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     print(data)
#     for row in data:
#          if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data =  pandas.read_csv("weather_data.csv")
print(data)
# print(type(data))
# two primary data structures, series, and dataframe. 
# series is a list or a single column 
# dataframe is similar to a spreadsheet intself 
# print(data["temp"])


#we can convert both series and dataframs data types that we can work with such as dictionaries and lists. 
data_dict=data.to_dict()
print(data_dict)

temp_list=data['temp'].to_list()
print(temp_list)


#these essentially do the same thing 
average=sum(temp_list)/len(temp_list)
print(average)

print(data['temp'].mean())
print(data['temp'].max())

#get data in columns 
data['condition']
print(data.condition)


#get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])
monday = data[data.day == 'Monday']
print(monday.condition)
monday_temp=int(monday.temp)
monday_temp_f=monday_temp*5/9+32
print(monday_temp_f)

#create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [12,13,14]
}

new_data=pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("new_data.csv")