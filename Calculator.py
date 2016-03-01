from tkinter import *
import math

root = Tk()
root.resizable(0,0)
equa = ""

root.title("Shaonty's Calculator")

#Display 
num1 = StringVar()
e = Label(root,textvariable=num1,height=3,width=25,font=150)
e.grid(columnspan = 4)

def btnPress(num):
	global equa
	equa = equa+str(num)
	num1.set(equa)

def equalPress():
	global equa
	total = str(eval(equa))
	num1.set(total)
	equa=total

def squre():
	global equa
	total = str(int(equa)*int(equa))
	num1.set(total)
	equa = str(total)

def clear():
	global equa
	equa=""
	num1.set("")

def power():
	global equa
	total = str(math.sqrt(float(equa)))
	num1.set(total)
	equa = str(total)

def Percent():
	global equa
	n = float(equa)
	total = str(n/100.0)
	equa=total
	num1.set(total)

#button
button1 = Button(root,text="1",font=8,padx=20,command = lambda:btnPress(1))
button1.grid(row=3,column=0)
button2 = Button(root,text="2",font=8,padx=20,command = lambda:btnPress(2))
button2.grid(row=3 , column = 1)
button3 = Button(root,text="3",font=8,padx=20,command = lambda:btnPress(3))
button3.grid(row=3 , column = 2)
button4 = Button(root,text="4",font=8,padx=20,command = lambda:btnPress(4))
button4.grid(row=2, column = 0)
button5 = Button(root,text="5",font=8,padx=20,command = lambda:btnPress(5))
button5.grid(row=2,column=1)
button6 = Button(root,text="6",font=8,padx=20,command = lambda:btnPress(6))
button6.grid(row=2,column=2)
button7 = Button(root,text="7",font=8,padx=20,command = lambda:btnPress(7))
button7.grid(row=1,column=0)
button8 = Button(root,text="8",font=8,padx=20,command = lambda:btnPress(8))
button8.grid(row=1,column=1)
button9 = Button(root,text="9",font=8,padx=20,command = lambda:btnPress(9))
button9.grid(row=1,column=2)
button0 = Button(root,text="0",font=8,padx=20,command = lambda:btnPress(0))
button0.grid(row=4,column=1)

clear1 = Button(root,text="C",font=8,bg="#EE691D",command = clear)
clear1.grid(row=1,column=3)
Plus = Button(root,text="+",font=8,bg="#13E2DB",command = lambda:btnPress("+"))
Plus.grid(row=2, column = 3)
Minus= Button(root,text="-",font=8,padx=20,bg="#13E2DB",command = lambda:btnPress("-"))
Minus.grid(row=2, column = 4)
mul = Button(root,text="*",font=8,padx=13,bg="#13E2DB",command = lambda:btnPress("*"))
mul.grid(row=3, column = 3)
div= Button(root,text="/",font=8,padx=20,bg="#13E2DB",command = lambda:btnPress("/"))
div.grid(row=3, column = 4)
point = Button(root,text=".",font=20,bg="#13E2DB",padx=22,command = lambda:btnPress("."))
point.grid(row=4,column=0)
percent = Button(root,text="%",padx=20,bg="#13E2DB",command=Percent)
percent.grid(row=4,column=2)

sqr = Button(root,text="x2",bg="#13E2DB",command=squre)
sqr.grid(row=4,column = 3)
pwr = Button(root,text="root",bg="#13E2DB",command=power)
pwr.grid(row=1,column=4)
equal = Button(root,text="=",font=10,padx=18,bg="#248A05",command = equalPress)
equal.grid(row=4,column=4)


root.mainloop()