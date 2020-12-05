import tkinter
import os
from tkinter import *

os.chdir('F:/Acads/5th sem/Python CS384/CS384_1801CE31/Projects/P1 Quiz_via_CSV')

import datamanager
import hashlib
import time
import queue
import threading
from tkinter import messagebox
import pandas as pd
import sqlite3

class login:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Quiz Login Screen')
        self.root.geometry('500x350')
        self.user_ds = datamanager.database()
        ##### Variables for Register
        self.reg_roll = StringVar()
        self.reg_password = StringVar()
        self.reg_name = StringVar()
        self.reg_wapp_number = StringVar()
        ###### Variables for login
        self.log_roll = StringVar()
        self.log_password = StringVar()
        self.homepage()
        self.root.mainloop()
        
    def homepage(self):
        self.header = Label(self.root,text="CS384 : Quiz Project",font=('',35))
        self.header.pack()
        self.header = Label(self.root,text="Quiz Login",font=('',25),padx=5,pady=5)
        self.header.pack()
        login_frame = Frame(self.root,padx=30,pady=30)
        Label(login_frame,text = 'Roll No: ',font = ('',20),pady=15,padx=45).grid(sticky = W)
        Entry(login_frame,textvariable = self.log_roll,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(login_frame,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(login_frame,textvariable = self.log_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(login_frame,text = ' Login ',bd = 7 ,font = ('',15),padx=5,pady=5,command = self.login).grid()
        Button(login_frame,text = ' Register ',bd = 7 ,font = ('',15),padx=5,pady=5,command = self.register_screen).grid(row=2,column=1)
        self.login_frame= login_frame
        self.login_frame.pack()
        
    def register_screen(self):
        reg_frame = Frame(self.root)
        reg_frame = Frame(self.root,padx =5,pady = 5)
        Label(reg_frame,text = 'Name : ',font = ('',18),pady=5,padx=5).grid(sticky = W)
        Entry(reg_frame,textvariable = self.reg_name,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(reg_frame,text = 'Password : ',font = ('',18),pady=5,padx=5).grid(sticky = W)
        Entry(reg_frame,textvariable = self.reg_password,bd = 5,font = ('',15)).grid(row=1,column=1)
        Label(reg_frame,text = 'Roll No : ',font = ('',18),pady=5,padx=5).grid(sticky = W)
        Entry(reg_frame,textvariable = self.reg_roll,bd = 5,font = ('',15)).grid(row=2,column=1)
        Label(reg_frame,text = 'Whatsapp_No : ',font = ('',18),pady=5,padx=5).grid(sticky = W)
        Entry(reg_frame,textvariable = self.reg_wapp_number,bd = 5,font = ('',15)).grid(row=3,column=1)
        Button(reg_frame,text = 'Register',bd = 7 ,font = ('',15),padx=5,pady=5,command=self.registration).grid()
        Button(reg_frame,text = 'Back',bd = 7 ,font = ('',15),padx=5,pady=5,command=self.login_screen).grid(row=4,column=1)
        self.reg_frame = reg_frame
        
        self.reg_roll.set('')
        self.reg_password.set('')
        self.reg_name.set('')
        self.reg_wapp_number.set('')
        self.login_frame.pack_forget()
        self.header['text'] = 'Registration'
        self.reg_frame.pack()
    
    def login_screen(self):
        self.log_roll.set('')
        self.log_password.set('')
        self.reg_frame.pack_forget()
        self.header["text"] = "Quiz Login"
        self.login_frame.pack()
        
    def registration(self):
        res = self.user_ds.register(self.reg_roll.get(),self.reg_password.get(),self.reg_name.get(),self.reg_wapp_number.get())
        if res :
            messagebox.showinfo("Success","successfully registered")
        else:
            messagebox.showerror("Error","{} already exists".format(self.reg_roll.get()))

    def login(self):
        res  = self.user_ds.check_cred(self.log_roll.get(),self.log_password.get())
        if res.get("success") == False:
            messagebox.showerror("Error",res.get("msg"))
        else:
            self.root.destroy()
            user_credentials = self.user_ds.get_user(self.log_roll.get())['data']
            user_roll = user_credentials[0]
            user_name = user_credentials[2]
            main_screen(user_roll,user_name)


l = login()