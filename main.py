from faker import Faker
import random
import numpy as np

fake = Faker()

# Fire Someone Without the Guilt of Firing Someone
# Track location of every employee
# Automatic Blackmail Upon bad workmanship

PEOPLE = 50

def generate_social_credit_score(avg=800):
    return np.random.normal(avg, 75, PEOPLE).round(0)

def generate_IQ(avg = 100): return np.random.normal(avg, 15, PEOPLE).round(0)

def generate_fake_address():
    street = fake.street_address()
    percentage = random.random()
    zipcode = fake.zipcode()

    # 10% chance to be out of state
    if percentage < .1:
        # Giving a city and zipcode that doesn't exist in a given state
        city = fake.city()
        state = fake.state()
    else:
        cities = ['Aberdeen',        'Acequia',       'Albion',        'American Falls', 'Ammon',       'Arco',        'Arimo',            'Ashton',
                  'Athol',           'Atomic City',   'Bancroft',      'Basalt',         'Bellebue',    'Blackfoot',   'Bliss',            'Bloomington',
                  'Boise',           'Bonners Ferry', 'Bovill',        'Buhl',           'Burley',      'Butte City',  'Caldwell',         'Cambridge',
                  'Carey',           'Cascade',       'Castleford',    'Challis',        'Chubbuck',    'Clark Fork',  'Clayton',          'Clifton',
                  "Coeur d'Alene",   'Cottonwood',    'Council',       'Craigmont',      'Crouch',      'Culdesac',    'Dalton Gardens',   'Dayton',
                  'Deary',           'Declo',         'Dietrich',      'Donnelly',       'Dover',       'Downey',      'Driggs',           'Drummond',
                  'Dubois',          'Eagle',         'East Hope',     'Eden',           'Elk River',   'Emmett',      'Fairfield',        'Ferdinand',
                  'Fernan Lake',     'Filer',         'Firth',         'Franklin',       'Fruitland',   'Garden City', 'Genesee',          'Georgetown',
                  'Glenns Ferry',    'Gooding',       'Grace',         'Grance View',    'Grangeville', 'Greenleaf',   'Hagerman',         'Hailey',
                  'Hamer',           'Hansen',        'Harrison',      'Hauser',         'Hayden',      'Hayden Lake', 'Hazelton',         'Heyburn',
                  'Hollister',       'Homedale',      'Hope',          'Horseshoe Bend', 'Huetter',     'Idaho City',  'Idaho Falls',      'Inkom',
                  'Iona',            'Irwin',         'Island Park',   'Jerome',         'Juliaetta',   'Kamiah',      'Kellogg',          'Kendrick',
                  'Ketchum',         'Kimberly',      'Kooskia',       'Kootenai',       'Kuna',        'Lapwai',      'Lava Hot Springs', 'Leadore',
                  'Lewiston',        'Lewisville',    'Mackay',        'Malad',          'Malta',       'Marsing',     'McCall',           'McCammon',
                  'Melba',           'Menan',         'Meridian',      'Middleton',      'Midvale',     'Minidoka',    'Montpelier',       'Moore',
                  'Moscow',          'Mountain Home', 'Moyie Springs', 'Mud Lake',       'Mullan',      'Murtaugh',    'Nampa',            'New Meadows',
                  'New Plymouth',    'Newdale',       'Nezperce',      'Notus',          'Oakley',      'Oldtown',     'Onaway',           'Orofino',
                  'Osburn',          'Oxford',        'Paris',         'Parker',         'Parma',       'Paul',        'Patette',          'Peck',
                  'Pierce',          'Pinehurst',     'Placerville',   'Plummer',        'Pocatello',   'Ponderay',    'Post Falls',       'Potlatch',
                  'Preston',         'Priest River',  'Rathdrum',      'Reubens',        'Rexburg',     'Richfield',   'Rigby',            'Riggins',
                  'Ririe',           'Roberts',       'Rockland',      'Rupert',         'Salmon',      'Sandpoint',   'Shelley',          'Shoshone',
                  'Smelterville',    'Soda Springs',  'Spencer',       'Spirit Lake',    'St. Anthony', 'St. Charles', 'St. Maries',       'Stanley',
                  'Star',            'State Line',    'Stites',        'Sugar City',     'Sun Valley',  'Swan Valley', 'Tensed',           'Teton',
                  'Tetonia',         'Troy',          'Twin Falls',    'Ucon',           'Victor',      'Wallace',     'Wardner',          'Warm River',
                  'Weippe',          'Weiser',        'Wendell',       'Weston',         'White Bird',  'Wilder',      'Winchester',       'Worley']
        # print(random.choices(numberList, weights=(10, 20, 30, 40, 50), k=5))
        city = random.choice(cities)
        state = 'ID'

    street += f" {city}, {state}. {zipcode}"    
    print(street)

def generate_fake_salary(): print(random.randrange(70000, 125000, 1000))

def generate_fake_age(): print(random.randrange(38, 74))

# Important Information For Data
generate_social_credit_score()
generate_IQ()
generate_fake_address()
generate_fake_salary()
generate_fake_age()
fake.name()
fake.phone_number()
fake.ssn()
fake.email()
fake.month() # Hire Date?
fake.year()  # Hire Date?
fake.date()  # Birthday?
fake.time()  # Clock In Time?
fake.latitude()
fake.longitude()
fake.license_plate()

# Data I don't think will be useful for our purpose
fake.country()
fake.job()
