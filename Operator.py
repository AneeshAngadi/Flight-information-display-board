import tkinter as tk
import sqlite3


conn = sqlite3.connect('Flight.db')
c = conn.cursor()



TITLE_FONT = ("Verdana", 18)

class Airport(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, ArrivalPage, DepaturePage, UpdatePage, ArrivalUpdate, DepatureUpdate):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame



            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Operator Window", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button2 = tk.Button(self, text="Enter Depature Flight Details",
                            command=lambda: controller.show_frame("DepaturePage"))
        
        button1 = tk.Button(self, text="Enter Arrival Flight Details",
                            command=lambda: controller.show_frame("ArrivalPage"))
        
        button3 = tk.Button(self, text="Update",
                            command=lambda: controller.show_frame("UpdatePage"))
        button4 = tk.Button(self, text="Quit",
                            command=quit)
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
      


class ArrivalPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller    
        label = tk.Label(self, text="Enter Arrival Flight Details", font=TITLE_FONT)
        label.grid(column=2,columnspan=2)
        label1 = tk.Label(self, text="Time: ")
        label1.grid(row=1, column=1, sticky="E")
        label2 = tk.Label(self, text="Flight Name: ")
        label2.grid(row=2, column=1, sticky="E")
        label3 = tk.Label(self, text="Ariline: ")
        label3.grid(row=3, column=1, sticky="E")
        label4 = tk.Label(self, text="Baggage: ")
        label4.grid(row=4, column=1, sticky="E")
        label5 = tk.Label(self, text="Origin: ")
        label5.grid(row=5, column=1, sticky="E")

        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=1, column=2)

        self.entry2 = tk.Entry(self)
        self.entry2.grid(row=1, column=3)
        self.entry3 = tk.Entry(self)
        self.entry3.grid(row=2, column=2)
        self.entry4 = tk.Entry(self)
        self.entry4.grid(row=3, column=2)
        self.entry5 = tk.Entry(self)
        self.entry5.grid(row=4, column=2)
        self.entry6 = tk.Entry(self)
        self.entry6.grid(row=5, column=2)

        self.button = tk.Button(self, text="Submit", command=self.on_button)
        self.button.grid(row=6,column=2, columnspan=2)
        
        button = tk.Button(self, text="Go to Operator Window",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=7,column=2, columnspan=2)

    def on_button(self):
        timehr=self.entry1.get()
        timemin=self.entry2.get()
        flightname=self.entry3.get()
        airline=self.entry4.get()
        baggage=self.entry5.get()
        origin=self.entry6.get()
        print(timehr)
        print(timemin)
        print(flightname)
        print(airline)
        print(baggage)
        print(origin)


        def create_table():
           c.execute('CREATE TABLE IF NOT EXISTS ArrivalFlight(Time_Hours INTEGER, Time_Minutes INTEGER, Flight_Name TEXT, Airline TEXT, Baggage INTEGER, Origin TEXT, Remarks Text)')

        def data_entry():
           c.execute("INSERT INTO ArrivalFlight (Time_Hours, Time_Minutes, Flight_Name, Airline, Baggage, Origin) VALUES (?,?,?,?,?,?)",(timehr, timemin, flightname, airline, baggage, origin))
           conn.commit()
           c.close()
           conn.close()

        create_table()
        data_entry()
        

class DepaturePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller    
        label = tk.Label(self, text="Enter Depature Flight Details", font=TITLE_FONT)
        label.grid(column=2,columnspan=2)
        label1 = tk.Label(self, text="Time: ")
        label1.grid(row=1, column=1, sticky="E")
        label2 = tk.Label(self, text="Flight Name: ")
        label2.grid(row=2, column=1, sticky="E")
        label3 = tk.Label(self, text="Ariline: ")
        label3.grid(row=3, column=1, sticky="E")
        label4 = tk.Label(self, text="Gate: ")
        label4.grid(row=4, column=1, sticky="E")
        label5 = tk.Label(self, text="Destination: ")
        label5.grid(row=5, column=1, sticky="E")

        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=1, column=2)

        self.entry2 = tk.Entry(self)
        self.entry2.grid(row=1, column=3)
        self.entry3 = tk.Entry(self)
        self.entry3.grid(row=2, column=2)
        self.entry4 = tk.Entry(self)
        self.entry4.grid(row=3, column=2)
        self.entry5 = tk.Entry(self)
        self.entry5.grid(row=4, column=2)
        self.entry6 = tk.Entry(self)
        self.entry6.grid(row=5, column=2)

        self.button = tk.Button(self, text="Submit", command=self.on_button)
        self.button.grid(row=6,column=2, columnspan=2)
        
        button = tk.Button(self, text="Go to Operator Window",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=7,column=2, columnspan=2)

    def on_button(self):
        timehr=self.entry1.get()
        timemin=self.entry2.get()
        flightname=self.entry3.get()
        airline=self.entry4.get()
        gate=self.entry5.get()
        destination=self.entry6.get()
        print(timehr)
        print(timemin)
        print(flightname)
        print(airline)
        print(gate)


        def create_table():
           c.execute('CREATE TABLE IF NOT EXISTS DepatureFlight(Time_Hours INTEGER, Time_Minutes INTEGER, Flight_Name TEXT, Airline TEXT, Gate INTEGER, Destination TEXT, Remarks Text)')

        def data_entry():
           c.execute("INSERT INTO DepatureFlight (Time_Hours, Time_Minutes, Flight_Name, Airline, Gate, Destination) VALUES (?,?,?,?,?,?)",(timehr, timemin, flightname, airline, gate, destination))
           conn.commit()
           c.close()
           conn.close()

        create_table()
        data_entry()
        

class UpdatePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Update Flight Details", font=TITLE_FONT)
        label.grid(column=2,columnspan=2)

        button1 = tk.Button(self, text="Update Arrival Flight",
                           command=lambda: controller.show_frame("ArrivalUpdate"))
        button1.grid(row=1,column=2, columnspan=2)
        button2 = tk.Button(self, text="Update Depature Flight",
                           command=lambda: controller.show_frame("DepatureUpdate"))
        button2.grid(row=2,column=2, columnspan=2)
     
        
        button = tk.Button(self, text="Go to Operator Window",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=3,column=2, columnspan=2)



class ArrivalUpdate(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller    
        label = tk.Label(self, text="Update Arrival Flight Details", font=TITLE_FONT)
        label.grid(column=2,columnspan=2)
        label1 = tk.Label(self, text="Flight Name: ")
        label1.grid(row=1, column=1, sticky="E")
        label2 = tk.Label(self, text="Remarks: ")
        label2.grid(row=2, column=1, sticky="E")
        

        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=1, column=2)

        
        self.entry3 = tk.Entry(self)
        self.entry3.grid(row=2, column=2)
        

        self.button = tk.Button(self, text="Submit", command=self.on_button)
        self.button.grid(row=3,column=2, columnspan=2)
        
        button = tk.Button(self, text="Go to Operator Window",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=4,column=2, columnspan=2)

    def on_button(self):
        flightname=self.entry1.get()
        remarks=self.entry3.get()
        print(flightname)
        print(remarks)

        c.execute('SELECT * FROM ArrivalFlight')
        #conn.execute('UPDATE ArrivalFlight SET Remarks=(?) WHERE Baggage=(?)',(remarks, flightname))
        conn.execute('UPDATE ArrivalFlight SET Remarks="Cancelled" WHERE Baggage=7')
        conn.commit()
        
        





class DepatureUpdate(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller    
        label = tk.Label(self, text="Update Depature Flight Details", font=TITLE_FONT)
        label.grid(column=2,columnspan=2)
        label1 = tk.Label(self, text="Flight Name: ")
        label1.grid(row=1, column=1, sticky="E")
        label2 = tk.Label(self, text="Remarks: ")
        label2.grid(row=2, column=1, sticky="E")
        

        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=1, column=2)

        
        self.entry3 = tk.Entry(self)
        self.entry3.grid(row=2, column=2)
        

        self.button = tk.Button(self, text="Submit", command=self.on_button)
        self.button.grid(row=3,column=2, columnspan=2)
        
        button = tk.Button(self, text="Go to Operator Window",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=4,column=2, columnspan=2)

    def on_button(self):
        flightname=self.entry1.get()
        reamrks=self.entry2.get()
        
        print(flightname)
        print(reamrks)

        c.execute('SELECT * FROM DipatureFlight')
        #conn.execute('UPDATE ArrivalFlight SET Remarks=(?) WHERE Baggage=(?)',(remarks, flightname))
        conn.execute('UPDATE DepatureFlight SET Remarks="Cancelled" WHERE Baggage=9')
        conn.commit()



if __name__ == "__main__":
    app = Airport()
    app.mainloop()
