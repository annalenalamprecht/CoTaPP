import pandas as pd
import matplotlib.pyplot as plt

def get_number_of_ticket_prices(df):
    
    # FILL THIS IN
    
    return None # replace by actual return value

def get_list_of_routes(df):
    
    # FILL THIS IN
    
    return None # replace by actual return value

def get_total_ticket_price_for_plane_and_train(df):
    
    # FILL THIS IN
    
    return None, None # replace by actual return value

def get_longest_journey_duration(df):
    
    # FILL THIS IN
    
    return None # replace by actual return value
 
def draw_barchart_of_ticket_price_per_weeks_ahead(df):
    
    # FILL THIS IN
    pass 

def get_three_most_contaminating_flights(df):
    
    # FILL THIS IN
    
    return None # replace by actual return value
    
def draw_comparison_of_routes(df):
    
    # FILL THIS IN
    pass 


#################################
# MAIN PROGRAM (do not change!) #
#################################

if __name__ == "__main__":
    
    # read the date from the file into a dataframe
    df = pd.read_csv("Flights-Trains.csv")
   
    # number of ticket prices
    ntp = get_number_of_ticket_prices(df)
    print(f"There is information from {ntp} ticket prices in the dataset.")
    
    # routes
    routes = get_list_of_routes(df)
    print(f"The analyzed routes are {routes}.")         
    
    # total price for all plane tickets and all train tickets 
    total_plane, total_train = get_total_ticket_price_for_plane_and_train(df)
    print(f"The total ticket price for the plane routes is {total_plane} euro.")
    print(f"The total ticket price for the train routes is {total_train} euro.")
    
    #longest journey duration
    longest = get_longest_journey_duration(df)
    print(f"The longest journey takes {total_plane} minutes.")
    
    #ticket price per weeks ahead
    draw_barchart_of_ticket_price_per_weeks_ahead(df)
    
    # three most contaminating flights 
    three_CO2 = get_three_most_contaminating_flights(df)
    print("The 3 most contaminating flights are:")
    print(three_CO2)
    
    #flight vs train ticket prices
    draw_comparison_of_routes(df)
