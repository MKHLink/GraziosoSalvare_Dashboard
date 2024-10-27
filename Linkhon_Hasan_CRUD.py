#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:14:17 2024

@author: linkhonhasan_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username, password):
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32340  
        DB = 'AAC'
        COL = 'animals'
        
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}/{DB}?authSource=admin')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def addAnimal(self, data):
        """ Insert: """
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"Error: {e}")
                return False
        else:
            raise ValueError("Empty data")

    def getAnimal(self, query):
        """ Query: """
        if query is not None:
            try:
                cursor = self.collection.find(query)
                return [doc for doc in cursor]
            except Exception as e:
                print(f"Error: {e}")
                return []
        else:
            raise ValueError("Empty data")

    def updateAnimal(self, query, new_values):
        """ Update: """
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(query, {"$set": new_values})
                if result.modified_count == 0:
                    raise ValueError("Animal not found")
                return result.modified_count
            except Exception as e:
                print(f"Error: {e}")
                return 0
        else:
            raise ValueError("Empty data")

    def deleteAnimal(self, query):
        """ Delete: """
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                if result.deleted_count == 0:
                    raise ValueError("Animal not found")
                return result.deleted_count
            except Exception as e:
                print(f"Error: {e}")
                return 0
        else:
            raise ValueError("Empty data")