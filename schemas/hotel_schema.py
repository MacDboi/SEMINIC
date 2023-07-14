from datetime import datetime, timezone
def hotel_serializer(hotel) -> dict:
    return {
        'City': hotel["city"],
        'Check In Date': dateconverter(hotel["checkindate"]),
        'Check Out Date': dateconverter(hotel["checkoutdate"]),
        'Hotel': hotel['Hotel'],
        'Price': hotel['Price']
    }

def dateconverter(utc_date_string) -> str:
    local_date = utc_date_string.date()
    return str(local_date)


def hotels_serializer(hotels) -> list:
    return [hotel_serializer(hotel) for hotel in hotels]