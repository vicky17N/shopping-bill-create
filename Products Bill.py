import tkinter.messagebox
from tkinter import *
import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',password='',database='products')
cursor = db.cursor()

def  tot():
    product_tot.set(product_price.get() * product_qty.get())

def add():
    global product_id
    global product_name
    global product_price
    global product_qty
    global product_tot
    id=product_id.get()
    name=product_name.get()
    price=product_price.get()
    qty=product_qty.get()
    tot=product_tot.get()
    cursor.execute('insert into products(id,name,price,qty,tot)values(%s,%s,%s,%s,%s)',[id,name,price,qty,tot])
    db.commit()
    tkinter.messagebox.showinfo('Details','Added')

def view():
    id=product_id.get()
    cursor.execute('select * from products where id=%s',[id])
    val=cursor.fetchone()
    product_name.set(val[1])
    product_price.set(val[2])
    product_qty.set(val[3])
    product_tot.set(val[4])

def update():
    id  =product_id.get()
    name=product_name.get()
    price=product_price.get()
    qty=product_qty.get()
    tot=product_tot.get()
    cursor.execute('UPDATE products SET name=%s,price=%s,qty=%s,tot=%s WHERE id=%s',[name,price,qty,tot,id])
    db.commit()
    tkinter.messagebox.showinfo('Details','Updated')

def delete():
    id=product_id.get()
    cursor.execute('delete from products where id=%s',[id])
    db.commit()
    tkinter.messagebox.showinfo('Detils','Deleted')

def clear():
    product_id.set('')
    product_name.set('')
    product_price.set('')
    product_qty.set('')
    product_tot.set('')

def overall():
    global view_details
    view_details=Toplevel(obj)
    view_details.geometry('800x400')
    view_details.title('Product list')
    view_details.configure(bg='royal blue')
    cursor.execute('select * from products')
    data=cursor.fetchall()
    row=len(data)
    cols=len(data[0])
    Label(view_details,width=15,text='PRODUCT ID',font=('calibri',14,'bold'),bg='royal blue',fg='white').grid(row=0,column=0)
    Label(view_details, width=15, text='PRODUCT NAME', font=('calibri', 14, 'bold'), bg='royal blue',fg='white').grid(row=0, column=1)
    Label(view_details, width=15, text='PRODUCT PRICE', font=('calibri', 14, 'bold'), bg='royal blue',fg='white').grid(row=0, column=2)
    Label(view_details, width=15, text='PRODUCT QTY', font=('calibri', 14, 'bold'), bg='royal blue',fg='white').grid(row=0, column=3)
    Label(view_details, width=15, text=' TOTAL', font=('calibri', 14, 'bold'), bg='royal blue',fg='white').grid(row=0, column=4)
    for i in range(row):
        for j in range(cols):
            e=Entry(view_details,width=15,font=('calibri',11))
            e.grid(row=i+1,column=j)
            e.insert(END,data[i][j])

obj=Tk()
obj.geometry('500x500')
obj.title('Access control matrix')
obj.configure(bg='Lightblue')


product_id_label=Label(obj,text='Product id',font=('calibri',15),bg='lightblue')
product_id_label.grid(row=1,column=1)
product_id=StringVar()
product_id_label_entry=Entry(obj,textvariable=product_id,font=('calibri',15))
product_id_label_entry.grid(row=1,column=2)

product_Name_label=Label(obj,text='Product Name',font=('calibri',15),bg='lightblue')
product_Name_label.grid(row=2,column=1)
product_name=StringVar()
product_Name_entry=Entry(obj,textvariable=product_name,font=('calibri',15))
product_Name_entry.grid(row=2,column=2)

product_price_label=Label(obj,text='Product price',font=('calibri',15),bg='lightblue')
product_price_label.grid(row=3,column=1)
product_price=IntVar()
product_price_label_entry=Entry(obj,textvariable=product_price,font=('calibri',15))
product_price_label_entry.grid(row=3,column=2)

product_qty_label=Label(obj,text='Product qty',font=('calibri',15),bg='lightblue')
product_qty_label.grid(row=4,column=1)
product_qty=IntVar()
product_qty_label_entry=Entry(obj,textvariable=product_qty,font=('calibri',15))
product_qty_label_entry.grid(row=4,column=2)

product_tot_label=Label(obj,text='Total',font=('calibri',15),bg='lightblue')
product_tot_label.grid(row=5,column=1)
product_tot=IntVar()
product_tot_entry=Entry(obj,textvariable=product_tot,font=('calibri',15))
product_tot_entry.grid(row=5,column=2)

but_tot=Button(obj,text='calculate',font=('calibri',15),bg='gray',fg='white',height='1',width='7',command=tot)
but_tot.grid(row=5,column=3)


but_add=Button(obj,text='ADD',font=('calibri',15),bg='gray',fg='white',height='1',width='7',command=add)
but_add.place(x=40,y=200)


but_view=Button(obj,text='VIEW',font=('calibri',15),bg='gray',fg='white',height='1',width='7',command=view)
but_view.place(x=180,y=200)

but_update=Button(obj,text='UPDATE',font=('calibri',15),bg='gray',fg='white',height='1',width='7',command=update)
but_update.place(x=320,y=200)

but_delete=Button(obj,text='DELETE',font=('calibri',15),bg='gray',fg='white',height='1',width='7',command=delete)
but_delete.place(x=40,y=300)

but_clear=Button(obj,text='CLEAR',font=('calibri',15),bg='gray',fg='white',height='1',width='7',command=clear)
but_clear.place(x=180,y=300)

but_overall=Button(obj,text='OVERALL',font=('calibri',15),bg='gray',fg='white',height='1',width='7',command=overall)
but_overall.place(x=320,y=300)

obj.mainloop()