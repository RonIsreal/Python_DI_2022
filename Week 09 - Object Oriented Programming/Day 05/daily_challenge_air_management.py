import datetime

current_day = datetime.datetime.now()
current_month = datetime.datetime.now()
current_year = datetime.datetime.now()


class Airline:

    def __init__(self, airline_id, name):
        self.airline_id = airline_id
        self.name = name
        self.airplanes = []

    def __repr__(self):
        print(f"Company: {self.name}\nID: {self.airline_id}\nAirplanes: {self.airplanes}")


class Airplane:

    airplane_count = 0

    def __init__(self, airline_owner, location):
        Airplane.airplane_count += 1
        self.airplane_id = Airplane.airplane_count
        self.location = location
        self.next_flights = [] #list of dates and locations of departure. if there is a flight on this specific day it should be appended with the location on the date
        self.airline_owner = airline_owner

    def add_plane(self, airline):
        if self.airline_owner == airline.name:
            airline.airplanes.append(self)
        print(f"The airplane was added to airline {airline.name}.")

    def fly(self, destination):
        return self.location == destination

    def location_on_date(self, current_location_ondate):
        if current_location_ondate == [current_day, current_month, current_year]:
            return self.location
        else:
            for all_flights in self.next_flights:
                if all_flights in

    def available_on_date(self, date, location):
        pass




class Flight:

    def __init__(self, fdate, destination):
        self.fdate = fdate #date of te flight
        self.destination = destination #final destination
        self.origin = None #initial departure location
        self.plane = 0 #airplane used for the flight
        self.id = f"{self.destination}UA{self.fdate}"

    def take_off(self):
        return self.origin == None


uaairline = Airline("UA","United Airlines")
uaplane = Airplane("United Airlines", "Tel Aviv")
myflight = Flight("07-12-2022","Sao Paulo")
uaplane.add_plane(uaairline)
print(uaairline.airplanes)
uaairline.__repr__()
print(myflight.id)

class Airport:

    def __init__(self, city):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []

    def schedule_flight(self, destination, date_time):
        pass

    def flights_info(self, start_date, end_date):
        # will go through the departures and arrivals lists and return all flights that are within the date range
        pass


