from tkinter import *
import sqlite3



conn=sqlite3.connect('Flight.db')


root= Tk()

dframe= Frame(root)
dframe.pack(side="top", fill="both", expand=True)

aframe= Frame(root)
aframe.pack(side="bottom", fill="both", expand=True)


labelhd=Label(dframe, text="Dipature Flights")
labelhd.grid(row=0, columnspan=4, sticky=NSEW)

labeld1=Label(dframe, text="Time")
labeld1.grid(row=1, columnspan=4, sticky=NSEW)

labeld2=Label(dframe, text="Flight Name")
labeld2.grid(row=1, column=4, sticky=NSEW)

labeld3=Label(dframe, text="Airline")
labeld3.grid(row=1, column=5, sticky=NSEW)

labeld4=Label(dframe, text="Gate")
labeld4.grid(row=1, column=6, sticky=NSEW)

labeld4=Label(dframe, text="Destination")
labeld4.grid(row=1, column=7, sticky=NSEW)

labeld5=Label(dframe, text="Remarks")
labeld5.grid(row=1, column=8, sticky=NSEW)

i=1
j=0


cursor=conn.execute("SELECT Time_Hours, Time_Minutes, Flight_Name, Airline, Gate, Destination, Remarks FROM DepatureFlight")
for row in cursor:
    i=i+1
    j=0
    labela=Label(dframe, text=row[0])
    labela.grid(row=i, column=j)
    j=j+1
    labela1=Label(dframe, text='Hr')
    labela1.grid(row=i, column=j)
    j=j+1
    
    labelb=Label(dframe, text=row[1])
    labelb.grid(row=i, column=j)
    j=j+1
    labela1=Label(dframe, text='Min')
    labela1.grid(row=i, column=j)
    j=j+1
    labele=Label(dframe, text=row[2])
    labele.grid(row=i, column=j)
    j=j+1
    labelf=Label(dframe, text=row[3])
    labelf.grid(row=i, column=j)
    j=j+1
    labelg=Label(dframe, text=row[4])
    labelg.grid(row=i, column=j)
    j=j+1
    labelh=Label(dframe, text=row[5])
    labelh.grid(row=i, column=j)



labelhd=Label(aframe, text="Arrival Flights")
labelhd.grid(row=0, columnspan=4, sticky=NSEW)

labeld1=Label(aframe, text="Time")
labeld1.grid(row=1, columnspan=4, sticky=NSEW)

labeld2=Label(aframe, text="Flight Name")
labeld2.grid(row=1, column=4, sticky=NSEW)

labeld3=Label(aframe, text="Airline")
labeld3.grid(row=1, column=5, sticky=NSEW)

labeld4=Label(aframe, text="Baggage")
labeld4.grid(row=1, column=6, sticky=NSEW)

labeld4=Label(aframe, text="Origin")
labeld4.grid(row=1, column=7, sticky=NSEW)

labeld5=Label(aframe, text="Remarks")
labeld5.grid(row=1, column=8, sticky=NSEW)

i=1
j=0


cursor=conn.execute("SELECT Time_Hours, Time_Minutes, Flight_Name, Airline, Baggage, Origin, Remarks FROM ArrivalFlight")
for row in cursor:
    i=i+1
    j=0
    labela=Label(aframe, text=row[0])
    labela.grid(row=i, column=j)
    j=j+1
    labela1=Label(aframe, text='Hr')
    labela1.grid(row=i, column=j)
    j=j+1
    
    labelb=Label(aframe, text=row[1])
    labelb.grid(row=i, column=j)
    j=j+1
    labela1=Label(aframe, text='Min')
    labela1.grid(row=i, column=j)
    j=j+1
    labele=Label(aframe, text=row[2])
    labele.grid(row=i, column=j)
    j=j+1
    labelf=Label(aframe, text=row[3])
    labelf.grid(row=i, column=j)
    j=j+1
    labelg=Label(aframe, text=row[4])
    labelg.grid(row=i, column=j)
    j=j+1
    labelh=Label(aframe, text=row[5])
    labelh.grid(row=i, column=j)



conn.close()

root.mainloop()
