# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:09:35 2024

@author: Marko
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mycol.drop()
