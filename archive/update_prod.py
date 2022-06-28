import pandas as pd
import random as rd

# Update Productivity
df = pd.read_csv("prod.csv")#.drop(columns = ['worker_id'])

def update_prod(df):
    last_prod = df.iloc[-1,:].values.tolist()

    new_prod = []

    for i in range(len(last_prod)):
        new_prod.append(int(last_prod[i]) + rd.randrange(-5, 7))

    df_length = len(df)

    df.loc[df_length] = new_prod

    df.to_csv("prod.csv", index = False)

update_prod(df)







