from tkinter import *  # importing tkinter
from tkinter import messagebox  # importing message box
import mysql.connector

window = Tk()  # creating a window
window.geometry("400x600")  # size of the window
window.title("LifeChoices Online")  # title of the window
window.resizable("false", "false")  # For the window to remain at size
window.config(bg="#dea5e6")  # background colour

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


def logout():  # creating a function for the logout button
    msg_box = messagebox.askquestion("Logout??", "Are you sure you want to log out?")
    if msg_box == "yes":  # if statement so that the current window will close
        window.destroy()
    else:  # if you choose not to logout in you will remain in this window
        messagebox.showinfo("Return", "You will remain on this page.")


def back():  # creating a function for the home page
    msg_box = messagebox.askquestion("Return?", "Do you want to return to the home page?")
    if msg_box == "yes":  # if statement so that the current window will close if yes is chosen and return to the home
        # page
        window.destroy()
        import main
    else:  # if you choose not to go the home page you will remain on this page
        messagebox.showinfo("Login", "You will remain on the login page")


# Buttons
logout = Button(window, text="logout", width="30", bg=color["lilac"], activebackground=color["lightpurple"], border=0,
                highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
                command=logout)
logout.place(x=60, y=350)
back = Button(window, text="Home", width="30", bg=color["lilac"], activebackground=color["lightpurple"], border=0,
              highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
              command=back)
back.place(x=60, y=450)

# Labels
logout = Label(window, text="Welcome to LC logout page \n"
                            "Please click the logout button below\n "
                            "Thank you. Enjoy your day.", bg="#dea5e6", fg="#2f1433", font="Arial")
logout.place(x=70, y=150)

window.mainloop()
