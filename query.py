# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 06:57:56 2024

@author: Marko
"""

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = {"address":"Park Lane 38"}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

myquery1 = {"address":{"$gt":"S"}}

print("Множинний запит:")
mydoc = mycol.find(myquery1)

for x in mydoc:
    print(x)

myquery2 = {"address":{"$regex":"^S"}}

print("Запит через регулярний вираз:")
mydoc = mycol.find(myquery2)

for x in mydoc:
    print(x)
