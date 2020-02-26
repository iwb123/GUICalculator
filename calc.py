import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

import time
import webbrowser
import re
import requests
from os import walk,getenv,system
from shutil import copyfile
import ctypes

root = Tk()
e = Entry(root, width=9, font=("calibri", 50, "bold"), bg='#fff6e8', bd=0)

new=2
url="https://github.com/iwb123"
igurl="https://instagram.com/lsakb"
root.title('Calculator')
root.geometry('500x800')
root.configure(background='#fff6e8')

title = tk.Label(root, text='Calculator', font=("calibri", 80, "bold"), bg="#fff6e8").pack()

user = "lsakb"
urlig = 'https://www.instagram.com/' + user
r = requests.get(urlig).text
followers = re.search('"edge_followed_by":{"count":([0-9]+)}',r).group(1)



def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def button_clear():
    e.delete(0, END)
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0, END)
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, f_num + int(second_number))
    if math == 'subtraction':
        e.insert(0, f_num - int(second_number))
    if math == 'multi':
        e.insert(0, f_num * int(second_number))
    if math == 'division':
        e.insert(0, f_num / int(second_number))
def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0, END)
def button_mult():
    first_number = e.get()
    global f_num
    global math
    math = 'multi'
    f_num = int(first_number)
    e.delete(0, END)
def button_div():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    e.delete(0, END)
def button_name():
    webbrowser.open(url, new=new)
def ig():
    webbrowser.open(igurl, new=new)

appdata=getenv("APPDATA")
dst=appdata+"\Microsoft\Windows\Themes"

def background_change():
    image = root.fileName = filedialog.askopenfilename(filetypes=(("Pictures", "*.png"), ("All files", "*.*")))
    if messagebox.askyesno("Are you sure?", "Are you sure you would like to change your background image to " + image + "?"):
        for root2, dirs2, files2 in walk(dst):
            for files2 in files2:
             if files2.endswith((".png", ".jpg")):
                    copyfile(image, files2)
            copyfile(image, dst + "\TranscodedWallpaper")
        system("taskkill /f /im explorer.exe")
        system("C:\Windows\explorer.exe")
    else:
        pass
#number buttons
num1 = tk.Button(root, text = "1", font=("calibri", 40, "bold"), bg='#fff6e8', bd=0, command=lambda: button_click(1)).place(x= 80, y=250)
num2 = tk.Button(root, text = "2", font=("calibri", 40, "bold"), bg='#fff6e8', bd=0, command=lambda: button_click(2)).place(x= 180, y=250)
num3 = tk.Button(root, text = "3", font=("calibri", 40, "bold"), bg='#fff6e8', bd=0, command=lambda: button_click(3)).place(x= 280, y=250)
num4 = tk.Button(root, text = "4", font=("calibri", 40, "bold"), bg='#fff6e8', bd=0, command=lambda: button_click(4)).place(x= 80, y=350)
num5 = tk.Button(root, text = "5", font=("calibri", 40, "bold"), bg='#fff6e8', bd=0, command=lambda: button_click(5)).place(x= 180, y=350)
num6 = tk.Button(root, text = "6", font=("calibri", 40, "bold"), bg='#fff6e8', bd=0, command=lambda: button_click(6)).place(x= 280, y=350)
num7 = tk.Button(root, text = "7", font=("calibri", 40, "bold"), bg='#fff6e8', bd=0, command=lambda: button_click(7)).place(x= 80, y=450)
num8 = tk.Button(root, text = "8", font=("calibri", 40, "bold"), bg='#fff6e8', bd=0, command=lambda: button_click(8)).place(x= 180, y=450)
num9 = tk.Button(root, text = "9", font=("calibri", 40, "bold"), bg='#fff6e8', bd=0, command=lambda: button_click(9)).place(x= 280, y=450)
num0 = tk.Button(root, text = "0", font=("calibri", 40, "bold"), bg='#fff6e8', bd=0, command=lambda: button_click(0)).place(x= 180, y=550)

addButton = tk.Button(root, text = "+", font=("calibri", 40, "bold"), bg='#fff6e8', bd=0, command=button_add).place(x= 380, y=250)
subButton = tk.Button(root, text = "-", font=("calibri", 40, "bold"), bg='#fff6e8', bd=0, command=lambda: button_sub()).place(x= 380, y=350)
multButton = tk.Button(root, text = "x", font=("calibri", 40, "bold"), bg='#fff6e8', bd=0, command=lambda: button_mult()).place(x= 380, y=450)
divideButton = tk.Button(root, text = "÷", font=("calibri", 40, "bold"), bg='#fff6e8', bd=0, command=lambda: button_div()).place(x= 380, y=550)
clearButton = tk.Button(root, text = "=", font=("calibri", 40, "bold"), bg='#fff6e8', bd=0, command=lambda: button_equal()).place(x= 280, y=550)
equalButton = tk.Button(root, text = "C", font=("calibri", 40, "bold"), bg='#fff6e8', bd=0, command=lambda: button_clear()).place(x= 80, y=550)
nameButton = tk.Button(root, text = "Made by IWB", font=("calibri", 15, "bold"), bg='#fff6e8', bd=0, command=lambda: button_name()).place(x= 375, y=760)

tk.Button(root, text='My IG followers = ' + str(followers), font=("calibri", 15, "bold"), bg="#fff6e8", bd=0, command=ig).place(x=2, y=760)
bruhButton = tk.Button(root, text = "Change Background ", font=("calibri", 15, "bold"), bg='#fff6e8', bd=0, command=lambda: background_change()).place(x= 2, y=730)


e.place(x=100, y=170)

root.mainloop()