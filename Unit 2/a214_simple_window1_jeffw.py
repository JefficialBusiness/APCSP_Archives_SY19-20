##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk




# main window
root = tk.Tk()
root.wm_geometry("200x200")
root.title("Authorization")




# create empty frame
frame_login = tk.Frame(root)
frame_login.grid()
lbl_username = tk.Label(frame_login, text = "Enter Username:", font = ("Times"))
ent_username = tk.Entry(frame_login, bd=3)

lbl_password = tk.Label(frame_login, text = "Enter Password:", font = ("Times"))
ent_password = tk.Entry(frame_login, bd=3)
lbl_username.pack(padx=50)
ent_username.pack(pady=5)
lbl_password.pack(padx=50)
ent_password.pack(pady=5)

frame_auth = tk.Frame(root)
frame_auth.grid()

def test_button():
    frame_auth.tkraise()
    flash()
    

b = tk.Button(frame_login, text="Log In", command=test_button)
b.pack()



root.mainloop()