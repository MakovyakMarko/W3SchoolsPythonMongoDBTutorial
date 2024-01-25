# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:59:02 2024

@author: Marko
"""

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydoc = mycol.find().sort("name")

for x in mydoc:
    print(x)
    
mydoc = mycol.find().sort("name", -1)
print("Сортування за спаданням:")
for x in mydoc:
    print(x)
