from fastapi import FastAPI, HTTPException, status
from routes.routes import helper
from fastapi.responses import RedirectResponse
from datetime import datetime



app = FastAPI(title="CSIT MINI-CHALLENGE")

@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse("/docs")

@app.get("/flight")
async def find_flight(departureDate:str, returnDate:str, destination: str):
     # Check input 
    if departureDate == "" or returnDate == "" or destination == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing query Parameters")
    
    # Check date format
    try:
        datetime.strptime(departureDate, '%Y-%m-%d')
        datetime.strptime(returnDate, '%Y-%m-%d')
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad input with datetime format")
    
    # formatting date
    departureDate =datetime.strptime(departureDate, '%Y-%m-%d')
    returnDate =datetime.strptime(returnDate, '%Y-%m-%d')

    departureflight = helper.depart(departureDate,destination)
    returnflight = helper.returnflight(returnDate,destination)

    if len(departureflight) == 0:
        return []
    if len(returnflight) == 0:
        return []
    departureflight = departureflight[0]
    returnflight =  returnflight[0]

    result = {}
    result["City"] = departureflight["City"]
    result["Departure Date"] = departureflight["Departure Date"]
    result["Departure Airline"] = departureflight["Departure Airline"]
    result["Departure Price"] = departureflight["Departure Price"]
    result["Return Date"] = returnflight["Return Date"]
    result["Return Airline"] = returnflight["Return Airline"]
    result["Return Price"] = returnflight["Return Price"]
    
    return [result]


@app.get("/hotel")
async def find_hotel(checkInDate:str, checkOutDate:str, destination: str):
    # TODO: Formatting for lowercase

    # Check input 
    if checkInDate == "" or checkOutDate == "" or destination == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing query Parameters")

    # Check date format
    try:
        datetime.strptime(checkInDate, '%Y-%m-%d')
        datetime.strptime(checkOutDate, '%Y-%m-%d')
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad input with datetime format")
    

    # formatting date
    checkInDate =datetime.strptime(checkInDate, '%Y-%m-%d')
    checkOutDate =datetime.strptime(checkOutDate, '%Y-%m-%d')

    
    hotels = helper.hotelsearch(checkInDate, checkOutDate, destination)
    if len(hotels)==0:
        return []
    # Process cheapest
    cheapest = hotels[0]["Price"]
    cheapesthotels = []
    for hotel in hotels:
        if hotel['Price'] <= cheapest:
            cheapesthotels.append(hotel)
    return cheapesthotels
    
    
