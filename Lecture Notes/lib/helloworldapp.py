import tkinter as tk      

class HelloWorldApp:
    
    def __init__(self,parent):
        self.parent = parent
        
        self.container0 = tk.Canvas(parent, width=100, height=100)
        self.container0.create_oval(0,0,100,100,fill="yellow")
        self.container0.create_oval(45,45,55,55,fill="red")
        self.container0.create_oval(25,25,35,35,fill="blue")
        self.container0.create_oval(65,25,75,35,fill="blue")
        self.container0.create_arc(25,55,75,80,fill="red",style="arc",start=180,extent=180)
        self.container0.pack()
        
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
        self.gbbutton = tk.Button(self.container2, text="Goodbye!", background="red")
        self.gbbutton.pack(side="left")
        self.gbbutton.bind("<Button-1>", self.gbbuttonClick)

    
    def hwbuttonClick(self,event):
        self.hwtext.configure(text="Hello World!")
    
    def gbbuttonClick(self,event):
        self.parent.destroy()

root = tk.Tk()
root.title('Hello!')
hwapp = HelloWorldApp(root)
root.mainloop()   
