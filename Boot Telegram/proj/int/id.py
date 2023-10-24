from tkinter import *
from tkinter import ttk

c1 = '#2a2c36'  #escuro
c2 = '#b1b7c9'  #claro
c3 = '#1d331d'  #verde

w_main = Tk()
w_main.title('Age Calculator')
w_main.geometry('400x200')
w_main.config(bg=c2)

value_entry = ' '
value_age = StringVar()


def calculate():
  global value_entry
  event = int(entry_age.get())
  value_entry = str(eval(str(2023 - event)))
  value_age.set(value_entry + ' years')
  entry_age.delete(0, END)


frame_corpo = Frame(w_main, width=400, height=150, bg=c2)
frame_corpo.place(x=0, y=0)

frame_age = Frame(w_main, width=400, height=50, bg=c2)
frame_age.place(x=0, y=140)

label_bday = Label(frame_corpo,
                   text=' Birthday: ',
                   width=0,
                   height=3,
                   font=('Arial 15 bold'),
                   bg=c2)
label_bday.place(x=0, y=0)

entry_age = Entry(frame_corpo, width=25, font=('Arial 10 bold'))
entry_age.place(x=130, y=28)

b_day = Button(frame_corpo,
               command=calculate,
               text='Your Age',
               width=18,
               height=2,
               fg=c1,
               font=('Arial 12 bold'))
b_day.place(x=135, y=80)

app_age = Label(frame_age,
                textvariable=value_age,
                width=12,
                height=2,
                font=('Arial 20 bold'),
                bg=c2)
app_age.place(x=150, y=0)

w_main.mainloop()
