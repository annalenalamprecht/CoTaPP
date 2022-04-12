import shutil
import json
import requests

def run_interface(csvfile):
    # FILL THIS IN
    pass

def read_values():
    # FILL THIS IN
    pass

def write_values(values, csvfile):
    # FILL THIS IN
    pass

# function to get list of country names from web service
def get_country_names():
    """
    Return a list of European countries in Western, Central or Northern Europe with at least 100000 inhabitants
    """
    # FILL THIS IN
    pass

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
