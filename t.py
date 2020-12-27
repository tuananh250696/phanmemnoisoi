from tkinter import *
import sqlite3
import tkinter as tk
import tkinter.messagebox
from datetime import date
from tkinter import ttk
import datetime
import sys
from fpdf import FPDF
import webbrowser
import cv2
import os
from PyQt5 import QtCore, QtGui, QtWidgets                     # uic
from PyQt5.QtWidgets import (QLabel)              # +++
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
import shutil
from test2_ui import Ui_Form
import numpy as np
import time
import imutils
# Load Yolo
net = cv2.dnn.readNet("yolov3-tiny_last.weights", "yolov3-tiny.cfg")
classes = []
with open("classes.txt", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))
font = cv2.FONT_HERSHEY_PLAIN
starting_time = time.time()
frame_id = 0

today = date.today()
date = datetime.datetime.now().date()
# temporary lists like sessions
products_list = []
product_price = []
product_quantity = []
product_id = []
# list for labels
#w = root.winfo_screenwidth()
#h = root.winfo_screenheight()f
root = Tk()
root.title("COMPANY BOSSCCOM")
labels_list = []
var = IntVar()
var1 = IntVar()
c = StringVar()
c1 = StringVar()
logic1 = 1



class Application:
    def __init__(self, master):
        self.master = master
        self.logic1 = 1
        # frame
        self.left = Frame(master, width=215, height=600, bg='white')
        self.left.pack(side=LEFT)
        # components
        self.date_l = Label(self.left,
                            text="Today's Date: " + str(today.day) + "-" + str(today.month) + "-" + str(today.year),
                            font=('arial 12 bold'), bg='lightblue',
                            fg='white')
        self.date_l.place(x=10, y=0)

        # button
        self.bt_st_catalog = Button(self.left, text="Hồ sơ bệnh nhân", width=16, height=4, font=('arial 14 bold'),
                                    bg='orange', command=self.ajax)
        self.bt_st_catalog.place(x=5, y=30)

        self.bt_st_form = Button(self.left, text="Nội soi", width=16, height=4, font=('arial 14 bold'), bg='orange',command=self.endoscopy)#get_itemsdatabase)
        self.bt_st_form.place(x=5, y=136)

        self.bt_patient = Button(self.left, text="Biểu mẫu in", width=16, height=4, font=('arial 14 bold'), bg='orange',
                                 command=self.add_to_bn)
        self.bt_patient.place(x=5, y=242)

        self.bt_endoscop = Button(self.left, text="Danh mục khám", width=16, height=4, font=('arial 14 bold'),
                                  bg='orange', command=self.createNewWindow)
        self.bt_endoscop.place(x=5, y=348)

        self.bt_exit1 = Button(self.left, text="Thoát", width=16, height=4, font=('arial 14 bold'), bg='orange',
                               command=self.quit)
        self.bt_exit1.place(x=5, y=454)



    def Search(self):
        # =====================================Table WIDGET=========================================
        self.tree.delete(*self.tree.get_children())
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM `member` WHERE `name` LIKE ? AND `job` LIKE ? AND `address` LIKE ? AND `age` LIKE ?",
            ('%' + str(self.name_infos.get()) + '%', '%' + str(self.from_jobs.get()) + '%',
             '%' + str(self.from_addss.get()) + '%', '%' + str(self.born_agess.get()) + '%'))
        fetch = cursor.fetchall()
        for data in fetch:
            self.tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        self.name_infos.delete(0, tk.END)
        self.from_jobs.delete(0, tk.END)
        self.from_addss.delete(0, tk.END)
        self.born_agess.delete(0, tk.END)

    def ajax(self):
        if (self.logic1 == 1):
            self.right = Frame(root, width=800, height=92, bg='white')
            self.right.pack(side=TOP)

            self.bottom = Frame(root, width=800, height=220, bg='lightblue')
            self.bottom.pack(side=TOP)

            self.bottom1 = Frame(root, width=800, height=80, bg='yellow')
            self.bottom1.pack(side=TOP)

            self.bottom2 = Frame(root, width=800, height=550, bg='lightblue')
            self.bottom2.pack(side=TOP)

            self.Top = Frame(self.bottom2, width=800, bd=2, relief=SOLID)
            self.Top.pack(side=TOP)
            self.MidFrame = Frame(self.bottom2, width=800)
            self.MidFrame.pack(side=TOP)
            self.RightForm = Frame(self.MidFrame, width=800)
            self.RightForm.pack(side=RIGHT)

            self.bt_add_patient = Button(self.right, text="Lưu hồ sơ", width=11, height=4, font=('arial 12 bold'),
                                         bg='white', command=self.get_itemsdatabase)
            self.bt_add_patient.place(x=0, y=0)

            self.bt_open_file = Button(self.right, text="Mở hồ sơ", width=11, height=4, font=('arial 12 bold'),
                                       bg='white',
                                       command=self.create_pdf1)
            self.bt_open_file.place(x=123, y=0)
            #
            self.bt_save_file = Button(self.right, text="Làm mới", width=11, height=4, font=('arial 12 bold'),
                                       bg='white',
                                       command=self.delete_text)
            self.bt_save_file.place(x=246, y=0)
            #
            self.bt_delele1 = Button(self.right, text="Xóa", width=11, height=4, font=('arial 12 bold'), bg='white',
                                     command=self.Deletedata)
            # command=self.Deletedata)
            self.bt_delele1.place(x=369, y=0)
            #
            self.bt_thoat = Button(self.right, text="Đóng", width=12, height=4, font=('arial 12 bold'), bg='white',
                                   command=self.add_to_cart)

            self.bt_thoat.place(x=492, y=0)
            self.bt_thoat = Button(self.right, text="Khôi phục cài đặt gốc", width=16, height=4, font=('arial 12 bold'),
                                   bg='white', command=self.Deletealldata)
            self.bt_thoat.place(x=625, y=0)

            self.tenbenhnhan = Label(self.bottom, text="Tên bệnh nhân:", font=('arial 12 bold'), fg='black',
                                     bg='lightblue')
            self.tenbenhnhan.place(x=15, y=5)

            self.name_p = Entry(self.bottom, font=('arial 20 bold'), width=20)
            self.name_p.place(x=5, y=30)
            self.name_p.focus()

            self.adr = Label(self.bottom, text="Địa chỉ:", font=('arial 12 bold'), fg='black', bg='lightblue')
            self.adr.place(x=15, y=75)

            self.adr_p = Entry(self.bottom, font=('arial 20 bold'), width=20)
            self.adr_p.place(x=5, y=100)

            self.year_b = Label(self.bottom, text="Năm sinh:", font=('arial 12 bold'), fg='black', bg='lightblue')
            self.year_b.place(x=15, y=150)

            self.y_b = Entry(self.bottom, font=('arial 20 bold'), width=20)
            self.y_b.place(x=5, y=175)

            self.job = Label(self.bottom, text="Nghề nghiệp:", font=('arial 12 bold'), fg='black', bg='lightblue')
            self.job.place(x=330, y=5)
            self.jobw = Entry(self.bottom, font=('arial 20 bold'), width=18)
            self.jobw.place(x=320, y=30)

            self.st = Label(self.bottom, text="Triệu chứng:", font=('arial 12 bold'), fg='black', bg='lightblue')
            self.st.place(x=330, y=75)
            self.stom = Entry(self.bottom, font=('arial 20 bold'), width=18)
            self.stom.place(x=320, y=100)

            self.sbh = Label(self.bottom, text="Số bảo hiểm:", font=('arial 12 bold'), fg='black', bg='lightblue')
            self.sbh.place(x=330, y=150)
            self.nbh = Entry(self.bottom, font=('arial 20 bold'), width=18)
            self.nbh.place(x=320, y=175)

            self.tel = Label(self.bottom, text="Điện thoại:", font=('arial 12 bold'), fg='black', bg='lightblue')
            self.tel.place(x=615, y=5)
            self.telw = Entry(self.bottom, font=('arial 20 bold'), width=12)
            self.telw.place(x=605, y=30)

            # self.enteride = Entry(self.bottom, width=25, font=('arial 18 bold'), bg='lightblue')
            # self.enteride.place(x=800, y=175)
            # self.enteride.focus()

            self.droplist = OptionMenu(self.bottom, c, 'NAM', 'NỮ')
            self.droplist.pack()
            self.menu = self.droplist.nametowidget(self.droplist.menuname)
            self.menu.configure(font=('arial 20 bold'))
            c.set('NAM')
            self.droplist.config(width=10, font=('arial 18 bold'))
            self.droplist.place(x=610, y=95)

            self.seachinfo = Button(self.bottom1, text="Tìm kiếm", width=12, height=2, font=('arial 14 bold'),
                                    bg='orange',
                                    command=self.Search)
            self.seachinfo.place(x=640, y=10)

            self.name_info = Label(self.bottom1, text="Tên:", font=('arial 12 bold'), fg='black', bg='lightblue')
            self.name_info.place(x=5, y=10)

            self.name_infos = Entry(self.bottom1, width=18, font=('arial 18 bold'), bg='white')
            self.name_infos.place(x=5, y=38)

            self.job_s = Label(self.bottom1, text="Nghề nghiệp:", font=('arial 12 bold'), fg='black', bg='lightblue')
            self.job_s.place(x=245, y=10)
            self.from_jobs = Entry(self.bottom1, font=('arial 18 bold'), width=12)
            self.from_jobs.place(x=245, y=38)

            self.aadd_s = Label(self.bottom1, text="Địa Chỉ:", font=('arial 12 bold'), fg='black', bg='lightblue')
            self.aadd_s.place(x=410, y=10)
            self.from_addss = Entry(self.bottom1, font=('arial 18 bold'), width=10)
            self.from_addss.place(x=410, y=38)

            self.born_s2 = Label(self.bottom1, text="Năm sinh:", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.born_s2.place(x=550, y=10)
            self.born_agess = Entry(self.bottom1, font=('arial 18 bold'), width=6)
            self.born_agess.place(x=550, y=38)

            self.scrollbarx = Scrollbar(self.RightForm, orient=HORIZONTAL)
            self.scrollbary = Scrollbar(self.RightForm, orient=VERTICAL)
            self.tree = ttk.Treeview(self.RightForm, columns=("Id", "Name", "Job", "Address", "Age"),
                                     selectmode="extended",
                                     height=400, yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
            self.scrollbary.config(command=self.tree.yview)
            self.scrollbary.pack(side=RIGHT, fill=Y)
            self.scrollbarx.config(command=self.tree.xview)
            self.scrollbarx.pack(side=BOTTOM, fill=X)
            self.tree.column('#0', stretch=NO, minwidth=0, width=0)
            self.tree.column('#1', stretch=NO, minwidth=0, width=50)
            self.tree.column('#2', stretch=NO, minwidth=0, width=300)
            self.tree.column('#3', stretch=NO, minwidth=0, width=160)
            self.tree.column('#4', stretch=NO, minwidth=0, width=160)

            self.tree.pack()
            self.tree.heading('Id', text="Id", anchor=W)
            self.tree.heading('Name', text="Name", anchor=W)
            self.tree.heading('Job', text="Job", anchor=W)
            self.tree.heading('Address', text="Address", anchor=W)
            self.tree.heading('Age', text="Age", anchor=W)
            self.logic1 = 2




    def Deletedata(self):

        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        for selected_item in self.tree.selection():
            print(selected_item)  # it prints the selected row id
            cursor.execute("DELETE FROM member WHERE id=?", (self.tree.set(selected_item, '#1'),))
            self.tree.delete(selected_item)
        conn.commit()
        conn.close()

    def Deletealldata(self):
        shutil.rmtree("anh")
        conn = sqlite3.connect("db_member.db")
        cur = conn.cursor()
        sql = 'DELETE FROM member'
        cur.execute(sql)
        conn.commit()

    def get_itemsdatabase(self):

        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()

        if self.logic1 == 1 or self.name_p.get() == '' or self.adr_p.get() == '' or self.y_b.get() == '' or self.jobw.get() == '' or self.stom.get() == '' or self.nbh.get() == '' or c.get() == '' or self.telw.get() == ''  :
            tkinter.messagebox.showinfo("Error", "Điền đầy đủ thông tin bệnh nhân.")
        else:

            cursor.execute('INSERT INTO member (name, address, age, job, symptom,sbh,sex,tel ) VALUES(?,?,?,?,?,?,?,?)', (
            self.name_p.get(), self.adr_p.get(), self.y_b.get(), self.jobw.get(), self.stom.get(), self.nbh.get(),
            c.get(),self.telw.get()))
            conn.commit()
            self.name_p.delete(0, END)
            self.adr_p.delete(0, END)
            self.y_b.delete(0, END)
            self.jobw.delete(0, END)
            self.stom.delete(0, END)
            self.nbh.delete(0, END)
            self.telw.delete(0, END)
            self.endoscopy()
            # textbox insert
            # tkinter.messagebox.showinfo("Success", "Successfully added to the database")


    def add_to_cart(self):

        self.right.destroy()
        self.bottom.destroy()
        self.bottom1.destroy()
        self.bottom2.destroy()
        self.logic1 =1

    def delete_text(self, *args, **kwargs):

        self.name_p.delete(0, END)
        self.adr_p.delete(0, END)
        self.y_b.delete(0, END)
        self.jobw.delete(0, END)
        self.stom.delete(0, END)
        self.nbh.delete(0, END)

    def database_print(self, *args, **kwargs):

        namepk = self.adr2_p.get()
        name_dt = self.doctor_p.get()
        address_pk = self.n2_p.get()
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        if namepk == '' or name_dt == '' or address_pk == '':
            tkinter.messagebox.showinfo("Error", "Điền đầy đủ thông tin.")
        else:
            cursor.execute("DELETE FROM print_dt WHERE id=1")
            cursor.execute('CREATE TABLE IF NOT EXISTS print_dt (name_pk TEXT,dt_name TEXT,address TEXT)')
            cursor.execute('INSERT INTO print_dt (name_pk,dt_name,address) VALUES(?,?,?)',
                           (namepk, name_dt, address_pk))
            tkinter.messagebox.showinfo("Success", "Đã thêm thông tin")
            conn.commit()
            cursor.close()

    def add_to_bn(self, *args, **kwargs):
        addWindow = Toplevel(root)
        addWindow.title("Set form print")
        addWindow.geometry("980x500+0+0")
        self.rightw2 = Frame(addWindow, width=550, height=600, bg='lightblue')
        self.rightw2.pack(side=RIGHT)
        self.rightw3 = Frame(addWindow, width=600, height=600, bg='lightblue')
        self.rightw3.pack(side=LEFT)

        self.adr2 = Label(self.rightw3, text="Phòng khám:", font=('arial 16 bold'), fg='black', bg='lightblue')
        self.adr2.place(x=10, y=10)
        self.adr2_p = Entry(self.rightw3, font=('arial 18 bold'), width=30)
        self.adr2_p.place(x=150, y=10)

        self.doctor = Label(self.rightw3, text=" Bác sĩ :", font=('arial 16 bold'), fg='black', bg='lightblue')
        self.doctor.place(x=10, y=85)

        self.doctor_p = Entry(self.rightw3, font=('arial 18 bold'), width=30)
        self.doctor_p.place(x=150, y=75)

        self.n2 = Label(self.rightw3, text="Địa chỉ:", font=('arial 16 bold'), fg='black', bg='lightblue')
        self.n2.place(x=10, y=150)

        self.n2_p = Entry(self.rightw3, font=('arial 18 bold'), width=30)
        self.n2_p.place(x=150, y=150)

        self.add_dt = Button(self.rightw3, text="Cập nhật", width=11, height=3, font=('arial 18 bold'), bg='orange',
                             command=self.database_print)
        self.add_dt.place(x=10, y=260)

        self.add_dl = Button(self.rightw3, text="Xóa", width=11, height=3, font=('arial 18 bold'), bg='orange',
                             command=self.Deletedata_print)
        self.add_dl.place(x=187, y=260)

        self.add_dltd = Button(self.rightw3, text="Đóng", width=11, height=3, font=('arial 18 bold'), bg='orange',
                               command=self.quit_print2)
        self.add_dltd.place(x=364, y=260)

        self.scrollbarx = Scrollbar(self.rightw2, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.rightw2, orient=VERTICAL)
        self.tree1 = ttk.Treeview(self.rightw2, columns=("Id", "Phòng khám", "Bác sĩ", "Địa chỉ"),
                                  selectmode="extended",
                                  height=400, yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.scrollbary.config(command=self.tree1.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbarx.config(command=self.tree1.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree1.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree1.column('#1', stretch=NO, minwidth=0, width=20)
        self.tree1.column('#2', stretch=NO, minwidth=0, width=180)
        self.tree1.column('#3', stretch=NO, minwidth=0, width=120)
        self.tree1.column('#4', stretch=NO, minwidth=0, width=80)

        self.tree1.pack()
        self.tree1.heading('Id', text="Id", anchor=W)
        self.tree1.heading('Phòng khám', text="Phòng khám", anchor=W)
        self.tree1.heading('Bác sĩ', text="Bác sĩ", anchor=W)
        self.tree1.heading('Địa chỉ', text="Địa chỉ", anchor=W)
        self.tree1.pack()

        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `print_dt`")
        fetch = cursor.fetchall()
        for data in fetch:
            self.tree1.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

    def Deletedata_print(self):
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        for selected_item1 in self.tree1.selection():
            print(selected_item1)  # it prints the selected row id
            cursor.execute("DELETE FROM print_dt WHERE id=?", (self.tree1.set(selected_item1, '#1'),))
            conn.commit()
            self.tree1.delete(selected_item1)
        conn.commit()
        cursor.close()

    def Chosedata_print(self):
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        for selected_item1 in self.tree1.selection():
            print(selected_item1)  # it prints the selected row id
            cursor.execute("DELETE FROM print_dt WHERE id=?", (self.tree1.set(selected_item1, '#1'),))
            conn.commit()
            self.tree1.delete(selected_item1)
        conn.commit()
        cursor.close()

    def database_print111(self):
        nameadd22 = c1.get()
        name_dt22 = self.ad_if2.get()

        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        if nameadd22 == '' or name_dt22 == '':
            tkinter.messagebox.showinfo("Error", "điền đầy đủ thông tin!.")

        else:
            cursor.execute('CREATE TABLE IF NOT EXISTS print_dt22 (name_pk22 TEXT,dt_name22 TEXT)')
            cursor.execute('INSERT INTO print_dt22 (name_pk22,dt_name22) VALUES(?,?)',
                           (nameadd22, name_dt22))
            tkinter.messagebox.showinfo("Success", "Đã thêm thông tin")
            conn.commit()
            cursor.close()

    def createNewWindow(self):
        newWindowaddf = Toplevel(root)
        newWindowaddf.title("add infomation")
        newWindowaddf.geometry("800x500+0+0")

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

        self.droplist = OptionMenu(self.rightw3, c1, 'TAI', 'MŨI', 'HỌNG')
        self.droplist.pack()

        self.menu = self.droplist.nametowidget(self.droplist.menuname)
        self.menu.configure(font=('arial 28 bold'))
        c1.set('HỌNG')

        self.droplist.config(width=16, height=2, font=('arial 18 bold'))
        self.droplist.place(x=5, y=120)

        self.add_ifmt = Button(self.rightw3, text="Cập nhật", width=14, height=2, font=('arial 20 bold'), bg='orange',
                               command=self.database_print111)
        self.add_ifmt.place(x=5, y=200)

        self.add_dltifmt = Button(self.rightw3, text="Xóa", width=14, height=2, font=('arial 20 bold'),
                                  bg='orange', command=self.Deletedata_NewWindow)
        self.add_dltifmt.place(x=5, y=300)

        self.add_dltd = Button(self.rightw3, text="Đóng", width=14, height=2, font=('arial 20 bold'),
                               bg='orange', command=self.quit_print1)
        self.add_dltd.place(x=5, y=400)
        scrollbary = Scrollbar(self.rightw2, orient=VERTICAL)
        scrollbarx = Scrollbar(self.rightw2, orient=HORIZONTAL)
        self.tree2 = ttk.Treeview(self.rightw2, columns=("Diagnostic", "Firstname"),
                                  selectmode="extended", height=500, yscrollcommand=scrollbary.set,
                                  xscrollcommand=scrollbarx.set)
        scrollbary.config(command=self.tree2.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=self.tree2.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree2.heading('Diagnostic', text="Diagnostic", anchor=W)
        self.tree2.heading('Firstname', text="Firstname", anchor=W)
        self.tree2.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree2.column('#1', stretch=NO, minwidth=0, width=200)
        self.tree2.column('#2', stretch=NO, minwidth=0, width=300)
        self.tree2.pack()

        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `print_dt22`")
        fetch = cursor.fetchall()
        for data in fetch:
            self.tree2.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

    def Deletedata_NewWindow(self):
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        for selected_item1 in self.tree2.selection():
            print(selected_item1)  # it prints the selected row id
            cursor.execute("DELETE FROM print_dt22 WHERE name_pk22=?", (self.tree2.set(selected_item1, '#1'),))
            conn.commit()
            self.tree2.delete(selected_item1)
        conn.commit()
        cursor.close()

    def quit(self):
        root.withdraw()
        root.destroy()

    def quit_print1(self):

        tkinter.messagebox.showinfo("Success", "Thoát cài đặt danh mục")


    def quit_print2(self):
        tkinter.messagebox.showinfo("Success", "Thoát cài đặt biểu mẫu")

    def hide(self):
        root.withdraw()

    def show(self):
        root.update()
        root.deiconify()

    def create_pdf1(self):
        # Set up a logo
        conn = sqlite3.connect("db_member.db")
        conn.row_factory = sqlite3.Row
        for selected_item in self.tree.selection():
            print(selected_item)
        cur = conn.cursor()
        cur.execute("SELECT * FROM `member` WHERE id=?", (self.tree.set(selected_item, '#1'),))
        rows = cur.fetchall()
        for row in rows:
            print("%s" % (row["id"]))
        #webbrowser.open_new(r'doccument/%s.pdf' % ("a" + str(row["id"])))
        webbrowser.open_new(r'doccument/%s.pdf' % ("a" + str(row["id"])))

    def endoscopy(self):

        class Window2(QMainWindow):  # <===
            def __init__(self):
                super().__init__()

                self.title = "Print Window"
                self.top = 0
                self.left = 0
                self.width = 700
                self.height = 500

                self.pushButton = QPushButton("In Phiếu Khám", self)
                self.pushButton.setGeometry(QtCore.QRect(130, 360, 220, 100))
                self.pushButton.setToolTip("<h3>Start Print</h3>")
                self.pushButton1 = QPushButton("Đóng", self)
                self.pushButton1.setGeometry(QtCore.QRect(350, 360, 220, 100))
                self.pushButton1.setToolTip("<h3>Close</h3>")

                font = QtGui.QFont()
                font.setPointSize(20)
                font1 = QtGui.QFont()
                font1.setPointSize(16)

                self.text2=QtWidgets.QLabel("Chẩn Đoán : ",self)
                self.text2.setGeometry(QtCore.QRect(90,20, 225,50))
                self.text2.setFont(font1)
                self.text1 = QtWidgets.QLabel("Điều Trị : ", self)
                self.text1.setGeometry(QtCore.QRect(90,125, 200, 50))
                self.text1.setFont(font1)

                self.text2 = QtWidgets.QLabel("Chỉ Định : ", self)
                self.text2.setGeometry(QtCore.QRect(90, 225, 200, 50))
                self.text2.setFont(font1)

                self.lineEdit = QtWidgets.QLineEdit(self)
                self.lineEdit.setGeometry(QtCore.QRect(70,70, 530 , 50))
                self.lineEdit.setObjectName("lineEdit")
                self.lineEdit.setPlaceholderText('chẩn đoán')
                self.lineEdit.setFont(font)

                self.lineEdit_2 = QtWidgets.QLineEdit(self)
                self.lineEdit_2.setGeometry(QtCore.QRect(70, 170, 530, 50))
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.lineEdit_2.setPlaceholderText('Phương pháp điều trị')
                self.lineEdit_2.setFont(font)

                self.lineEdit_3 = QtWidgets.QLineEdit(self)
                self.lineEdit_3.setGeometry(QtCore.QRect(70, 270, 530, 50))
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                self.lineEdit_3.setFont(font)
              #  self.pushButton.move(275,420)
                self.pushButton.clicked.connect(self.create_pdf2)#self.create_pdf2)
                self.pushButton1.clicked.connect(self.winc)
                self.main_window()

            def main_window(self):

                self.setWindowTitle(self.title)
                self.setGeometry(self.top, self.left, self.width, self.height)
                self.show()


            def winc(self):
                self.hide()

            def create_pdf2(self):
                # Set up a logo
                shost = self.lineEdit.text()
                shost2 = self.lineEdit_2.text()
                shost3 = self.lineEdit_3.text()

                conn = sqlite3.connect("db_member.db")
                conn.row_factory = sqlite3.Row
                cur = conn.cursor()
                cur.execute("SELECT max(id) FROM member")
                rows = cur.fetchall()
                for row in rows:
                    print("%s" % (row["max(id)"]))

                cur2 = conn.cursor()
                cur2.execute("SELECT name_pk FROM print_dt")
                cur3 = conn.cursor()
                cur3.execute("SELECT address FROM print_dt")
                cur4 = conn.cursor()
                cur4.execute("SELECT dt_name FROM print_dt")
                cur5 = conn.cursor()
                cur5.execute("SELECT * FROM `member`")

                rows5 = cur5.fetchall()
                rows4 = cur4.fetchall()
                rows3 = cur3.fetchall()
                rows2 = cur2.fetchall()

                for row5 in rows5:
                    row5[6]
                for row2 in rows2:
                    row2["name_pk"]

                for row3 in rows3:
                    row3["address"]

                for row4 in rows4:
                    row4["dt_name"]

                t = row2["name_pk"]
                t1 = row3["address"]
                t2 = "BS: " + row4["dt_name"]

                pdf = FPDF()
                pdf.set_font("Arial", size=12)
                pdf.add_page()

                pdf.image('demo.png', 8, 10, 25)
                pdf.add_font('DejaVu', '', 'DejaVuSerif-Italic.ttf', uni=True)
                pdf.set_font('DejaVu', '', 16)
                pdf.set_text_color(0, 70, 255)
                pdf.cell(35)
                pdf.cell(0, 5, t, ln=1)
                pdf.set_font('DejaVu', '', 14)

                pdf.cell(70)
                pdf.cell(0, 10, t2, ln=1)
                pdf.set_font('DejaVu', '', 14)
                pdf.set_text_color(0, 70, 255)
                pdf.cell(30)

                pdf.cell(0, 0, "ĐC:", ln=1)
                pdf.set_font('DejaVu', '', 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(40)
                pdf.cell(0, 0, t1, ln=1)
                pdf.set_draw_color(0, 0, 0)
                pdf.set_line_width(1)
                pdf.line(30, 30, 180, 30)

                pdf.set_font('DejaVu', '', 16)
                pdf.set_text_color(255, 0, 40)
                pdf.cell(35)
                pdf.cell(0, 5, ' ', ln=1)

                pdf.set_font('DejaVu', '', 16)
                pdf.set_text_color(255, 0, 40)
                pdf.cell(35)
                pdf.cell(0, 15, 'PHIẾU KHÁM NỘI SOI TAI-MŨI-HỌNG', ln=1)

                pdf.set_font('DejaVu', '', 12)
                pdf.set_text_color(0, 70, 255)
                pdf.cell(75)
                pdf.cell(0, 0, 'Số Phiếu : ' + str(row5[0]), ln=1)

                pdf.set_font('DejaVu', '', 16)
                pdf.set_text_color(0, 70, 255)
                pdf.cell(0, 8, ' ', ln=1)

                pdf.set_font('DejaVu', '', 10)
                pdf.cell(5)
                pdf.cell(0, 0, 'Tên bệnh nhân : ' + str(row5[1]), ln=1)
                pdf.cell(85)
                pdf.cell(0, 0, 'Tuổi : ' + str(row5[4]), ln=1)
                pdf.cell(135)
                pdf.cell(0, 0, 'Giới tính : ' + str(row5[6]), ln=1)

                pdf.set_font('DejaVu', '', 10)
                pdf.set_text_color(0, 70, 255)
                pdf.cell(0, 8, ' ', ln=1)
                pdf.cell(5)
                pdf.cell(0, 0, 'Địa chỉ : ' + str(row5[3]), ln=1)
                pdf.cell(85)
                pdf.cell(0, 0, 'Số bảo hiểm : ' + str(row5[7]), ln=1)
                pdf.cell(135)
                pdf.cell(0, 0, 'Nghề nghiệp : ' + str(row5[2]), ln=1)

                pdf.set_font('DejaVu', '', 10)
                pdf.set_text_color(0, 70, 255)
                pdf.cell(0, 8, ' ', ln=1)
                pdf.cell(5)
                pdf.cell(0, 0, 'Triệu chứng : ' + str(row5[5]), ln=1)
                pdf.cell(85)
                pdf.cell(0, 0, 'Điện thoại: ' + str(row5[8]), ln=1)

                pdf.set_font('DejaVu', '', 14)
                pdf.cell(0, 15, ' ', ln=1)
                pdf.cell(70)
                pdf.cell(0, 0, 'HÌNH ẢNH NỘI SOI ', ln=1)
                #
                file_name =  ('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(1)))
                file_name1 = ('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(2)))
                file_name2 = ('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(3)))
                file_name3 = ('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(4)))
                file_name4 = ('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(5)))
                file_name5 = ('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(6)))
                #
                pdf.image(file_name, 12, 90, 60)
                pdf.image(file_name1, 12, 150, 60)
                pdf.image(file_name2, 74, 90, 60)
                pdf.image(file_name3, 74, 150, 60)
                pdf.image(file_name4, 136, 90, 60)
                pdf.image(file_name5, 136, 150, 60)

                pdf.set_font('DejaVu', '', 16)
                pdf.cell(0, 130, ' ', ln=1)
                pdf.cell(60)
                pdf.cell(0, 0, 'MÔ TẢ KẾT QUẢ NỘI SOI ', ln=1)
                pdf.set_font('DejaVu', '', 12)
                pdf.cell(0,5, ' ', ln=1)
                pdf.cell(12)
                pdf.cell(0, 7, 'Chẩn đoán : %s'% (shost), ln=1)
                pdf.cell(12)
                pdf.cell(0, 7, 'Điều trị : %s'% (shost2), ln=1)
                pdf.cell(12)
                pdf.cell(0, 7, 'Chỉ định bác sĩ : %s'% (shost3), ln=1)

                pdf.set_x(120)
                pdf.cell(0, 14, " Ngày " + str(today.day) + " Tháng " + str(today.month) + " Năm " + str(today.year),
                         ln=1)
                pdf.set_x(145)
                pdf.cell(0, 6, 'Bác sĩ : ', ln=1)
                pdf.cell(0, 15, ' ', ln=1)
                pdf.set_x(126)
                pdf.cell(0, 0, t2, ln=1)
                directory1 = "doccument/"
                if not os.path.exists(directory1):
                    os.makedirs(directory1)
                pdf.output('doccument\%s.pdf' %("a" + str(row["max(id)"])))
                webbrowser.open_new(r'doccument\%s.pdf' %("a" + str(row["max(id)"])))
#                 pdf.output('doccument/%s.pdf' % ("a" + str(row["max(id)"])))
#                 webbrowser.open_new(r'doccument\%s.pdf' % ("a" + str(row["max(id)"])))
                conn.commit()
                cur.close()
                
                self.winc()

        class video(QtWidgets.QDialog, Ui_Form):

            def __init__(self):
                self.value1 = 0
                super().__init__()
                self.value = 0                 # ---
                self.setupUi(self)  # ++
                self.CAPTURE.clicked.connect(self.capture_image)
                self.NEXT_3.clicked.connect(self.window2)

                # adding items to the combo box
                self.available_cameras = QCameraInfo.availableCameras()
                self.camera_selector.addItem("  CAMERA USB3.0")
                self.camera_selector.addItems([camera.description()
                                          for camera in self.available_cameras])
                self.camera_selector1.addItem("   Chụp Tự Động")
                self.camera_selector1.addItem("  Chụp Thủ Công")
                self.camera_selector.currentIndexChanged.connect(self.select_camera)

                self.NEXT_7.clicked.connect(self.w1)
                self.imgLabel.setScaledContents(True)
                self.cap = None  # -capture <-> +cap
                self.timer = QtCore.QTimer(self, interval=5)
                self.timer.timeout.connect(self.update_frame)
                self._image_counter = 0
                self.start_webcam()
                self.saveTimer = QTimer()

            @QtCore.pyqtSlot()
            def start_webcam(self):
                if self.cap is None:
                    self.cap = cv2.VideoCapture(0)
                self.timer.start()
            @QtCore.pyqtSlot()

            def update_frame(self):
                ret, image = self.cap.read()
                # Define the codec and create VideoWriter object
                #image = imutils.resize(image, width=320, height=256)
                #time.sleep(2.0)
                if ret == True:
                    image = cv2.resize(image, (640, 360))
                    image = cv2.flip(image, 1)
                    frame1 = imutils.resize(image, width=160)
                    #frame1 = imutils.resize(image, width=640, height=480)
                    (H, W) = frame1.shape[:2]
                    height, width, channels = frame1.shape
                    # Detecting objects
                    blob = cv2.dnn.blobFromImage(frame1, 0.00392, (W, H), (0, 0, 0), True, crop=False)
                    # blob = cv2.dnn.blobFromImage(frame, 0.00392, (224, 224), (0, 0, 0), True, crop=False)
                    net.setInput(blob)
                    outs = net.forward(output_layers)
                    # Showing informations on the screen
                    class_ids = []
                    confidences = []
                    boxes = []
#                     start_time = time.time()
#                  
#                     if (time.time() - start_time ) > 0:
#                         fpsInfo = "FPS: " + str(1.0 / (time.time() - start_time)) # FPS = 1 / time to process loop
#                         font = cv2.FONT_HERSHEY_DUPLEX
#                         cv2.putText(image, fpsInfo, (10, 20), font, 0.4, (255, 255, 255), 1)
#         
                    for out in outs:
                        for detection in out:
                            scores = detection[5:]
                            class_id = np.argmax(scores)
                            confidence = scores[class_id]
                            if confidence > 0.01:
                                # Object detected
                                center_x = int(detection[0] * width)
                                center_y = int(detection[1] * height)
                                w = int(detection[2] * width)
                                h = int(detection[3] * height)
                                # Rectangle coordinates
                                x = int(center_x - w / 2)
                                y = int(center_y - h / 2)
                                boxes.append([x, y, w, h])
                                confidences.append(float(confidence))
                                class_ids.append(class_id)
                    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.4, 0.3)
                    for i in range(len(boxes)):
                        if i in indexes:
                            label = str(classes[class_ids[i]])
                             #cv2.putText(image, label , (20,20), font, 2,(255, 255, 255), 2)
                            print(label)
                            confidence = confidences[i]
                            color = colors[class_ids[i]]
                            cv2.putText(image, label + " " + str(round(confidence, 2)), (x, y + 30), font, 3, (255,255,255), 3)
                            if self.value < 8:
                                self.value = self.value + 1
                                conn = sqlite3.connect("db_member.db")
                                conn.row_factory = sqlite3.Row
                                cur = conn.cursor()
                                cur.execute("SELECT max(id) FROM member")
                                rows = cur.fetchall()
                                directory = "anh/"
                                if not os.path.exists(directory):
                                    os.makedirs(directory)
                                for row in rows:
                                    print("%s" % (row["max(id)"]))
                                cv2.imwrite('anh/%s.png' % ( "a" + str(row["max(id)"]) +  "a" + str(self.value)),frame1)
                                # self.TEXT.setText('your Image have been Saved')
                                self.label = QLabel(self)
                                
                                self.it.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) + "a" +  str(1))))
                                self.it1.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) +  "a" + str(2))))
                                self.it2.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) +  "a" + str(3))))
                                self.it3.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) +  "a" + str(4))))
                                self.it4.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) +  "a" + str(5))))
                                self.it5.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) +  "a" + str(6))))
                                self.it6.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) +  "a" + str(7))))
                                self.it7.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) +  "a" + str(8))))
                                self.it8.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) +  "a" + str(9))))
                                self.it9.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) +  "a" + str(10))))
                                self.it10.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) +  "a" + str(11))))
                                self.it11.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) +  "a" + str(12))))
                                self.it12.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) +  "a" + str(13))))
                                self.it13.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) + "a" +  str(14))))
                                self.it14.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) +  "a" + str(15))))
                                self.it15.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) +  "a" + str(16))))
                                self.it16.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) +  "a" + str(17))))
                                self.it17.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) +  "a" + str(18))))
                                 # self.TEXT.setText(str(row["max(id)"]) + label+ str(self.value))
                                self.TEXT.setText('anh/%s.png')
                    elapsed_time = time.time() - starting_time
                    fps = frame_id / elapsed_time
                    cv2.putText(image, "FPS: " + str(round(fps, 2)), (10, 50), font, 3, (0, 0, 0), 3)
                    self.displayImage(image, True)
                else:
                    self.cap.release()
            @QtCore.pyqtSlot()
            def capture_image(self):
                flag, frame = self.cap.read()
                frame1 = imutils.resize(frame, width=200, height=150)
                self.value1 = self.value1 + 1
                conn = sqlite3.connect("db_member.db")
                conn.row_factory = sqlite3.Row
                cur = conn.cursor()
                cur.execute("SELECT max(id) FROM member")
                rows = cur.fetchall()
                directory = "anh/"
                if not os.path.exists(directory):
                    os.makedirs(directory)
                for row in rows:
                    print("%s" % (row["max(id)"]))
                cv2.imwrite('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.value1)), frame1)
                self.TEXT.setText('your Image have been Saved')
                self.label = QLabel(self)
                self.it.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) + "a" +  "1")))
                self.it1.setIcon(QtGui.QIcon('anh/%s.png' % ("a" +str(row["max(id)"]) +  "a" + "2")))
                self.it2.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" +  "3")))
                self.it3.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" +  "4")))
                self.it4.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) + "a" +  "5")))
                self.it5.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) + "a" +  "6")))
                self.it6.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) + "a" +  "7")))
                self.it7.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) + "a" +  "8")))
                self.it8.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) + "a" +  "9")))
                self.it9.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) + "a" +  "10")))
                self.it10.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) + "a" +  "11")))
                self.it11.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) +  "a" + "12")))
                self.it12.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) +  "a" + "13")))
                self.it13.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) + "a" +  "14")))
                self.it14.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) + "a" +  "15")))
                self.it15.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) + "a" +  "16")))
                self.it16.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) + "a" +  "17")))
                self.it17.setIcon(QtGui.QIcon('anh/%s.png' % ( "a" + str(row["max(id)"]) + "a" +  "18")))            
                conn.commit()
                conn.close()

            def window2(self):  # <===
                self.w = Window2()
                self.w.show()
                #self.hide()
            

            def select_camera(self, i):

                # getting the selected camera
                self.camera = QCamera(self.available_cameras[i])
                # setting view finder to the camera
                self.camera.setViewfinder(self.viewfinder)
                # setting capture mode to the camera
                self.camera.setCaptureMode(QCamera.CaptureStillImage)
                # if any error occur show the alert
                self.camera.error.connect(lambda: self.alert(self.camera.errorString()))
                # start the camera
                self.camera.start()
                # creating a QCameraImageCapture object
                self.capture = QCameraImageCapture(self.camera)
                # showing alert if error occur
                self.capture.error.connect(lambda error_msg, error,
                                                  msg: self.alert(msg))

                # when image captured showing message
                self.capture.imageCaptured.connect(lambda d,
                                                          i: self.status.showMessage("Image captured : "
                                                                                     + str(self.save_seq)))
                # getting current camera name
                self.current_camera_name = self.available_cameras[i].description()
                # inital save sequence
                self.save_seq = 0

            def displayImage(self, img, window=True):
                qformat = QtGui.QImage.Format_Indexed8
                if len(img.shape) == 3:
                    if img.shape[2] == 4:
                        qformat = QtGui.QImage.Format_RGBA8888
                    else:
                        qformat = QtGui.QImage.Format_RGB888
                outImage = QtGui.QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
                outImage = outImage.rgbSwapped()
                if window:
                    self.imgLabel.setPixmap(QtGui.QPixmap.fromImage(outImage))

            
            def w1(self):
                window.close()
                self.cap.release()

        window = video()
        window.setGeometry(0,0, 1024, 600)
        window.show()
        try:
            sys.exit(app.exec_())
        except:
            print('excitng')

app = QApplication(sys.argv)
root.geometry("1024x600+0+0")
b = Application(root)
root.mainloop()

