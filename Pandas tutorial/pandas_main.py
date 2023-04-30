import pandas as pd

# data = open("weather_data.csv", "r")
# print(data.readlines())

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row[1])

# df = pd.read_csv('weather_data.csv')
# print(df.describe())

df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
g_count = len(df[df['Primary Fur Color']=='Gray'])
r_count = len(df[df['Primary Fur Color']=='Cinnamon'])
b_count = len(df[df['Primary Fur Color']=='Black'])

sq_dict = {
    'Fur color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [g_count, r_count, b_count]
}

sq_data = pd.DataFrame(sq_dict)
sq_data.to_csv('Squirrel_count.csv')
