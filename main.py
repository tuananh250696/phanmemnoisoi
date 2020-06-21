from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import math
import os
import random
from tkinter import ttk
from PIL import ImageTk,Image
import cv2


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



class Application:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        # frame
        self.left1 = Frame(master, width=1920, height=96, bg='white')
        self.left1.pack(side=TOP)
        Label(self.left1, image=img_resize, bg="white", relief=SUNKEN).pack(pady=5)

        self.left = Frame(master, width=320, height=1300, bg='white')
        self.left.pack(side=LEFT)

        # components
        self.date_l = Label(self.left, text="Today's Date: " + str(date), font=('arial 16 bold'), bg='lightblue', fg='white')
        self.date_l.place(x=20, y=0)

        # button
        self.bt_st_catalog = Button(self.left, text="Hồ sơ bệnh nhân", width=18, height=2,  font=('arial 18 bold'),bg='orange', command=self.ajax)
        self.bt_st_catalog.place(x=8, y=45)

        self.bt_st_form = Button(self.left, text="Nội soi", width=18, height=2,  font=('arial 18 bold'),bg='orange', command=self.endoscopy)
        self.bt_st_form.place(x=8, y=135)

        self.bt_patient = Button(self.left, text="Biểu mẫu in", width=18, height=2,  font=('arial 18 bold'),bg='orange', command=self.ajax)
        self.bt_patient.place(x=8, y=225)

        self.bt_endoscop = Button(self.left, text="Danh mục in", width=18, height=2,  font=('arial 18 bold'),bg='orange', command=self.ajax)
        self.bt_endoscop.place(x=8, y=315)

        self.bt_diagnose = Button(self.left, text="Danh mục chẩn đoán", width=18, height=2,  font=('arial 18 bold'),bg='orange', command=self.ajax)
        self.bt_diagnose.place(x=8, y=405)

        self.bt_exit1 = Button(self.left, text="Thoát", width=18, height=2,  font=('arial 18 bold'),bg='orange', command=self.quit)
        self.bt_exit1.place(x=8, y=495)

    def ajax(self,*args, **kwargs):
        self.right = Frame(root, width=2100, height=53, bg='white')
        self.right.pack(side=TOP)

        self.bottom = Frame(root, width=2100, height=220, bg='lightblue')
        self.bottom.pack(side=TOP)

        self.bottom1 = Frame(root, width=2100, height=60, bg='yellow')
        self.bottom1.pack(side=TOP)
        self.bottom2 = Frame(root, width=2100, height=1100, bg='white')
        self.bottom2.pack(side=TOP)

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

        self.job = Label(self.bottom, text="Nghề nghiệp:", font=('arial 12 bold'), fg='black', bg='lightblue')
        self.job.place(x=425, y=5)
        self.jobw = Entry(self.bottom, font=('arial 24 bold'), width=20)
        self.jobw.place(x=410, y=30)

        self.st = Label(self.bottom, text="Triệu chứng:", font=('arial 12 bold'), fg='black', bg='lightblue')
        self.st.place(x=420, y=75)

        self.stom = Entry(self.bottom, font=('arial 24 bold'), width=20)
        self.stom.place(x=410, y=100)

        self.sbh = Label(self.bottom, text="Số bảo hiểm:", font=('arial 12 bold'), fg='black', bg='lightblue')
        self.sbh.place(x=420, y=150)

        self.nbh = Entry(self.bottom, font=('arial 24 bold'), width=20)
        self.nbh.place(x=410, y=175)

        self.sex = Label(self.bottom, text="Giới tính:", font=('arial 12 bold'), fg='black', bg='lightblue')
        self.sex.place(x=800, y=5)
        #
        var3 = IntVar()
        var4 = IntVar()
        self.chkbtn1 = Checkbutton(self.bottom, text='Nam', variable=var3, font=('arial 18 bold'), fg='black', bg='lightblue').place(x=810, y=25)
        self.chkbtn2 = Checkbutton(self.bottom, text='Nữ', variable=var4, font=('arial 18 bold'), fg='black', bg='lightblue').place(x=900, y=25)

        self.seachinfo = Button(self.bottom1, text="Tìm kiếm", width=15, height=1, font=('arial 18 bold'), bg='orange',command=self.ajax)
        self.seachinfo.place(x=800, y=5)

        self.name_info = Label(self.bottom1, text="Tên:", font=('arial 12 bold'), fg='black', bg='lightblue')
        self.name_info.place(x=5, y=15)

        self.name_infos = Entry(self.bottom1, font=('arial 18 bold'), width=15)
        self.name_infos.place(x=55, y=10)

        var1 = IntVar()
        self.chkbtn3 =Checkbutton(self.bottom1, text="Nam", variable=var1, font=('arial 14 bold'), fg='black', bg='lightblue').place(x=260, y=10)
        var2 = IntVar()
        chkbtn4 =Checkbutton(self.bottom1, text="Nữ", variable=var2, font=('arial 14 bold'), fg='black', bg='lightblue').place(x=340, y=10)


        self.date_s = Label(self.bottom1, text="Từ:", font=('arial 12 bold'), fg='black', bg='lightblue')
        self.date_s.place(x=420, y=15)
        self.from_date = Entry(self.bottom1, font=('arial 18 bold'), width=8)
        self.from_date.place(x=455, y=10)

        self.date_s2 = Label(self.bottom1, text="Đến:", font=('arial 12 bold'), fg='black', bg='lightblue')
        self.date_s2.place(x=575, y=15)
        self.from_todate = Entry(self.bottom1, font=('arial 18 bold'), width=8)
        self.from_todate.place(x=620, y=10)

        # infseach
        self.s_stt = Label(self.bottom2, text="Stt", font=('arial 12 bold'), fg='black', bg='lightblue',width=5)
        self.s_stt.place(x=0, y=5)
        self.s_name = Label(self.bottom2, text="Họ và tên", font=('arial 12 bold'), fg='black', bg='lightblue', width=20)
        self.s_name.place(x=65, y=5)
        self.s_address = Label(self.bottom2, text="Địa chỉ", font=('arial 12 bold'), fg='black', bg='lightblue',width=25)
        self.s_address.place(x=275, y=5)
        self.s_sexgt = Label(self.bottom2, text="Giới tính", font=('arial 12 bold'), fg='black', bg='lightblue', width=8)
        self.s_sexgt.place(x=535, y=5)
        self.s_born = Label(self.bottom2, text="Tuổi", font=('arial 12 bold'), fg='black', bg='lightblue', width=8)
        self.s_born.place(x=625, y=5)
        self.s_job = Label(self.bottom2, text="Nghề nghiệp", font=('arial 12 bold'), fg='black', bg='lightblue', width=15)
        self.s_job.place(x=715, y=5)
        self.s_sbh = Label(self.bottom2, text="Số bảo hiểm", font=('arial 12 bold'), fg='black', bg='lightblue',width=10)
        self.s_sbh.place(x=875, y=5)




    def add_to_cart(self, *args, **kwargs):
        self.right.destroy()
        self.bottom.destroy()
        self.bottom1.destroy()
        self.bottom2.destroy()

    def endoscopy(self):
        self.left.destroy()
        self.left1.destroy()

        vc = cv2.VideoCapture(0)
        rval, frame = vc.read()

        self.right.destroy()
        self.bottom.destroy()
        self.bottom1.destroy()
        self.bottom2.destroy()

    def quit(self):
        root.destroy()


b = Application(root)

root.geometry("1920x1080+0+0")
root.mainloop()
