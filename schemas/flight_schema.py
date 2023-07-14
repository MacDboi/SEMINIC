def depart_flight_serializer(flight) -> dict:
    return {
        'City': flight["destcity"],
        'Departure Date': flight["date"].strftime('%Y-%m-%d'),
        'Departure Airline': flight["airlinename"],
        'Departure Price': flight['price']
    }

def depart_flights_serializer(flights) -> list:
    return [depart_flight_serializer(flight) for flight in flights]

def return_flight_serializer(flight) -> dict:
    return {
        'Return Date': flight["date"].strftime('%Y-%m-%d'),
        'Return Airline':flight["airlinename"],
        'Return Price': flight['price']
    }

def return_flights_serializer(flights) -> list:
    return [return_flight_serializer(flight) for flight in flights]
