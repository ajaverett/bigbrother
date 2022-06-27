from math import prod
import pandas as pd
import random

df = pd.read_csv('people.csv')

print(df.head())
productivity = df['productivity']
# for i in range(len(productivity)):

def add_num(x):
    num = x + random.randrange(-5, 5)
    if num < 0: num = 0
    return num

for i in range(len(productivity)): productivity[i] = add_num(int(productivity[i]))

df.drop(columns='productivity')
df.add(productivity)

df.to_csv('people.csv', index=False)