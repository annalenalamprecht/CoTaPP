import tkinter as tk
import shutil
import json
import requests

class RunApp:
    
    # init function, defining the GUI elements
    def __init__(self, parent, csvfile):
        self.parent = parent
        self.csvfile = csvfile

        # add labels and text fields for the information to enter
        self.container_orig = tk.Frame(self.parent)
        self.lbl_orig = tk.Label(self.container_orig, text="Origin: ")
        self.lbl_orig.pack(side="left")
        self.input_orig = tk.Entry(self.container_orig)
        self.input_orig.pack(side="right")
        self.container_orig.pack()

        self.container_dest = tk.Frame(self.parent)
        self.lbl_dest = tk.Label(self.container_dest, text="Destination: ")
        self.lbl_dest.pack(side="left")
        self.input_dest = tk.Entry(self.container_dest)
        self.input_dest.pack(side="right")
        self.container_dest.pack()

        self.container_mode = tk.Frame(self.parent)
        self.lbl_mode = tk.Label(self.container_mode, text="Mode: ")
        self.lbl_mode.pack(side="left")
        self.input_mode = tk.Entry(self.container_mode)
        self.input_mode.pack(side="right")
        self.container_mode.pack()

        self.container_weeks = tk.Frame(self.parent)
        self.lbl_weeks = tk.Label(self.container_weeks, text="Weeks ahead: ")
        self.lbl_weeks.pack(side="left")
        self.input_weeks = tk.Entry(self.container_weeks)
        self.input_weeks.pack(side="right")
        self.container_weeks.pack()

        self.container_co2 = tk.Frame(self.parent)
        self.lbl_co2 = tk.Label(self.container_co2, text="Eco passenger CO2: ")
        self.lbl_co2.pack(side="left")
        self.input_co2 = tk.Entry(self.container_co2)
        self.input_co2.pack(side="right")
        self.container_co2.pack()

        self.container_time = tk.Frame(self.parent)
        self.lbl_time = tk.Label(self.container_time, text="Raw travel time: ")
        self.lbl_time.pack(side="left")
        self.input_time = tk.Entry(self.container_time)
        self.input_time.pack(side="right")
        self.container_time.pack()

        self.container_price = tk.Frame(self.parent)
        self.lbl_price = tk.Label(self.container_price, text="Ticket price: ")
        self.lbl_price.pack(side="left")
        self.input_price = tk.Entry(self.container_price)
        self.input_price.pack(side="right")
        self.container_price.pack()

        # add buttons for writing info to CSV file and for quitting
        self.container_buttons = tk.Frame(self.parent)
        self.write_button = tk.Button(self.container_buttons, text="Save to file")
        self.write_button.pack(side="left")
        self.write_button.bind("<Button-1>", self.writeButtonClick)
        self.exit_button = tk.Button(self.container_buttons, text="Exit")
        self.exit_button.pack(side="left")
        self.exit_button.bind("<Button-1>", self.exitButtonClick)
        self.container_buttons.pack()

        # Add a label with the allowed countries
        self.container_co2 = tk.Frame(self.parent)
        self.lbl_co2 = tk.Label(self.container_co2,
                                text=f"IMPORTANT: allowed countries:\n{get_country_names()}",
                                wraplength=400)
        self.lbl_co2.pack(side="left")
        self.container_co2.pack()

    # function for the save-to-file button
    def writeButtonClick(self, event):
        members = (f'{self.input_orig.get()}-{self.input_dest.get()}',
                   self.input_mode.get(),
                   self.input_weeks.get(),
                   self.input_co2.get(),
                   self.input_time.get(),
                   self.input_price.get())
        with open(self.csvfile, "a") as file:
            file.write(','.join([el for el in members]) + '\n')

    # function for the exit-button
    def exitButtonClick(self, event):
        self.parent.destroy()

    

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
    root = tk.Tk()
    root.title("Route Registration")
    root.geometry("400x250+300+300")
    app = RunApp(root, csvfile_copy)
    root.mainloop()
    
