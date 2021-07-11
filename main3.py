from tkinter import *  # importing tkinter
from tkinter import messagebox  # importing messagebox
import mysql.connector  # importing mysql.connector so i can link mysql to tkinter
from validate_email import validate_email  # importing validate email to check if the email is valid
import rsaidnumber  # importing rsaidnumber to check if a real ID number is given

window = Tk()  # creating a window
window.geometry("400x800")  # size of the window
window.title("LifeChoices Online")  # title of the window
window.resizable("false", "false")  # For the window to remain at size
window.config(bg="#dea5e6")  # background colour

# Dictionary of colours:
color = {"purple": "#5a1c61", "lightpurple": "#8c1c99", "darkpurple": "#390340", "lilac": "#dea5e6"}

# Top frame
top_frame = Frame(window, bg=color["purple"])
top_frame.pack(side="top", fill=X)

# header
home2_label = Label(top_frame, text="LifeChoices Online - Registration", font="Arial 15", bg=color["purple"],
                    fg="white",
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


def exit_btn():  # creating a function for the exit button
    msg_box = messagebox.askquestion("Exit?", "Are you sure you want to leave this program?")
    if msg_box == "yes":  # if statement so that the current window will close if yes is chosen
        window.destroy()
    else:  # if you choose not to exit in you will remain in this window
        messagebox.showinfo("Return", "You will now return to the App", icon="warning")


def back():  # creating a function for the home page
    msg_box = messagebox.askquestion("Return?", "Do you want to return to the home page?")
    if msg_box == "yes":  # if statement so that the current window will close if yes is chosen and return to the home
        # page
        window.destroy()
        import main
    else:  # if you choose not to go the home page you will remain on this page
        messagebox.showinfo("Registration", "You will remain on the registration page")


def register():  # creating a function for registration
    mydb = mysql.connector.connect(user="lifechoices", password="@Lifechoices1234",  # linking the the database to
                                   # tkinter with all relevant details
                                   host="127.0.0.1", database="LifeChoicesOnline",
                                   auth_plugin="mysql_native_password")
    mycursor = mydb.cursor(buffered=True)  # creating a variable cursor  which allows row by row processing of the
    # results
    select = "SELECT user_id FROM Login"
    user_id = mycursor.execute(select)  # executing a command in the database
    user_id = mycursor.fetchone()
    print(user_id[0])

    sql = "INSERT INTO Registration (email, name, surname, IDnumber, phoneNumber, NextOfKinName, " \
          "NextOfKinNumber, user_id) \n VALUES (%s,%s,%s,%s,%s,%s,%s,%s) "
    value = (
        email_ent.get(), name_ent.get(), surname_ent.get(), IDnumber_ent.get(),
        phoneNum_ent.get(), Nameofkin_ent.get(), Numofkin_ent.get(), user_id[0])
    print(value)
    print(sql)
    mycursor.execute(sql, value)
    mydb.commit()  # committing all the transactions above

    mycursor.execute("Select * from Registration")  # executing a command in the database

    name = name_ent.get()  # creating variables for entries
    email = email_ent.get()
    id = IDnumber_ent.get()
    if name == " ":  # creating an if statement to check if the user's details are correct
        if email == " ":
            messagebox.showerror("Error", "Enter correct email")
        else:
            if not validate_email(email):
                messagebox.showerror("Error", "Enter correct Email")
            else:
                if len(id) != 13:  # if the id is not 13 digits show an error
                    messagebox.showerror("Error", "Please enter correct ID number")

                elif len(id) == 13:  # if ID is 13 digits accept
                    id = rsaidnumber.parse(id)
                    id.valid
    else:
        messagebox.showinfo("Success", "Your registration was successful.")
        window.destroy()
    import main


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
