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
home2_label = Label(top_frame, text="LifeChoices Online Admin", font="Arial 15", bg=color["purple"], fg="white",
                    height=2,
                    padx=20)
home2_label.pack(side="left")

home_label = Label(top_frame, text="LC", font="Arial 15", bg=color["purple"], fg="white", height=2, padx=20)
home_label.pack(side="right")

# Labels
email = Label(window, text="Email:", bg=color["lilac"], fg=color["purple"])
email.place(x=20, y=100)
password = Label(window, text="Password:", bg=color["lilac"], fg=color["purple"])
password.place(x=20, y=150)

# Entries
email_ent = Entry(window)
email_ent.place(x=200, y=100)
password_ent = Entry(window, show="*")
password_ent.place(x=200, y=150)


def back():
    msg_box = messagebox.askquestion("Return?", "Do you want to return to the home page?")
    if msg_box == "yes":
        window.destroy()
        import main
    else:
        messagebox.showinfo("Login", "You will remain on the admin page")


def exit_btn():
    msg_box = messagebox.askquestion("Exit?", "Are you sure you want to leave this program?")
    if msg_box == "yes":
        window.destroy()
    else:
        messagebox.showinfo("Return", "You will now return to the App", icon="warning")


# Buttons
confirm = Button(window, text="confirm", width="30", bg=color["lilac"], activebackground=color["lightpurple"],
                 border=0,
                 highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"], )
confirm.place(x=60, y=300)
back = Button(window, text="Home Page", width="30", bg=color["lilac"], activebackground=color["lightpurple"], border=0,
              highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
              command=back)
back.place(x=60, y=400)
exit_btn = Button(window, text="Exit", width="30", bg=color["lilac"], activebackground=color["lightpurple"], border=0,
                  highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
                  command=exit_btn)
exit_btn.place(x=60, y=500)

window.mainloop()
