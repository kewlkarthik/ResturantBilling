from tkinter import *
from tkinter import ttk

window = Tk()
window.title("NAAK Billing System")
window.geometry("1400x720")

def admin():
    head = Label(window, text="Billing System").grid(row=0, column=0, columnspan=2, padx=(300,0), pady=(300,0))
    username_lable = Label(window, text="User Name").grid(row=1, column=0, sticky=W, padx=(200,0))
    password_lable = Label(window, text="Password").grid(row=2, column=0, sticky=W, padx=(200,0))

    username_box = Entry(window, width=15)
    username_box.grid(row=1, column=1, sticky=W)
    password_box = Entry(window, width=15)
    password_box.grid(row=2, column=1, sticky=W)



customer_mobile_lable = Label(window, text="Mobile").grid(row=0, column=0, sticky=W, pady=20, padx=(10,0))
customer_name_lable = Label(window, text="Name").grid(row=0, column=2, sticky=W, padx=(10,10))
customer_address_lable = Label(window, text="Address").grid(row=0, column=4, sticky=W, pady=20, padx=(10,10))
delivery_option_lable = Label(window, text="Mode").grid(row=0, column=6, sticky=W, padx=(10,10))
item_name_lable = Label(window, text="Select Product").grid(row=1, column=0, sticky=W, pady=10, padx=(10,10))
item_price_lable = Label(window, text="Item Price").grid(row=1, column=2, sticky=W, pady=10, padx=(10,10))
item_quantity_lable = Label(window, text="Quantity").grid(row=1, column=4, sticky=W, pady=10, padx=(10,10))
total_price_lable = Label(window, text="Total Price").grid(row=1, column=6, sticky=W, pady=10, padx=(10,10))


customer_mobile_box = Entry(window, width=15)
customer_mobile_box.grid(row=0, column=1, sticky=W)
customer_name_box = Entry(window, width=15)
customer_name_box.grid(row=0, column=3, sticky=W)
customer_address_box = Entry(window, width=15)
customer_address_box.grid(row=0, column=5, sticky=W)

option = StringVar()
option.set("<--Select-->")
delivery_option_dropbox = OptionMenu(window, option, "Dine In", "Delivery", "Take Away")
delivery_option_dropbox.grid(row=0, column=7, sticky=W)

item = StringVar()
item.set("<-Select Product->")
item_name_dropbox = OptionMenu(window, item, "Pizza", "Pasta", "Burger")
item_name_dropbox.grid(row=1, column=1, sticky=W)


def billdata(a,b,c,d,e):
    global item
    global rate
    global quantity
    global t
    global total_1
    global billTV
    gst = float(t.get())*.05
    total = float(t.get())+gst
    i = 0
    print(len(billsTV.get_children()))


    if len(billsTV.get_children()) == 0:
        billsTV.insert("", "end", text=item.get(), values=(rate, quantity.get(), t.get(), gst, total))
        #for child in billsTV.get_children():
        #i = i + float(billsTV.item(child, "values")[4])
        #total_1.set("%.2f" % i)

    else:
        child = 0
        for child in billsTV.get_children():
            if billsTV.item(child, "text") == item.get():
                ch = child
                record = 1
                break


            else:
                record = 0
                continue

        if record == 1:
            billsTV.item(ch, text=item.get(), values=(int(rate), int(quantity.get())+int(billsTV.item(ch, "values")[1]), int(t.get())+int(billsTV.item(ch, "values")[2]), float(billsTV.item(ch, "values")[3])+gst, float(billsTV.item(ch, "values")[4])+total))


        else:
            billsTV.insert("", "end", text=item.get(), values=(rate, quantity.get(), t.get(), gst, total))

    for child in billsTV.get_children():
        i = i + float(billsTV.item(child, "values")[4])
        total_1.set("%.2f" % i)


def add(a, b, c):
    global rate
    global quantity
    global t

    try:
        temp = float(quantity.get())
        test = rate*temp
        t.set("%.0f"%test)
    except:
        pass

def delete(a):
    global item
    for child in billsTV.get_children():
        if billsTV.item(child, "text") == item.get():
            billsTV.delete(child)


item_price = StringVar()
rate = 5
item_price.set("%.0f" %rate)
item_price_entry = Entry(window, textvariable =item_price, width=15)
item_price_entry.grid(row=1, column=3, sticky=W)


quantity = StringVar()
test = item_price_entry.get()
item_quantity_entry = Entry(window, textvariable = quantity, width=15)
item_quantity_entry.grid(row=1, column=5, sticky=W)
quantity.trace('w', add)


t = StringVar()
total_price_entry = Entry(window, textvariable = t, width=15)
total_price_entry.grid(row=1, column=7, sticky=W)

bill_no_lable = Label(window, text="Bill No").grid(row=2,column=0)
bill_no_entry = Entry(window, width=10)
bill_no_entry.grid(row=2,column=1)
#date_entry
add_item = Button(window, text="Add Item", command=lambda: billdata(item, rate, quantity, t, total_1))
add_item.grid(row=2, column=2)
generate_bill = Button(window, text = "Generate Bill")
generate_bill.grid(row=2, column=4)
delete_item = Button(window, text = "Delete Item", command=lambda : delete(item))
delete_item.grid(row=2, column=6)


#Billing Tree View
billsTV = ttk.Treeview(height=15, columns=('Item Name','Unit Cost','Quantity','Product Cost','GST','Total Cost'))
billLable = Label(window, text="Bills")
billLable.grid(row=3, column=1, columnspan=7)

billsTV.grid(row=4, column=0, columnspan=11)

scrollBar = Scrollbar(window, orient="vertical", command=billsTV.yview)
scrollBar.grid(row=4, column=7, sticky="NES")

billsTV.configure(yscrollcommand=scrollBar.set)

billsTV.heading('#0', text="Item Name")
billsTV.heading('#1', text="Unit Cost")
billsTV.heading('#2', text="Quantity")
billsTV.heading('#3', text="Product Cost")
billsTV.heading('#4', text="GST")
billsTV.heading('#5', text="Total Cost")

total_1 = StringVar()
total_lable = Label(window, text="Total").grid(row=5, column=2, pady=20)
total_entry = Entry(window, textvariable=total_1)
total_entry.grid(row=5,column=3)

payment = StringVar()
payment.set("Select")
payment_mode_lable = Label(window, text="Payment Mode").grid(row=5, column=4, pady=20)
payment_mode_dropbox = OptionMenu(window, payment, "Cash", "Card", "UPI")
payment_mode_dropbox.grid(row=5,column=5)

add_product = Button(window, text = "Add Products")
add_product.grid(row=5,column=6)



window.mainloop()