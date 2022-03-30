import tkinter as tk

class HelloWorldApp:

    def __init__(self,parent):
        self.parent = parent

        self.container1 = tk.Frame(parent)
        self.container1.pack()

        self.hwtext = tk.Label(self.container1)
        self.hwtext.configure(text="",background="white")
        self.hwtext.pack(side="left")

        self.container2 = tk.Frame(parent)
        self.container2.pack()

        self.hwbutton = tk.Button(self.container2)
        self.hwbutton["text"] = "Say hello!"
        self.hwbutton.pack(side="left")
        self.hwbutton.bind("<Button-1>", self.hwbuttonClick)

        self.gbbutton = tk.Button(self.container2,
                                  text="Goodbye!", background="red")
        self.gbbutton.pack(side="left")
        self.gbbutton.bind("<Enter>", self.gbbuttonClick)

    def hwbuttonClick(self,event):
        self.hwtext.configure(text="Hello World!")

    def gbbuttonClick(self,event):
        self.parent.destroy()

root = tk.Tk()
hwapp = HelloWorldApp(root)
root.mainloop()
