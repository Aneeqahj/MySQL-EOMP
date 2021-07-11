from tkinter import *  # importing tkinter
from tkinter import ttk
from tkinter import messagebox  # importing messagebox
import mysql.connector  # importing mysql.connector so i can link mysql to tkinter

window = Tk()  # creating a window
window.geometry("800x900")  # size of the window
window.title("LifeChoices Online")  # title of the window
window.resizable("false", "false")  # For the window to remain at size
window.config(bg="#dea5e6")  # background colour

# Dictionary of colours:
color = {"purple": "#5a1c61", "lightpurple": "#8c1c99", "darkpurple": "#390340", "lilac": "#dea5e6", "white": "#ffffff"}

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

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                               database='LifeChoicesOnline', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
xy = mycursor.execute('Select * from Login')


def edit():  # creating a function for the edit button
    selected = window.focus()  # creating variable that set focus to the current window
    id = window.item(selected, 'values')[1]
    name = edit_ent.get()
    idnumber = edit_ent2.get()
    mycursor = mydb.cursor()
    xy = mycursor.execute(
        f"UPDATE Login SET username = '{name}', IDnumber = '{idnumber}' WHERE user_id = '{id}';")  # executing a
    # command in the database
    mydb.commit()  # committing all the transactions above


def delete():  # creating a function for the delete button
    selected = window.focus()  # creating variable that set focus to the current window
    id = window.item(selected, 'values')[1]
    mycursor = mydb.cursor()
    xy = mycursor.execute(f"DELETE FROM Login WHERE user_id = {id};")  # executing a command in the database
    mydb.commit()  # committing all the transactions above


def add():  # creating an add function for add  button
    mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234",  # linking the the database to
                                   # tkinter with all relevant details
                                   host="127.0.0.1", database="LifeChoicesOnline",
                                   auth_plugin="mysql_native_password")
    mycursor = mydb.cursor(buffered=True)  # creating a variable cursor  which allows row by row processing of the
    # results
    select = "SELECT user_id FROM Login"
    user_id = mycursor.execute(select)  # executing a command in the database
    user_id = mycursor.fetchone()
    print(user_id[0])

    sql = "INSERT INTO Registration(email, name, surname, IDnumber, phoneNumber, NextOfKinName, " \
          "NextOfKinNumber, user_id) \n VALUES(%s,%s,%s,%s,%s,%s,%s,%s) "
    value = (
        email_ent.get(), name_ent.get(), surname_ent.get(), IDnumber_ent.get(),
        phoneNum_ent.get(), Nameofkin_ent.get(), Numofkin_ent.get(), user_id[0])
    exe = mycursor.execute(sql, value)
    mydb.commit()  # committing all the transactions above

    mycursor.execute("Select * from Registration")  # executing a command in the database


def back():  # creating a function for the home page
    msg_box = messagebox.askquestion("Return?", "Do you want to return to the home page?")
    if msg_box == "yes":  # if statement so that the current window will close if yes is chosen and return to the home
        # page
        window.destroy()
        import main
    else:  # if you choose not to go the home page you will remain on this page
        messagebox.showinfo("Login", "You will remain on the logout page")


# frames
frame = Frame(window, width=656, height=400, relief="groove", borderwidth=1, bg=color["lightpurple"])
frame.place(x=71, y=400)
frame2 = Frame(window, width=656, height=90, relief="groove", borderwidth=0, bg=color["lightpurple"])
frame2.place(x=71, y=300)

# Labels
edit_lbl = Label(window, text="Edit user", bg=color["lightpurple"], fg=color["white"], font="Arial, 20")
edit_lbl.place(x=300, y=305)
edit1 = Label(window, text="Name:", bg=color["lightpurple"], fg=color["white"])
edit1.place(x=200, y=330)
edit2 = Label(window, text="ID Number:", bg=color["lightpurple"], fg=color["white"])
edit2.place(x=200, y=360)
add_lbl = Label(window, text="Add new user", bg=color["lightpurple"], fg=color["white"], font="Arial, 20")
add_lbl.place(x=300, y=410)
name = Label(window, text="Name:", bg=color["lightpurple"], fg=color["white"])
name.place(x=200, y=450)
surname = Label(window, text="Surname:", bg=color["lightpurple"], fg=color["white"])
surname.place(x=200, y=500)
email = Label(window, text="Email:", bg=color["lightpurple"], fg=color["white"])
email.place(x=200, y=550)
IDnumber = Label(window, text="ID Number:", bg=color["lightpurple"], fg=color["white"])
IDnumber.place(x=200, y=600)
phoneNum = Label(window, text="Phone Number:", bg=color["lightpurple"], fg=color["white"])
phoneNum.place(x=200, y=650)
Nameofkin = Label(window, text="Next of kin Name:", bg=color["lightpurple"], fg=color["white"])
Nameofkin.place(x=200, y=700)
Numofkin = Label(window, text="Next of kin PhoneNumber:", bg=color["lightpurple"], fg=color["white"])
Numofkin.place(x=200, y=750)

# Entries
edit_ent = Entry(window)
edit_ent.place(x=500, y=330)
edit_ent2 = Entry(window)
edit_ent2.place(x=500, y=360)
name_ent = Entry(window)
name_ent.place(x=500, y=450)
surname_ent = Entry(window)
surname_ent.place(x=500, y=500)
email_ent = Entry(window)
email_ent.place(x=500, y=550)
IDnumber_ent = Entry(window)
IDnumber_ent.place(x=500, y=600)
phoneNum_ent = Entry(window)
phoneNum_ent.place(x=500, y=650)
Nameofkin_ent = Entry(window)
Nameofkin_ent.place(x=500, y=700)
Numofkin_ent = Entry(window)
Numofkin_ent.place(x=500, y=750)

# Buttons
edit = Button(window, text="Update", width="10", bg=color["lilac"], activebackground=color["lightpurple"],
              border=0,
              highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
              command=edit)
edit.place(x=650, y=850)

delete = Button(window, text="Delete", width="10", bg=color["lilac"], activebackground=color["lightpurple"], border=0,
                highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
                command=delete)
delete.place(x=50, y=850)
add = Button(window, text="Add", width="10", bg=color["lilac"], activebackground=color["lightpurple"], border=0,
             highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"], command=add)
add.place(x=200, y=850)
exit_btn = Button(window, text="Exit", width="10", bg=color["lilac"], activebackground=color["lightpurple"], border=0,
                  highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
                  command=exit)
exit_btn.place(x=350, y=850)
back = Button(window, text="Home", width="10", bg=color["lilac"], activebackground=color["lightpurple"], border=0,
              highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
              command=back)
back.place(x=500, y=850)
window = ttk.Treeview(window)

# Defining columns
window['columns'] = ('username', 'user_id', 'IDnumber', 'login_date', 'login_time', 'logout_time')

# Format columns
window.column('#0', width=75, minwidth=25)  # Phantom column
window.column('username', anchor=CENTER, width=100)
window.column('user_id', anchor=W, width=60)
window.column('IDnumber', anchor=W, width=120)
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
    window.insert(parent='', index='end', iid=x, text="User",
                  values=(data[0], data[1], data[2], data[3], data[4], data[5]))
    x += 1

# Placing treeview table
window.pack(pady=20)

# Run Window
window.mainloop()
