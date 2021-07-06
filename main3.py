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
username = Label(window, text="Username:", bg=color["lilac"], fg=color["purple"])
username.place(x=20, y=100)
password = Label(window, text="Password:", bg=color["lilac"], fg=color["purple"])
password.place(x=20, y=150)
email = Label(window, text="Email:", bg=color["lilac"], fg=color["purple"])
email.place(x=20, y=200)
name = Label(window, text="Name:", bg=color["lilac"], fg=color["purple"])
name.place(x=20, y=250)
surname = Label(window, text="Surname:", bg=color["lilac"], fg=color["purple"])
surname.place(x=20, y=300)
idnum = Label(window, text="ID Number:", bg=color["lilac"], fg=color["purple"])
idnum.place(x=20, y=350)
phoneNum = Label(window, text="Phone Number:", bg=color["lilac"], fg=color["purple"])
phoneNum.place(x=20, y=400)
Nameofkin = Label(window, text="Next of kin Name:", bg=color["lilac"], fg=color["purple"])
Nameofkin.place(x=20, y=450)
Numofkin = Label(window, text="Next of kin PhoneNumber:", bg=color["lilac"], fg=color["purple"])
Numofkin.place(x=20, y=500)

# Entries
username_ent = Entry(window)
username_ent.place(x=200, y=100)
password_ent = Entry(window, show="*")
password_ent.place(x=200, y=150)
email_ent = Entry(window)
email_ent.place(x=200, y=200)


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
    pass


register = Button(window, text="Register", width="30", bg=color["lilac"], activebackground=color["lightpurple"],
                  border=0,
                  highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
                  command=register)
register.place(x=60, y=550)
exit_btn = Button(window, text="Exit", width="30", bg=color["lilac"], activebackground=color["lightpurple"], border=0,
                  highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
                  command=exit_btn)
exit_btn.place(x=60, y=650)
back = Button(window, text="Back", width="30", bg=color["lilac"], activebackground=color["lightpurple"], border=0,
              highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
              command=back)
back.place(x=60, y=750)
window.mainloop()
