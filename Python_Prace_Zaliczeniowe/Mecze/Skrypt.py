
from ctypes.wintypes import VARIANT_BOOL
from errno import errorcode
import pandas as pd
from tkinter import *
import openpyxl





#odczyt i manipulacja danymi
df = pd.read_excel(r'Skoroszyt_1.xlsx', engine='openpyxl')
col_list = df[df.columns[0]].values.tolist()
col_list1 = df[df.columns[0]].values.tolist()


#okienko
window = Tk()
window.geometry("600x600")
variable = StringVar(window)
variable1 = StringVar(window)


    
def Write():
    jeden = (variable.get())
    dwa = (variable1.get())
    wynik = str_out2.set(TextTeam1_Goals.get("1.0",END))
    if jeden == dwa:
        Err = Label(window, text = "BLAD! Nie moga byc dwie druzyny o tej samej nazwie", height = 5)
        Err.grid()
        
    else:
       jeden = str_out.set(variable.get())
       dwa = str_out1.set(variable1.get())
       
       df_mecze = pd.DataFrame({'mecze': [variable.get(), variable1.get()]})
       df["mecze"] = df_mecze
       
       df_gole = pd.DataFrame({'wynik' : [TextTeam1_Goals.get("1.0",END)] })
       df['wynik'] = df_gole
       #wpisanie dwoch meczy do pliku Excel
       df.to_excel("Skoroszyt_OG.xlsx",index=False)
       
       
        

#wybor druzyny 1
LabelTeam1 = Label(window, text = "Select first team", height = 5)
SelectTeam1 = OptionMenu(window, variable, *col_list)

#wybor druzyny 2
LabelTeam2 = Label(window, text = "Select second team", height = 5)
SelectTeam2 = OptionMenu(window, variable1, *col_list1)

#ilosc goli
LabelTeam1_goals = Label(window, text = "Wpisz wynik meczu: ")
TextTeam1_Goals = Text(window, height=3, width=10)

Przycisk = Button(window, text = "Wpisz mecz i wynik do csv", command= Write)


#output druzyna 1
str_out=StringVar(window)
str_out.set("Druzyna1")

#output druzyna 2
str_out1=StringVar(window)
str_out1.set("Druzyna2")

#output wynik meczu
str_out2 = StringVar(window)
str_out2.set("Wynik spotkania")


#label outputow
LabelResult = Label(window, textvariable= str_out, width=20 )
LabelResult1 = Label(window, textvariable= str_out1, width=20 )
LabelResult2 = Label(window, textvariable=str_out2, width=20)



LabelTeam1.grid()
SelectTeam1.grid()

LabelTeam2.grid()
SelectTeam2.grid()

LabelTeam1_goals.grid()
TextTeam1_Goals.grid()

Przycisk.grid(pady = 10)

LabelResult.grid()
LabelResult1.grid()
LabelResult2.grid()



print(df)
print()


mainloop()
