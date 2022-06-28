import pandas as pd

def fire_person(people, prod, id):
    # removes person from the database
    people = people[people.worker_id != id]
    people.to_csv('people.csv', index=False)

    prod = prod.drop(columns=[id])
    prod.to_csv('prod.csv', index=False)

def determine_fire():

    people = pd.read_csv('people.csv')
    prod = pd.read_csv('prod.csv')
    
    productivity = list(prod.iloc[len(prod) - 1])
    worker_ids = people['worker_id']

    for i in range(len(productivity)):
        if productivity[i] <= 10: fire_person(people, prod, worker_ids[i])

determine_fire()