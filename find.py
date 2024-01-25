# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 06:45:12 2024

@author: Marko
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
mycol = mydb["customers"]

x = mycol.find_one()

print(x)

#for x in mycol.find():
#    print(x)
    
print("Return only some results (name, address):")
for x in mycol.find({}, { "_id":0, "name":1, "address":1 }):
    print(x)
    
print("Return only name:")
for x in mycol.find({},{ "address": 0 }):
    print(x)