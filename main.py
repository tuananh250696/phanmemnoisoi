from tkinter import *
import sqlite3
import tkinter as tk
import tkinter.messagebox
import datetime
import math
import os
import random
from tkinter import ttk
from PIL import ImageTk, Image
import cv2
import sys
import keyboard
import numpy as np
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import imutils
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
var = IntVar()
var1 = IntVar()
c = StringVar()
c1 = StringVar()


class Application:
    def __init__(self, master, *args, **kwargs):
        self.master = master
        # frame
        self.left1 = Frame(master, width=1360, height=96, bg='white')
        self.left1.pack(side=TOP)
        Label(self.left1, image=img_resize, bg="white", relief=SUNKEN).pack(pady=5)

        self.left = Frame(master, width=320, height=1300, bg='white')
        self.left.pack(side=LEFT)

        # components
        self.date_l = Label(self.left, text="Today's Date: " + str(date), font=('arial 16 bold'), bg='lightblue',
                            fg='white')
        self.date_l.place(x=20, y=0)

        # button
        self.bt_st_catalog = Button(self.left, text="Hồ sơ bệnh nhân", width=18, height=2, font=('arial 18 bold'),
                                    bg='orange', command=self.ajax)
        self.bt_st_catalog.place(x=8, y=45)

        self.bt_st_form = Button(self.left, text="Nội soi", width=18, height=2, font=('arial 18 bold'), bg='orange',
                                 command=self.endoscopy)
        self.bt_st_form.place(x=8, y=135)

        self.bt_patient = Button(self.left, text="Biểu mẫu in", width=18, height=2, font=('arial 18 bold'), bg='orange',
                                 command=self.add_to_bn)
        self.bt_patient.place(x=8, y=225)

        self.bt_endoscop = Button(self.left, text="Danh mục khám", width=18, height=2, font=('arial 18 bold'),
                                  bg='orange', command=self.createNewWindow)
        self.bt_endoscop.place(x=8, y=315)


        self.bt_exit1 = Button(self.left, text="Thoát", width=18, height=2, font=('arial 18 bold'), bg='orange',
                               command=self.quit)
        self.bt_exit1.place(x=8, y=405)

    def Search(self, *args, **kwargs):
        # =====================================Table WIDGET=========================================
        self.tree.delete(*self.tree.get_children())
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `member` WHERE `name` LIKE ? AND `job` LIKE ? AND `address` LIKE ? AND `age` LIKE ?",
                       ('%'+str(self.name_infos.get())+'%','%'+str(self.from_jobs.get())+'%','%'+str(self.from_addss.get())+'%','%'+str(self.born_agess.get())+'%'))
        fetch = cursor.fetchall()
        for data in fetch:
            self.tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        self.name_infos.delete(0, tk.END)
        self.from_jobs.delete(0, tk.END)
        self.from_addss.delete(0, tk.END)
        self.born_agess.delete(0, tk.END)

    def ajax(self, *args, **kwargs):

        self.right = Frame(root, width=1100, height=53, bg='white')
        self.right.pack(side=TOP)

        self.bottom = Frame(root, width=1100, height=220, bg='lightblue')
        self.bottom.pack(side=TOP)

        self.bottom1 = Frame(root, width=1100, height=80, bg='yellow')
        self.bottom1.pack(side=TOP)

        self.bottom2 = Frame(root, width=1100, height=550, bg='lightblue')
        self.bottom2.pack(side=TOP)

        self.Top = Frame(self.bottom2, width=1000, bd=2, relief=SOLID)
        self.Top.pack(side=TOP)
        self.MidFrame = Frame(self.bottom2, width=1000)
        self.MidFrame.pack(side=TOP)
        self.RightForm = Frame(self.MidFrame, width=1100)
        self.RightForm.pack(side=RIGHT)

        self.bt_add_patient = Button(self.right, text="Lưu hồ sơ", width=15, height=2, font=('arial 12 bold'),
                                     bg='white',command=self.get_itemsdatabase)
        self.bt_add_patient.place(x=0, y=0)

        self.bt_open_file = Button(self.right, text="Mở hồ sơ", width=15, height=2, font=('arial 12 bold'), bg='white',
                                   )
        self.bt_open_file.place(x=160, y=0)
        #
        self.bt_save_file = Button(self.right, text="Chuyên tiếp", width=15, height=2, font=('arial 12 bold'), bg='white',
                                   command=self.endoscopy)
        self.bt_save_file.place(x=320, y=0)
        #
        self.bt_delele1 = Button(self.right, text="Xóa", width=15, height=2, font=('arial 12 bold'), bg='white',
                                 command=self.delete_text)
        self.bt_delele1.place(x=480, y=0)
        #
        self.bt_thoat = Button(self.right, text="Đóng", width=15, height=2, font=('arial 12 bold'), bg='white',
                               command=self.add_to_cart)
        self.bt_thoat.place(x=640, y=0)

        self.tenbenhnhan = Label(self.bottom, text="Tên bệnh nhân:", font=('arial 12 bold'), fg='black', bg='lightblue')
        self.tenbenhnhan.place(x=15, y=5)


        self.name_p = Entry(self.bottom, font=('arial 24 bold'), width=20)
        self.name_p.place(x=5, y=30)
        self.name_p.focus()

        self.adr = Label(self.bottom, text="Địa chỉ:", font=('arial 12 bold'), fg='black', bg='lightblue')
        self.adr.place(x=15, y=75)

        self.adr_p = Entry(self.bottom, font=('arial 24 bold'), width=20)
        self.adr_p.place(x=5, y=100)

        self.year_b = Label(self.bottom, text="Năm sinh:", font=('arial 12 bold'), fg='black', bg='lightblue')
        self.year_b.place(x=15, y=150)

        self.y_b = Entry(self.bottom,  font=('arial 24 bold'), width=20)
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
        self.nbh = Entry(self.bottom,font=('arial 24 bold'), width=20)
        self.nbh.place(x=410, y=175)

        self.droplist = OptionMenu(self.bottom, c, 'NAM', 'NỮ')
        self.droplist.pack()
        self.menu = self.droplist.nametowidget(self.droplist.menuname)
        self.menu.configure(font=('arial 20 bold'))
        c.set('NAM')
        self.droplist.config(width=10,font=('arial 18 bold'))
        self.droplist.place(x=800, y=30)

        self.seachinfo = Button(self.bottom1, text="Tìm kiếm", width=15, height=1, font=('arial 18 bold'), bg='orange',
                                command=self.Search)
        self.seachinfo.place(x=800, y=5)

        self.name_info = Label(self.bottom1, text="Tên:", font=('arial 12 bold'), fg='black', bg='lightblue')
        self.name_info.place(x=5, y=10)

        self.name_infos = Entry(self.bottom1, width=18,  font=('arial 20 bold'), bg='white')
        self.name_infos.place(x=5, y=38)

        self.job_s = Label(self.bottom1, text="Nghề nghiệp:", font=('arial 12 bold'), fg='black', bg='lightblue')
        self.job_s.place(x=290, y=10)
        self.from_jobs = Entry(self.bottom1, font=('arial 20 bold'), width=12)
        self.from_jobs.place(x=290, y=38)

        self.aadd_s = Label(self.bottom1, text="Địa Chỉ:", font=('arial 12 bold'), fg='black', bg='lightblue')
        self.aadd_s.place(x=485, y=10)
        self.from_addss = Entry(self.bottom1, font=('arial 20 bold'), width=10)
        self.from_addss.place(x=485, y=38)

        self.born_s2 = Label(self.bottom1, text="Năm sinh:", font=('arial 12 bold'), fg='black', bg='lightblue')
        self.born_s2.place(x=650, y=10)
        self.born_agess = Entry(self.bottom1, font=('arial 20 bold'), width=5)
        self.born_agess.place(x=650, y=38)

        self.scrollbarx = Scrollbar(self.RightForm, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.RightForm, orient=VERTICAL)
        self.tree = ttk.Treeview(self.RightForm, columns=("MemberID", "Name", "Job", "Address", "Age"),
                                 selectmode="extended",
                                 height=400, yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=0)
        self.tree.column('#2', stretch=NO, minwidth=0, width=250)
        self.tree.column('#3', stretch=NO, minwidth=0, width=250)
        self.tree.column('#4', stretch=NO, minwidth=0, width=250)
        self.tree.column('#5', stretch=NO, minwidth=0, width=250)
        self.tree.pack()
        self.tree.heading('MemberID', text="MemberID", anchor=W)
        self.tree.heading('Name', text="Name", anchor=W)
        self.tree.heading('Job', text="Job", anchor=W)
        self.tree.heading('Address', text="Address", anchor=W)
        self.tree.heading('Age', text="Age", anchor=W)


    def get_itemsdatabase(self, *args, **kwargs):

        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()

        if self.name_p.get()== '' or self.adr_p.get()== '' or self.y_b.get() == '' or self.jobw.get()== '' or self.stom.get()== '' or self.nbh.get() == '' or c.get() == '':
            tkinter.messagebox.showinfo("Error", "Please Fill all the entries.")
        else:

            cursor.execute('INSERT INTO member (name, address, age, job, symptom,sbh,sex ) VALUES(?,?,?,?,?,?,?)',(self.name_p.get(),self.adr_p.get(), self.y_b.get(),self.jobw.get(), self.stom.get(), self.nbh.get(),c.get()))
            conn.commit()
            # textbox insert
            tkinter.messagebox.showinfo("Success", "Successfully added to the database")


    def add_to_cart(self, *args, **kwargs):
        self.right.destroy()
        self.bottom.destroy()
        self.bottom1.destroy()
        self.bottom2.destroy()

    def delete_text(self, *args, **kwargs):

        self.name_p.delete(0, END)
        self.adr_p.delete(0, END)
        self.y_b.delete(0, END)
        self.jobw.delete(0, END)
        self.stom.delete(0, END)
        self.nbh.delete(0, END)

    def database_print(self, *args, **kwargs):

        namepk = self.adr2_p.get()
        name_dt = self.n2_p.get()
        address_pk = self.n2_p.get()
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        if namepk== '' or name_dt== '' or address_pk == '':
            tkinter.messagebox.showinfo("Error", "Please Fill all the entries.")

        else:
            cursor.execute('CREATE TABLE IF NOT EXISTS print_dt (name_pk TEXT,dt_name TEXT,address TEXT)')
            cursor.execute('INSERT INTO print_dt (name_pk,dt_name,address) VALUES(?,?,?)',
                           (namepk, name_dt, address_pk))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Successfully added to the database")


    def add_to_bn(self, *args, **kwargs):
        addWindow = Toplevel(root)
        addWindow.title("Set form print")
        addWindow.geometry("600x350")
        self.rightadd2 = Frame(addWindow, width=600, height=450, bg='lightblue')
        self.rightadd2.pack(side=TOP)

        self.adr2 = Label(self.rightadd2, text="Phòng khám:", font=('arial 16 bold'), fg='black', bg='lightblue')
        self.adr2.place(x=10, y=10)
        self.adr2_p = Entry(self.rightadd2, font=('arial 18 bold'), width=32)
        self.adr2_p.place(x=150, y=10)

        self.doctor = Label(self.rightadd2, text=" Bác sĩ :", font=('arial 16 bold'), fg='black', bg='lightblue')
        self.doctor.place(x=10, y=85)

        self.doctor_p = Entry(self.rightadd2, font=('arial 18 bold'), width=32)
        self.doctor_p.place(x=150, y=75)

        self.n2 = Label(self.rightadd2, text="Địa chỉ:", font=('arial 16 bold'), fg='black', bg='lightblue')
        self.n2.place(x=10, y=150)

        self.n2_p = Entry(self.rightadd2, font=('arial 18 bold'), width=32)
        self.n2_p.place(x=150, y=150)

        self.add_dt = Button(self.rightadd2, text="Thêm", width=12, height=1, font=('arial 18 bold'), bg='orange',command=self.database_print)
        self.add_dt.place(x=10, y=260)

        self.add_dl = Button(self.rightadd2, text="Sửa", width=12, height=1, font=('arial 18 bold'), bg='orange',
                             )
        self.add_dl.place(x=200, y=260)

        self.add_dltd = Button(self.rightadd2, text="Xóa", width=12, height=1, font=('arial 18 bold'), bg='orange',
                               )
        self.add_dltd.place(x=390, y=260)

    def database_print111(self, *args, **kwargs):

        nameadd22 = c1.get()
        name_dt22 = self.ad_if2.get()

        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        if nameadd22 == '' or name_dt22 ==  '':
            tkinter.messagebox.showinfo("Error", "Please Fill all the entries.")

        else:
            cursor.execute('CREATE TABLE IF NOT EXISTS print_dt22 (name_pk22 TEXT,dt_name22 TEXT)')
            cursor.execute('INSERT INTO print_dt22 (name_pk22,dt_name22) VALUES(?,?)',
                           (nameadd22, name_dt22))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Successfully added to the database")

    def createNewWindow(self, *args, **kwarg):
        newWindowaddf = Toplevel(root)
        newWindowaddf.title("add infomation")
        newWindowaddf.geometry("800x500")

        self.rightw2 = Frame(newWindowaddf, width=500, height=500, bg='lightblue')
        self.rightw2.pack(side=RIGHT)
        self.rightw3 = Frame(newWindowaddf, width=290, height=500, bg='lightblue')
        self.rightw3.pack(side=LEFT)

        self.n3 = Label(self.rightw3, text="Chẩn Đoán:", font=('arial 14 bold'), fg='black', bg='lightblue')
        self.n3.place(x=10, y=10)

        self.ad_if2 = Entry(self.rightw3, font=('arial 20 bold'), width=16)
        self.ad_if2.place(x=10, y=40)

        self.n4 = Label(self.rightw3, text="Danh Mục:", font=('arial 14 bold'), fg='black', bg='lightblue')
        self.n4.place(x=10, y=90)

        self.droplist = OptionMenu(self.rightw3,c1, 'TAI', 'MŨI','HỌNG')
        self.droplist.pack()

        self.menu = self.droplist.nametowidget(self.droplist.menuname)
        self.menu.configure(font=('arial 28 bold'))
        c1.set('HỌNG')

        self.droplist.config(width=16,height=2,font=('arial 18 bold'))
        self.droplist.place(x=5, y=120)

        self.add_ifmt = Button(self.rightw3,text="Thêm", width=14, height=2, font=('arial 20 bold'), bg='orange',command=self.database_print111)
        self.add_ifmt.place(x=5, y=200)

        self.add_dltifmt = Button(self.rightw3, text="Lưu", width=14, height=2, font=('arial 20 bold'),
                                  bg='orange')
        self.add_dltifmt.place(x=5, y=300)

        self.add_dltd = Button(self.rightw3, text="Xóa", width=14, height=2, font=('arial 20 bold'),
                               bg='orange')
        self.add_dltd.place(x=5, y=400)
        scrollbary = Scrollbar(self.rightw2, orient=VERTICAL)
        scrollbarx = Scrollbar(self.rightw2, orient=HORIZONTAL)
        tree = ttk.Treeview(self.rightw2, columns=("Diagnostic", "Firstname"),
                            selectmode="extended", height=500, yscrollcommand=scrollbary.set,
                            xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('Diagnostic', text="Diagnostic", anchor=W)
        tree.heading('Firstname', text="Firstname", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=200)
        tree.column('#2', stretch=NO, minwidth=0, width=300)
        tree.pack()

        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `print_dt22`")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()


    def quit(self):
        root.destroy()

    def endoscopy(self):
        class tehseencode(QDialog):
            def __init__(self):

                super(tehseencode, self).__init__()
                loadUi("untitled2.ui", self)
                self.logic = 0
                self.value = 1
                self.SHOW.clicked.connect(self.onClicked)
                self.TEXT.setText("Kindly Press 'Show' to connect with webcam.")
                self.CAPTURE.clicked.connect(self.CaptureClicked)
                self.NEXT_3.clicked.connect(self.exitpro)
                self.CAPTURE_2.clicked.connect(self.f2vrec)
                self.NEXT_2.clicked.connect(self.w1)

            @pyqtSlot()
            def onClicked(self):
                self.TEXT.setText('Kindly Press "Capture Image " to Capture image')
                cap = cv2.VideoCapture(0)
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                op = cv2.VideoWriter('Sample1.avi', fourcc, 11.0, (800, 600))
                while (cap.isOpened()):
                    ret, frame = cap.read()
                    frame = imutils.resize(frame, width=800, height=600)
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    if ret == True:
                        print('here')
                        self.displayImage(frame, 1)
                        cv2.waitKey()
                        if (self.logic == 2):
                            self.value = self.value + 1
                            cv2.imwrite('anh\%s.png' % (self.value), frame)
                            self.logic = 1
                            self.TEXT.setText('your Image have been Saved')
                        if (self.logic == 3):
                            op.write(frame)
                        if (self.logic == 4):
                            cap.release()
                            break

                    else:
                        print('not found')
                cap.release()
                cv2.destroyAllWindows()

            def CaptureClicked(self):
                self.logic = 2

            def displayImage(self, img, window=1):
                qformat = QImage.Format_Indexed8
                if len(img.shape) == 3:
                    if (img.shape[2]) == 4:
                        qformat = QImage.Format_RGBA888
                    else:
                        qformat = QImage.Format_RGB888
                img = QImage(img, img.shape[1], img.shape[0], qformat)
                img = img.rgbSwapped()
                self.imgLabel.setPixmap(QPixmap.fromImage(img))
                self.imgLabel.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignLeft)

            def exitpro(self):
                self.logic = 4

            def f2vrec(self):
                self.logic = 3

            def w1(self):

                window.close()
                self.logic = 4



        window = tehseencode()
        window.show()
        try:
            sys.exit(app.exec_())
        except:
            print('excitng')


app = QApplication(sys.argv)
b = Application(root)

root.geometry("1360x786+0+0")
root.mainloop()
