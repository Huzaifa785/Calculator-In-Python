
from tkinter import *
from tkinter import messagebox
import math
screen=Tk()
screen.title('Mr.Calc!')
screen.configure(bg='gold')
screen.iconbitmap('Calc1.ico')
screen.maxsize(width=500,height=565)
screen.minsize(width=390,height=565)
screen.geometry('390x570')

def click(number):
    global operator
    operator+=str(number)
    tex.set(operator)

def clear():
    global operator
    operator=''
    tex.set(operator)

def equal():
    try:
        global operator
        result=eval(operator)
        operator=str(result)
        tex.set(result)
    except:
        messagebox.showinfo('Notification','Try again ! Something is wrong .',parent=screen)

def cmdsin():
    try:
        global operator
        result=math.sin(eval(operator))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification','Try again ! Something is wrong .',parent=screen)

def cmdcos():
    try:
        global operator
        result=math.cos(eval(operator))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification','Try again ! Something is wrong .',parent=screen)

def cmdtan():
    try:
        global operator
        result=math.tan(eval(operator))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification','Try again ! Something is wrong .',parent=screen)

def cmdsqrt():
    try:
        global operator
        result=math.sqrt(eval(operator))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification','Try again ! Something is wrong .',parent=screen)

def cmdlog():
    try:
        global operator
        result=math.log(eval(operator))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('Notification','Try again ! Something is wrong .',parent=screen)

#binding functions

def on_enter7(n):
    btn7.configure(bg='aqua')

def on_leave7(n):
    btn7.configure(bg='gold')

def on_enter8(n):
    btn8.configure(bg='aqua')

def on_leave8(n):
    btn8.configure(bg='gold')

def on_enter9(n):
    btn9.configure(bg='aqua')

def on_leave9(n):
    btn9.configure(bg='gold')

def on_enteradd(n):
    btnadd.configure(bg='aqua')

def on_leaveadd(n):
    btnadd.configure(bg='gold')

def on_enter4(n):
    btn4.configure(bg='aqua')

def on_leave4(n):
    btn4.configure(bg='gold')

def on_enter5(n):
    btn5.configure(bg='aqua')

def on_leave5(n):
    btn5.configure(bg='gold')

def on_enter6(n):
    btn6.configure(bg='aqua')

def on_leave6(n):
    btn6.configure(bg='gold')

def on_entersub(n):
    btnsub.configure(bg='aqua')

def on_leavesub(n):
    btnsub.configure(bg='gold')

def on_enter1(n):
    btn1.configure(bg='aqua')

def on_leave1(n):
    btn1.configure(bg='gold')

def on_enter2(n):
    btn2.configure(bg='aqua')

def on_leave2(n):
    btn2.configure(bg='gold')

def on_enter3(n):
    btn3.configure(bg='aqua')

def on_leave3(n):
    btn3.configure(bg='gold')

def on_entermul(n):
    btnmul.configure(bg='aqua')

def on_leavemul(n):
    btnmul.configure(bg='gold')

def on_enter0(n):
        btn0.configure(bg='aqua')

def on_leave0(n):
        btn0.configure(bg='gold')

def on_enterclear(n):
    btnclear.configure(bg='aqua')

def on_leaveclear(n):
    btnclear.configure(bg='gold')

def on_enterequal(n):
    btnequal.configure(bg='aqua')

def on_leaveequal(n):
    btnequal.configure(bg='gold')

def on_enterdiv(n):
    btndiv.configure(bg='aqua')

def on_leavediv(n):
    btndiv.configure(bg='gold')

def on_entryenter(n):
    entry1.configure(bg='aqua',fg='magenta')
def on_entryleave(n):
    entry1.configure(bg='white',fg='magenta')

def on_entersin(n):
    btnsin.configure(bg='aqua')
def on_leavesin(n):
    btnsin.configure(bg='gold')

def on_entercos(n):
    btncos.configure(bg='aqua')
def on_leavecos(n):
    btncos.configure(bg='gold')

def on_entertan(n):
    btntan.configure(bg='aqua')
def on_leavetan(n):
    btntan.configure(bg='gold')

def on_entersqrt(n):
    btnsqrt.configure(bg='aqua')
def on_leavesqrt(n):
    btnsqrt.configure(bg='gold')

def on_enterlog(n):
    btnlog.configure(bg='aqua')
def on_leavelog(n):
    btnlog.configure(bg='gold')

tex=StringVar()
operator=''


entry1=Entry(screen,bg='white',font=('arial',20,'italic bold'),bd=15,justify='right',textvariable=tex)
entry1.grid(row=0,columnspan=4)

#buttons

btn7=Button(screen,text='7',bg='gold',font=('arial',20,'italic bold',),bd=11,padx=16,pady=16,
            command=lambda:click(7),activebackground='white',activeforeground='magenta')
btn7.grid(row=1,column=0)

btn8=Button(screen,text='8',bg='gold',font=('arial',20,'italic bold',),bd=11,padx=16,pady=16,
            command=lambda:click(8),activebackground='white',activeforeground='magenta')
btn8.grid(row=1,column=1)

btn9=Button(screen,text='9',bg='gold',font=('arial',20,'italic bold',),bd=11,padx=16,pady=16,
            command=lambda:click(9),activebackground='white',activeforeground='magenta')
btn9.grid(row=1,column=2)

btnadd=Button(screen,text='+',bg='gold',font=('arial',20,'italic bold',),bd=11,padx=16,pady=16,
              command=lambda:click('+'),activebackground='white',activeforeground='magenta')
btnadd.grid(row=1,column=3)

btn4=Button(screen,text='4',bg='gold',font=('arial',20,'italic bold',),bd=11,padx=16,pady=16,
            command=lambda:click(4),activebackground='white',activeforeground='magenta')
btn4.grid(row=2,column=0)

btn5=Button(screen,text='5',bg='gold',font=('arial',20,'italic bold',),bd=11,padx=16,pady=16,
            command=lambda:click(5),activebackground='white',activeforeground='magenta')
btn5.grid(row=2,column=1)

btn6=Button(screen,text='6',bg='gold',font=('arial',20,'italic bold',),bd=11,padx=16,pady=16,
            command=lambda:click(6),activebackground='white',activeforeground='magenta')
btn6.grid(row=2,column=2)

btnsub=Button(screen,text='-',bg='gold',font=('arial',20,'italic bold',),bd=11,padx=18,pady=16,
              command=lambda:click('-'),activebackground='white',activeforeground='magenta')
btnsub.grid(row=2,column=3)

btn1=Button(screen,text='1',bg='gold',font=('arial',20,'italic bold',),bd=11,padx=16,pady=16,
            command=lambda:click(1),activebackground='white',activeforeground='magenta')
btn1.grid(row=3,column=0)

btn2=Button(screen,text='2',bg='gold',font=('arial',20,'italic bold',),bd=11,padx=16,pady=16,
            command=lambda:click(2),activebackground='white',activeforeground='magenta')
btn2.grid(row=3,column=1)

btn3=Button(screen,text='3',bg='gold',font=('arial',20,'italic bold',),bd=11,padx=16,pady=16,
            command=lambda:click(3),activebackground='white',activeforeground='magenta')
btn3.grid(row=3,column=2)

btnmul=Button(screen,text='*',bg='gold',font=('arial',20,'italic bold',),bd=11,padx=18,pady=16,
              command=lambda:click('*'),activebackground='white',activeforeground='magenta')
btnmul.grid(row=3,column=3)

btn0=Button(screen,text='0',bg='gold',font=('arial',20,'italic bold',),bd=11,padx=16,pady=16,
            command=lambda:click(0),activebackground='white',activeforeground='magenta')
btn0.grid(row=4,column=0)

btnclear=Button(screen,text='C',bg='gold',font=('arial',20,'italic bold',),bd=11,padx=16,pady=16,
                command=clear,activebackground='white',activeforeground='magenta')
btnclear.grid(row=4,column=1)

btnequal=Button(screen,text='=',bg='gold',font=('arial',20,'italic bold',),bd=11,padx=16,pady=16,
                command=equal,activebackground='white',activeforeground='magenta')
btnequal.grid(row=4,column=2)

btndiv=Button(screen,text='/',bg='gold',font=('arial',20,'italic bold',),bd=11,padx=18,pady=16,
              command=lambda:click('/'),activebackground='white',activeforeground='magenta')
btndiv.grid(row=4,column=3)

#Advanced Buttons

btnsin=Button(screen,text='sin',bg='gold',font=('arial',15,'italic bold',),bd=11,padx=14,pady=20,
            command=cmdsin,activebackground='white',activeforeground='magenta')
btnsin.grid(row=0,column=4)

btncos=Button(screen,text='cos',bg='gold',font=('arial',15,'italic bold',),bd=11,padx=14,pady=20,
            command=cmdcos,activebackground='white',activeforeground='magenta')
btncos.grid(row=1,column=4)

btntan=Button(screen,text='tan',bg='gold',font=('arial',15,'italic bold',),bd=11,padx=14,pady=20,
            command=cmdtan,activebackground='white',activeforeground='magenta')
btntan.grid(row=2,column=4)

btnsqrt=Button(screen,text='sqrt',bg='gold',font=('arial',15,'italic bold',),bd=11,padx=10,pady=20,
            command=cmdsqrt,activebackground='white',activeforeground='magenta')
btnsqrt.grid(row=3,column=4)

btnlog=Button(screen,text='log',bg='gold',font=('arial',15,'italic bold',),bd=11,padx=14,pady=20,
            command=cmdlog,activebackground='white',activeforeground='magenta')
btnlog.grid(row=4,column=4)


#binding

btnsin.bind('<Enter>',on_entersin)
btnsin.bind('<Leave>',on_leavesin)

btncos.bind('<Enter>',on_entercos)
btncos.bind('<Leave>',on_leavecos)

btntan.bind('<Enter>',on_entertan)
btntan.bind('<Leave>',on_leavetan)

btnsqrt.bind('<Enter>',on_entersqrt)
btnsqrt.bind('<Leave>',on_leavesqrt)

btnlog.bind('<Enter>',on_enterlog)
btnlog.bind('<Leave>',on_leavelog)

entry1.bind('<Enter>',on_entryenter)
entry1.bind('<Leave>',on_entryleave
            )
btn7.bind('<Enter>',on_enter7)
btn7.bind('<Leave>',on_leave7)

btn8.bind('<Enter>',on_enter8)
btn8.bind('<Leave>',on_leave8)

btn9.bind('<Enter>',on_enter9)
btn9.bind('<Leave>',on_leave9)

btnadd.bind('<Enter>',on_enteradd)
btnadd.bind('<Leave>',on_leaveadd)

btn4.bind('<Enter>',on_enter4)
btn4.bind('<Leave>',on_leave4)

btn5.bind('<Enter>',on_enter5)
btn5.bind('<Leave>',on_leave5)

btn6.bind('<Enter>',on_enter6)
btn6.bind('<Leave>',on_leave6)

btnsub.bind('<Enter>',on_entersub)
btnsub.bind('<Leave>',on_leavesub)

btn1.bind('<Enter>',on_enter1)
btn1.bind('<Leave>',on_leave1)

btn2.bind('<Enter>',on_enter2)
btn2.bind('<Leave>',on_leave2)

btn3.bind('<Enter>',on_enter3)
btn3.bind('<Leave>',on_leave3)

btnmul.bind('<Enter>',on_entermul)
btnmul.bind('<Leave>',on_leavemul)

btn0.bind('<Enter>',on_enter0)
btn0.bind('<Leave>',on_leave0)

btnclear.bind('<Enter>',on_enterclear)
btnclear.bind('<Leave>',on_leaveclear)

btnequal.bind('<Enter>',on_enterequal)
btnequal.bind('<Leave>',on_leaveequal)

btndiv.bind('<Enter>',on_enterdiv)
btndiv.bind('<Leave>',on_leavediv)



screen.mainloop()
