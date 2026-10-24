import customtkinter as ctk
from tkinter import messagebox

def update_select(event):
    catagory=catagorycombo.get()
    if catagory=="Length":
        units=["mm", "cm", "m", "km", "in", "ft", "mi"]
    elif catagory=="Weight":
        units = ["mg", "g", "kg", "t", "oz", "lb"]
    elif catagory=="Temperature":
        units=["C","F","K"]
    else:
        units=[]

    fromcombo.configure(values=units)
    tocombo.configure(values=units)
    fromcombo.set(units[0])
    tocombo.set(units[1])


def convert():
    try:
        catagory=catagorycombo.get()
        value=float(enterentry.get())
        fromunit=fromcombo.get()
        tounit=tocombo.get()
        if catagory=="Length":
            result=length_cal(value,fromunit,tounit)
        elif catagory=="Weight":
            result=weigth_cal(value,fromunit,tounit)
        elif catagory=="Temperature":
            result=temparature_cal(value,fromunit,tounit)
        resultlabel.configure(text=f"{value} {fromunit} = {result} {tounit}")
    except ValueError:
        messagebox.showerror(title="Error",message="Enter a valid number")
    except KeyError:
        messagebox.showerror(title="Error",message="Select a valid unit")



def length_cal(value,fromunit,tounit):
    lunits = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
    "in": 0.0254,
    "ft": 0.3048,
    "mi": 1609.344
    }
    calculation=value*lunits[fromunit]/lunits[tounit]
    return calculation



def weigth_cal(value,fromunit,tounit):
    wunits = {
    "mg": 0.001,
    "g": 1,
    "kg": 1000,
    "t": 1000000,
    "oz": 28.349523125,
    "lb": 453.59237
    }
    calculation=value*wunits[fromunit]/wunits[tounit]
    return calculation
   



def temparature_cal(value,fromunit,tounit):
    if fromunit=="C":
        if tounit=="C":
            calculation=value
        elif tounit=="F":
            calculation=(value * 9/5) + 32
        elif tounit=="K":
            calculation=value + 273.15
    elif fromunit=="F":
        if tounit=="F":
            calculation=value
        elif tounit=="C":
            calculation=(value - 32) * 5/9
        elif tounit=="K":
            calculation=(value - 32) * 5/9 + 273.15
    elif fromunit=="K":
        if tounit=="K":
            calculation=value
        elif tounit=="C":
            calculation=value - 273.15
        elif tounit=="F":
            calculation=(value - 273.15) * 9/5 + 32

    return calculation


window=ctk.CTk()
window.title("Unit Converter")
window.geometry("400x400")

catagorycombo=ctk.CTkComboBox(window,values=["Length","Weight","Temperature"],command=update_select)
catagorycombo.pack()

frame=ctk.CTkFrame(window)
frame.pack()

fromlabel=ctk.CTkLabel(frame,text="From")
fromlabel.grid(row=0,column=0,pady=10,padx=5)
fromcombo=ctk.CTkComboBox(frame)
fromcombo.grid(row=0,column=1,padx=10)

tolabel=ctk.CTkLabel(frame,text="To")
tolabel.grid(row=1,column=0,pady=10,padx=5)
tocombo=ctk.CTkComboBox(frame)
tocombo.grid(row=1,column=1,pady=10)


enterlabel=ctk.CTkLabel(window,text="Enter the value")
enterlabel.pack()
enterentry=ctk.CTkEntry(window)
enterentry.pack()

resultlabel=ctk.CTkLabel(window,text="Result will appear here!")
resultlabel.pack(pady=10)

convertbutton=ctk.CTkButton(window,text="Convert",hover_color="red",command=convert)
convertbutton.pack(pady=10)


update_select("Length")



window.mainloop()