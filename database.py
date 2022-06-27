from pymongo import MongoClient

class Database():
    def __init__(self, cluster):
        self.cluster = cluster

    def return_database(self, name):
        people = self.cluster['TotallyLegalStuff']
        dataCollection = people[name]
        return dataCollection

cluster = MongoClient("mongodb+srv://precious_butthead:sparky123592n600@cluster0.y0bo003.mongodb.net/?retryWrites=true&w=majority")
people = cluster['TotallyLegalStuff']
dataCollection = people['People']

# person = {'name': 'John Smith', 'age': 69}
# dataCollection.insert_one(person)