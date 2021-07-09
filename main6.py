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
home2_label = Label(top_frame, text="LifeChoices Online - logout", font="Arial 15", bg=color["purple"], fg="white",
                    height=2,
                    padx=20)
home2_label.pack(side="left")

home_label = Label(top_frame, text="LC", font="Arial 15", bg=color["purple"], fg="white", height=2, padx=20)
home_label.pack(side="right")


def logout():
    msg_box = messagebox.askquestion("Logout??", "Are you sure you want to log out?")
    if msg_box == "yes":
        window.destroy()
    else:
        messagebox.showinfo("Return", "You will remain on this page.")


# Buttons
logout = Button(window, text="logout", width="30", bg=color["lilac"], activebackground=color["lightpurple"], border=0,
                highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
                command=logout)
logout.place(x=60, y=350)

# Labels
logout = Label(window, text="Welcome to LC logout page \n"
                            "Please click the logout button below\n "
                            "Thank you. Enjoy your day.", bg="#dea5e6", fg="#2f1433", font="Arial")
logout.place(x=70, y=150)

window.mainloop()
