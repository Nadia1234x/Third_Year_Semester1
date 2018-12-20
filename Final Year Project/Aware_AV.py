from Tkinter import *
import check_login_details


def raise_frame(frame):
    frame.tkraise()

def save_login_details(event):
    username1 = username.get()
    password1 = password.get()

    check_login_details.validate_credentials(str(username1), str(password1))
    
window = Tk()
window.geometry("800x120")
window.title("Intrusion Detection - Pink Panther!")


f1 = Frame(window, width = 800, height = 500)
f1.configure(background = "Blue")
f1.grid_propagate(0)

f2 = Frame(window)
f2.configure(background = "Blue")
f2.grid_propagate(0)

window.configure(background = "Blue")

for frame in (f1, f2):
    frame.grid(row = 1000, column = 1000, sticky = 'news')

login_label = Label(f1, text = "Login:")
login_label.grid(row = 0, column = 0, sticky = W)
login_label.configure(background = "Blue", fg = "White")

register_label = Label(f1, text = "   Register:")
register_label.grid(row =0, column = 10, sticky = W)
register_label.configure(background = "Blue", fg = "White")

#c = Checkbutton(f1, text="Are you the admin?")
#c.configure(background = "Blue", fg = "white")
#c.grid(row = 1, column = 0)

username = StringVar()
password = StringVar()
new_username = StringVar()
new_password = StringVar()

username_label = Label(f1, text = "Username: ")
username_label.configure(background = "Blue", fg = "white")
username_label.grid(row = 5, column = 0, sticky = W)
username_entry_path = Entry(f1, textvariable = username)
username_entry_path.grid(row = 5, column = 1)

password_label = Label(f1, text = "Password: ")
password_label.configure(background = "Blue", fg = "white")
password_label.grid(row = 6, column = 0, sticky = W)
password_entry_path = Entry(f1, textvariable = password)
password_entry_path.grid(row = 6, column = 1)

or_label = Label(f1, text="                           or                            ")
or_label.configure(background = "Blue", fg = "White")
or_label.grid(row = 5, column =9)

reg_username_label = Label(f1, text = "   Username: ")
reg_username_label.configure(background = "Blue", fg = "white")
reg_username_label.grid(row = 5, column = 10)
reg_username_entry_path = Entry(f1, textvariable=new_username)
reg_username_entry_path.grid(row = 5, column = 11)

reg_password_entry_path = Entry(f1,  show = "*", textvariable = new_password)
reg_password_entry_path.grid(row = 6, column = 11)
reg_password_label = Label(f1, text = "   Password: ")
reg_password_label.configure(background = "Blue", fg = "white")
reg_password_label.grid(row = 6, column = 10)
#reg_secretword_entry_path

submit_button = Button(f1, text = 'Submit', command=lambda:raise_frame(f2))
submit_button.bind("<Button-1>", save_login_details)
submit_button.grid(row = 7, column = 1)

register_button = Button(f1, text = 'register')
register_button.grid(row = 7, column = 11)


raise_frame(f1)
window.mainloop()