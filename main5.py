from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

window = Tk()
window.geometry("800x600")
window.title("LifeChoices Online")
window.resizable("false", "false")
window.config(bg="#dea5e6")

# Dictionary of colours:
color = {"purple": "#5a1c61", "lightpurple": "#8c1c99", "darkpurple": "#390340", "lilac": "#dea5e6"}

# Top frame
top_frame = Frame(window, bg=color["purple"])
top_frame.pack(side="top", fill=X)

# header
home2_label = Label(top_frame, text="LifeChoices Online - Admin", font="Arial 15", bg=color["purple"], fg="white",
                    height=2,
                    padx=20)
home2_label.pack(side="left")

home_label = Label(top_frame, text="LC", font="Arial 15", bg=color["purple"], fg="white", height=2, padx=20)
home_label.pack(side="right")

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='LifeChoicesOnline', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
xy = mycursor.execute('Select * from Login')

window = ttk.Treeview(window)

# Defining columns
window['columns'] = ('username', 'user_id', 'IDnumber', 'login_date', 'login_time', 'logout_time')

# Format columns
window.column('#0', width=75, minwidth=25)  # Phantom column
window.column('username', anchor=CENTER, width=100)
window.column('user_id', anchor=W, width=50)
window.column('IDnumber', anchor=W, width=100)
window.column('login_date', anchor=W, width=100)
window.column('login_time', anchor=W, width=100)
window.column('logout_time', anchor=W, width=100)

# Defining column headings
window.heading('#0', text='Label', anchor=CENTER)  # Phantom Column
window.heading('username', text='Name', anchor=CENTER)
window.heading('user_id', text='User ID', anchor=CENTER)
window.heading('IDnumber', text='ID number', anchor=CENTER)
window.heading('login_date', text='Date', anchor=CENTER)
window.heading('login_time', text='Sign in', anchor=CENTER)
window.heading('logout_time', text='Sign out', anchor=CENTER)

# Obtain data from database
x = 0
for data in mycursor:
    window.insert(parent='', index='end', iid=x, text="User", values=(data[0], data[1], data[2], data[3], data[4], data[5]))
    x += 1

# Placing treeview table
window.pack(pady=20)

# Run Window
window.mainloop()