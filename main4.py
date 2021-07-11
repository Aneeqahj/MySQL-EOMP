from tkinter import *  # importing tkinter
from tkinter import messagebox  # importing messagebox
import mysql.connector  # importing mysql.connector so i can link mysql to tkinter

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


def confirm():  # creating a function to confirm details entered
    # creating variable for the entries
    email = email_ent.get()
    password = password_ent.get()

    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                   # linking the the database to
                                   # tkinter with all relevant details
                                   database='LifeChoicesOnline', auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()  # creating a variable cursor  which allows row by row processing of the results
    xy = mycursor.execute(
        f"SELECT * FROM Admin WHERE email = '{email}' and password = '{password}'")  # executing a command in the
    # database
    results = mycursor.fetchall()  # fetching everything in the database
    if len(results) > 0:
        window.destroy()
        import main5
    else:
        messagebox.showerror("Error", "User details are incorrect")


def back():  # creating a function for the home page
    msg_box = messagebox.askquestion("Return?", "Do you want to return to the home page?")
    if msg_box == "yes":  # if statement so that the current window will close if yes is chosen and return to the home
        # page
        window.destroy()
        import main
    else:  # if you choose not to go the home page you will remain on this page
        messagebox.showinfo("Login", "You will remain on the admin page")


def exit_btn():  # creating a function for the exit button
    msg_box = messagebox.askquestion("Exit?", "Are you sure you want to leave this program?")
    if msg_box == "yes":  # if statement so that the current window will close if yes is chosen and return to the home
        # page
        window.destroy()
    else:  # if you choose not to go the home page you will remain on this page
        messagebox.showinfo("Return", "You will now return to the App", icon="warning")


# Buttons
confirm = Button(window, text="confirm", width="30", bg=color["lilac"], activebackground=color["lightpurple"],
                 border=0,
                 highlightbackground=color["darkpurple"], fg=color["purple"], activeforeground=color["purple"],
                 command=confirm)
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
