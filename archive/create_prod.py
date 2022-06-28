import pandas as pd


# Transform People File
people = (pd.read_csv('people.csv')
    .filter(['worker_id', 'productivity'])
    .transpose()
)

people.columns = people.iloc[0,:]

     
lines = []
with open('prod.csv', 'r+') as file:
    count = 0
    for i in file:
        if count != 0: lines += i
        count += 1

with open('prod.csv', 'w+') as file:
    for line in lines: file.writelines(line)