import tkinter as tk
import shutil
import json
import requests

class RunApp:
    
    # init function, defining the GUI elements
    def __init__(self, parent, csvfile):
        self.parent = parent
        self.csvfile = csvfile
        
        # FILL THIS IN


    # function for the save-to-file button
    def writeButtonClick(self, event):
        
        # FILL THIS IN
        pass
    
    
    # function for the exit-button
    def exitButtonClick(self, event):

        # FILL THIS IN      
        pass

    

# function to get list of country names from web service
def get_country_names():
    """
    Return a list of European countries in Western, Central or Northern Europe with at least 100000 inhabitants
    """
    
    # FILL THIS IN
    
    return ["Netherlands", "Germany", "UK"] # replace by actual return value    
        
        
#################################
# MAIN PROGRAM (do not change!) #
#################################

if __name__ == "__main__":

    # create working copy of original file
    csvfile_orig = "Flights-Trains.csv"
    csvfile_copy = "Flights-Trains_test.csv"
    shutil.copyfile(csvfile_orig, csvfile_copy)
    
    # launch application
    root = tk.Tk()
    root.title("Route Registration")
    root.geometry("400x250+300+300")
    app = RunApp(root, csvfile_copy)
    root.mainloop()
    
