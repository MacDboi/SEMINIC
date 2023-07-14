from pydantic import BaseModel 

class hotel(BaseModel):
    City: str
    Checkindate: str
    Checkoutdate: str
    Hotel: str
    Price: int