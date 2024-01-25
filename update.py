# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:10:17 2024

@author: Marko
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address":"Valley 345"}
newvalues = { "$set": {"address":"Canyon 123"}}

mycol.update_one(myquery, newvalues)

for x in mycol.find():
    print(x)
    
myquery = { "address":{ "$regex": "^S"}}
newvalues = { "$set": {"name":"Minnie"}}

mycol.update_one(myquery, newvalues)

print(x.modifyied_count, "documents updated.")
    
