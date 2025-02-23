#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# GUI.py
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import configparser
import requests
import json
import time
import webbrowser
import os
import sys
import traceback
from datetime import date
from ppadb.client import Client
import cv2
import numpy as np
from PIL import Image
import pytesseract
import xlwt
import keyboard
import random
import subprocess


##### functions #####
def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    kingdom = config.get('General', 'kingdom')
    search_range = config.get('General', 'search_range')
    port = config.get('General', 'port')
    config_values = {'kingdom': kingdom, 'search_range': search_range, 'port': port}
    return config_values


# variables
repo_owner = 'Tyrsus666'
repo_name = 'pythonProject'
local_version = 'Version 1.1'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
today = date.today()
Y = [285, 390, 490, 590, 605]  # Positions for governors
kingdom = '1'
search_range = '1'
port = '1'
connection = '1'
adb = '1'
device = '1'



def update_config(*args):
    config = configparser.ConfigParser()
    config.add_section('General')
    config.set('General', 'kingdom', kingdom.get())
    config.set('General', 'search_range', search_range.get())
    config.set('General', 'port', port.get())
    with open('config.ini', 'w') as config_file:
        config.write(config_file)


# def version_check(repo_owner, repo_name, local_version):
#     url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest'
#     response = requests.get(url)
#     response.raise_for_status()
#     release_data = response.json()
#     github_version = release_data['name']
    # if local_version != github_version:
    #     button3 = ttk.Button(leftFrame, text='Update available',
    #                          command=lambda: webbrowser.open("https://github.com/Tyrsus666/pythonProject"))
    #     button3.grid(column=0, row=5, columnspan=2, pady=5)
        # bo = tkinter.Tk()
        # bo.withdraw()
        # messagebox.showinfo('Tool is outdated', 'New Version can be found on Github.')
        # bo.destroy()

def tointcheck(element):
    try:
        return int(element)
    except ValueError:
        return element


def tointprint(element):
    try:
        return f'{int(element):,}'
    except ValueError:
        return str(element)


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def adb_connect():
    port.set(config_data['port'])
    global connection
    connection = 'localhost:' + str(port.get())
    subprocess.call(['./platform-tools/adb.exe', 'start-server'])
    subprocess.call(['./platform-tools/adb.exe', 'connect', connection])
    global adb
    adb = Client(host='localhost', port=5037)
    global device
    device = adb.device(connection)


def callback(*args):
    update_config()


##### GUI #####
def gui():
    # window
    mainWin = Tk()
    mainWin.title('SKDAS')
    mainWin.geometry('500x250')

    # variables
    global port
    global kingdom
    global search_range
    port = StringVar()
    port.set(config_data['port'])
    kingdom = StringVar()
    kingdom.set(config_data['kingdom'])  # default kingdom
    search_range = StringVar()
    search_range.set(config_data['search_range'])  # default value

    # left frame
    leftFrame = ttk.Frame(mainWin, borderwidth=20, relief='flat', width=200, height=200, padding='10 10 10 10')
    leftFrame.grid_propagate(0)
    leftFrame.grid(row=0, column=0)

    # left content
    label0 = ttk.Label(leftFrame, text='Port:')
    label0.grid(column=0, row=0, pady=5)
    entry_port = ttk.Entry(leftFrame, textvariable=port, width=4)
    entry_port.grid(column=1, row=0, pady=5, sticky=W)
    label1 = ttk.Label(leftFrame, text='Kingdom:')
    label1.grid(column=0, row=1, pady=5)
    entry_KD = ttk.Entry(leftFrame, textvariable=kingdom, width=4)
    entry_KD.grid(column=1, row=1, pady=5, sticky=W)
    entry_KD.focus_set()
    label2 = ttk.Label(leftFrame, text='Search range:')
    label2.grid(column=0, row=2, pady=5)
    entry_Gov = ttk.Entry(leftFrame, textvariable=search_range, width=4)
    entry_Gov.grid(column=1, row=2, pady=5, sticky=W)

    button1 = ttk.Button(leftFrame, text='Scan', command=lambda: [callback()])
    button1.grid(column=0, row=6, pady=5)
    button2 = ttk.Button(leftFrame, text='Cancel', command=lambda: [mainWin.destroy()])
    button2.grid(column=1, row=6, pady=5)

    # version check
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest'
    response = requests.get(url)
    response.raise_for_status()
    release_data = response.json()
    github_version = release_data['name']
    if local_version != github_version:  # if version is outdated show button
        button3 = ttk.Button(leftFrame, text='Update available',
                             command=lambda: webbrowser.open("https://github.com/Tyrsus666/pythonProject"))
        button3.grid(column=0, row=7, columnspan=2, pady=5)

    # right frame
    rightFrame = ttk.Frame(mainWin, borderwidth=5, relief='sunken', width=300, height=200)
    rightFrame.grid_propagate(0)
    rightFrame.grid(row=0, column=1)

    # right content
    label3 = ttk.Label(rightFrame, text='Rank:')
    label3.grid(column=0, row=0, sticky=W, ipadx=5)
    # label4 = ttk.Label(rightFrame, textvariable=i + 1)
    # label4.grid(column=1, row=0, sticky=W)
    label5 = ttk.Label(rightFrame, text='Name:')
    label5.grid(column=0, row=1, sticky=W)
    # label6 = ttk.Label(rightFrame, textvariable=gov_name)
    # label6.grid(column=1, row=1, sticky=W)
    label7 = ttk.Label(rightFrame, text='ID:')
    label7.grid(column=0, row=2, sticky=W)
    # label8 = ttk.Label(rightFrame, textvariable=tointcheck(gov_id))
    # label8.grid(column=1, row=2, sticky=W)
    label9 = ttk.Label(rightFrame, text='Power:')
    label9.grid(column=0, row=3, sticky=W)
    # label10 = ttk.Label(rightFrame, textvariable=tointcheck(gov_power))
    # label10.grid(column=1, row=3, sticky=W)
    label11 = ttk.Label(rightFrame, text='Kill Points:')
    label11.grid(column=0, row=4, sticky=W)
    # label12 = ttk.Label(rightFrame, textvariable=tointcheck(gov_killpoints))
    # label12.grid(column=1, row=4, sticky=W)
    label13 = ttk.Label(rightFrame, text='Deads:')
    label13.grid(column=0, row=5, sticky=W)
    # label14 = ttk.Label(rightFrame, textvariable=tointcheck(gov_dead))
    # label14.grid(column=1, row=5, sticky=W)
    label15 = ttk.Label(rightFrame, text='T4 Kills:')
    label15.grid(column=0, row=6, sticky=W)
    # label16 = ttk.Label(rightFrame, textvariable=tointcheck(gov_kills_tier4))
    # label16.grid(column=1, row=6, sticky=W)
    label17 = ttk.Label(rightFrame, text='T5 Kills:')
    label17.grid(column=0, row=7, sticky=W)
    # label18 = ttk.Label(rightFrame, textvariable=tointcheck(gov_kills_tier5))
    # label18.grid(column=1, row=7, sticky=W)
    label19 = ttk.Label(rightFrame, text='Rss Assistance:')
    label19.grid(column=0, row=8, sticky=W)
    # label20 = ttk.Label(rightFrame, textvariable=tointcheck(gov_rss_assistance))
    # label20.grid(column=1, row=8, sticky=W)
    label21 = ttk.Label(rightFrame, text='Helptimes:')
    label21.grid(column=0, row=9, sticky=W)
    # label22 = ttk.Label(rightFrame, textvariable=tointcheck(gov_helptimes))
    # label22.grid(column=1, row=9, sticky=W)

    # progressbar
    progress = ttk.Progressbar(mainWin, orient=HORIZONTAL, length=450, mode='determinate')
    progress.grid(column=0, row=1, columnspan=2, pady=10)

    # using keyboard return
    mainWin.bind('<Return>', callback)

    mainWin.mainloop()

def setup_excel():
    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet(str(today))
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.bold = True
    style.font = font

    headers = ['Date', 'Kingdom', 'Rank', 'Governor Name', 'Governor ID', 'Power', 'Kill Points', 'Deads', 'Tier 1 Kills', 'Tier 2 Kills', 'Tier 3 Kills', 'Tier 4 Kills', 'Tier 5 Kills', 'Rss Assistance', 'Alliance Helps', 'Alliance','KvK Kills High', 'KvK Deads High', 'KvK Severely Wounds High']
    for col, header in enumerate(headers):
        sheet1.write(0, col, header, style)
    return wb, sheet1

def capture_image(device, filename):
    image = device.screencap()
    with open(filename, 'wb') as f:
        f.write(image)
    return

def random_time(max_pause: float):
    min_pause = max_pause * 2 / 3
    sleep_time = random.uniform(min_pause, max_pause)
    time.sleep(sleep_time)


def preprocess_image(filename, roi):
    img = cv2.imread(filename)

    # Crop the image based on ROI
    x, y, w, h = roi
    cropped_image = img[y:y + h, x:x + w]

    # Convert to grayscale
    gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

    # Improved preprocessing for better OCR accuracy
    _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return binary_image


def preprocess_image2(filename, roi):
    img = cv2.imread(filename)

    # Crop the image based on ROI
    x, y, w, h = roi
    cropped_image = img[y:y + h, x:x + w]

    # Convert to grayscale
    gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

    # Improved preprocessing for better OCR accuracy
    _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    return binary_image


def preprocess_image3(filename, roi):
    img = cv2.imread(filename)

    # Crop the image based on ROI
    x, y, w, h = roi
    cropped_image = img[y:y + h, x:x + w]

    # Convert to grayscale
    gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

    gray_image = cv2.medianBlur(gray_image, 3)
    _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    return binary_image

def read_ocr_from_image(image, config=""):
    return pytesseract.image_to_string(image, config=config)

if __name__ == "__main__":
    config_data = read_config()
    gui()