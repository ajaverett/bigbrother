from faker import Faker
import random
import pandas as pd
import numpy as np

fake = Faker()

# Fire Someone Without the Guilt of Firing Someone
# Track location of every employee
# Automatic Blackmail Upon bad workmanship

class FakePerson():

    def __init__(self):
        pass

    def _generate_social_credit_score(self, avg=800): return np.random.normal(avg, 75, 1).round(0)

    def _generate_fake_IQ(self, avg = 100): return np.random.normal(avg, 15, 1).round(0)

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

    def _generate_fake_salary(self): random.randrange(70000, 125000, 1000)

    def _generate_fake_age(self): return random.randrange(38, 74)

    def create_person(self, amount = 1):
        for i in range(amount):
            # Generating all the important information for a "person"
            scs = self._generate_social_credit_score()
            iq = self._generate_fake_IQ()
            address = self._generate_fake_address()
            salary = self._generate_fake_salary()
            age = self._generate_fake_age()
            name = fake.name()
            phone_number = fake.phone_number()
            ssn = fake.ssn()
            email = fake.email()
            hire_month = fake.month()
            hire_year = fake.year()
            birth_date = fake.date()
            current_latitude = fake.latitude()
            current_longitude = fake.longitude()
            license_plate = fake.license_plate()
            fake.time()
            data = {'name': name, 'address': address, 'ssn': ssn, 'age': age, 'email': email, 'phone_number': phone_number, \
                           'salary': salary, 'birth_date': birth_date, 'iq': iq, 'social_credit_score': scs, 'hire_month': hire_month, \
                           'hire_year': hire_year, 'current_latitude': current_latitude, 'current_longitude': current_longitude, \
                           'license_plate': license_plate}
            
            # Creating or adding person to the pandas dataframe
            if i == 0: df = pd.DataFrame(data)
            else: df.loc[len(df.index)] = data
        return df

fakeperson = FakePerson()
people = fakeperson.create_person(50)
print(people)

# Data I don't think will be useful for our purpose
fake.country()
fake.job()
