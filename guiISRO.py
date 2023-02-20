# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 23:09:04 2023

@author: Pratham Rao
"""


from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd

'''tkinter'''
parent = Tk()

parent.geometry('600x600+50+50')
parent.resizable("true","true")
''''parent.iconbitmap("path to icon")'''



redbtn = Button(parent, text="Red").grid(column=0, row=0)
bluebtn = Button(parent, text="Blue", fg="blue").grid(column=1,row=0)
label1 = Label(parent, text="Hello World").grid(column=0, row=2)
'''command parameter is used to call function'''



'''Graph in tkinter'''
data1 = {'country':['A','B','C','D'], 'gdp_per_capita': [45000,78000,98000,56000]}

df1 = pd.DataFrame(data1)

figure1 = plt.Figure(figsize=(5, 4), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, parent)
bar1.get_tk_widget().grid(column=0, row=1)
df1 = df1[['country', 'gdp_per_capita']].groupby('country').sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Country Vs. GDP Per Capita')


parent.mainloop()


