from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import math
import os
import random
date = datetime.datetime.now().date()

#Tạo cửa sổ windown trong python
window=Tk()
# tất cả đối tượng trong windown sẽ được định nghĩa trong này
window.title("myraming in python") # Tên chương trình trên cửa sổ
window.configure(background="white")    #chọn màu nền cho cửa sổ
#  #define photo
# photo1=PhotoImage(file="iconbosscom.gif") #me.gif tên file chứa cùng thư mục
# pt=Label(window,image=photo1,bg="black")
# pt.grid(row=0,column=0,sticky=W) #đặt tại vị trí 0,0
# Tạo đối tượng Lable với nội dung là title
l1=Label(window,text="title")
#đặt tại vị trí (0,0) trên cửa sổ window
l1.grid(row=50,column=20)
#khai báo biến title_text
title_text=StringVar()
#tạo đổi tượng ô nhập dữ liệu
e1=Entry(window,textvariable=title_text)
#cài vị trí cho ô nhập dữ liệu
e1.grid(row=50,column=55)

#define four labels title author year isbn
l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l1=Label(window,text="Author")
l1.grid(row=0,column=2)

l1=Label(window,text="Year")
l1.grid(row=1,column=0)

l1=Label(window,text="ISBN")
l1.grid(row=1,column=2)
#define entries
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

#Tạo đối tượng list box
list1=Listbox(window,height=9,width=25, font=10)
# Gắn tọa độ cho đối tượng
#row column là tọa độ gốc trên window,
#columnspan, rowspan: tạo độ kết thúc trên windown
list1.grid(row=30,column=1,columnspan=1)

#label1= Label(window, text = 'Hello', size = '50')
list1.insert(1, "C++")
list1.insert(2, "C#")
list1.insert(3, "Python")
list1.insert(4, "Java")
list1.insert(5, "Javascript")

list2=Listbox(window,height=11,width=25, font=10)
# Gắn tọa độ cho đối tượng
#row column là tọa độ gốc trên window,
#columnspan, rowspan: tạo độ kết thúc trên windown
list2.grid(row=50,column=1,columnspan=1)
list2.insert(1, "C+")
list2.insert(2, "C")
list2.insert(3, "Python")
list2.insert(4, "Jav")
list2.insert(5, "Javascrit")

list3=Listbox(window,height=11,width=25, font=10)
list3.grid(row=80,column=1,columnspan=1)
list3.insert(1, "C")
list3.insert(2, "C")



# #tọa thanh cuộn
# sb1=Scrollbar(window)
# sb1.grid(row=50,column=0,rowspan=60)
# #điều khiển listbox bằng scrollbar
# list1.configure(yscrollcommand=sb1.set)
# sb1.configure(command=window.yview)

#khai bao nút nhấn
b1=Button(window,text="view all",width=12)
#Định tọa độ
b1.grid(row=2,column=3)



window.geometry("2560x1440+0+0")
window.mainloop()

