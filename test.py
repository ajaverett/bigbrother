from pymongo import MongoClient

# cluster = MongoClient("mongodb+srv://precious_butthead:sparky123592n600@cluster0.y0bo003.mongodb.net/?retryWrites=true&w=majority")
# data = cluster['TotallyLegalStuff']

# people = data['People'].find()
# for person in people:
#     print(person)

cluster = MongoClient("mongodb+srv://precious_butthead:sparky123592n600@cluster0.y0bo003.mongodb.net/?retryWrites=true&w=majority")
people = cluster['TotallyLegalStuff']
dataCollection = people['People']
data = dataCollection.find()

for person in data:
    print(person)
    break