# import all the modules
from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import math
import os
import random
from tkinter import ttk
from PIL import ImageTk,Image


conn = sqlite3.connect("Database\store.db")
c = conn.cursor()

# date
date = datetime.datetime.now().date()

# temporary lists like sessions
products_list = []
product_price = []
product_quantity = []
product_id = []

# list for labels
root = Tk()
root.title("COMPANY BOSSCCOM")
labels_list = []
image = PhotoImage(file="ngang1.png")
img_resize = image.subsample(1, 1)
Label(root, image=img_resize, bg="white", relief=SUNKEN).pack(pady=5)


class Application:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        # frame
        self.left = Frame(master, width=320, height=1300, bg='white')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=2100, height=53, bg='white')
        self.right.pack(side=TOP)

        self.bottom = Frame(master, width=2100, height=1000, bg='lightblue')
        self.bottom.pack(side=TOP)

        # components
        self.date_l = Label(self.left, text="Today's Date: " + str(date), font=('arial 16 bold'), bg='lightblue', fg='white')
        self.date_l.place(x=20, y=0)

        # button
        self.bt_st_catalog = Button(self.left, text="Hồ sơ bệnh nhân", width=18, height=2,  font=('arial 18 bold'),bg='orange', command=self.ajax)
        self.bt_st_catalog.place(x=8, y=45)

        self.bt_st_form = Button(self.left, text="Nội soi", width=18, height=2,  font=('arial 18 bold'),bg='orange', command=self.ajax)
        self.bt_st_form.place(x=8, y=135)

        self.bt_patient = Button(self.left, text="Biểu mẫu in", width=18, height=2,  font=('arial 18 bold'),bg='orange', command=self.ajax)
        self.bt_patient.place(x=8, y=225)

        self.bt_endoscop = Button(self.left, text="Danh mục in", width=18, height=2,  font=('arial 18 bold'),bg='orange', command=self.ajax)
        self.bt_endoscop.place(x=8, y=315)

        self.bt_diagnose = Button(self.left, text="Danh mục chẩn đoán", width=18, height=2,  font=('arial 18 bold'),bg='orange', command=self.ajax)
        self.bt_diagnose.place(x=8, y=405)

        self.bt_exit1 = Button(self.left, text="Thoát", width=18, height=2,  font=('arial 18 bold'),bg='orange', command=self.quit)
        self.bt_exit1.place(x=8, y=495)


        self.master.bind("<Return>", self.ajax)
        self.master.bind("<Up>", self.add_to_cart)
        self.master.bind("<space>", self.generate_bill)

    def ajax(self, *args, **kwargs):

        # button control system
        self.bt_add_patient = Button(self.right, text="Thêm bệnh nhân", width=15, height=2, font=('arial 12 bold'), bg='white', command=self.ajax)
        self.bt_add_patient.place(x=0, y=0)

        self.bt_open_file = Button(self.right, text="Mở hồ sơ", width=15, height=2, font=('arial 12 bold'),bg='white', command=self.ajax)
        self.bt_open_file.place(x=160, y=0)
        #
        self.bt_save_file = Button(self.right, text="lưu hồ sơ", width=15, height=2, font=('arial 12 bold'),bg='white', command=self.ajax)
        self.bt_save_file.place(x=320, y=0)
        #
        self.bt_delele1 = Button(self.right, text="Xóa", width=15, height=2, font=('arial 12 bold'), bg='white', command=self.ajax)
        self.bt_delele1.place(x=480, y=0)
        #
        self.bt_thoat = Button(self.right, text="Đóng", width=15, height=2, font=('arial 12 bold'), bg='white',command=self.add_to_cart)
        self.bt_thoat.place(x=640, y=0)

        self.tenbenhnhan = Label(self.bottom, text="Tên bệnh nhân:", font=('arial 12 bold'), fg='black',bg='lightblue')
        self.tenbenhnhan.place(x=15, y=5)

        self.name_p = Entry(self.bottom, font=('arial 24 bold'), width=20)
        self.name_p.place(x=5, y=30)

        self.adr = Label(self.bottom, text="Địa chỉ:", font=('arial 12 bold'), fg='black', bg='lightblue')
        self.adr.place(x=15, y=75)

        self.adr_p = Entry(self.bottom, font=('arial 24 bold'), width=20)
        self.adr_p.place(x=5, y=100)

        self.year_b = Label(self.bottom, text="Năm sinh:", font=('arial 12 bold'), fg='black', bg='lightblue')
        self.year_b.place(x=15, y=150)

        self.y_b = Entry(self.bottom, font=('arial 24 bold'), width=20)
        self.y_b.place(x=5, y=175)

        self.tlpnb = Entry(self.bottom, font=('arial 24 bold'), width=20)
        self.tlpnb.place(x=465, y=30)

        self.st = Label(self.bottom, text="Triệu chứng:", font=('arial 12 bold'), fg='black', bg='lightblue')
        self.st.place(x=470, y=75)

        self.stom = Entry(self.bottom, font=('arial 24 bold'), width=20)
        self.stom.place(x=465, y=100)


        self.sex = Label(self.bottom, text="Giới tính:", font=('arial 12 bold'), fg='black', bg='lightblue')
        self.sex.place(x=470, y=150)

        self.chkbtn1 = Checkbutton(self.bottom, text='Nam',font=('arial 18 bold'),fg='black', bg='lightblue',takefocus=0).place(x=475, y=175)
        self.chkbtn2 = Checkbutton(self.bottom, text='Nữ',font=('arial 18 bold'),fg='black', bg='lightblue',takefocus=0).place(x=600, y=175)

    def add_to_cart(self, *args, **kwargs):
        # get the quantity value and from the database
        self.bt_thoat.destroy()
        self.bt_delele1.destroy()
        self.bt_save_file.destroy()
        self.bt_open_file.destroy()
        self.bt_add_patient.destroy()


        self.tenbenhnhan.destroy()
        self.name_p.destroy()
        self.adr.destroy()
        self.adr_p.destroy()
        self.year_b.destroy()

        self.y_b.destroy()
        self.tlpnb.destroy()
        self.st.destroy()
        self.stom.destroy()
        self.sex.destroy()
        self.chkbtn1.destroy()
        self.chkbtn2.destroy()
        self.bottom.destroy()

    def quit(self):
        root.destroy()



    def change_func(self, *args, **kwargs):
        # get the amount given by the customer and the amount generated by the computer
        self.amount_given = float(self.change_e.get())
        self.our_total = float(sum(product_price))

        self.to_give = self.amount_given - self.our_total

        # label change
        self.c_amount = Label(self.left, text="Change: Rs. " + str(self.to_give), font=('arial 18 bold'), fg='red',
                              bg='white')
        self.c_amount.place(x=0, y=600)

    def generate_bill(self, *args, **kwargs):
        # create the bill before updating to the database.
        #  directory = "D:/Store Management Software/Invoice/" + str(date) + "/"
        directory = "D:\code examp\Store-Management-Software\print/"
        if not os.path.exists(directory):
            os.makedirs(directory)

        # TEMPLATES FOR THE BILL
        company = "\t\t\t\tBibek Company Pvt. Ltd.\n"
        address = "\t\t\t\tKathmandu, Nepal\n"
        phone = "\t\t\t\t\t99999999999\n"
        sample = "\t\t\t\t\tInvoice\n"
        dt = "\t\t\t\t\t" + str(date)

        table_header = "\n\n\t\t\t---------------------------------------\n\t\t\tSN.\tProducts\t\tQty\t\tAmount\n\t\t\t---------------------------------------"
        final = company + address + phone + sample + dt + "\n" + table_header

        # open a file to write it to
        file_name = str(directory) + str(random.randrange(5000, 10000)) + ".doc"
        f = open(file_name, 'w')
        f.write(final)

        # fill dynamics
        r = 1
        i = 0
        for t in products_list:
            f.write("\n\t\t\t" + str(r) + "\t" + str(products_list[i] + ".......")[:7] + "\t\t" + str(
                product_quantity[i]) + "\t\t" + str(product_price[i]))
            i += 1
            r += 1
        f.write("\n\n\t\t\tTotal: Rs. " + str(sum(product_price)))
        f.write("\n\t\t\tThanks for Visiting.")
        os.startfile(file_name, "print")
        f.close()
        # decrease the stock
        self.x = 0

        initial = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(initial, (product_id[self.x],))

        for i in products_list:
            for r in result:
                self.old_stock = r[2]
            self.new_stock = int(self.old_stock) - int(product_quantity[self.x])

            # updating the stock
            sql = "UPDATE inventory SET stock=? WHERE id=?"
            c.execute(sql, (self.new_stock, product_id[self.x]))
            conn.commit()

            # insert into the transaction
            sql2 = "INSERT INTO transactions (product_name, quantity, amount, date) VALUES (?, ?, ?, ?)"
            c.execute(sql2, (products_list[self.x], product_quantity[self.x], product_price[self.x], date))
            conn.commit()

            self.x += 1

        for a in labels_list:
            a.destroy()

        del (products_list[:])
        del (product_id[:])
        del (product_quantity[:])
        del (product_price[:])

        self.total_l.configure(text="")
        self.c_amount.configure(text="")
        self.change_e.delete(0, END)
        self.enteride.focus()
        tkinter.messagebox.showinfo("Success", "Done everything smoothly")



b = Application(root)

root.geometry("1920x1080+0+0")
root.mainloop()

