from faker import Faker
from database import Database
import random
from pymongo import MongoClient
import pandas as pd
import numpy as np

fake = Faker()

# Fire Someone Without the Guilt of Firing Someone
# Track location of every employee
# Automatic Blackmail Upon bad workmanship

class FakePerson():

    def __init__(self, database):
        self.database = database

    def _generate_social_credit_score(self): return random.randrange(725, 950)

    def _generate_fake_IQ(self): return random.randrange(95, 130)

    def _generate_fake_address(self):
        address = fake.street_address()
        percentage = random.random()
        zipcode = fake.zipcode()

        # 10% chance to be out of state
        if percentage < .05:
            # Giving a city and zipcode that doesn't exist in a given state
            city = fake.city()
            state = fake.state()
        else:
            cities = ['Aberdeen', 'Acequia', 'Albion', 'American Falls', 'Ammon', 'Arco', 'Arimo', 'Ashton',
                      'Athol', 'Atomic City', 'Bancroft', 'Basalt', 'Bellebue', 'Blackfoot', 'Bliss', 'Bloomington',
                      'Boise', 'Bonners Ferry', 'Bovill', 'Buhl', 'Burley', 'Butte City', 'Caldwell', 'Cambridge',
                      'Carey', 'Cascade', 'Castleford', 'Challis', 'Chubbuck', 'Clark Fork', 'Clayton', 'Clifton',
                      "Coeur d'Alene", 'Cottonwood', 'Council', 'Craigmont', 'Crouch', 'Culdesac', 'Dalton Gardens', 'Dayton',
                      'Deary', 'Declo', 'Dietrich', 'Donnelly', 'Dover', 'Downey', 'Driggs', 'Drummond',
                      'Dubois', 'Eagle', 'East Hope', 'Eden', 'Elk River', 'Emmett', 'Fairfield', 'Ferdinand',
                      'Fernan Lake', 'Filer', 'Firth', 'Franklin', 'Fruitland', 'Garden City', 'Genesee', 'Georgetown',
                      'Glenns Ferry', 'Gooding', 'Grace', 'Grance View', 'Grangeville', 'Greenleaf', 'Hagerman', 'Hailey',
                      'Hamer', 'Hansen', 'Harrison', 'Hauser', 'Hayden', 'Hayden Lake', 'Hazelton', 'Heyburn',
                      'Hollister', 'Homedale', 'Hope', 'Horseshoe Bend', 'Huetter', 'Idaho City', 'Idaho Falls', 'Inkom',
                      'Iona', 'Irwin', 'Island Park', 'Jerome', 'Juliaetta', 'Kamiah', 'Kellogg', 'Kendrick',
                      'Ketchum', 'Kimberly', 'Kooskia', 'Kootenai', 'Kuna', 'Lapwai', 'Lava Hot Springs', 'Leadore',
                      'Lewiston', 'Lewisville', 'Mackay', 'Malad', 'Malta', 'Marsing', 'McCall', 'McCammon',
                      'Melba', 'Menan', 'Meridian', 'Middleton', 'Midvale', 'Minidoka', 'Montpelier', 'Moore',
                      'Moscow', 'Mountain Home', 'Moyie Springs', 'Mud Lake', 'Mullan', 'Murtaugh', 'Nampa', 'New Meadows',
                      'New Plymouth', 'Newdale', 'Nezperce', 'Notus', 'Oakley', 'Oldtown', 'Onaway', 'Orofino',
                      'Osburn', 'Oxford', 'Paris', 'Parker', 'Parma', 'Paul', 'Patette', 'Peck',
                      'Pierce', 'Pinehurst', 'Placerville', 'Plummer', 'Pocatello', 'Ponderay', 'Post Falls', 'Potlatch',
                      'Preston', 'Priest River', 'Rathdrum', 'Reubens', 'Rexburg', 'Richfield', 'Rigby', 'Riggins',
                      'Ririe', 'Roberts', 'Rockland', 'Rupert', 'Salmon', 'Sandpoint', 'Shelley', 'Shoshone',
                      'Smelterville', 'Soda Springs', 'Spencer', 'Spirit Lake', 'St. Anthony', 'St. Charles', 'St. Maries', 'Stanley',
                      'Star', 'State Line', 'Stites', 'Sugar City', 'Sun Valley', 'Swan Valley', 'Tensed', 'Teton',
                      'Tetonia', 'Troy', 'Twin Falls', 'Ucon', 'Victor', 'Wallace', 'Wardner', 'Warm River',
                      'Weippe', 'Weiser', 'Wendell', 'Weston', 'White Bird', 'Wilder', 'Winchester', 'Worley']
            # print(random.choices(numberList, weights=(10, 20, 30, 40, 50), k=5))
            city = random.choice(cities)
            state = 'ID'

        address += f" {city}, {state}. {zipcode}"    
        return address

    def _generate_fake_salary(self): return random.randrange(70000, 125000, 1000)

    def _generate_fake_age(self): return random.randrange(38, 74)

    def _generate_worker_id(self):
        cap_letters = [chr(i) for i in range(65, 91)]
        low_letters = [chr(i) for i in range(97, 123)]
        numbers = [str(i) for i in range(10)]

        worker_id = ''

        for i in range(7):
            choice = random.choice([cap_letters, low_letters, numbers])
            worker_id += random.choice(choice)

        return worker_id

    def _add_email(self, name):
        name = name.split(' ')
        fname = name[0]
        lname = name[1]
        email = (fname[0] + lname + "@byui.edu").lower()
        return email

    def create_person(self, amount = 1):
        collection = self.database.return_database('People')
        for i in range(amount):
            # Generating all the important information for a "person"
            worker_id = self._generate_worker_id()
            name = fake.name()
            scs = self._generate_social_credit_score()
            iq = self._generate_fake_IQ()
            address = self._generate_fake_address()
            salary = self._generate_fake_salary()
            age = self._generate_fake_age()
            phone_number = fake.phone_number()
            ssn = fake.ssn()
            email = self._add_email(name)
            hire_month = fake.month()
            hire_year = fake.year()
            birth_date = fake.date()
            current_latitude = float(fake.latitude())
            current_longitude = float(fake.longitude())
            license_plate = fake.license_plate()
            # fake.time()
            data = {'_id': worker_id, 'name': name, 'address': address, 'ssn': ssn, 'age': age, 'email': email, 'phone_number': phone_number, \
                    'salary': salary, 'birth_date': birth_date, 'iq': iq, 'social_credit_score': scs, 'hire_month': hire_month, \
                    'hire_year': hire_year, 'current_latitude': current_latitude, 'current_longitude': current_longitude, \
                    'license_plate': license_plate}

            # UNCOMMENT IF DATABASE RESET REQUIRED
            collection.insert_one(data)

cluster = MongoClient("mongodb+srv://precious_butthead:sparky123592n600@cluster0.y0bo003.mongodb.net/?retryWrites=true&w=majority")
fakeperson = FakePerson(Database(cluster))

# Run this function ONCE upon database creation
fakeperson.create_person(420)