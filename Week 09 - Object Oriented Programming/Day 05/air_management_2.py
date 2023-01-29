import datetime

todays_day = datetime.date.today().strftime('%d')
todays_month = datetime.date.today().strftime('%m')
todays_year = datetime.date.today().strftime('%Y')

class Airline:

    def __init__(self, airline_id, airline_name):
        self.airline_id = airline_id
        self.airline_name = airline_name
        self.planes = []



class Airplane:

    airplane_count = 0

    def __init__(self, airline_owner, current_location):
        Airplane.airplane_count += 1
        self.airplane_id = Airplane.airplane_count
        self.current_location = current_location
        self.airline_owner = airline_owner
        self.next_flights = []

    def fly(self, destination):
        print(f"The airplane has taken off from {self.current_location} and it's flying towards {self.next_flights['destination']}.")
        self.current_location == destination
        return

    def location_on_date(self):
        todays_date = datetime.date.today().strftime('%d/%m/%Y')
        if todays_date:
            return self.current_location

    def available_on_date(self, date, location):
        if date in Airport.scheduled_flights and location == self.current_location:
            return True
        else:
            return False

    def add_plane(self, airline):
        if self.airline_owner == airline.airline_name:
            airline.planes.append(self)
        print(f"The airplane was added to airline {airline.airline_name}.")



class Flight:

    def __init__(self, date, destination):
        self.date = datetime.date.strftime('%d/%m/%Y')
        self.destination = destination
        self.origin = Airplane.current_location
        self.plane = Airplane()
        self.flight_id = f"{self.destination}{Airline.id}{self.date}"

    def take_off(self):
        return self.origin == None

    def land(self):
        return self.origin == destination


class Airport:

    def __init__(self, city):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []

    def schedule_flight(self):
        self.destination = input("Please choose your destination: ").lower()
        self.datetime = input("Please choose the date using the format (DD/MM/YYYY): ")
        for plane in self.planes:
            if self.planes['next_flights']['date'] == self.datetime and self.planes['next_flights']['destination'] == self.destination:
                print(f"The following Airplane is available on your desired date: {plane}.")
                self.scheduled_departures.append(plane)
                return
            else:
                print("There are no airplanes available matching your requirements.")
                return

    def flights_info(self):
        self.startdate = input(" Please choose your starting date (DD/MM/YYYY): ")
        self.enddate = input(" Please choose your starting date (DD/MM/YYYY): ")
        for flights in self.scheduled_departures:
            if self.scheduled_departures['date'] in range(self.startdate, self.enddate):
                return flights

airline1 = Airline("UA", "United Airlines")
airline2 = Airline("GOL", "Gol Linhas Aereas")
airplane1 = Airplane("United Airlines", "Texas")
airplane2 = Airplane("Gol Linhas Aereas", "Sao Paulo")
airplane1.add_plane(airline1)
airplane2.add_plane(airline2)
gru = Airport("Sao Paulo")
txs = Airport("Texas")
gru.schedule_flight()



