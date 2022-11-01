from tkinter import *
from tkinter.ttk import Notebook


okno = Tk()

okno.geometry("500x500")

tab_main = Notebook(okno)
tab1 = Frame(tab_main)
tab2 = Frame(tab_main)

tab_main.add(tab1, text= "tab1")
tab_main.add(tab2, text = "tab2")
tab_main.grid()

current_value = DoubleVar()


def get_current_value():
    return '{: .2f}'.format(current_value.get())


def slider_changed(event):
    value_label.configure(text=get_current_value() + 'm')


# label dla slidera
slider_label =Label(
    okno,
    text='Slider:'
)

slider_label.grid(

)

#  slider
slider = Scale(
    okno,
    from_=0,
    to=100,
    orient='horizontal',  # vertical
    command=slider_changed,
    variable=current_value
)

slider.grid(

)

# wartosc labela obecny
current_value_label = Label(
    okno,
    text='Wysokosc masztu:' 
)

current_value_label.grid(
    row=1,
    columnspan=2,
    sticky='n',
    ipadx=10,
    ipady=10
)


value_label = Label(
    okno,
    text=get_current_value() 
)
value_label.grid(
    row=2,
    columnspan=2,
    sticky='n'
)

Button_calc = Button(
    okno, 
    text= 'Oblicz')

Button_calc.grid(
    
)

okno.mainloop()