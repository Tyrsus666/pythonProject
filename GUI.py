#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# GUI.py
from tkinter import *
from tkinter import ttk
import configparser
import time


def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    kingdom = config.get('General','kingdom')
    governor = config.get('General','scans')

    config_values = {'kingdom': kingdom, 'governor': governor}
    return config_values

def update_config(*args):
    config = configparser.ConfigParser()
    config.set('General', 'kingdom', kingdom.get())
    config.set('General', 'scans', governor.get())
    with open('config.ini', 'w') as config_file:
        config.write(config_file)

if __name__ == "__main__":
    config_data = read_config()

def showKD(*args):
    Kingdom.set(kingdom.get())

def showGov(*args):
    Governor.set(governor.get())

def callback(*args):
    showKD()
    showGov()


##### GUI #####

# window
mainWin = Tk()
mainWin.title('SKDAS')
mainWin.geometry('500x200')

# variables
kingdom = StringVar()
kingdom.set(config_data['kingdom']) # devault kingdom
Governor = StringVar()
governor = StringVar()
governor.set(config_data['governor']) # devault value
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

button1 = ttk.Button(leftFrame, text='Scan', command=lambda: [showKD(), showGov(), update_config()])
button1.grid(column=0, row=4)

# right frame
rightFrame = ttk.Frame(mainWin, borderwidth=5, relief='sunken', width=300, height=150)
rightFrame.grid_propagate(0)
rightFrame.grid(row=0, column=1)

# right content
label3 = ttk.Label(rightFrame, text='Name:')
label3.grid(column=0, row=0, sticky=W, ipadx=5)
label4 = ttk.Label(rightFrame, textvariable=Kingdom)
label4.grid(column=1, row=0)
label5 = ttk.Label(rightFrame, text='ID:')
label5.grid(column=0, row=1, sticky=W)
label6 = ttk.Label(rightFrame, textvariable=Governor)
label6.grid(column=1, row=1)


# progressbar
progress = ttk.Progressbar(mainWin, orient=HORIZONTAL, length=450, mode='determinate')
progress.grid(column=0, row=1, columnspan=2, pady=10)


# using keyboard return
mainWin.bind('<Return>', callback)

mainWin.mainloop()