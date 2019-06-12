from tkinter import *
import random
import time

root =Tk()
#root.geometry('1600*800+0+0')
root.title("Restaurant Management System ")
operator=""
text_Input = StringVar()

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    Cof =float(fries.get())
    CoP =float(Pizza.get())
    CoB = float(Burger.get())
    CoD = float(Drinks.get())
    CoI = float(Icecreams.get())
    Cop = float(pasta.get())

    Costoffries = Cof*0.99
    CostofPizza = CoP*1.00
    CostofBurger = CoB*2.99
    CostofDrinks = CoD*2.89
    CostofIcecreams = CoI*3.00
    Costofpasta = Cop*2.69

    CostofMeal = "$", str('%.2f'%(Costoffries+CostofPizza+CostofBurger+CostofDrinks+CostofIcecreams+Costofpasta))

    PayTax=((Costoffries+CostofPizza+CostofBurger+CostofDrinks+CostofIcecreams+Costofpasta)*0.2)

    TotalCost =(Costoffries+CostofPizza+CostofBurger+CostofDrinks+CostofIcecreams+Costofpasta)

    Ser_Charge=((Costoffries+CostofPizza+CostofBurger+CostofDrinks+CostofIcecreams+Costofpasta)/99)

    Service="$",str('%.2f'%Ser_Charge)
    OverAllCost="$",str('%.2f'%(PayTax + TotalCost + Ser_Charge))
    PaidTax = "$",str('%.2f'%PayTax)
    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    Subtotal.set(CostofMeal)
    Total.set(OverAllCost)

def qExit():
    root.destroy()

def Reset():
    rand.set("")
    fries.set("")
    Pizza.set("")
    Burger.set("")
    Drinks.set("")
    Icecreams.set("")
    pasta.set("")
    Cost.set("")
    Service_Charge.set("")
    Tax.set("")
    Subtotal.set("")
    Total.set("")


Tops=Frame(root,width=1600 ,height=50,bg="powder blue" ,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800 , height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=1600 ,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

#=======TIME===========
localtime=time.asctime(time.localtime(time.time()))

#===========SYSTEM INFO===============
lblInfo=Label(Tops, font=('arial',50,'bold'),text="Restaurant Management Systems",fg="steel blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops, font=('arial',20,'bold'),text=localtime,fg="steel blue",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

#======CALCULATOR============
txtDisplay = Entry(f2,font=('arial',20,'bold'),textvariable=text_Input, bd=30 , insertwidth=3 ,bg="cyan", justify='right').grid(columnspan=4)

button7 = Button(f2,padx=16,pady=16,bd=8 ,fg="black", font=('arial',20,'bold'),text="7",command = lambda:btnClick(7))
button7.grid(row=1,column=0)

button8 = Button(f2,padx=16,pady=16,bd=8 ,fg="black", font=('arial',20,'bold'),text="8",command = lambda:btnClick(8))
button8.grid(row=1,column=1)

button9 = Button(f2,padx=16,pady=16,bd=8 ,fg="black", font=('arial',20,'bold'),text="9",command = lambda:btnClick(9))
button9.grid(row=1,column=2)

buttonAdd = Button(f2,padx=16,pady=16,bd=8 ,fg="black", font=('arial',20,'bold'),text="+",command = lambda:btnClick("+"))
buttonAdd.grid(row=1,column=3)

button4 = Button(f2,padx=16,pady=16,bd=8 ,fg="black", font=('arial',20,'bold'),text="4",command = lambda:btnClick(4))
button4.grid(row=2,column=0)

button5 = Button(f2,padx=16,pady=16,bd=8 ,fg="black", font=('arial',20,'bold'),text="5",command = lambda:btnClick(5))
button5.grid(row=2,column=1)

button6 = Button(f2,padx=16,pady=16,bd=8 ,fg="black", font=('arial',20,'bold'),text="6",command = lambda:btnClick(6))
button6.grid(row=2,column=2)

buttonSub = Button(f2,padx=16,pady=16,bd=8 ,fg="black", font=('arial',20,'bold'),text="-",command = lambda:btnClick("-"))
buttonSub.grid(row=2,column=3)

button1 = Button(f2,padx=16,pady=16,bd=8 ,fg="black", font=('arial',20,'bold'),text="1",command = lambda:btnClick(1))
button1.grid(row=3,column=0)

button2 = Button(f2,padx=16,pady=16,bd=8 ,fg="black", font=('arial',20,'bold'),text="2",command = lambda:btnClick(2))
button2.grid(row=3,column=1)

button3 = Button(f2,padx=16,pady=16,bd=8 ,fg="black", font=('arial',20,'bold'),text="3",command = lambda:btnClick(3))
button3.grid(row=3,column=2)

buttonMul = Button(f2,padx=16,pady=16,bd=8 ,fg="black", font=('arial',20,'bold'),text="*",command = lambda:btnClick("*"))
buttonMul.grid(row=3,column=3)

button0 = Button(f2,padx=16,pady=16,bd=8 ,fg="black", font=('arial',20,'bold'),text="0",command = lambda:btnClick(0))
button0.grid(row=4,column=0)

buttonClr = Button(f2,padx=16,pady=16,bd=8 ,fg="black", font=('arial',20,'bold'),text="C",command = btnClear)
buttonClr.grid(row=4,column=1)

buttonEqu = Button(f2,padx=16,pady=16,bd=8 ,fg="black", font=('arial',20,'bold'),text="=",command = btnEquals)
buttonEqu.grid(row=4,column=2)

buttonDiv = Button(f2,padx=16,pady=16,bd=8 ,fg="black", font=('arial',20,'bold'),text="/",command =lambda:btnClick("/"))
buttonDiv.grid(row=4,column=3)

#============================RESTAURANT==============================
rand =StringVar()
fries =StringVar()
Pizza =StringVar()
Burger =StringVar()
Drinks =StringVar()
Icecreams =StringVar()
pasta =StringVar()
Cost =StringVar()
Service_Charge =StringVar()
Tax =StringVar()
Subtotal =StringVar()
Total =StringVar()


lblReference=Label(f1,font=('arial',16,'bold'),text="Reference",bd=16,anchor='w').grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="powder blue", justify='right').grid(row=0,column=1)

lblFries=Label(f1,font=('arial',16,'bold'),text="French Fries",bd=16,anchor='w').grid(row=1,column=0)
txtFries=Entry(f1,font=('arial',16,'bold'),textvariable=fries,bd=10,insertwidth=4,bg="powder blue", justify='right').grid(row=1,column=1)

lblPizza=Label(f1,font=('arial',16,'bold'),text="Pizza",bd=16,anchor='w').grid(row=2,column=0)
txtPizza=Entry(f1,font=('arial',16,'bold'),textvariable=Pizza,bd=10,insertwidth=4,bg="powder blue", justify='right').grid(row=2,column=1)

lblBurger=Label(f1,font=('arial',16,'bold'),text="Burger",bd=16,anchor='w').grid(row=3,column=0)
txtBurger=Entry(f1,font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="powder blue", justify='right').grid(row=3,column=1)

lblDrinks=Label(f1,font=('arial',16,'bold'),text="Drinks",bd=16,anchor='w').grid(row=4,column=0)
txtDrinks=Entry(f1,font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="powder blue", justify='right').grid(row=4,column=1)

lblIcecreams=Label(f1,font=('arial',16,'bold'),text="Icecreams",bd=16,anchor='w').grid(row=5,column=0)
txtIcecreams=Entry(f1,font=('arial',16,'bold'),textvariable=Icecreams,bd=10,insertwidth=4,bg="powder blue", justify='right').grid(row=5,column=1)

#============RESTAURANT 2=========================
lblpasta=Label(f1,font=('arial',16,'bold'),text="Pasta",bd=16,anchor='w').grid(row=0,column=2)
txtpasta=Entry(f1,font=('arial',16,'bold'),textvariable=pasta,bd=10,insertwidth=4,bg="powder blue", justify='right').grid(row=0,column=3)

lblCost=Label(f1,font=('arial',16,'bold'),text="Cost of Meal",bd=16,anchor='w').grid(row=1,column=2)
txtCost=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="powder blue", justify='right').grid(row=1,column=3)

lblService_Charge=Label(f1,font=('arial',16,'bold'),text="Service_Charge",bd=16,anchor='w').grid(row=2,column=2)
txtService_Charge=Entry(f1,font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="powder blue", justify='right').grid(row=2,column=3)

lblTax=Label(f1,font=('arial',16,'bold'),text="Tax",bd=16,anchor='w').grid(row=3,column=2)
txtTax=Entry(f1,font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="powder blue", justify='right').grid(row=3,column=3)

lblSubtotal=Label(f1,font=('arial',16,'bold'),text="Sub Total",bd=16,anchor='w').grid(row=4,column=2)
txtSubtotal=Entry(f1,font=('arial',16,'bold'),textvariable=Subtotal,bd=10,insertwidth=4,bg="powder blue", justify='right').grid(row=4,column=3)

lblTotal=Label(f1,font=('arial',16,'bold'),text="Total",bd=16,anchor='w').grid(row=5,column=2)
txtTotal=Entry(f1,font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="powder blue", justify='right').grid(row=5,column=3)

#============Buttons=============
btnTotal=Button(f1,padx=16,pady=8, bd=16,fg="black",font=('arial',16,'bold'), width=10,text="Total",bg="powder blue",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8, bd=16,fg="black",font=('arial',16,'bold'), width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8, bd=16,fg="black",font=('arial',16,'bold'), width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)

root.mainloop()
