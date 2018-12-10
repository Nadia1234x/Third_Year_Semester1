from Tkinter import *

def raise_frame(frame):
    frame.tkraise()
    
window = Tk()
window.geometry("800x500")
window.title("Intrusion Detection - Pink Panther!")


f1 = Frame(window, width = 800, height = 800)
f1.configure(background = "Blue")
f1.grid_propagate(0)

f2 = Frame(window)
f2.configure(background = "Blue")
f2.grid_propagate(0)



window.configure(background = "Blue")


for frame in (f1, f2):
    frame.grid(row = 0, column = 0, sticky = 'news')

c = Checkbutton(f1, text="Are you the admin?")
c.configure(background = "Blue", fg = "white")
c.grid(row = 0, column = 25)



username_label = Label(f1, text = "Username: ")
username_label.configure(background = "Blue", fg = "white")
username_label.grid(row = 8, column = 5)
password_label = Label(f1, text = "Password: ")
password_label.configure(background = "Blue", fg = "white")
password_label.grid(row = 9, column = 5)
username_entry_path = Entry(f1)
username_entry_path.grid(row = 8, column = 6)
password_entry_path = Entry(f1)
password_entry_path.grid(row = 9, column = 6)


submit_button = Button(f1, text = 'Submit', command=lambda:raise_frame(f2))
submit_button.grid(row = 30, column = 6)

raise_frame(f1)
window.mainloop()