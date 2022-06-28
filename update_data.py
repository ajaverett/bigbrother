import random
import pandas as pd

def send_blackmail(email):
    emails = []
    with open('blackmail.txt', 'r') as file:
        for i in file: emails.append(i)
    print(f'{email} has been sent the following encouraging e-mail: {random.choice(emails)}!')

def determine_blackmail():
    df = pd.read_csv('people.csv')
    print('Sending Blackmail to Incompetent Employees')
    emails = df['email']
    productivity = df['productivity']

    for i in range(len(productivity)):
        if 10 < int(productivity[i]) and int(productivity[i]) <= 20: send_blackmail(emails[i])

def add_num(x):
    num = x + random.randrange(-5, 5)
    if num < 0: num = 0
    elif num > 100: num = 100
    return num

def update_productivity():
    df = pd.read_csv("prod.csv")
    last_prod = df.iloc[-1,:].values.tolist()
    new_prod = []

    for i in range(len(last_prod)):
        num = add_num(int(last_prod[i]) + random.randrange(-5, 7))
        new_prod.append(num)
        
    df_length = len(df)
    df.loc[df_length] = new_prod
    df.to_csv("prod.csv", index = False)

    determine_blackmail()
update_productivity()