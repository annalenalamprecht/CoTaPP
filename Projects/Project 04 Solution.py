import tkinter as tk
import random

def create_random_numbers():
    # noinspection PyTypeChecker
    bottom_row = ['S'] + [random.randint(0, 9) for _ in range(4)]
    # noinspection PyTypeChecker
    top_row = [random.randint(0, 9) for _ in range(4)] + ['G']
    return [bottom_row] + [[random.randint(0, 9) for _ in range(5)] for _ in range(4)] + [top_row]

def get_default_numbers():
    return [['S', 0, 1, 3, 5], [3, 1, 0, 2, 0], [2, 2, 0, 2, 1], [1, 2, 0, 2, 3], [2, 0, 1, 1, 'G']]


# noinspection PyUnusedLocal
def get_canvas(parent, numbers):
    container0 = tk.Canvas(parent, width=100, height=100)
    container0.create_oval(0, 0, 100, 100, fill="yellow")
    container0.create_oval(45, 45, 55, 55, fill="red")
    container0.create_oval(25, 25, 35, 35, fill="blue")
    container0.create_oval(65, 25, 75, 35, fill="blue")
    container0.create_arc(25, 55, 75, 80, fill="red",
                               style="arc", start=180, extent=180)
    container0.pack()
    return container0

def get_frame(parent, numbers):
    my_numbers = numbers.copy()
    my_numbers.reverse()
    grand_container = tk.Frame(parent)
    grand_container.pack()
    for row in my_numbers:
        container = tk.Frame(grand_container)
        container.pack()
        for el in row:
            label = tk.Label(container)
            background = 'gray' if type(el) == str else 'white'
            label.configure(text=str(el), background=background)
            label.pack(side='left')
    return grand_container

class PathfinderApp:

    def __init__(self, parent):
        self.parent = parent
        self.numbers = get_default_numbers()
        self.container0 = get_frame(self.parent, self.numbers)

        self.container1 = tk.Frame(parent)
        self.container1.pack()
        self.best_path_text = tk.Label(self.container1)
        self.best_path_text.configure(text="", background="white")
        self.best_path_text.pack(side="left")

        self.container2 = tk.Frame(parent)
        self.container2.pack()
        self.find_best_path_button = tk.Button(self.container2)
        self.find_best_path_button["text"] = "Find best path"
        self.find_best_path_button.pack(side="left")
        self.find_best_path_button.bind("<Button-1>", self.findBestPathButtonClick)
        self.new_numbers_button = tk.Button(self.container2,
                                            text="Create new random field")
        self.new_numbers_button.pack(side="left")
        self.new_numbers_button.bind("<Button-1>", self.createNewRandomFieldClick)
        self.exit_button = tk.Button(self.container2,
                                     text='Exit program')
        self.exit_button.pack(side='left')
        self.exit_button.bind("<Button-1>", self.exitProgramClick)

    # noinspection PyUnusedLocal
    def findBestPathButtonClick(self, event):
        score = self.find_best_path()
        self.best_path_text.configure(text=f"Maximal possible score: {score}")

    # noinspection PyUnusedLocal
    def createNewRandomFieldClick(self, event):
        # Todo: this new field should replace the existing one
        self.numbers = create_random_numbers()
        self.best_path_text.configure(text='')
        self.container0 = get_frame(self.parent, self.numbers)
        self.container0.pack()

    # noinspection PyUnusedLocal
    def exitProgramClick(self, event):
        self.parent.destroy()

    # noinspection PyMethodMayBeStatic
    def find_best_path(self):
        # Todo: this should traverse self.numbers, find the best score, and draw it on the frame
        return 'unknown'

root = tk.Tk()
pathfinderApp = PathfinderApp(root)
root.mainloop()
