from pydantic import BaseModel 

class flight(BaseModel):
    City: str
    DepartureDate: str
    DepartureAirline: str
    DeparturePrice: int
    # ReturnDate: str
    # ReturnAirline: str
    # ReturnPrice: int