# from numpy import product
# import pandas as pd
# import random
# from datetime import datetime

# df = pd.read_csv('people.csv')

# print(df.head())

# def add_num(x):
#     num = x + random.randrange(-5, 5)
#     if num < 0: num = 0
#     elif num > 100: num = 100
#     return num

# def update_productivity(df):
#     productivity = df['productivity']
#     for i in range(len(productivity)): productivity[i] = add_num(int(productivity[i]))
#     df.drop(columns='productivity')
#     df.add(productivity)
#     df.to_csv('people.csv', index=False)

# def fire_person(df, id):
#     # removes person from the database
#     df = df[df.worker_id != id]
#     df.to_csv('people.csv', index=False)

# def determine_fire(df):
#     productivity = df['productivity']
#     worker_ids = df['worker_id']
#     for i in range(len(productivity)):
#         if productivity[i] <= 10: fire_person(df, worker_ids[i])
#         elif 10 < productivity[i] and productivity[i] <= 15:
#             # 30% chance of being fired
#             chance = random.random()
#             if chance < .3: fire_person(df, worker_ids[i])

#         elif 15 < productivity[i] and productivity[i] <= 20:
#             # 5% chance of being fired
#             chance = random.random()
#             if chance < .05: fire_person(df, worker_ids[i])

# def make_birthday(df):
#     # Creates birthday and age
#     birth = df['birth_date']
#     old = df['age']

#     for i in range(len(old)):
#         year_born = random.randrange(1952, 1985)
#         month_born = random.randrange(1, 12)
#         day_born = random.randrange(1, 28)
#         birthday = f'{year_born}-{month_born}-{day_born}'
#         born = datetime.now() - datetime.strptime(f'{year_born}-{month_born}-{day_born}', '%Y-%m-%d')
#         age = int(int(str(born).split(' ')[0]) // 365.25)
        
#         old[i] = age
#         birth[i] = birthday

#     df.drop(columns='age')
#     df.drop(columns='birth_date')
#     df.add(birth)
#     df.add(old)
#     df.to_csv('people.csv', index=False)

# def hire_year(df):
#     # Creates years an employee was hired
#     hire_year = df['hire_year']
#     age = df['age']

#     for i in range(len(hire_year)):
        
#         old = age[i]
#         gap = random.randrange(29, 51)
#         # n = age - gap; year - n = year
#         if gap > int(old): year = 2022
#         else:
#             n = int(old) - gap
#             year = 2022 - n

#         hire_year[i] = year

#     df.drop(columns='hire_year')
#     df.add(hire_year)
#     df.to_csv('people.csv', index=False)

# def send_blackmail(email):
#     emails = []
#     with open('blackmail.txt', 'r') as file:
#         for i in file: emails.append(i)
#     print(f'{email} has been sent the following encouraging e-mail: {random.choice(emails)}!')

# def determine_blackmail(df):
#     emails = df['email']
#     productivity = df['productivity']

#     for i in range(len(productivity)):
#         if 10 < int(productivity[i]) and int(productivity[i]) <= 20: send_blackmail(emails[i])

# determine_fire(df)

import asyncio
import threading

async def firing(message):
    count = 0
    while True:
        await asyncio.sleep(5)
        print(message)
        count += 1
        if count > 5: break

def run_fire(message):
    print('Creating Loop')
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(firing(message))
    loop.close()

async def bm(message):
    count = 0
    while True:
        await asyncio.sleep(3)
        print(message)
        count += 1
        if count > 5: break

def run_blackmail(message):
    print('Creating Loop')
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(bm(message))
    loop.close()

async def produce(message):
    count = 0
    while True:
        await asyncio.sleep(1)
        print(message)
        count += 1
        if count > 5: break

def run_productivity(message):
    print('Creating Loop')
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(produce(message))
    loop.close()

def test():
    t1 = threading.Thread(target = run_fire, args=('Firing People',))
    t2 = threading.Thread(target = run_productivity, args=('Updating Productivity',))
    t3 = threading.Thread(target = run_blackmail, args=('Sending Encouraging Emails',))
    
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

main()