# class representing the cost of a trip
class TravelingCost:

    all_traveling_costs = dict()
    
    def __init__(self, route, weeks_ahead, company, raw_travel_time, ticket_price):
        
        # FILL THIS IN
        pass

    def print_info(self):
        # FILL THIS IN
        pass
        
    @classmethod
    def print_traveling_costs(cls, company):
        
        # FILL THIS IN
        pass
        
    @classmethod
    def print_all_traveling_costs(cls):
        
        # FILL THIS IN
        pass

# class representing a travel route
class Route:
    
    def __init__(self, name, mode, eco_passenger_co2):
        self.name = name
        self.mode = mode
        self.eco_passenger_co2 = eco_passenger_co2

    def print_info(self):
        print(f"{self.name} ({self.mode}): {self.eco_passenger_co2} CO2")

    def update_co2(self, co2):
        # FILL THIS IN
        pass
        

class PlaneRoute(Route):
    
    def __init__(self, name, eco_passenger_co2):
 
        # FILL THIS IN
        pass


class TrainRoute(Route):

    def __init__(self, name, eco_passenger_co2):

        # FILL THIS IN
        pass

class BusRoute(Route):
    def __init__(self, name, eco_passenger_co2):
        # FILL THIS IN
        pass
    
# class representing a travel operator
class Company:
   
    def __init__(self, name, country):
        
        # FILL THIS IN
        pass
        
    def add_route(self, route):
 
        # FILL THIS IN
        pass
        
    def get_routes(self):
  
        # FILL THIS IN
        pass
            
    def print_info(self):

        # FILL THIS IN
        pass
    

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
    ams_ber_train_cost.print_info()
    print()
    
    # Print the traveling costs associated with a company
    TravelingCost.print_traveling_costs(db)

    # Print all the traveling costs
    TravelingCost.print_all_traveling_costs()

    # Update the CO2 associated with a route
    ams_ber_plane.update_co2(120)
    ams_ber_plane.print_info()
    print()

    # Print all the routes for a company
    print(flixbus.get_routes())

    # Print the information for one of the companies
    print(klm.print_info())
