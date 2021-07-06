from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()
window.geometry("400x600")
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
username = Label(window, text="Username:", bg=color["lilac"])
username.place(x=20, y=100)
password = Label(window, text="Password:", bg=color["lilac"])
password.place(x=20, y=150)
email = Label(window, text="Email:", bg=color["lilac"])
email.place(x=20, y=200)

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
register.place(x=60, y=350)
exit_btn = Button(window, text="Exit", width="30", bg=color["lilac"], activebackground=color["lightpurple"], border=0,
                  highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
                  command=exit_btn)
exit_btn.place(x=60, y=450)
back = Button(window, text="Back", width="30", bg=color["lilac"], activebackground=color["lightpurple"], border=0,
              highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
              command=back)
back.place(x=60, y=550)
window.mainloop()
