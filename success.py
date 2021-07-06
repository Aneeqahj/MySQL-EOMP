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
home2_label = Label(top_frame, text="LifeChoices Online", font="Arial 15", bg=color["purple"], fg="white", height=2,
                    padx=20)
home2_label.pack(side="left")

home_label = Label(top_frame, text="LC", font="Arial 15", bg=color["purple"], fg="white", height=2, padx=20)
home_label.pack(side="right")

welcome = Label(window, text="Login Successful!\n Enjoy Your Day\n Don't forget to sanitze, \n wear a mask and \n "
                             "social "
                             "distance is key!!", bg="#dea5e6", fg="#2f1433", font="Arial, 20")
welcome.place(x=40, y=150)


def cool():
    msg_box = messagebox.askquestion("Nice!!", "You were successful, would you like to leave??")
    if msg_box == "yes":
        window.destroy()
    else:
        messagebox.showinfo("Return", "You will remain on this page.")


cool = Button(window, text="Cool beans", width="30", bg=color["lilac"], activebackground=color["lightpurple"], border=0,
              highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
              command=cool)
cool.place(x=60, y=350)

window.mainloop()
