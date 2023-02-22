# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 23:09:04 2023

@author: Pratham Rao
"""


from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy import random


def raise_frame(frame):
    frame.tkraise()

root = Tk()
root.geometry('1000x600')
f1 = Frame(root, bg="blue")
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, columnspan=5, rowspan=5, sticky='news')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.title('Arduino Interfacing')



'''Home'''
attr = {'borderwidth':1, 'relief':"solid", 'padx':10, 'width':20}

leftbar = Frame(f1, bg='grey')
leftbar.pack(side=LEFT, fill='y')

topbar = Frame(f1, bg="grey")
topbar.pack(side=TOP, fill='x')

heading_home = Label(topbar, text="Home", bg='grey')
heading_home.pack(side=TOP)

option1 = Button(leftbar, text='Home', bg='grey', command=lambda:raise_frame(f1))
option1.pack(side=TOP, pady=10, fill="x")
option2 = Button(leftbar, text='Graph', bg='grey', command=lambda:raise_frame(f2))
option2.pack(side=TOP, pady=10, fill="x")
option3 = Button(leftbar, text='Setpoints', bg='grey', command=lambda:raise_frame(f3))
option3.pack(side=TOP, pady=10, fill="x")
option4 = Button(leftbar, text='Exit', bg='grey', command=lambda:raise_frame(f4))
option4.pack(side=TOP, pady=10, fill="x")

'''var GUI'''
table_frame = Frame(f1)
table_frame.pack(side=LEFT, anchor='nw', pady=30, padx=30)

channel_heading = Label(table_frame, text="Channels", **attr, font='bold')
channel_heading.grid(row=0, column=0)
gauge_heading = Label(table_frame, text="Gauge Name", **attr, font='bold')
gauge_heading.grid(row=0, column=1)
reading_heading = Label(table_frame, text="Readings", **attr, font='bold')
reading_heading.grid(row=0, column=2)


channel1 = Label(table_frame, text="Channel 1", **attr, font='bold')
channel1.grid(row=1, column=0)
gauge1 = Label(table_frame, text="PKR251", **attr, font='bold')
gauge1.grid(row=1, column=1)
reading1 = Label(table_frame, text="Readings", **attr, font='bold')
reading1.grid(row=1, column=2)

channel2 = Label(table_frame, text="Channel 2", **attr, font='bold')
channel2.grid(row=2, column=0)
gauge2 = Label(table_frame, text="PKB134", **attr, font='bold')
gauge2.grid(row=2, column=1)
reading2 = Label(table_frame, text="Readings", **attr, font='bold')
reading2.grid(row=2, column=2)


'''Graph'''
Label(f2, text='FRAME 2').pack()
Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()



'''Setpoints'''
Label(f3, text='FRAME 3').pack(side='left')
Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')


Label(f4, text='FRAME 4').pack()
Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()

raise_frame(f1)
root.mainloop()
    


