import tkinter as tk
import shutil
import json
import requests

class RunApp:
    
    # init function, defining the GUI elements
    def __init__(self, parent, csvfile):
        self.parent = parent
        self.csvfile = csvfile
        self.container_date = tk.Frame(self.parent)
        self.container_date.pack()
        self.date_text = tk.Label(self.container_date, text="Date: ")
        self.date_text.pack(side="left")
        self.date_input = tk.Entry(self.container_date)
        self.date_input.pack(side="left")
        self.container_time = tk.Frame(self.parent)
        self.container_time.pack()
        self.time_text = tk.Label(self.container_time, text="Time: ")
        self.time_text.pack(side="left")
        self.time_input = tk.Entry(self.container_time)
        self.time_input.pack(side='left')
        self.container_distance = tk.Frame(self.parent)
        self.container_distance.pack()
        self.distance_text = tk.Label(self.container_distance, text="Distance: ")
        self.distance_text.pack(side="left")
        self.distance_input = tk.Entry(self.container_distance)
        self.distance_input.pack(side='left')
        self.container_place = tk.Entry(self.parent)
        self.container_place.pack()
        self.place_text = tk.Label(self.container_place, text="Place: ")
        self.place_text.pack(side="left")
        self.place_input = tk.Entry(self.container_place)
        self.place_input.pack(side='left')
        self.country_variable = tk.StringVar()
        country_names = get_country_names()
        self.country_variable.set(country_names)
        self.container_country = tk.Frame(self.parent)
        self.container_country.pack()
        self.country_text = tk.Label(self.container_country, text="Country: ")
        self.country_text.pack(side="left")
        self.country_input = tk.OptionMenu(self.container_country,
                                           self.country_variable,
                                           *country_names)
        self.country_input.pack(side='left')
        self.container_buttons = tk.Frame(self.parent)
        self.container_buttons.pack()
        self.save_button = tk.Button(self.container_buttons)
        self.save_button["text"] = "Save to file"
        self.save_button.pack(side="left")
        self.save_button.bind("<Button-1>", self.writeButtonClick)
        self.exit_button = tk.Button(self.container_buttons,
                                     text="Exit", background="red")
        self.exit_button.pack(side="left")
        self.exit_button.bind("<Button-1>", self.exitButtonClick)

    # function for the save-to-file button
    def writeButtonClick(self, event):
        # Collects the values from the Entry fields and OptionMenu
        date = self.date_input.get()
        time = self.time_input.get()
        distance = self.distance_input.get()
        place = self.place_input.get()
        country = self.country_variable.get()
        # appends them to the CSV file as a new row
        with open(self.csvfile, 'a') as f:
            f.write(','.join([date, time, distance, place, country]) + '\n')

    # function for the exit-button
    def exitButtonClick(self, event):
        self.parent.destroy()

# function to get list of country names from web service
def get_country_names():
    response = requests.get("https://restcountries.com/v3.1/region/europe")
    response_json = json.loads(response.text)
    return [el['name']['common'] for el in response_json]
        
#################################
# MAIN PROGRAM (do not change!) #
#################################

if __name__ == "__main__":

    # create working copy of original file
    csvfile_orig = "run_statistics.csv"
    csvfile_copy = "run_statistics_test.csv"
    shutil.copyfile(csvfile_orig, csvfile_copy)
    
    # launch application
    root = tk.Tk()
    root.title("Marathon Result Registration")
    root.geometry("400x120+300+300")
    app = RunApp(root, csvfile_copy)
    root.mainloop()
    
