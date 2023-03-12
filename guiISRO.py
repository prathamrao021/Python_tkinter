# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 23:09:04 2023

@author: Pratham Rao
"""


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

channel2 = Label(table_frame, text="Channel 2", **attr, font=channel_font)
channel2.grid(row=2, column=0)
gauge2 = Label(table_frame, text="PKB134", **attr, font=channel_font)
gauge2.grid(row=2, column=1)
reading2 = Label(table_frame, text="Readings", **attr, font=channel_font)
reading2.grid(row=2, column=2)

channel3 = Label(table_frame, text="Channel 3", **attr, font=channel_font)
channel3.grid(row=3, column=0)
gauge3 = Label(table_frame, text="PKB134", **attr, font=channel_font)
gauge3.grid(row=3, column=1)
reading3 = Label(table_frame, text="Readings", **attr, font=channel_font)
reading3.grid(row=3, column=2)

channel4 = Label(table_frame, text="Channel 4", **attr, font=channel_font)
channel4.grid(row=4, column=0)
gauge4 = Label(table_frame, text="PKB134", **attr, font=channel_font)
gauge4.grid(row=4, column=1)
reading4 = Label(table_frame, text="Readings", **attr, font=channel_font)
reading4.grid(row=4, column=2)

channel5 = Label(table_frame, text="Channel 5", **attr, font=channel_font)
channel5.grid(row=5, column=0)
gauge5 = Label(table_frame, text="PKB134", **attr, font=channel_font)
gauge5.grid(row=5, column=1)
reading5 = Label(table_frame, text="Readings", **attr, font=channel_font)
reading5.grid(row=5, column=2)

channel6 = Label(table_frame, text="Channel 6", **attr, font=channel_font)
channel6.grid(row=6, column=0)
gauge6 = Label(table_frame, text="PKB134", **attr, font=channel_font)
gauge6.grid(row=6, column=1)
reading6 = Label(table_frame, text="Readings", **attr, font=channel_font)
reading6.grid(row=6, column=2)



'''Graph'''
attr = {'borderwidth':1, 'relief':"solid", 'padx':10, 'pady':20, 'width':20}

leftbar = Frame(f2, bg='grey')
leftbar.pack(side=LEFT, fill='y')

topbar = Frame(f2, bg="grey")
topbar.pack(side=TOP, fill='x')

heading_home = Label(topbar, text="Graph", font=heading_font, bg='grey')
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
graphanalysisframe = Frame(f2)
graphanalysisframe.pack(fill=BOTH, expand=1)

contentframe = Frame(graphanalysisframe)
contentframe.pack(side=TOP, anchor='nw', pady=30, padx=30)

stdate = StringVar()
endate = StringVar()
sttime = StringVar()
entime = StringVar()

startdate_label = Label(contentframe, text='Starting Date', font=graphlabel_font)
startdate_label.grid(row=0, column=0)
startdate = Entry(contentframe, textvariable = stdate, width=30)
startdate.grid(row=0, column=1)

enddate_label = Label(contentframe, text='Ending Date', font=graphlabel_font)
enddate_label.grid(row=1, column=0)
enddate = Entry(contentframe, textvariable = endate, width=30)
enddate.grid(row=1, column=1)

starttime_label = Label(contentframe, text='Starting Time', font=graphlabel_font)
starttime_label.grid(row=0, column=2, padx=(20,15))
starttime = Entry(contentframe, textvariable = sttime, width=30)
starttime.grid(row=0, column=3)

endtime_label = Label(contentframe, text='Ending Time', font=graphlabel_font)
endtime_label.grid(row=1, column=2, padx=(20,15))
endtime = Entry(contentframe, textvariable = entime, width=30)
endtime.grid(row=1, column=3)

channel1_btn = Button(contentframe, text="Channel1 Graph", font=graphlabel_font, command=lambda:graphshow(chart1,0,0))
channel1_btn.grid(row=2, column=0, pady=20)

channel2_btn = Button(contentframe, text="Channel2 Graph", font=graphlabel_font, command=lambda:graphshow(chart2,0,1))
channel2_btn.grid(row=2, column=1, pady=20)

channel3_btn = Button(contentframe, text="Channel3 Graph", font=graphlabel_font, command=lambda:graphshow(chart3,0,2))
channel3_btn.grid(row=2, column=2, pady=20)

channel4_btn = Button(contentframe, text="Channel4 Graph", font=graphlabel_font, command=lambda:graphshow(chart4,0,3))
channel4_btn.grid(row=2, column=3, pady=20)

channel5_btn = Button(contentframe, text="Channel5 Graph", font=graphlabel_font, command=lambda:graphshow(chart5,0,4))
channel5_btn.grid(row=2, column=4, pady=20)

channel6_btn = Button(contentframe, text="Channel6 Graph", font=graphlabel_font, command=lambda:graphshow(chart6,0,5))
channel6_btn.grid(row=2, column=5, pady=20, padx=30)


channel1_delete = Button(contentframe, text="Channel1 Hide", font=graphlabel_font, command=lambda:graphhide(chart1))
channel1_delete.grid(row=3, column=0, pady=(0,20))

channel2_delete = Button(contentframe, text="Channel2 Hide", font=graphlabel_font, command=lambda:graphhide(chart2))
channel2_delete.grid(row=3, column=1, pady=(0,20))

channel3_delete = Button(contentframe, text="Channel3 Hide", font=graphlabel_font, command=lambda:graphhide(chart3))
channel3_delete.grid(row=3, column=2, pady=(0,20))

channel4_delete = Button(contentframe, text="Channel4 Hide", font=graphlabel_font, command=lambda:graphhide(chart4))
channel4_delete.grid(row=3, column=3, pady=(0,20))

channel5_delete = Button(contentframe, text="Channel5 Hide", font=graphlabel_font, command=lambda:graphhide(chart5))
channel5_delete.grid(row=3, column=4, pady=(0,20))

channel6_delete = Button(contentframe, text="Channel6 Hide", font=graphlabel_font, command=lambda:graphhide(chart6))
channel6_delete.grid(row=3, column=5, pady=(0,20))

separate = ttk.Separator(contentframe, orient=HORIZONTAL, takefocus= 1)
separate.grid(row=4, column=0, columnspan=6, ipadx=500)

liv_graphlab = Label(contentframe, text="Graph", font=channel_font)
liv_graphlab.grid(row=5, column=0)

'''Frame for Graph'''

my_canvas = Canvas(contentframe, height=400, borderwidth=0, relief='flat')
#my_canvas.pack(side=TOP, fill=BOTH, expand=1)
my_canvas.grid(row=6, columnspan=6, sticky='news')

# scrollbar
my_scrollbar = Scrollbar(contentframe, orient=HORIZONTAL, command=my_canvas.xview)
#my_scrollbar.pack(side=TOP, fill=X)
my_scrollbar.grid(row=7, columnspan=6, sticky='news')

# configure the canvas
my_canvas.configure(xscrollcommand=my_scrollbar.set)
my_canvas.bind(
    '<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"))
)

second_frame = Frame(my_canvas, width = 2750)

figure = plt.Figure(figsize=(6,5))
ax = figure.add_subplot(111)
y1 = [i**2 for i in range(101)]
y2 = [i**3 for i in range(101)]
ax.plot(y1, label="Channel1")
ax.plot(y2)
leg = ax.legend()
ax.set_title('Channel1')
chart_type1 = FigureCanvasTkAgg(figure, second_frame)
chart1 = chart_type1.get_tk_widget()

figure = plt.Figure(figsize=(6,5))
ax = figure.add_subplot(111)
y = [i**2 for i in range(101)]
ax.plot(y)
ax.set_title('Channel2')
chart_type2 = FigureCanvasTkAgg(figure, second_frame)
chart2 = chart_type2.get_tk_widget()

figure = plt.Figure(figsize=(6,5))
ax = figure.add_subplot(111)
y = [((i*3)+4)*2 for i in range(101)]
ax.plot(y)
ax.set_title('Channel3')
chart_type3 = FigureCanvasTkAgg(figure, second_frame)
chart3 = chart_type3.get_tk_widget()

figure = plt.Figure(figsize=(6,5))
ax = figure.add_subplot(111)
y = [math.cos(x) for x in range(180)]
ax.plot(y)
ax.set_title('Channel4')
chart_type4 = FigureCanvasTkAgg(figure, second_frame)
chart4 = chart_type4.get_tk_widget()

figure = plt.Figure(figsize=(6,5))
ax = figure.add_subplot(111)
y = [math.tan(x) for x in range(180)]
ax.plot(y)
ax.set_title('Channel5')
chart_type5 = FigureCanvasTkAgg(figure, second_frame)
chart5 = chart_type5.get_tk_widget()

figure = plt.Figure(figsize=(6,5))
ax = figure.add_subplot(111)
y = [math.sin(x) for x in range(180)]
ax.plot(y)
ax.set_title('Channel6')
chart_type6 = FigureCanvasTkAgg(figure, second_frame)
chart6 = chart_type6.get_tk_widget()

my_canvas.create_window((0, 0), window=second_frame, anchor="nw")



'''LIVE Graph'''
attr = {'borderwidth':1, 'relief':"solid", 'padx':10, 'pady':20, 'width':20}

leftbar = Frame(f3, bg='grey')
leftbar.pack(side=LEFT, fill='y')

topbar = Frame(f3, bg="grey")
topbar.pack(side=TOP, fill='x')

heading_home = Label(topbar, text="Graph", font=heading_font, bg='grey')
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

'''figure = plt.Figure(figsize=(6,5))
ax = figure.add_subplot(111)

arra1 = ['11','32','21','15','14','24','20','19','6','13']
f1 = open('testdata.txt', 'w')
for i in range(101):
    j=i
    j = i%10
    f1.write(strftime("%S")+arra1[j])'''
 
# def animate():
#     data = open('testdata.txt','r').read()
#     dataarr = data.split('\n')
#     xarr=[]
#     yarr=[]
#     for i in dataarr:
#         if len(i)>1:
#             x,y = i.split(',')
#             xarr.append(int(x))
#             yarr.append(int(y))
#     ax.clear()
#     ax.plot(xarr,yarr, label="random")
#     leg = ax.legend()
# canvas = FigureCanvasTkAgg(figure, f3)
# #canvas.show()
# canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# fig, ax = plt.subplots(2, 2, figsize=(15, 8), dpi=200)
    

figure = plt.Figure(figsize=(12,10), dpi=100)
ax = figure.add_subplot(111)
def animate(i):
    data = open('traildata.txt','r').read()
    dataarr = data.split('\n')
    # xarr=[]
    # yarr=[]
    t_arr=[]
    a_arr=[] 
    b_arr=[]
    c_arr=[] 
    d_arr=[] 
    e_arr=[] 
    f_arr=[]
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
    # ax.clear()
    ax.clear()
    values_arr = [a_arr, b_arr, c_arr, d_arr, e_arr, f_arr]
    channel_arr = ['Ch1','Ch2','Ch3','Ch4','Ch5','Ch6']
    for i in range(0,6):
        ax.scatter(t_arr, values_arr[0], label=channel_arr[i])
    plt.setp(ax.get_xticklabels(), rotation=90, horizontalalignment='right')
    
    # plt.yticks(np.arange(y.min(), y.max(), 0.005))
    plt.show()
    # fig.autofmt_xdate()
    leg = ax.legend()
canvas = FigureCanvasTkAgg(figure, f3)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

'''Setpoints'''
Label(f4, text='FRAME 3').pack(side='left')
Button(f4, text='Go to frame 4', command=lambda:raise_frame(f1)).pack(side='left')


raise_frame(f1)
ani = animation.FuncAnimation(figure, animate, interval=1000)
root.mainloop()

