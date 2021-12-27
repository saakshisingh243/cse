import random
import time
import datetime
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter import ttk  # For labels, frames etc...
import tkinter.messagebox as tkMessageBox
import mysql.connector as mys

conn=mys.connect(host='localhost',user='root',passwd='root')
cursor=conn.cursor()
cursor.execute("USE restaurant")

"""=============== Methods ================================="""
def raise_frame(frame):
    frame.tkraise()

def validate_password():
    username = ent_username.get()
    password = ent_password.get()
    cursor.execute("SELECT COUNT(*) FROM login WHERE username = '%s' AND password = '%s'" % (username, password))
    output = cursor.fetchone()
    numRows = output[0]
    if(numRows == 1):
        Database()
        raise_frame(startPage)
    else:
        result = messagebox.askyesno("Login","Invalid username or password. Want to try again?")
        if(result == False):
            root.destroy()

"""========================================================="""

root = Tk()
root.title("SWIZZL Restaurant Management System")
width = 900
height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#c7c3c3")

login = Frame(root)
startPage = Frame(root)
foodItem = Frame(root)
orders = Frame(root)

for frame in (login, startPage, foodItem, orders):
    frame.grid(row=0, column=0, sticky='news')


"""=========================== LOGIN PAGE BEGIN =============================="""
loginFrame = Frame(login, height = 700, width = 900, bg='#ded3b6')
loginFrame.grid(row=0, column=0, sticky=W)
loginFrame.grid_propagate(0)

#=====BG IMAGE=======
bg1=ImageTk.PhotoImage(file="C:\Saakshi\python\loginpage.png")
bg_image=Label(loginFrame,image=bg1).place(x=0,y=0,relwidth=1,relheight=1)
root.resizable(False,False)

loginFrame.columnconfigure((0,1,2,3,4), weight=1)
loginFrame.rowconfigure((3,4,5), weight=1)
loginFrame.rowconfigure((0,1,2,6,7,8,9,10,11,12), weight=2)

#Project Header
projHeader = ttk.Label(loginFrame, text = "Restaurant Management System", background="#b0acac", font=("Courier", 14, 'bold'), padding=(10,5,10,5))
projHeader.grid(row = 0, column = 0, columnspan=5, pady = 2, sticky=N)


#creating username label  
lbl_username = Label(loginFrame, text = "Username:", background="#fff000", padx=10, pady=3, bd=3, relief=RAISED, font=("Verdana", 11, 'bold'))
lbl_username.grid(row=3, column=1, sticky = SE, pady = 2)
#creating password label  
lbl_password = Label(loginFrame, text = "Password:", background="#fff000", padx=10, pady=3, bd=3, relief=RAISED, font=("Verdana", 11, 'bold'))
lbl_password.grid(row=4, column=1, sticky = NE, pady = 7)

#creating username entry
ent_username = Entry(loginFrame, font=("Verdana", 12))
ent_username.grid(row=3, column=2, sticky = SW, padx=5,pady=5,ipady=5)

#creating password entry
ent_password = ttk.Entry(loginFrame, font=("Verdana", 12), show='*')
ent_password.grid(row=4, column=2, sticky = NW, padx=5,pady=5,ipady=5)

btn_submit = Button(loginFrame, text = "Login", padx='15', pady='5', command = lambda:validate_password())
btn_submit.grid(row=5, column=1, sticky = E, pady = 2)

btn_exit = Button(loginFrame, text = "Exit", padx='18', pady='5', command = root.destroy)
btn_exit.grid(row=5, column=2, sticky = W, padx=5, pady = 2)

"""=========================== LOGIN PAGE END =============================="""

"""=========================== START PAGE BEGIN =============================="""
def iExit():
        iExit = messagebox.askyesno("Exit", "Do you want to exit?")
        if iExit>0:
            root.destroy()
            return
        
startPageFrame = Frame(startPage, height = 700, width = 900, bg='#ded3b6')
startPageFrame.grid(row=0, column=0, sticky=W)
startPageFrame.grid_propagate(0)

#=====BG IMAGE=======
bg_image1=Label(startPageFrame,image=bg1).place(x=0,y=0,relwidth=1,relheight=1)
root.resizable(False,False)

projHeader = ttk.Label(startPageFrame, text = "Welcome  to", font=("Courier", 28, 'bold'), padding=(10,5,10,5))
projHeader.place(x = 290, y = 130)
projHeader = ttk.Label(startPageFrame, text = "SWIZZL", font=("Courier", 50, 'bold'), padding=(10,5,10,5))
projHeader.place(x = 290, y = 200)
projHeader1 = ttk.Label(startPageFrame, text = "Restaurant Management System", font=("Courier", 28, 'bold'), padding=(10,5,10,5))
projHeader1.place(x = 120, y = 300)

btn_foodItem = Button(startPageFrame, text = "Food Item", padx='15', pady='5', command = lambda:raise_frame(foodItem))
btn_foodItem.place(x = 250, y = 380)

btn_orders = Button(startPageFrame, text = "ORDERS", padx='15', pady='5', command = lambda:raise_frame(orders))
btn_orders.place(x = 400, y = 380)

btn_exit = Button(startPageFrame, text = "EXIT", padx='25', pady='5', bg="#fa756b", command = lambda:iExit())
btn_exit.place(x = 550, y = 380)

"""=========================== START PAGE END =============================="""

"""=========================== FOOD ITEM BEGIN =============================="""

#============================VARIABLES===================================
ITEM_CATEGORY = StringVar()
ITEM_NAME = StringVar()
ITEM_QUANTITY = StringVar()
ITEM_PRICE = StringVar()

#============================METHODS=====================================

def Database():
    conn=mys.connect(host='localhost',user='root',passwd='root')
    cursor=conn.cursor()
    cursor.execute("USE restaurant")
    cursor.execute("SELECT * FROM fooditems ORDER BY category")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def SubmitData():
    if  ITEM_CATEGORY.get() == "" or ITEM_NAME.get() == "" or ITEM_QUANTITY.get() == "" or ITEM_PRICE.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn=mys.connect(host='localhost',user='root',passwd='root',database='restaurant')
        cursor=conn.cursor()
        insertSQL = "INSERT INTO fooditems (category, item_name, quantity, item_price) VALUES(%s, %s, %s, %s)"
        insertVAL = (str(ITEM_CATEGORY.get()), str(ITEM_NAME.get()), str(ITEM_QUANTITY.get()), str(ITEM_PRICE.get()))
        cursor.execute(insertSQL, insertVAL)
        conn.commit()
        cursor.execute("SELECT * FROM fooditems ORDER BY category ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        ITEM_CATEGORY.set("")
        ITEM_NAME.set("")
        ITEM_QUANTITY.set("")
        ITEM_PRICE.set("")
    if 'NewWindow' in globals():
        NewWindow.destroy()

def UpdateData():
    if ITEM_QUANTITY.get() == "":
       result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn=mys.connect(host='localhost',user='root',passwd='root',database='restaurant')
        cursor=conn.cursor()
        cursor.execute("UPDATE fooditems SET category = %s, item_name = %s, quantity = %s, item_price = %s WHERE itemid = %s", (str(ITEM_CATEGORY.get()), str(ITEM_NAME.get()), str(ITEM_QUANTITY.get()), str(ITEM_PRICE.get()), str(itemid)))
        conn.commit()
        cursor.execute("SELECT * FROM fooditems ORDER BY category ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        ITEM_CATEGORY.set("")
        ITEM_NAME.set("")
        ITEM_QUANTITY.set("")
        ITEM_PRICE.set("")
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()
        
    
def OnSelected(event):
    global itemid, UpdateWindow
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    itemid = selecteditem[0]
    ITEM_CATEGORY.set("")
    ITEM_NAME.set("")
    ITEM_QUANTITY.set("")
    ITEM_PRICE.set("")
    ITEM_CATEGORY.set(selecteditem[1])
    ITEM_NAME.set(selecteditem[2])
    ITEM_QUANTITY.set(selecteditem[3])
    ITEM_PRICE.set(selecteditem[4])
    UpdateWindow = Toplevel()
    UpdateWindow.title("Food Item List")
    width = 400
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) + 450) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    UpdateWindow.resizable(0, 0)
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'NewWindow' in globals():
        NewWindow.destroy()

    #===================FRAMES==============================
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    foodItemForm = Frame(UpdateWindow)
    foodItemForm.pack(side=TOP, pady=10)
    
    #===================LABELS==============================
    lbl_title = Label(FormTitle, text="Updating Food Item", font=('arial', 16), bg="orange",  width = 300)
    lbl_title.pack(fill=X)
    lbl_category = Label(foodItemForm, text="Category", font=('arial', 14), bd=5)
    lbl_category.grid(row=0, sticky=W)
    lbl_item_name = Label(foodItemForm, text="Item Name", font=('arial', 14), bd=5)
    lbl_item_name.grid(row=1, sticky=W)
    lbl_quantity = Label(foodItemForm, text="Quantity", font=('arial', 14), bd=5)
    lbl_quantity.grid(row=2, sticky=W)
    lbl_item_price = Label(foodItemForm, text="Price", font=('arial', 14), bd=5)
    lbl_item_price.grid(row=3, sticky=W)

    #===================ENTRY===============================
    category = Entry(foodItemForm, textvariable=ITEM_CATEGORY, font=('arial', 14))
    category.grid(row=0, column=1)
    item_name = Entry(foodItemForm, textvariable=ITEM_NAME, font=('arial', 14))
    item_name.grid(row=1, column=1)
    item_quantity = Entry(foodItemForm, textvariable=ITEM_QUANTITY, font=('arial', 14))
    item_quantity.grid(row=2, column=1)
    item_price = Entry(foodItemForm, textvariable=ITEM_PRICE,  font=('arial', 14))
    item_price.grid(row=3, column=1)    

    #==================BUTTONS==============================
    btn_updatecon = Button(foodItemForm, text="Update", width=50, command=UpdateData)
    btn_updatecon.grid(row=6, columnspan=2, pady=10)


def DeleteData():
    if not tree.selection():
       result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
    else:
        result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            conn=mys.connect(host='localhost',user='root',passwd='root',database='restaurant')
            cursor=conn.cursor()
            print("Selected Item:",selecteditem[0])
            cursor.execute("DELETE FROM fooditems WHERE itemid = %s" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
    
def AddNewWindow():
    global NewWindow
    ITEM_CATEGORY.set("")
    ITEM_NAME.set("")
    ITEM_QUANTITY.set("")
    ITEM_PRICE.set("")
    NewWindow = Toplevel()
    NewWindow.title("Food Item List")
    width = 400
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) - 455) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    NewWindow.resizable(0, 0)
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()
    
    #===================FRAMES==============================
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    foodItemForm = Frame(NewWindow)
    foodItemForm.pack(side=TOP, pady=10)
    
    #===================LABELS==============================
    lbl_title = Label(FormTitle, text="Adding New Food Item", font=('arial', 16), bg="#e0be5a",  width = 300)
    lbl_title.pack(fill=X)
    lbl_category = Label(foodItemForm, text="Category", font=('arial', 14), bd=5)
    lbl_category.grid(row=0, sticky=W)
    lbl_item_name = Label(foodItemForm, text="Item Name", font=('arial', 14), bd=5)
    lbl_item_name.grid(row=1, sticky=W)
    lbl_quantity = Label(foodItemForm, text="Quantity", font=('arial', 14), bd=5)
    lbl_quantity.grid(row=2, sticky=W)
    lbl_item_price = Label(foodItemForm, text="Price", font=('arial', 14), bd=5)
    lbl_item_price.grid(row=3, sticky=W)

    #===================ENTRY===============================
    category = Entry(foodItemForm, textvariable=ITEM_CATEGORY, font=('arial', 14))
    category.grid(row=0, column=1)
    item_name = Entry(foodItemForm, textvariable=ITEM_NAME, font=('arial', 14))
    item_name.grid(row=1, column=1)
    item_quantity = Entry(foodItemForm, textvariable=ITEM_QUANTITY, font=('arial', 14))
    item_quantity.grid(row=2, column=1)
    item_price = Entry(foodItemForm, textvariable=ITEM_PRICE,  font=('arial', 14))
    item_price.grid(row=3, column=1)

    #==================BUTTONS==============================
    btn_addcon = Button(foodItemForm, text="Save", width=50, command=SubmitData)
    btn_addcon.grid(row=6, columnspan=2, pady=10)
	

#============================FRAMES======================================
foodItemFrame = Frame(foodItem, height = 700, width = 900, bg='#c7c3c3')
foodItemFrame.pack(side=TOP, fill=X)

foodItemTop = Frame(foodItemFrame, width=900, bd=0, relief=SOLID, highlightbackground="#d4c69d", highlightcolor="#d4c69d", highlightthickness=1)
foodItemTop.pack(side=TOP)

Mid = Frame(foodItemFrame, width=900,  bg="#c7c3c3")
Mid.pack(side=TOP)

MidLeft = Frame(Mid, width=100)
MidLeft.pack(side=LEFT, pady=10)

MidLeftPadding = Frame(Mid, width=370, bg="#ded3b6")
MidLeftPadding.pack(side=LEFT, pady=20, padx=150)
MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)
TableMargin = Frame(foodItemFrame, width=500)
TableMargin.pack(side=TOP)
#============================LABELS======================================
lbl_title = Label(foodItemTop, text="SWIZZL Restaurant Management System", font=('arial', 16), bg="#b0acac")
lbl_title.pack(fill=X)

#============================ENTRY=======================================

#============================BUTTONS=====================================
btn_add = Button(MidLeft, text="+ ADD ITEM", bg="#95c7a5", padx = 10, command=AddNewWindow)
btn_add.pack()
btn_foodItemExit = Button(MidRight, text="EXIT", bg="#d1c9c9", padx = 20, command = lambda: raise_frame(startPage))
btn_foodItemExit.pack(side=RIGHT)
btn_delete = Button(MidLeftPadding, text="DELETE ITEM", bg="#ff8282", padx = 10, command=DeleteData)
btn_delete.pack(side=RIGHT)

#============================TABLES======================================
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("ItemID", "Category", "Item Name", "Quantity", "Price"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('ItemID', text="ItemID", anchor=W)
tree.heading('Category', text="Category", anchor=W)
tree.heading('Item Name', text="Item Name", anchor=W)
tree.heading('Quantity', text="Quantity", anchor=W)
tree.heading('Price', text="Price", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=90)
tree.column('#2', stretch=NO, minwidth=0, width=180)
tree.column('#3', stretch=NO, minwidth=0, width=290)
tree.column('#4', stretch=NO, minwidth=0, width=120)
tree.column('#5', stretch=NO, minwidth=0, width=120)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected)

"""=========================== FOOD ITEM END =============================="""

"""=========================== ORDERS START ==============================="""
#============================FRAMES======================================
ordersFrame = Frame(orders, height = 700, width = 900, bg='#c7c3c3')
ordersFrame.pack(side=TOP, fill=X)
orders.config(bg="#c7c3c3")

#============================LABELS======================================
Tops= Frame(ordersFrame, bg='#c7c3c3', bd=0, pady=5, relief=RIDGE, width=900)
Tops.pack(side=TOP)

lblTitle = Label(Tops, font=("Courier", 14, 'bold'), text = "SWIZZL Restaurant Management System", background="#b0acac",justify=CENTER)
lblTitle.grid(row = 0, column = 0)

ReceiptCal_F= Frame(ordersFrame, bg='Powder Blue', bd=2, relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=5, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Receipt_F=Frame(ReceiptCal_F, bg='Powder Blue', bd=4, relief=RIDGE)
Receipt_F.pack(side=TOP)

MenuFrame= Frame(ordersFrame, bg='#e0aa0b', bd=1, relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame, bg='#debf64', bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame, bg='#ebca6c', bd=1, relief=RIDGE)
Drinks_F.pack(side=TOP)

#===========================================Variables==============================================
DateofOrder= StringVar()
Receipt_Ref= StringVar()
PaidTax= StringVar()
SubTotal= StringVar()
TotalCost= StringVar()
CostofDrinks= StringVar()
ServiceCharge= StringVar()

text_Input= StringVar()
operator=""

conn=mys.connect(host='localhost',user='root',passwd='root',database='restaurant')
cursor=conn.cursor()
cursor.execute("SELECT item_name FROM fooditems ORDER BY category ASC")
itemNames = cursor.fetchall()

entryVarList = []
entry = {}
label = []
foodDict = {}

for itemVal in itemNames:
        itemName = itemVal[0]
        entryVar = "E_" + itemName.replace(" ", "")
        entryVarList.append(entryVar)
        foodDict[entryVar] = itemName

for itemLabel in itemNames:
        itemName = itemLabel[0]
        label.append(itemName)

DateofOrder.set(time.strftime("%d/%m/%Y"))

#===========================================Function Declaration======================================
class funcdeclare:
    def Reset(self):
        #Reset entry variables to zero
        for ent in entryVarList:
                entry[ent].delete(0, 'end')
                entry[ent].insert(END, 0)
        
        CostofDrinks.set("0")
        ServiceCharge.set("0")
        SubTotal.set("0")
        PaidTax.set("0")
        TotalCost.set("0")

    def CostofItem(self):
        global RecieptTC
        PriceofDrinks = 0

        cursor.execute("SELECT item_name, item_price FROM fooditems ORDER BY category ASC")
        itemsPrice = cursor.fetchall()

        itemPriceDict = {}
        for itmPrice in itemsPrice:
                itemName = itmPrice[0]
                itemPrice = itmPrice[1]
                if(itemName != ""):
                        entryVar = "E_" + itemName.replace(" ", "")
                        itemPriceDict[entryVar] = itemPrice

        for x in itemPriceDict:
                val = float(entry[x].get())
                PriceofDrinks = PriceofDrinks + (val * int(itemPriceDict[x]))

        DrinksPrice="Rs", str('%.2f'%(PriceofDrinks))
        CostofDrinks.set(DrinksPrice)
        SC="Rs", str('%.2f'%(2.5))
        ServiceCharge.set(SC)

        SubTotalofITEMS="Rs", str('%.2f'%(PriceofDrinks + 2.5))
        SubTotal.set(SubTotalofITEMS)

        Tax="Rs", str('%.2f'%((PriceofDrinks + 2.5)*0.1))
        PaidTax.set(Tax)
        TT=((PriceofDrinks + 2.5) * 0.1)
        TC="Rs", str('%.2f'%(PriceofDrinks + 2.5 + TT))
        RecieptTC="Rs " + str('%.2f'%(PriceofDrinks + 2.5 + TT))
        TotalCost.set(TC)
		
    def Receipt(self):
        txtReceipt.delete("1.0",END)
        x= random.randint(10903, 609235)
        randomRef= str(x)
        Receipt_Ref.set("BILL" + randomRef)

        txtReceipt.insert(END, 'Receipt Ref:\t\t\t' + Receipt_Ref.get() + "\t" + DateofOrder.get() + "\n")
        txtReceipt.insert(END, 'Item:\t\t\t' + "No of Items\n")

        for x in foodDict:
                val = entry[x].get()
                if(val != "0"):
                    txtReceipt.insert(END, foodDict[x] + ': \t\t\t\t' + val + "\n")
                
        txtReceipt.insert(END, 'Total Price: \t\t\t' + str(RecieptTC) + "\n")

obj=funcdeclare()

#===========================================Drinks===================================================
i = 0
for name in label:
        lb=Label(Drinks_F, text=name, font=('arial',10,'bold'),bg= "#ebca6c", padx=8).grid(row=i,sticky=W)
        i += 1

#===========================================Entry Box for Drinks===========================================================
r = 0
for item in entryVarList:
        e = Entry(Drinks_F,font=('arial',10,'bold'),bd=5, width=15, justify=LEFT, textvariable=item)
        e.insert(END, 0)
        e.grid(row=r,column=1)
        entry[item] = e
        r += 1

#=======================================================Total Cost=========================================================
lblCostofDrinks =Label(Cost_F, font=('arial',12,'bold'),text='Cost of Items\t',bg='#debf64',fg='black')
lblCostofDrinks.grid(row=0,column=0, sticky=W)
txtCostofDrinks= Entry(Cost_F, width=35, bg='white', bd=5, font=('arial',9,'bold'), justify=RIGHT, textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0, column=1)

lblServiceCharge =Label(Cost_F, font=('arial',12,'bold'),text='Service Charge\t',bg='#debf64',fg='black')
lblServiceCharge.grid(row=1,column=0, sticky=W)
lblServiceCharge= Entry(Cost_F, bg='white',width=35, bd=5, font=('arial',9,'bold'), justify=RIGHT, textvariable=ServiceCharge)
lblServiceCharge.grid(row=1, column=1)

#=======================================================Payment Information================================================
lblSubTotal =Label(Cost_F, font=('arial',12,'bold'),text='Sub Total',bg='#debf64',fg='black')
lblSubTotal.grid(row=2,column=0, sticky=W)
txtSubTotal= Entry(Cost_F, width=35, bg='white', bd=5, font=('arial',9,'bold'), justify=RIGHT, textvariable=SubTotal)
txtSubTotal.grid(row=2, column=1)

lblPaidTax =Label(Cost_F, font=('arial',12,'bold'),text='Paid Tax',bg='#debf64',fg='black')
lblPaidTax.grid(row=3,column=0, sticky=W)
txtPaidTax= Entry(Cost_F, width=35, bg='white', bd=5, font=('arial',9,'bold'), justify=RIGHT, textvariable=PaidTax)
txtPaidTax.grid(row=3, column=1)

lblTotalCost =Label(Cost_F, font=('arial',12,'bold'),text='Total Cost',bg='#debf64',fg='black')
lblTotalCost.grid(row=4,column=0, sticky=W)
txtTotalCost= Entry(Cost_F, width=35, bg='white', bd=5, font=('arial',9,'bold'), justify=RIGHT, textvariable=TotalCost)
txtTotalCost.grid(row=4, column=1)

#=======================================================Receipt============================================================

txtReceipt= Text(Receipt_F, width=48, height=22, bg='white', bd=4, font=('arial',12,'bold'))
txtReceipt.grid(row=0, column=0)

#=======================================================Buttons============================================================

btnTotal=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',10,'bold'),
                width=4, text="Total", bg="Powder Blue", command=obj.CostofItem).grid(row=0,column=0)
btnReceipt=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',10,'bold'),
                width=4, text="Receipt", bg="Powder Blue", command=obj.Receipt).grid(row=0,column=1)
btnReset=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',10,'bold'),
                width=4, text="Reset", bg="Powder Blue", command=obj.Reset).grid(row=0,column=2)
btnExit=Button(Buttons_F, padx=16, pady=1, bd=7, fg='black', font=('arial',10,'bold'),
                width=4, text="Exit", bg="Powder Blue", command = lambda: raise_frame(startPage)).grid(row=0,column=3)

"""=========================== ORDERS END ================================="""

raise_frame(login)
root.mainloop()
