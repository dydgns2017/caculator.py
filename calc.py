from tkinter import *

def calcClick():
    data = txt.get()
    print(data)
    print(eval(data))
    txt.delete(0, 100)
    txt.insert(0, eval(data))

def calcClear():
    txt.delete(0, 100)

## insert data inline
def insertPlus():
	txt.insert(100, "+")
def insertMinus():
	txt.insert(100, "-")
def insertDivision():
	txt.insert(100, "/")
def insertDot():
    txt.insert(100, ".")
def insertZero():
    txt.insert(100, "0")
def insertNumber_1():
   txt.insert(100, "1") 
def insertNumber_2():
   txt.insert(100, "2") 
def insertNumber_3():
   txt.insert(100, "3") 
def insertNumber_4():
   txt.insert(100, "4") 
def insertNumber_5():
   txt.insert(100, "5") 
def insertNumber_6():
   txt.insert(100, "6") 
def insertNumber_7():
   txt.insert(100, "7") 
def insertNumber_8():
   txt.insert(100, "8") 
def insertNumber_9():
   txt.insert(100, "9") 

root = Tk()
root.title("Calculator")
root.geometry("300x200")

txt = Entry(root, width=15)
txt.place(x = 150, y = 15, anchor=CENTER)

## exceptions
btnClear = Button(root, text="CLS", command=calcClear)
btnClear.place(x = 32, y = 30)

btnDot = Button(root, text=".", width=1, command=insertDot)
btnDot.place(x = 92, y = 120)

btn0 = Button(root, text="0", command=insertZero)
btn0.place(x = 132, y = 120)

btnC = Button(root, text="=", width=1, command=calcClick)
btnC.place(x = 172, y = 120)

btnP = Button(root, text="+", width=1, command=insertPlus)
btnP.place(x = 92, y = 150)

btnM = Button(root, text="-", width=1, command=insertMinus)
btnM.place(x = 132, y = 150)

btnDiv = Button(root, text="÷", width=1, command=insertDivision)
btnDiv.place(x = 172, y = 150)

for i in range(9):
    if i < 3:
        yy = 30
    elif i >= 3 and i < 6:
        yy = 60
    else:
        yy = 90
    if i == 0 or i == 3 or i == 6:
        xx = 92
    btn = "btn"+str(i+1)
    insertNumber = eval("insertNumber_"+str(i+1))
    btn = Button(root, text=str(i+1), command=insertNumber)
    btn.place(x = str(xx), y = str(yy))
    xx += 40

root.mainloop()
