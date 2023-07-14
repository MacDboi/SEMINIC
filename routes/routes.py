from fastapi import APIRouter, HTTPException, status
from models.flight_model import flight
from schemas.flight_schema import depart_flights_serializer, return_flights_serializer
from schemas.hotel_schema import hotels_serializer
from datetime import datetime
from config.database import collection_flight, collection_hotel
import re





# @object.get("/flight")
# async def find__all_flight():
#     flights = flights_serializer(collection_flight.find())
#     return {"status": "200","data": flights}
class helper:

    def depart(departureDate,destination):
        pattern = re.compile(destination, re.IGNORECASE)
        query = {"srccity": "Singapore", "destcity": {"$regex":pattern}, "date": departureDate}
        flights = depart_flights_serializer(collection_flight.find(query).sort("price",1).limit(1))

        return flights
    
    def returnflight(returnDate,destination):
        pattern = re.compile(destination, re.IGNORECASE)
        query = {"srccity": {"$regex":pattern}, "destcity": "Singapore", "date": returnDate}
        flights = return_flights_serializer(collection_flight.find(query).sort("price",1).limit(1))

        return flights

    def hotelsearch(checkInDate, checkOutDate, destination):

        pattern = re.compile(destination, re.IGNORECASE)
        # Processes that make up the pipeline that aggregates the results
        # Query the hotels in the destination country that fit into the date range in match
        matching = {
            '$match':{
                "$and":[
                    {"city": {"$regex":pattern}},
                    {"date": {"$gte":checkInDate,"$lte":checkOutDate}}
                ]
            }
        }
        #  This groups by hotel and sum the prices over the days
        grouping={
            '$group':{
                "_id": "$hotelName",
                "city" : {"$first": "$city"},
                "checkindate" : {"$first": "$date"},
                "checkoutdate" : {"$last": "$date"},
                'Hotel': {"$first": '$hotelName'},
                "Price": {"$sum": "$price"},
            }
        }
        # Sort price in ascending order
        sorting = {
            "$sort": {
                "Price": 1
            }
        }

        pipeline=[matching,grouping,sorting]
        hotels = hotels_serializer(collection_hotel.aggregate(pipeline))
        if hotels is None:
            return []
        return hotels


    


