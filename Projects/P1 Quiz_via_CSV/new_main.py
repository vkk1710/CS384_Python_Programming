import tkinter
from tkinter import *
import datastore
import hashlib


class login:
    def __init__(self):
        self.connect = sqlite3.connect("project1_quiz_cs384")
        self.connect.execute('''CREATE TABLE IF NOT EXISTS project1_registration(
                username VARCHAR(15),
                password VARCHAR(45),
                name VARCHAR(30), 
                whatsapp_number VARCHAR(10)
        )''')
        self.connect.commit()

        self.root = tkinter.Tk()
        self.root.title('Quiz')
        self.root.geometry('700x600')
        self.user_ds = datastore.user_datastore()
        ##### Variables for Register
        self.rg_roll = StringVar()
        self.rg_password = StringVar()
        self.rg_name = StringVar()
        self.rg_wapp_number = StringVar()
        ###### Variables for login
        self.lg_roll = StringVar()
        self.lg_password = StringVar()
        self.homepage()
        self.root.mainloop()
        
    def get_user(self,roll):
        self.found = 1
        cursor = self.connect.cursor()
        self.data = cursor.execute('''SELECT * FROM project1_registration WHERE username=:roll''',{"roll":roll}).fetchone()
        if self.data == None:
            self.found = 0
        cursor.close()
        
    def register(self,roll,text_password,name,whatsapp_number):
        self.get_user(roll)
        if (self.found == 1):
            return False
        
        password = hashlib.md5(text_password.encode()).hexdigest()
        self.connect.execute('''INSERT INTO project1_registration(username,password,name,whatsapp_number) VALUES(?,?,?,?)''',
        [
            (roll),
            (password),
            (name),
            (whatsapp_number)
        ])
        self.connect.commit()
        return True
    
    def check_credentials(self,roll,password):
        check = True
        msg = "Logged in"
        data = self.get_user(roll)
        if data.get("found") == False:
            check = False
            msg = "{} not found".format(roll)
        if found and data.get("data")[1] != utils.genMD5(password):
            msg = "invalid Password"
            found = False
        return {
            "success" : check,
            "msg" : msg
        }
        
    def homepage(self):
        self.header = Label(self.root,text="Login",font=('',35))
        self.header.pack()
        login_frame = Frame(self.root,padx=5,pady=5)
        Label(login_frame,text = 'Roll No: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(login_frame,textvariable = self.lg_roll,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(login_frame,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(login_frame,textvariable = self.lg_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(login_frame,text = ' Login ',bd = 3 ,font = ('',15),padx=5,pady=5,command = self.login).grid()
        Button(login_frame,text = ' Register ',bd = 3 ,font = ('',15),padx=5,pady=5,command = self.register_screen).grid(row=2,column=1)
        self.login_frame= login_frame
        self.login_frame.pack()
        
        
    
    def register_screen(self):
        reg_frame = Frame(self.root)
        reg_frame = Frame(self.root,padx =5,pady = 5)
        Label(reg_frame,text = 'Name: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(reg_frame,textvariable = self.rg_name,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(reg_frame,text = 'Password: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(reg_frame,textvariable = self.rg_password,bd = 5,font = ('',15)).grid(row=1,column=1)
        Label(reg_frame,text = 'Roll No: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(reg_frame,textvariable = self.rg_roll,bd = 5,font = ('',15)).grid(row=2,column=1)
        Label(reg_frame,text = 'Whatsapp_No: ',font = ('',20),pady=5,padx=5).grid(sticky = W)
        Entry(reg_frame,textvariable = self.rg_wapp_number,bd = 5,font = ('',15)).grid(row=3,column=1)
        Button(reg_frame,text = 'Register',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.registration).grid()
        Button(reg_frame,text = 'Back',bd = 3 ,font = ('',15),padx=5,pady=5,command=self.login_screen).grid(row=4,column=1)
        self.reg_frame = reg_frame
        
        self.rg_roll.set('')
        self.rg_password.set('')
        self.rg_name.set('')
        self.rg_wapp_number.set('')
        self.login_frame.pack_forget()
        self.header['text'] = 'Registration'
        self.reg_frame.pack()
    
    def login_screen(self):
        self.lg_roll.set('')
        self.lg_password.set('')
        self.reg_frame.pack_forget()
        self.header["text"] = "Login"
        self.login_frame.pack()
        
    def registration(self):
        ret = self.user_ds.register(
            self.rg_roll.get(),
            self.rg_password.get(),
            self.rg_name.get(),
            self.rg_wapp_number.get()
        )
        if ret :
            messagebox.showinfo("Success","successfully registered")
        else:
            messagebox.showerror("Error","{} already exists".format(self.rg_roll.get()))
    
    def login(self):
        res  = self.user_ds.check_cred(self.lg_roll.get(),self.lg_password.get())
        if res.get("success") == False:
            messagebox.showerror("Error",res.get("msg"))
        else:
            self.root.destroy()
            #home_screen()
    
    
        
        
        
#root = tkinter.Tk()
#root.title('Quiz')
#root.geometry('700x600')

#root.mainloop()

l = login()