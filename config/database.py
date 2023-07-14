from pymongo import MongoClient
db_connection = MongoClient("mongodb+srv://userReadOnly:7ZT817O8ejDfhnBM@minichallenge.q4nve1r.mongodb.net/")
db = db_connection["minichallenge"]
collection_flight = db["flights"]
collection_hotel = db["hotels"]
