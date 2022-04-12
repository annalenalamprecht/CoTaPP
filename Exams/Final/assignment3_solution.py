# class representing the cost of a trip
class TravelingCost:

    all_traveling_costs = set()
    
    def __init__(self, route, weeks_ahead, company, raw_travel_time, ticket_price):
        self.route = route
        self.weeks_ahead = weeks_ahead
        self.company = company
        self.raw_travel_time = raw_travel_time
        self.ticket_price = ticket_price
        TravelingCost.all_traveling_costs.add(self)

    def print_info(self):
        print(f'{self.route.name} ({self.weeks_ahead} weeks ahead)')
        print(f'Company: {self.company.name}')
        print(f'Raw travel time: {self.raw_travel_time}')
        print(f'Ticket price: {self.ticket_price}')

    @classmethod
    def print_traveling_costs(cls, company):
        costs = []
        for cost in cls.all_traveling_costs:
            if cost.company.name == company.name:
                cost.print_info()

    @classmethod
    def print_all_traveling_costs(cls):
        for cost in cls.all_traveling_costs:
            cost.print_info()

# class representing a travel route
class Route:
    
    def __init__(self, name, mode, eco_passenger_co2):
        self.name = name
        self.mode = mode
        self.eco_passenger_co2 = eco_passenger_co2

    def print_info(self):
        print(f"{self.name} ({self.mode}): {self.eco_passenger_co2} CO2")

    def update_co2(self, co2):
        self.eco_passenger_co2 = co2


class PlaneRoute(Route):
    
    def __init__(self, name, eco_passenger_co2):
        Route.__init__(self, name, 'plane', eco_passenger_co2)


class TrainRoute(Route):

    def __init__(self, name, eco_passenger_co2):
        Route.__init__(self, name, 'train', eco_passenger_co2)

class BusRoute(Route):
    def __init__(self, name, eco_passenger_co2):
        Route.__init__(self, name, 'bus', eco_passenger_co2)

# class representing a travel operator
class Company:
   
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.routes = []

    def add_route(self, route):
        self.routes.append(route)

    def get_routes(self):
        return self.routes

    def print_info(self):
        print(f'{self.name} ({self.country})')
        print('Routes:')
        for route in self.routes:
            route.print_info()


#################################
# MAIN PROGRAM (do not change!) #
#################################


if __name__ == "__main__":

    # create some new routes
    ams_ber_plane = PlaneRoute('Amsterdam-Berlin', 56)
    ams_ber_train = TrainRoute('Amsterdam-Berlin', 27)
    ams_ber_bus = BusRoute('Amsterdam-Berlin', 14)

    # create a company and add a route to it
    db = Company('DB', 'Germany')
    db.add_route(ams_ber_train)

    # create a couple more companies and add routes
    klm = Company('KLM', 'Netherlands')
    klm.add_route(ams_ber_plane)

    flixbus = Company('FlixBus', 'Germany')
    flixbus.add_route(ams_ber_bus)

    # create new travel costs associated with some of those routes
    ams_ber_train_cost = TravelingCost(ams_ber_train, 4, db, 300, 100)
    ams_ber_plane_cost = TravelingCost(ams_ber_plane, 4, klm, 60, 200)

    # print travel cost info
    print('Train traveling costs:')
    ams_ber_train_cost.print_info()
    print('----------------------------')
    
    # Print the traveling costs associated with a company
    print('DB traveling costs:')
    TravelingCost.print_traveling_costs(db)
    print('----------------------------')

    # Print all the traveling costs
    print('All traveling costs:')
    TravelingCost.print_all_traveling_costs()
    print('----------------------------')

    # Update the CO2 associated with a route
    ams_ber_plane.update_co2(120)
    print('Updated plane info:')
    ams_ber_plane.print_info()
    print('----------------------------')

    # Print all the routes for a company
    print('Flixbus routes:')
    for route in flixbus.get_routes():
        route.print_info()
    print('----------------------------')

    # Print the information for one of the companies
    print('KLM info:')
    klm.print_info()
    print('----------------------------')
