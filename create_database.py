# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 16:06:38 2024

@author: Marko
"""

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# створенння бази даних
mydb = myclient["mydatabase"]
# перевірка чи бд існує (не стоврюється доки не буде наповнена)
# dblist = myclient.list_database_names()
# if "mydatabase" in dblist:
#     print("The database exists.")

# стоврення колекції
mycol = mydb["customers"]
# перевірка чи колекція існує (не сторюється доки не буде наповнена)
# collist = mydb.list_collection_names()
# if "customers" in collist:
#     print("The collection exists.")

# вставити документ в колекцію (документ = запис)
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)
print(x.inserted_id)

mylist = [
    { "name": "Amy", "address": "Apple st 652"},
    { "name": "Hannah", "address": "Mountain 21"},
    { "name": "Michael", "address": "Valley 345"},
    { "name": "Sandy", "address": "Ocean blvd 2"},
    { "name": "Betty", "address": "Green Grass 1"},
    { "name": "Richard", "address": "Sky st 331"},
    { "name": "Susan", "address": "One way 98"},
    { "name": "Vicky", "address": "Yellow Garden 2"},
    { "name": "Ben", "address": "Park Lane 38"},
    { "name": "William", "address": "Central st 954"},
    { "name": "Chuck", "address": "Main Road 989"},
    { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

print(x.inserted_ids)