#for reading csv file in row
# import csv
# with open("C:\\Users\\sneha\\Downloads\\store_cities.csv","r") as file:
#    rows=csv.reader(file)
#    for row in rows:
#       print(row)       #we can write column instead of rows

import pandas as pd
df = pd.read_csv("C:\\Users\\sneha\\Downloads\\store_cities.csv", encoding='ISO-8859-1')
for index,row in df.iterrows():
    print(row)