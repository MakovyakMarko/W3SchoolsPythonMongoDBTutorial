# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:04:32 2024

@author: Marko
"""

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = {"address": "Mountain 21"}

mycol.delete_one(myquery)

myquery1 = {"address": {"$regex":"^S"}}

x = mycol.delete_many(myquery)

print(x.delete_count, "documents deleted")

x = mycol.delete_many({})

print(x.delete_count, "documnets deleted.")

