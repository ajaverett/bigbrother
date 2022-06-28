import random

def fire_person(df, id):
    # removes person from the database
    df = df[df.worker_id != id]
    df.to_csv('people.csv', index=False)

def determine_fire(df):
    print('Firing Unproductive Employees')
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
            if chance < .05: fire_person(df, worker_ids[i])