#!/usr/bin/env python3
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    my_db = client["my_db"]
    collection_school = my_db["school"]

'''INSERT ONE'''
mydict = {"name": "UCSF", "address": "505 Parnassus Ave"}
document_id = collection_school.insert_one(mydict)
print("New school created: {}".format(document_id))

'''INSERT MANY'''
mylist = [
        {"name": "Amy", "address": "Apple st 652"},
        {"name": "Hannah", "address": "Mountain 21"},
        {"name": "Michael", "address": "Valley 345"},
        {"name": "Sandy", "address": "Ocean blvd 2"},
        {"name": "Betty", "address": "Green Grass 1"},
        {"name": "Richard", "address": "Sky st 331"},
        {"name": "Susan", "address": "One way 98"},
        {"name": "Vicky", "address": "Yellow Garden 2"},
        {"name": "Ben", "address": "Park Lane 38"},
        {"name": "William", "address": "Central st 954"},
        {"name": "Chuck", "address": "Main Road 989"},
        {"name": "Viola", "address": "Sideway 1633"}
    ]
document_ids = collection_school.insert_many(mylist) #返回的是一个对象
print(document_ids.inserted_ids) #这个对象中的一个属性，inserted_ids是一个list，记录所有的插入生成的id

'''FIND ONE'''
one = collection_school.find_one()
print(one)

'''FIND ALL'''
all = collection_school.find()
for one in all:
    print(one)

b = [1, 2, 3]

for a in b:
    print(a)

'''FIND只显示某些行'''
print("FIND by parameter")
for x in collection_school.find({}, {"_id": 0, "name": 1, "address": 1}):
    print(x)

for x in collection_school.find({}, {"address": 0}):
    print(x)

'''查询过滤'''
print("查询过滤")
myquery = {"address": "Park Lane 38"}
mydoc = collection_school.find(myquery)
for x in mydoc:
    print(x)

myquery = {"address": {"$gt": "S"}}

mydoc = collection_school.find(myquery)
for x in mydoc:
    print(x)

'''排序'''
print("排序1")
mydoc = collection_school.find().sort("name")
for x in mydoc:
    print(x)

print("排序2")
mydoc = collection_school.find().sort("name",-1)
for x in mydoc:
    print(x)

'''update'''
myquery = {"address": "Valley 345"}
newvalues = {"$set": {"address": "Canyon 123"}}

collection_school.update_one(myquery, newvalues)
# print "customers" after the update:
for x in collection_school.find():
    print(x)

x = collection_school.delete_many({})