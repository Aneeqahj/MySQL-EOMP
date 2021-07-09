from tkinter import *  # importing tkinter
from tkinter import messagebox  # importing message box
import mysql.connector
from PIL import Image

window = Tk()  # creating a window
window.geometry("400x600")  # window size
window.title("LifeChoices Online")  # window title
window.resizable("false", "false")  # For the window to remain at size
window.config(bg="#dea5e6")  # background colour
window.bind('<Control-a>', lambda z: admin())  # creating a shortcut kry for the admin page


def admin():  # creating a function for the shortcut key
    window.destroy()  # once the shortcut key is pressed and this window will close
    import main4  # once this window closes it will open the admin login


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

welcome = Label(window, text="Welcome, if you're already registered with LifeChoices\n"
                             "online click the login button, if not then\n "
                             "click on register and complete the form.\n Thank you.", bg="#dea5e6", fg="#2f1433")
welcome.place(x=20, y=150)


def login():  # creating a function for the login button
    msg_box = messagebox.askquestion("Login??", "Are you sure you want to log in?")
    if msg_box == "yes":  # if statement so that the current window will close and another will open
        window.destroy()
        import main2
    else:  # if you choose not to log in you will remain in this window
        messagebox.showinfo("Return", "You will remain on the home page.")


def register():  # creating a function for registration
    msg_box = messagebox.askquestion("Register??", "Would you like to register with LC online?")
    if msg_box == "yes":  # if statement so that the current window will close and another will open
        window.destroy()
        import main3
    else:  # if you choose not to register in you will remain in this window
        messagebox.showinfo("Return", "You will now return to the home page.")


def exit_btn():  # creating a function for the exit button
    msg_box = messagebox.askquestion("Exit?", "Are you sure you want to leave this program?")
    if msg_box == "yes":  # if statement so that the current window will close if yes is chosen
        window.destroy()
    else:  # if you choose not to exit in you will remain in this window
        messagebox.showinfo("Return", "You will now return to the App", icon="warning")


# Buttons
login = Button(window, text="login", width="30", bg=color["lilac"], activebackground=color["lightpurple"], border=0,
               highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
               command=login)
login.place(x=60, y=350)

register = Button(window, text="Register", width="30", bg=color["lilac"], activebackground=color["lightpurple"],
                  border=0,
                  highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
                  command=register)
register.place(x=60, y=450)

exit_btn = Button(window, text="Exit", width="30", bg=color["lilac"], activebackground=color["lightpurple"], border=0,
                  highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
                  command=exit_btn)
exit_btn.place(x=60, y=550)
window.mainloop()  # run window
