from tkinter import *
from tkinter import ttk

cor1 = '#1e1f1e'
cor2 = '#feffff'
cor3 = '#38576b'
cor4 = '#ECEFF1'
cor5 = '#FFAB40'

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x316')
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

todos_valores = ' '
valor_texto = StringVar()


def entrar_valores(event):
  global todos_valores
  todos_valores = todos_valores + str(event)
  valor_texto.set(todos_valores)


def calculo():
  global todos_valores
  resultado = str(eval(todos_valores))
  imprimir(resultado)


def limpar_tela():
  global todos_valores
  todos_valores = ''
  imprimir('')


def limpar_ultimo():
  global todos_valores
  todos_valores = todos_valores[:-1]
  imprimir(todos_valores)


def imprimir(value):
  if str(value) == '0':
    valor_texto.set('ERR')
  else:
    valor_texto.set(value)
    

app_label = Label(frame_tela,
                  textvariable=valor_texto,
                  width=20,
                  height=3,
                  padx=7,
                  relief=FLAT,
                  anchor='e',
                  justify=RIGHT,
                  font=('Ivy 13'),
                  bg=cor3,
                  fg=cor2)
app_label.place(x=0, y=0)

b_19 = Button(frame_corpo,
              command=limpar_tela,
              text='AC',
              width=3,
              height=2,
              bg=cor4,
              font=('Ivy 13 bold'),
              relief=RAISED,
              overrelief=RIDGE)
b_19.place(x=0, y=0)

b_1 = Button(frame_corpo,
             command=limpar_ultimo,
             text='C',
             width=3,
             height=2,
             bg=cor4,
             font=('Ivy 13 bold'),
             relief=RAISED,
             overrelief=RIDGE)
b_1.place(x=59, y=0)

b_2 = Button(frame_corpo,
             command=lambda: entrar_valores('%'),
             text='%',
             width=3,
             height=2,
             bg=cor4,
             font=('Ivy 13 bold'),
             relief=RAISED,
             overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(frame_corpo,
             command=lambda: entrar_valores('/'),
             text='/',
             width=3,
             height=2,
             bg=cor5,
             fg=cor2,
             font=('Ivy 13 bold'),
             relief=RAISED,
             overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo,
             command=lambda: entrar_valores('7'),
             text='7',
             width=3,
             height=2,
             bg=cor4,
             font=('Ivy 13 bold'),
             relief=RAISED,
             overrelief=RIDGE)
b_4.place(x=0, y=52)

b_5 = Button(frame_corpo,
             command=lambda: entrar_valores('8'),
             text='8',
             width=3,
             height=2,
             bg=cor4,
             font=('Ivy 13 bold'),
             relief=RAISED,
             overrelief=RIDGE)
b_5.place(x=59, y=52)

b_6 = Button(frame_corpo,
             command=lambda: entrar_valores('9'),
             text='9',
             width=3,
             height=2,
             bg=cor4,
             font=('Ivy 13 bold'),
             relief=RAISED,
             overrelief=RIDGE)
b_6.place(x=118, y=52)

b_7 = Button(frame_corpo,
             command=lambda: entrar_valores('*'),
             text='*',
             width=3,
             height=2,
             bg=cor5,
             fg=cor2,
             font=('Ivy 13 bold'),
             relief=RAISED,
             overrelief=RIDGE)
b_7.place(x=177, y=52)

b_8 = Button(frame_corpo,
             command=lambda: entrar_valores('4'),
             text='4',
             width=3,
             height=2,
             bg=cor4,
             font=('Ivy 13 bold'),
             relief=RAISED,
             overrelief=RIDGE)
b_8.place(x=0, y=104)

b_9 = Button(frame_corpo,
             command=lambda: entrar_valores('5'),
             text='5',
             width=3,
             height=2,
             bg=cor4,
             font=('Ivy 13 bold'),
             relief=RAISED,
             overrelief=RIDGE)
b_9.place(x=59, y=104)

b_10 = Button(frame_corpo,
              command=lambda: entrar_valores('6'),
              text='6',
              width=3,
              height=2,
              bg=cor4,
              font=('Ivy 13 bold'),
              relief=RAISED,
              overrelief=RIDGE)
b_10.place(x=118, y=104)

b_11 = Button(frame_corpo,
              command=lambda: entrar_valores('-'),
              text='-',
              width=3,
              height=2,
              bg=cor5,
              fg=cor2,
              font=('Ivy 13 bold'),
              relief=RAISED,
              overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(frame_corpo,
              command=lambda: entrar_valores('1'),
              text='1',
              width=3,
              height=2,
              bg=cor4,
              font=('Ivy 13 bold'),
              relief=RAISED,
              overrelief=RIDGE)
b_12.place(x=0, y=156)

b_13 = Button(frame_corpo,
              command=lambda: entrar_valores('2'),
              text='2',
              width=3,
              height=2,
              bg=cor4,
              font=('Ivy 13 bold'),
              relief=RAISED,
              overrelief=RIDGE)
b_13.place(x=59, y=156)

b_14 = Button(frame_corpo,
              command=lambda: entrar_valores('3'),
              text='3',
              width=3,
              height=2,
              bg=cor4,
              font=('Ivy 13 bold'),
              relief=RAISED,
              overrelief=RIDGE)
b_14.place(x=118, y=156)

b_15 = Button(frame_corpo,
              command=lambda: entrar_valores('+'),
              text='+',
              width=3,
              height=2,
              bg=cor5,
              fg=cor2,
              font=('Ivy 13 bold'),
              relief=RAISED,
              overrelief=RIDGE)
b_15.place(x=177, y=156)

b_16 = Button(frame_corpo,
              command=lambda: entrar_valores('0'),
              text='0',
              width=8,
              height=2,
              bg=cor4,
              font=('Ivy 13 bold'),
              relief=RAISED,
              overrelief=RIDGE)
b_16.place(x=0, y=208)

b_17 = Button(frame_corpo,
              command=lambda: entrar_valores('.'),
              text='.',
              width=3,
              height=2,
              bg=cor4,
              font=('Ivy 13 bold'),
              relief=RAISED,
              overrelief=RIDGE)
b_17.place(x=118, y=208)

b_18 = Button(frame_corpo,
              command=calculo,
              text='=',
              width=3,
              height=2,
              bg=cor5,
              fg=cor2,
              font=('Ivy 13 bold'),
              relief=RAISED,
              overrelief=RIDGE)
b_18.place(x=177, y=208)

janela.mainloop()
