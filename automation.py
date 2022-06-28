import random
import asyncio
import pandas as pd
import threading

# '1 Day' = 5 seconds

def add_num(x):
    num = x + random.randrange(-5, 5)
    if num < 0: num = 0
    elif num > 100: num = 100
    return num

async def update_productivity(lock):
    while True:
        await asyncio.sleep(5)
        lock.acquire()
        df = pd.read_csv('people.csv')
        print('Updating Productivity')
        '''
        productivity = df['productivity']
        for i in range(len(productivity)): productivity[i] = add_num(int(productivity[i]))
        df.drop(columns='productivity')
        df.add(productivity)
        df.to_csv('people.csv', index=False)'''
        determine_fire(df)
        lock.release()

def fire_person(df, id):
    # removes person from the database
    df = df[df.worker_id != id]
    df.to_csv('people.csv', index=False)

def determine_fire(df):
    print('Firing Unproductive Employees')
    '''
    productivity = df['productivity']
    worker_ids = df['worker_id']
    for i in range(len(productivity)):
        if productivity[i] <= 10: fire_person(df, worker_ids[i])
        elif 10 < productivity[i] and productivity[i] <= 15:
            # 30% chance of being fired
            chance = random.random()
            if chance < .3: fire_person(df, worker_ids[i])

        elif 15 < productivity[i] and productivity[i] <= 20:
            # 5% chance of being fired
            chance = random.random()
            if chance < .05: fire_person(df, worker_ids[i])'''

def send_blackmail(email):
    emails = []
    with open('blackmail.txt', 'r') as file:
        for i in file: emails.append(i)
    print(f'{email} has been sent the following encouraging e-mail: {random.choice(emails)}!')

async def determine_blackmail(lock):
    while True:
        await asyncio.sleep(15)
        lock.acquire()
        df = pd.read_csv('people.csv')
        print('Sending Blackmail to Incompetent Employees')
        '''
        emails = df['email']
        productivity = df['productivity']

        for i in range(len(productivity)):
            if 10 < int(productivity[i]) and int(productivity[i]) <= 20: send_blackmail(emails[i])'''
        lock.release()

def run_blackmail(lock):
    print('Creating Loop')
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(determine_blackmail(lock))
    loop.close()

def run_productivity(lock):
    print('Creating Loop')
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(update_productivity(lock))
    loop.close()

def main():
    lock = threading.Lock()
    
    t1 = threading.Thread(target = run_productivity, args=(lock,))
    t2 = threading.Thread(target = run_blackmail, args=(lock,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

main()