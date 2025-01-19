#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# GUI.py
from tkinter import *
from tkinter import ttk
import time

def showKD(*args):
    Kingdom.set(kingdom.get())

def showGov(*args):
    Governor.set(governor.get())

def callback(*args):
    showKD()
    showGov()

number = 450

##### GUI #####

# window
mainWin = Tk()
mainWin.title('SKDAS')

# variables
kingdom = StringVar()
Governor = StringVar()
governor = StringVar()
Kingdom = StringVar()

# left frame
leftFrame = ttk.Frame(mainWin, borderwidth=20, relief='flat', width=200, height=150, padding='10 10 10 10')
leftFrame.grid_propagate(0)
leftFrame.grid(row=0, column=0)

# left content
label1 = ttk.Label(leftFrame, text='Select your Kingdom:')
label1.grid(column=0, row=0)
entry_KD = ttk.Entry(leftFrame, textvariable=kingdom, width=4)
entry_KD.grid(column=0, row=1)
entry_KD.focus()
label2 = ttk.Label(leftFrame, text='Governors to scan:')
label2.grid(column=0, row=2)
entry_Gov = ttk.Entry(leftFrame, textvariable=governor, width=4)
entry_Gov.grid(column=0, row=3)

button1 = ttk.Button(leftFrame, text='Scan', command=lambda: [showKD(), showGov()])
button1.grid(column=0, row=4)

# right frame
rightFrame = ttk.Frame(mainWin, borderwidth=50, relief='sunken', width=200, height=150, padding='10 10 10 10')
rightFrame.grid_propagate(0)
rightFrame.grid(row=0, column=1)

# right content
label3 = ttk.Label(rightFrame, text='Your Kingdom is:')
label3.grid(column=0, row=0)
label4 = ttk.Label(rightFrame, textvariable=Kingdom)
label4.grid(column=0, row=1)
label5 = ttk.Label(rightFrame, text='Governors to scan:')
label5.grid(column=0, row=2)
label6 = ttk.Label(rightFrame, textvariable=Governor)
label6.grid(column=0, row=3)


# progressbar
progress = ttk.Progressbar(mainWin, orient=HORIZONTAL, length=450, mode='determinate')
progress.grid(column=0, row=1, columnspan=2)


# using keyboard return
mainWin.bind('<Return>', callback)

mainWin.mainloop()