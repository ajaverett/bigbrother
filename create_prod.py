import pandas as pd

# Transform People File
people = (pd.read_csv('people.csv')
    .filter(['worker_id', 'productivity'])
    .transpose()
)

people.columns = people.iloc[0,:]

people.to_csv('prod.csv')

