#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# GUI.py
from tkinter import *
from tkinter import ttk
import configparser
import requests
import json
import time
import webbrowser


def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    kingdom = config.get('General', 'kingdom')
    governor = config.get('General', 'scans')

    config_values = {'kingdom': kingdom, 'governor': governor}
    return config_values

def update_config(*args):
    config = configparser.ConfigParser()
    config.add_section('General')
    config.set('General', 'kingdom', kingdom.get())
    config.set('General', 'scans', governor.get())
    with open('config.ini', 'w') as config_file:
        config.write(config_file)

def version_check(repo_owner , repo_name, local_version):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest'
    response = requests.get(url)
    response.raise_for_status()
    release_data = response.json()
    github_version = release_data['name']
    if local_version != github_version:
        button3 = ttk.Button(leftFrame, text='Update available.', command=lambda: webbrowser.open("https://github.com/Tyrsus666/pythonProject"))
        button3.grid(column=0, row=5, columnspan=2, pady=5)



repo_owner = 'Tyrsus666'
repo_name = 'pythonProject'
local_version = 'Version 1.1'


if __name__ == "__main__":
    config_data = read_config()

def showKD(*args):
    Kingdom.set(kingdom.get())

def showGov(*args):
    Governor.set(governor.get())

def callback(*args):
    showKD()
    showGov()
    update_config()


##### GUI #####

# window
mainWin = Tk()
mainWin.title('SKDAS')
mainWin.geometry('500x250')

# variables
kingdom = StringVar()
kingdom.set(config_data['kingdom'])  # default kingdom
Governor = StringVar()
governor = StringVar()
governor.set(config_data['governor'])  # default value
Kingdom = StringVar()

# left frame
leftFrame = ttk.Frame(mainWin, borderwidth=20, relief='flat', width=200, height=200, padding='10 10 10 10')
leftFrame.grid_propagate(0)
leftFrame.grid(row=0, column=0)

# left content
label1 = ttk.Label(leftFrame, text='Select your Kingdom:')
label1.grid(column=0, row=0, columnspan=2)
entry_KD = ttk.Entry(leftFrame, textvariable=kingdom, width=4)
entry_KD.grid(column=0, row=1, columnspan=2)
entry_KD.focus()
label2 = ttk.Label(leftFrame, text='Governors to scan:')
label2.grid(column=0, row=2, columnspan=2)
entry_Gov = ttk.Entry(leftFrame, textvariable=governor, width=4)
entry_Gov.grid(column=0, row=3, columnspan=2)

button1 = ttk.Button(leftFrame, text='Scan', command=lambda: [callback()])
button1.grid(column=0, row=4, pady=5)
button2 = ttk.Button(leftFrame, text='Cancel', command=lambda: [mainWin.destroy()])
button2.grid(column=1, row=4, pady=5)

# right frame
rightFrame = ttk.Frame(mainWin, borderwidth=5, relief='sunken', width=300, height=200)
rightFrame.grid_propagate(0)
rightFrame.grid(row=0, column=1)

# right content
label3 = ttk.Label(rightFrame, text='Rank:')
label3.grid(column=0, row=0, sticky=W, ipadx=5)
#label4 = ttk.Label(rightFrame, textvariable=i+1)
#label4.grid(column=1, row=0, sticky=W)
label5 = ttk.Label(rightFrame, text='Name:')
label5.grid(column=0, row=1, sticky=W)
#label6 = ttk.Label(rightFrame, textvariable=gov_name)
#label6.grid(column=1, row=1, sticky=W)
label7 = ttk.Label(rightFrame, text='ID:')
label7.grid(column=0, row=2, sticky=W)
#label8 = ttk.Label(rightFrame, textvariable=tointcheck(gov_id))
#label8.grid(column=1, row=2, sticky=W)
label9 = ttk.Label(rightFrame, text='Power:')
label9.grid(column=0, row=3, sticky=W)
#label10 = ttk.Label(rightFrame, textvariable=tointcheck(gov_power))
#label10.grid(column=1, row=3, sticky=W)
label11 = ttk.Label(rightFrame, text='Kill Points:')
label11.grid(column=0, row=4, sticky=W)
#label12 = ttk.Label(rightFrame, textvariable=tointcheck(gov_killpoints))
#label12.grid(column=1, row=4, sticky=W)
label13 = ttk.Label(rightFrame, text='Deads:')
label13.grid(column=0, row=5, sticky=W)
#label14 = ttk.Label(rightFrame, textvariable=tointcheck(gov_dead))
#label14.grid(column=1, row=5, sticky=W)
label15 = ttk.Label(rightFrame, text='T4 Kills:')
label15.grid(column=0, row=6, sticky=W)
#label16 = ttk.Label(rightFrame, textvariable=tointcheck(gov_kills_tier4))
#label16.grid(column=1, row=6, sticky=W)
label17 = ttk.Label(rightFrame, text='T5 Kills:')
label17.grid(column=0, row=7, sticky=W)
#label18 = ttk.Label(rightFrame, textvariable=tointcheck(gov_kills_tier5))
#label18.grid(column=1, row=7, sticky=W)
label19 = ttk.Label(rightFrame, text='Rss Assistance:')
label19.grid(column=0, row=8, sticky=W)
#label20 = ttk.Label(rightFrame, textvariable=tointcheck(gov_rss_assistance))
#label20.grid(column=1, row=8, sticky=W)
label21 = ttk.Label(rightFrame, text='Helptimes:')
label21.grid(column=0, row=9, sticky=W)
#label22 = ttk.Label(rightFrame, textvariable=tointcheck(gov_helptimes))
#label22.grid(column=1, row=9, sticky=W)


# progressbar
progress = ttk.Progressbar(mainWin, orient=HORIZONTAL, length=450, mode='determinate')
progress.grid(column=0, row=1, columnspan=2, pady=10)

result = version_check(repo_owner, repo_name, local_version)

# using keyboard return
mainWin.bind('<Return>', callback)

mainWin.mainloop()