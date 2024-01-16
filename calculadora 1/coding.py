from tkinter import *

a= Tk()  

a.geometry("460x300+450+200") 

a.maxsize(460,300)

a.minsize(460,300)

a.title("Calculadora")

a.configure(background="white")

bc="white"

def fun(e):
    t1.insert(END,e)

def Res():
    try:
        val=eval(t1.get("1.0",END))
        t1.delete("1.0",END)
        t1.insert("1.0",val)
    except:
        error="Error"
        t1.delete("1.0",END)
        t1.insert("1.0",error)

f=Frame()

f.grid(row=1)

f2=Frame()

f2.grid(row=0)

t1=Text(f2,bg="white",width=40,height=2.5)

t1.grid(row=0,column=1)

b1=Button(f,text="1",bg=bc,command =lambda : fun("1"),width=15,height=3)

b1.grid(row=3,column=0)

b2=Button(f,text="2",bg=bc,command = lambda : fun("2"),width=15,height=3)

b2.grid(row=3,column=1)

b3=Button(f,text="3",bg=bc,command = lambda : fun("3"),width=15,height=3)

b3.grid(row=3,column=2)

b4=Button(f,text="4",bg=bc,command = lambda : fun("4"),width=15,height=3)

b4.grid(row=2,column=0)

b5=Button(f,text="5",bg=bc,command = lambda : fun("5"),width=15,height=3)

b5.grid(row=2,column=1)

b6=Button(f,text="6",bg=bc,command = lambda : fun("6"),width=15,height=3)

b6.grid(row=2,column=2)

b7=Button(f,text="7",bg=bc,command = lambda : fun("7"),width=15,height=3)

b7.grid(row=1,column=0) 

b8=Button(f,text="8",bg=bc,command = lambda : fun("8"),width=15,height=3)

b8.grid(row=1,column=1)

b9=Button(f,text="9",bg=bc,command = lambda : fun("9"),width=15,height=3)

b9.grid(row=1,column=2)

b0=Button(f,text="0",bg=bc,command = lambda : fun("0"),width=15,height=3)

b0.grid(row=4,column=0)

bMen=Button(f,text="-",bg=bc,command = lambda : fun("-"),width=15,height=3)

bMen.grid(row=2,column=3)

bMan=Button(f,text="+",bg=bc,command = lambda : fun("+"),width=15,height=3)

bMan.grid(row=3,column=3)

bDiv=Button(f,text="/",bg=bc,command = lambda : fun("/"),width=15,height=3)

bDiv.grid(row=4,column=2)

bMul=Button(f,text="*",bg=bc,command = lambda : fun("*"),width=15,height=3)

bMul.grid(row=1,column=3)

bPun=Button(f,text=".",bg=bc,command = lambda : fun("."),width=15,height=3)

bPun.grid(row=4,column=1) 

bIgu=Button(f,text="=",bg=bc,command = lambda : Res(),width=15,height=3)

bIgu.grid(row=4,column=3)

bClear=Button(f2,text="Clear",bg=bc,command = lambda : t1.delete("1.0",END),width=10,height=3)

bClear.grid(row=0,column=2)

bCl=Button(f2,text="C",bg=bc,command = lambda : t1.delete("end-2c", "end-1c"),width=5,height=3)

bCl.grid(row=0,column=3)

a.mainloop()  