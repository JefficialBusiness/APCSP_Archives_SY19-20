# Module multifactorgui.py
# Includes new methods for activity 2.1.5

import tkinter as tk
import tkinter.messagebox as mb
import multifactorgui as mfg

# MultiFactorAuth is a class with three frames: 
#    an authorization (username/password) frame
#    an authentication (information factor) frame
#    the restircted applicaiton frame
# Users must pass all authorization and authentication steps to access the restricted app

class MultiFactorAuth(tk.Tk):

  # authorization and authentication info
  username = ""
  password = ""
  security_question = ""
  answer = ""

  # save username and password
  def set_authorization(self, user="admin", pw="secret"):
    self.username = user
    self.password = pw

  # save security question/answer that the user wants to use
  def set_authentication(self, user_question="unknwon", user_answer="unknown"):
    self.security_question = user_question
    self.answer = user_answer

  # create an instance of this class with a authorization window
  def __init__(self):
    tk.Tk.__init__(self)

    self.set_authorization()
    print (self.username, self.password)
    
    # create authorization frame and place widgets in it
    self.frame_login = tk.Frame(self)
    self.title("Authorize")
    self.frame_login.grid(row=0, column=0, sticky="news")

    self.lbl_username = tk.Label(self.frame_login,text="Username")
    self.lbl_username.pack(pady=5)
    self.ent_username = tk.Entry(self.frame_login, bd=3)
    self.ent_username.pack(pady=5)

    self.lbl_passwd = tk.Label(self.frame_login,text="Password")
    self.lbl_passwd.pack(pady=5)
    self.ent_password = tk.Entry(self.frame_login, show="*", bd=3)
    self.ent_password.pack(pady=5)

    self.btn_login = tk.Button(self.frame_login, text="LOG IN", command=self.authorize)
    self.btn_login.pack(padx=175, pady=20)
    
    # show this authorization frame
    self.frame_login.tkraise()

  # get the authorization information and if authorized, 
  # create and show the authentication frame
  def authorize(self):
    student_username = self.ent_username.get()
    student_password = self.ent_password.get()
    if (student_username == self.username and  student_password == self.password):
        # authorized - create authentication frame and widgets
        self.frame_auth = tk.Frame(self, bg= user_answer)
        self.title("Authenticate")
        self.frame_auth.grid(row=0, column=0, sticky="news")

        self.lbl_auth = tk.Label(self.frame_auth,text=self.security_question + "?", bg= user_answer)
        self.lbl_auth.pack(pady=5)
        self.ent_auth = tk.Entry(self.frame_auth, show="*", bd=3)
        self.ent_auth.pack(pady=5)

        self.btn_auth = tk.Button(self.frame_auth, text="AUTHENTICATE", command=self.authenticate)
        self.btn_auth.pack(pady=15)
        
        # show this authtication frame
        self.frame_auth.tkraise()

    else:
        mb.showinfo("Login failed","Invalid username and/or password")
   
  # get the authorization information and if authorized,
  # create and show the restricted app
  def authenticate(self):
    factor_info = self.ent_auth.get()
    if(factor_info == self.answer):
        # authenticted - create the restricted app 
        
        self.frame_restrict = tk.Frame(self, bg= "sienna2")
        self.title("Welcome to the Restricted Application")
        self.frame_restrict.grid(row=0, column=0, sticky="news")
  
        lbl_msg = tk.Label(self.frame_restrict,text="This is a restricted appliation.", bg="sienna2")
        lbl_msg.config(font=("Arial", 18))
        lbl_msg.pack(pady=15)

        lbl_auth = tk.Label(self.frame_restrict,text="Congratulations!\nYou have authenticated, and that makes Jeff very happy.", bg="sienna2")
        lbl_auth.pack(pady=30)

        # show this restricted app frame
        self.frame_restrict.tkraise()
        
    else:
        mb.showinfo("Authentication","We're sorry, but our records do not match your entry.")

 # Reset 
  def reset_authorizaiton(self):
    student_username = self.ent_username.get()
    student_password = self.ent_password.get()
    if (student_username == self.username and  student_password == self.password):
        # reset
        self.frame_reset = tk.Frame(self)
        self.title("RESET ")
        self.frame_reset.grid(row=0, column=0, sticky='news')

        self.lbl_reset_username = tk.Label(self.frame_reset,text='RESET Username:')
        self.lbl_reset_username.pack(pady=5)
        self.ent_reset_username = tk.Entry(self.frame_reset, bd=3)
        self.ent_reset_username.pack(pady=5)

        self.lbl_reset_passwd = tk.Label(self.frame_reset,text='RESET Password: ')
        self.lbl_reset_passwd.pack(pady=5)
        self.ent_reset_password = tk.Entry(self.frame_reset, show="*", bd=3)
        self.ent_reset_password.pack(pady=5)

        self.btn_reset_auth = tk.Button(self.frame_reset, text='SET new Username and Password', command=self.set_authorization_UI)
        self.btn_reset_auth.pack(pady=15)
        
        # show this   frame
        self.frame_reset.tkraise()

    else:
        mb.showinfo('Login failed','Invalid username and/or password')
   
     # get current password
  def get_password(self):
    return self.password

  def get_authorization(self):
    s1 = [None]*49
    a = self.username
    b = self.password

    i = 0
    for c in a:
      s1[i] = c
      i += 1   
    s1[24] = ":"
    i = 24
    for c in b:
      s1[i] = c
      i += 1

    s2 = "["
    for c in s1:
      if c == None:
        s2 = s2 + " "
      else:
        s2 = s2 + c
    s2 = s2 + "]"
    
    return s2


# prompts the user to configure a username, password, and favorite color

use_inp = True


def valid_user():
  if (8 <= len(user) <= 24):
    valid_user == True
    print("Username meets requirements!")
  else:
    valid_user == False
    print("Please make sure your username meets length requirements. Usernames must be in between 8 and 24 characters in length.")

def valid_pass():
  if (8 <= len(pw) <= 24):
    if pw.isdigit() == True:
      if pw.isalpha() == True:
        valid_pass() == True
        print("Password meets requirements!")
      else:
        valid_pass() == False
        print("Please make sure your password meets length requirements. Passwords must be in 8 and 24 characters in length and contain both letters and numbers.")
  

while (use_inp):
    user = input("Set a username.")
    pw = input("Now, select a password.")
    user_answer = input("Select a favorite color")
    valid_user()
    valid_pass()
    if valid_user() == False or valid_pass() == False:
      continue
    else:
      break
    break
  
    


# create a multi-factor interface to a restircted app
my_auth = mfg.MultiFactorAuth()

my_auth.set_authorization(user, pw)
# confirm authorization info
auth_info = my_auth.get_authorization()
print(auth_info)

# set the users authentication information
question = "What is your favorite color?"
answer = user_answer
my_auth.set_authentication(question, answer)

# start the GUI
my_auth.mainloop()


  
      
      

