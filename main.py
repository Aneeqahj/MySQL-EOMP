from tkinter import *

from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()
window.geometry("400x400")
window.title("LifeChoices Online")
window.resizable("false", "false")
window.config(bg="#5a1c61")

frame = Frame(window, width=300, height=300, relief="groove", borderwidth=0, bg="#8c1c99")
frame.place(x=50, y=50)

welcome = Label(window, text="Welcome to LifeChoices Online.", bg="#5a1c61", font="Arial")
welcome.place(x=90, y=25)

intro = Label(window, text="If you're already registered with LifeChoices\n"
                           "online click the login button, if not then\n "
                           "click on register and complete the form.\n Thank you.", bg="#8c1c99")
intro.place(x=50, y=60)

login = Button(window, text="login")
login.place(x=60, y=300)

register = Button(window, text="Register")
register.place(x=160, y=300)

exit = Button(window)
window.mainloop()
