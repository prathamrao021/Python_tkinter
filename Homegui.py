
from tkinter import *
from tkinter import ttk
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy import random
import math
import matplotlib.animation as animation
from matplotlib import style
from time import strftime

'''global definitions'''
t_arr = []
a_arr = []
b_arr = []
c_arr = []
d_arr = []
e_arr = []
f_arr = []
gauge_label = []
main_arr = []
conflict_arr = [['1','2'],['3','4']]
gauge_ident = ['0']*6
conflict = False
'''functions'''
def raise_frame(frame):
    frame.tkraise()

root = Tk()
root.geometry('1200x720')
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)

def graphshow(chart, i, j):
    chart.grid(row=i, column=j, padx=10, pady=10)

def graphhide(chart):
    chart.grid_remove()

def exit():
    root.destroy()

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, columnspan=5, rowspan=5, sticky='news')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.title('Arduino Interfacing')

'''global variables'''
option_font = ('Verdana', 15, 'bold')
heading_font = ('Verdana', 25, 'bold')
channel_font = ('Verdana', 12, 'bold')
graphlabel_font = ('Verdana', 10, 'bold')




'''Home'''
attr = {'borderwidth':1, 'relief':"solid", 'padx':10, 'pady':20, 'width':20}

leftbar = Frame(f1, bg='grey')
leftbar.pack(side=LEFT, fill='y')

topbar = Frame(f1, bg="grey")
topbar.pack(side=TOP, fill='x')

heading_home = Label(topbar, text="Home", font=heading_font, bg='grey')
heading_home.pack(side=TOP)

option1 = Button(leftbar, text='Home', bg='grey', font=option_font, command=lambda:raise_frame(f1))
option1.pack(side=TOP, pady=10, fill="x")
option2 = Button(leftbar, text='Graph', bg='grey', font=option_font, command=lambda:raise_frame(f2))
option2.pack(side=TOP, pady=10, fill="x")
option3 = Button(leftbar, text='Live Graph', bg='grey', font=option_font, command=lambda:raise_frame(f3))
option3.pack(side=TOP, pady=10, fill="x")
option4 = Button(leftbar, text='Setpoints', bg='grey', font=option_font, command=lambda:raise_frame(f4))
option4.pack(side=TOP, pady=10, fill="x")
option5 = Button(leftbar, text='Exit', bg='grey', font=option_font, command=exit)
option5.pack(side=TOP, pady=10, fill="x")

'''var GUI'''
table_frame = Frame(f1)
table_frame.pack(side=LEFT, anchor='nw', pady=30, padx=30)

channel_heading = Label(table_frame, text="Channels", **attr, font=channel_font)
channel_heading.grid(row=0, column=0)
gauge_heading = Label(table_frame, text="Gauge Name", **attr, font=channel_font)
gauge_heading.grid(row=0, column=1)
reading_heading = Label(table_frame, text="Readings", **attr, font=channel_font)
reading_heading.grid(row=0, column=2)



channel1 = Label(table_frame, text="Channel 1", **attr, font=channel_font)
channel1.grid(row=1, column=0)
gauge1 = Label(table_frame, text="PKR251", **attr, font=channel_font)
gauge1.grid(row=1, column=1)
reading1 = Label(table_frame, text="Readings", **attr, font=channel_font)
reading1.grid(row=1, column=2)
select1 = Label(table_frame, text="Select the gauge:")
cbtn_1 = Button(table_frame)
cbtn1_1 = Button(table_frame)

channel2 = Label(table_frame, text="Channel 2", **attr, font=channel_font)
channel2.grid(row=2, column=0)
gauge2 = Label(table_frame, text="PKB134", **attr, font=channel_font)
gauge2.grid(row=2, column=1)
reading2 = Label(table_frame, text="Readings", **attr, font=channel_font)
reading2.grid(row=2, column=2)
select2 = Label(table_frame, text="Select the gauge:")
cbtn_2 = Button(table_frame)
cbtn1_2 = Button(table_frame)

channel3 = Label(table_frame, text="Channel 3", **attr, font=channel_font)
channel3.grid(row=3, column=0)
gauge3 = Label(table_frame, text="PKB134", **attr, font=channel_font)
gauge3.grid(row=3, column=1)
reading3 = Label(table_frame, text="Readings", **attr, font=channel_font)
reading3.grid(row=3, column=2)
select3 = Label(table_frame, text="Select the gauge:")
cbtn_3 = Button(table_frame)
cbtn1_3 = Button(table_frame)

channel4 = Label(table_frame, text="Channel 4", **attr, font=channel_font)
channel4.grid(row=4, column=0)
gauge4 = Label(table_frame, text="PKB134", **attr, font=channel_font)
gauge4.grid(row=4, column=1)
reading4 = Label(table_frame, text="Readings", **attr, font=channel_font)
reading4.grid(row=4, column=2)
select4 = Label(table_frame, text="Select the gauge:")
cbtn_4 = Button(table_frame)
cbtn1_4 = Button(table_frame)

channel5 = Label(table_frame, text="Channel 5", **attr, font=channel_font)
channel5.grid(row=5, column=0)
gauge5 = Label(table_frame, text="PKB134", **attr, font=channel_font)
gauge5.grid(row=5, column=1)
reading5 = Label(table_frame, text="Readings", **attr, font=channel_font)
reading5.grid(row=5, column=2)
select5 = Label(table_frame, text="Select the gauge:")
cbtn_5 = Button(table_frame)
cbtn1_5 = Button(table_frame)

channel6 = Label(table_frame, text="Channel 6", **attr, font=channel_font)
channel6.grid(row=6, column=0)
gauge6 = Label(table_frame, text="PKB134", **attr, font=channel_font)
gauge6.grid(row=6, column=1)
reading6 = Label(table_frame, text="Readings", **attr, font=channel_font)
reading6.grid(row=6, column=2)
select6 = Label(table_frame, text="Select the gauge:")
cbtn_6 = Button(table_frame)
cbtn1_6 = Button(table_frame)


def change():
    file = open('traildata.txt','r')
    data = file.read()
    dataarr = data.split('\n')
    for i in dataarr:
        if len(i)>1:
            t,a,b,c,d,e,f = i.split(',')
            t_arr.append(t)
            a_arr.append(a)
            b_arr.append(b)
            c_arr.append(c)
            d_arr.append(d)
            e_arr.append(e)
            f_arr.append(f)
    
    gauge_label = [gauge1, gauge2, gauge3, gauge4, gauge5, gauge6]
    main_arr = [a_arr, b_arr, c_arr, d_arr, e_arr, f_arr]
    select_label = [select1, select2, select3, select4, select5, select6]
    con_btn = [cbtn_1, cbtn_2, cbtn_3, cbtn_4, cbtn_5, cbtn_6]
    con_btn1 = [cbtn1_1, cbtn1_2, cbtn1_3, cbtn1_4, cbtn1_5, cbtn1_6]
    conf_num = [0]*6
    for j in range(0,6):
        label = Label(table_frame, text="Select the gauge:")
        select_label.append(label)
        cbtn = Button(table_frame)
        con_btn.append(cbtn)
        cbtn1 = Button(table_frame)
        con_btn1.append(cbtn1)
        
        
    for i in range(0, len(gauge_label)):
        
        gauge_label[i].config(text=main_arr[i][-2])
        if (float(main_arr[i][-2]) >= 1 and float(main_arr[i][-2]) <= 1.3):
            conf_num[i] = 1
        else:
            conf_num[i] = 0
        
        if(conf_num[i]):
            gauge_ident[i] = 'Select'
            # Select_label = Label(table_frame, text="Select the gauge:")
            # Select_label.grid(row=i+1, column=3)
            # con_btn = Button(table_frame, text=conflict_arr[0][0], command=lambda:grid_remove())
            # con_btn.grid(row=i+1, column=4)
            # con_btn1 = Button(table_frame, text=conflict_arr[0][1], command=lambda:grid_remove())
            # con_btn1.grid(row=i+1, column=5)
            select_label[i].grid(row=i+1, column=3)
            con_btn[i].config(text=conflict_arr[0][0])
            con_btn[i].grid(row=i+1, column=4)
            con_btn1[i].config(text=conflict_arr[0][1])
            con_btn1[i].grid(row=i+1, column=5)
    for i in range(0,6):
        if (conf_num[i]==0):
            print(i, conf_num)
            select_label[i].grid_remove()
            con_btn[i].grid_remove()
            con_btn1[i].grid_remove()
            
            
    file.close()
    root.after(1000, change)

raise_frame(f1)
# ani = animation.FuncAnimation(figure, animate, interval=1000)
change()
root.mainloop()

