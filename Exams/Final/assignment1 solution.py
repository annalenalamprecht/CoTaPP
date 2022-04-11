import pandas as pd
import matplotlib.pyplot as plt
import time

def get_number_of_ticket_prices(df):
    return len(df)

def get_list_of_routes(df):
    routes = pd.unique(df["Route"])
    #routes = set(df["Route"])
    return routes

def get_total_ticket_price_for_plane_and_train(df):
    total_plane = df[df["Mode"] == "Plane"]["Ticket price"].sum()
    total_train = df[df["Mode"] == "Train"]["Ticket price"].sum()
    return total_plane, total_train

def get_longest_journey_duration(df):
    return max(df["Raw travel time"])
 
def draw_barchart_of_ticket_price_per_weeks_ahead(df):
    df_grouped_by_weeks = df.groupby("WeeksAhead").sum()
    plt.bar(df_grouped_by_weeks.index, df_grouped_by_weeks["Ticket price"])
    plt.title("Total ticket price per WeeksAhead")
    plt.show()  

def get_three_most_contaminating_flights(df):
    routes = df[(df["Mode"]=="Plane") & (df["WeeksAhead"]==1) ]
    routes = routes.sort_values(by="EcoPassengerCO2", ascending=False)
    return routes.head(3)
    
def draw_comparison_of_routes(df):
    routes = get_list_of_routes(df)
    for route in routes:
        data = df[df["Route"] == route]
        data_p = data[data["Mode"] == "Plane"]
        data_t = data[data["Mode"] == "Train"]
        plt.plot(data_p["WeeksAhead"], data_p["Ticket price"], color="red")
        plt.plot(data_t["WeeksAhead"], data_t["Ticket price"], color="blue")
        plt.title(route)
        plt.legend(['Plane', 'Train'], loc="upper right")
        plt.show()


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
    print()
    
    #flight vs train ticket prices
    draw_comparison_of_routes(df)
