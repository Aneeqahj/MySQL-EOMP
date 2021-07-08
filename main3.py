from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()
window.geometry("400x800")
window.title("LifeChoices Online")
window.resizable("false", "false")
window.config(bg="#dea5e6")

# Dictionary of colours:
color = {"purple": "#5a1c61", "lightpurple": "#8c1c99", "darkpurple": "#390340", "lilac": "#dea5e6"}

# Top frame
top_frame = Frame(window, bg=color["purple"])
top_frame.pack(side="top", fill=X)

# header
home2_label = Label(top_frame, text="LifeChoices Online Registration", font="Arial 15", bg=color["purple"], fg="white",
                    height=2,
                    padx=20)
home2_label.pack(side="left")

home_label = Label(top_frame, text="LC", font="Arial 15", bg=color["purple"], fg="white", height=2, padx=20)
home_label.pack(side="right")

# more labels

name = Label(window, text="Name:", bg=color["lilac"], fg=color["purple"])
name.place(x=20, y=100)
surname = Label(window, text="Surname:", bg=color["lilac"], fg=color["purple"])
surname.place(x=20, y=150)
email = Label(window, text="Email:", bg=color["lilac"], fg=color["purple"])
email.place(x=20, y=200)
IDnumber = Label(window, text="ID Number:", bg=color["lilac"], fg=color["purple"])
IDnumber.place(x=20, y=250)
phoneNum = Label(window, text="Phone Number:", bg=color["lilac"], fg=color["purple"])
phoneNum.place(x=20, y=300)
Nameofkin = Label(window, text="Next of kin Name:", bg=color["lilac"], fg=color["purple"])
Nameofkin.place(x=20, y=350)
Numofkin = Label(window, text="Next of kin PhoneNumber:", bg=color["lilac"], fg=color["purple"])
Numofkin.place(x=20, y=400)

# Entries
name_ent = Entry(window)
name_ent.place(x=200, y=100)
surname_ent = Entry(window)
surname_ent.place(x=200, y=150)
email_ent = Entry(window)
email_ent.place(x=200, y=200)
IDnumber_ent = Entry(window)
IDnumber_ent.place(x=200, y=250)
phoneNum_ent = Entry(window)
phoneNum_ent.place(x=200, y=300)
Nameofkin_ent = Entry(window)
Nameofkin_ent.place(x=200, y=350)
Numofkin_ent = Entry(window)
Numofkin_ent.place(x=200, y=400)


def exit_btn():
    msg_box = messagebox.askquestion("Exit?", "Are you sure you want to leave this program?")
    if msg_box == "yes":
        window.destroy()
    else:
        messagebox.showinfo("Return", "You will now return to the App", icon="warning")


def back():
    msg_box = messagebox.askquestion("Return?", "Do you want to return to the home page?")
    if msg_box == "yes":
        window.destroy()
        import main
    else:
        messagebox.showinfo("Registration", "You will remain on the registration page")


def register():
    mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234",
                                   host="127.0.0.1", database="LifeChoicesOnline",
                                   auth_plugin="mysql_native_password")
    mycursor = mydb.cursor()
    select = "SELECT user_id FROM Login"
    user_id = mycursor.execute(select)
    user_id = mycursor.fetchone()
    print(user_id[0])

    sql = "INSERT INTO Registration(email, name, surname, IDnumber, phoneNumber, NextOfKinName, " \
          "NextOfKinNumber, user_id) \n VALUES(%s,%s,%s,%s,%s,%s,%s,%s) "
    value = (
        email_ent.get(), name_ent.get(), surname_ent.get(), IDnumber_ent.get(),
        phoneNum_ent.get(), Nameofkin_ent.get(), Numofkin_ent.get(), user_id[0])
    exe = mycursor.execute(sql, value)
    mydb.commit()

    mycursor.execute("Select * from Registration")

    if surname_ent == "" or phoneNum_ent == "" or Nameofkin_ent == "" or Numofkin_ent == "":
        messagebox.showerror("ERROR", "Please ensure that all fields are filled in.")
    else:
        messagebox.showinfo("Success", "your registration was successful.")
        window.destroy()
        import main2


register = Button(window, text="Register", width="30", bg=color["lilac"], activebackground=color["lightpurple"],
                  border=0,
                  highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
                  command=register)
register.place(x=60, y=500)
exit_btn = Button(window, text="Exit", width="30", bg=color["lilac"], activebackground=color["lightpurple"], border=0,
                  highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
                  command=exit_btn)
exit_btn.place(x=60, y=600)
back = Button(window, text="Back", width="30", bg=color["lilac"], activebackground=color["lightpurple"], border=0,
              highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
              command=back)
back.place(x=60, y=700)
window.mainloop()
