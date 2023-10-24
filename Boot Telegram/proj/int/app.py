from tkinter import *

c1 = '#000000'  # preto
c2 = '#757678'  # claro
c3 = '#919191'  # cinza
c4 = '#f1f52f'  # amarelo
c5 = '#1c1c1c'  # cinza
c6 = '#fcfcfc'

w = Tk()
w.title('Cronometer')
w.geometry('700x390')
w.resizable(width=False, height=False)
w.config(bg=c3)

mil = 0
seg = 0
min = 0
hour = 0
time = '00:00:00:000'
flag = 0
count = 0
laps = []
i = 1


def start():

  global mil, seg, min, hour, time, flag

  mil = mil + 1
  if mil == 1000:
    mil = 0
    seg = seg + 1
    if seg == 60:
      seg = 0
      min = min + 1
      if min == 60:
        min = 0
        hour = hour + 1

  time = str(hour) + ':' + str(min) + ':' + str(seg) + ':' + str(mil)
  app_label.config(text=time)

  if flag == 0:
    app_label.after(1, start)


def stop():
  global flag
  flag = 1
  app_label.config(text=time)


def contin():
  global flag
  flag = 0
  app_label.after(1, start)


def restart():
  global mil, seg, min, hour, flag, time
  mil = 0
  seg = 0
  min = 0
  hour = 0
  time = '00:00:00:000'
  flag = 0
  app_label.after(1, start)


def lap():
  global count, laps, i
  count = count + 1
  lap = 'Lap ' + str(count) + ':               ' + str(time)
  laps.append(lap)

  app_lap_atual.config(text=lap)

  if len(laps) <= 1:
    app_laps_1.config(text='Lap 1:             ' + str(laps[0][15:]))
  elif len(laps) == 2:
    app_laps_1.config(text='Lap 1:             ' + str(laps[0][15:]))
    app_laps_2.config(text='Lap 2:             ' + str(laps[1][15:]))
  elif len(laps) == 3:
    app_laps_1.config(text='Lap 1:             ' + str(laps[0][15:]))
    app_laps_2.config(text='Lap 2:             ' + str(laps[1][15:]))
    app_laps_3.config(text='Lap 3:             ' + str(laps[2][15:]))
  elif len(laps) == 4:
    app_laps_1.config(text='Lap 1:             ' + str(laps[0][15:]))
    app_laps_2.config(text='Lap 2:             ' + str(laps[1][15:]))
    app_laps_3.config(text='Lap 3:             ' + str(laps[2][15:]))
    app_laps_4.config(text='Lap 4:             ' + str(laps[3][15:]))
  else:
    app_laps_1.config(text='Lap 1:             ' + str(laps[i][15:]))
    app_laps_2.config(text='Lap 2:             ' + str(laps[i + 1][15:]))
    app_laps_3.config(text='Lap 3:             ' + str(laps[i + 2][15:]))
    app_laps_4.config(text='Lap 4:             ' + str(laps[i + 3][15:]))
    i = i + 1


def restart_laps():
  global laps, count, i
  i = 0
  count = 0
  while len(laps) != 0:
    laps.pop()

  app_lap_atual.config(text='No Lap')
  app_laps_1.config(text=' ')
  app_laps_2.config(text=' ')
  app_laps_3.config(text=' ')
  app_laps_4.config(text=' ')


def reset():
  global mil, seg, min, hour, flag, time
  mil = 0
  seg = 0
  min = 0
  hour = 0
  time = '00:00:00:000'
  flag = 0
  restart_laps()
  app_label.config(text=time)
  app_lap_atual.config(text='No Lap')


frame_cron = Frame(w, width=700, height=120)
frame_cron.grid(row=0, column=0, sticky=NW)

frame_laps = Frame(w, width=700, height=140, bg=c6)
frame_laps.grid(row=1, column=0, sticky=NW)

frame_corpo = Frame(w, width=700, height=140, bg=c5)
frame_corpo.grid(row=2, column=0, sticky=NW)

app_label = Label(frame_cron,
                  text=time,
                  width=12,
                  height=1,
                  font=('Arial 70'),
                  fg=c4,
                  bg=c1)
app_label.grid(row=0, column=0)

app_lap_atual = Label(frame_laps,
                      text='No Lap',
                      width=60,
                      height=1,
                      font=('Arial 17'),
                      anchor='w',
                      fg=c6,
                      bg=c1)
app_lap_atual.grid(row=0, column=0)

app_laps_1 = Label(frame_laps,
                   text=' ',
                   width=75,
                   height=1,
                   font=('Arial 14'),
                   anchor='w',
                   fg=c6,
                   bg=c1)
app_laps_1.grid(row=1, column=0)

app_laps_2 = Label(frame_laps,
                   text=' ',
                   width=75,
                   height=1,
                   font=('Arial 14'),
                   anchor='w',
                   fg=c6,
                   bg=c1)
app_laps_2.grid(row=2, column=0)

app_laps_3 = Label(frame_laps,
                   text=' ',
                   width=75,
                   height=1,
                   font=('Arial 14'),
                   anchor='w',
                   fg=c6,
                   bg=c1)
app_laps_3.grid(row=3, column=0)

app_laps_4 = Label(frame_laps,
                   text=' ',
                   width=75,
                   height=1,
                   font=('Arial 14'),
                   anchor='w',
                   fg=c6,
                   bg=c1)
app_laps_4.grid(row=4, column=0)

b_start = Button(frame_corpo,
                 command=start,
                 text='Start',
                 font=('Arial 10 bold'),
                 width=12,
                 height=2,
                 bg=c3)
b_start.place(x=15, y=15)

b_stop = Button(frame_corpo,
                command=stop,
                text='Stop',
                font=('Arial 10 bold'),
                width=12,
                height=2,
                bg=c3)
b_stop.place(x=15, y=75)

b_continue = Button(frame_corpo,
                    command=contin,
                    text='Continue',
                    font=('Arial 10 bold'),
                    width=12,
                    height=2,
                    bg=c3)
b_continue.place(x=190, y=15)

b_restart = Button(frame_corpo,
                   command=restart,
                   text='Restart',
                   font=('Arial 10 bold'),
                   width=12,
                   height=2,
                   bg=c3)
b_restart.place(x=190, y=75)

b_lap = Button(frame_corpo,
               command=lap,
               text='Lap',
               font=('Arial 10 bold'),
               width=12,
               height=2,
               bg=c3)
b_lap.place(x=365, y=15)

b_restart_laps = Button(frame_corpo,
                        command=restart_laps,
                        text='Restart Laps',
                        font=('Arial 10 bold'),
                        width=12,
                        height=2,
                        bg=c3)
b_restart_laps.place(x=365, y=75)

b_RESET = Button(frame_corpo,
                 command=reset,
                 text='RESET ALL',
                 font=('Arial 10 bold'),
                 width=12,
                 height=5,
                 bg=c3)
b_RESET.place(x=535, y=18)

w.mainloop()
