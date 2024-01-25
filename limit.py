# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:14:10 2024

@author: Marko
"""

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myresult = mycol.find().limit(5)

for x in myresult:
    print(x)
    
    