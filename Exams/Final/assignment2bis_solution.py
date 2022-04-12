import shutil
import json
import requests

def run_interface(csvfile):
    while True:
        response = input('Would you like to enter a new route? (y/[n])')
        if response != 'y':
            break
        values = read_values()
        response = input('Would you like to save the values to the file? (y/[n])')
        if response == 'y':
            write_values(values, csvfile)

def read_values():
    print('List of allowed countries:')
    print(get_country_names())
    route = input('Route: ')
    mode = input('Mode: ')
    weeks_ahead = input('Weeks ahead: ')
    eco_passenger_co2 = input('Eco passenger CO2: ')
    raw_travel_time = input('Raw travel time: ')
    ticket_price = input('Ticket price: ')
    return route, mode, weeks_ahead, eco_passenger_co2, raw_travel_time, ticket_price

def write_values(values, csvfile):
    with open(csvfile, "a") as file:
        file.write(','.join(values) + '\n')

# function to get list of country names from web service
def get_country_names():
    response = requests.get("https://restcountries.eu/rest/v2/region/europe") # only Europe
    response_json = json.loads(response.text)
    names = []
    for r in response_json:
        if r["subregion"] not in ("Western Europe", "Central Europe", "Northern Europe"):
            continue
        if r["population"] < 100000:
            continue
        names.append(r["name"]["common"])
    return sorted(names)
        
#################################
# MAIN PROGRAM (do not change!) #
#################################

if __name__ == "__main__":

    # create working copy of original file
    csvfile_orig = "Flights-Trains.csv"
    csvfile_copy = "Flights-Trains_test.csv"
    shutil.copyfile(csvfile_orig, csvfile_copy)
    
    # launch application
    run_interface(csvfile_copy)

