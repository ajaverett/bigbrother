import pandas as pd
import random as rd

df = pd.read_csv("people.csv")

people1 = (df.filter(['worker_id','productivity']).
    transpose()
)

# df1 = pd.read_csv("prod.csv")
# len(df1)


def update_prod(df):
    last_prod = df.iloc[-1,:].values.tolist()

    new_prod = []

    for i in range(len(last_prod)):
        new_prod.append(last_prod[i] + rd.randint(-5, 7))

    df_length = len(df)

    df.loc[df_length] = new_prod

    df.to_csv("prod.csv", index = False)

update_prod(people1)







