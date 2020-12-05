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
            

class main_screen:
    def __init__(self,roll,name):
        self.roll = roll
        self.name = name
        self.root = Tk()
        self.root.config(background = "#ffffff")
        self.root.geometry('500x500')
        self.choose_quiz()
        self.root.mainloop()
    
    ######## Function to choose which quiz to attempt............

    def choose_quiz(self):
        Label(self.root,text="Which quiz do you want to attend?",background = "#ffffff",font=("Goudy Old Style", 20, "bold"),pady=30,padx=20).pack()
        quiz = StringVar()
        print(quiz.get())
        for i in os.listdir("./quiz_wise_questions"):
            if i[-4:] == '.csv':
                Radiobutton(self.root,text=i[:-4],background = "#ffffff",variable=quiz,value=i,anchor="e",font=(None, 16), justify=LEFT,height=2, width=2).pack()
        Button(self.root,text="OK",background = "#ffffff",font=(None, 16),bd = 3,command = lambda : [self.root.destroy(),self.start_quiz(quiz.get())]).pack()
    
    ######## Timer function............

    def timer(self):
            #min,sec  = divmod(self.max_time,60)
            min = int(self.max_time // 60)
            sec = int(self.max_time % 60)
            self.timer_lb["text"] = f'{min}:{sec}'
            if int(self.max_time) == 0:
                self.channel.put("Stop")
                print("time out.........Quiz Over!")
                self.end_quiz()
                return
            self.timer_lb.after(1000,self.timer)
            self.max_time-=1
            
    def start_quiz(self,quiz):
        root = Tk()
        root.config(background = "#ffffff")
        root.geometry('700x600')
        self.user_scores_db = users_marks_database()

        ######## Shortcut trigger functions............

        def goto_event(event):
            self.__go_to()
        root.bind("<Control_L><Alt_L><G>",goto_event)
        
        def unatt_event(event):
            self.__get_unattem()
        root.bind("<Control_L><Alt_L><U>",unatt_event)
        
        def submit_event(event):
            self.submit()
        root.bind("<Control_L><Alt_L><F>",submit_event)
        
        self.filename = quiz
        self.quiz_details = datamanager.get_quiz(self.filename)
        info_frame = Frame(root,background = "#ffffff")
        info_frame.pack(side = TOP)
        self.channel = queue.Queue()
        self.max_time = self.quiz_details["time"]
        
        Label(info_frame, text = "Time Remaining (min : sec) : ",font = ('',17, 'bold'),background = "#ffffff", pady=20,padx=20).grid(row = 0, sticky = W)
        self.timer_lb = Label(info_frame,text="",font = ('',17),background = "#ffffff",)
        self.timer_lb.grid(row = 0, column = 1)
        thread = threading.Thread(target=self.timer)
        thread.start()
        Label(info_frame, text = "Name : ",background = "#ffffff",font=(None, 15, 'bold'),pady=10,padx=20).grid(row = 1, sticky = W)
        Label(info_frame, text = self.name,background = "#ffffff",font=(None, 15)).grid(row = 1, column = 1)
        Label(info_frame, text = "Roll : ",background = "#ffffff",font=(None, 15, 'bold'),pady=10,padx=20).grid(row = 2, sticky = W)
        Label(info_frame, text = self.roll,background = "#ffffff",font=(None, 15)).grid(row = 2, column = 1)

        ######## Buttons for Unattempted questions, Go To Question, Export database into Quiz CSVs............

        Button(info_frame, text = "Unattempted Questions List",bd = 3,background = "#ffffff",font=(None, 10,'bold'),command=self.__get_unattem).grid(row = 3, sticky = W)
        Button(info_frame, text = "Goto Question Number",bd = 3,background = "#ffffff",font=(None, 10,'bold'),command=self.__go_to).grid(row = 3, column = 1)
        Button(info_frame, text = "Export into CSV",bd = 3,background = "#ffffff",font=(None, 10,'bold'),justify=LEFT,command = self.user_scores_db.export_to_csv).grid(row = 4, sticky = W)
   
        def export_event(event):
            self.user_scores_db.export_to_csv()
            
        root.bind("<Control_L><Alt_L><E>",export_event)
        
        self.info_frame = info_frame
        ques_num =  self.quiz_details["questions"].keys()
        self.response = {key:value for key,value in zip(ques_num,[-1]*len(self.quiz_details["questions"]))}
        
        self.ques_frame = Frame(root,background="#ffffff",padx=40,pady=40)
        self.ques_frame.pack()
        self.q_num = 1
        self.ques,self.opts = self.questionset(self.q_num)
        self.display_q(self.q_num)
        self.next_but = Button(self.ques_frame,bd = 3, text = "Save & Next",font=(None, 10,'bold'),background="#ffffff",command=self.next_ques)
        self.next_but.pack(pady = 10, padx = 5, side = LEFT)
        self.submit_but = Button(self.ques_frame,bd = 3, text = "Submit",font=(None, 10,'bold'),background="#ffffff",command = self.submit)
        self.submit_but.pack(pady = 10, padx = 5)
        self.quiz_screen = root
        root.mainloop()
        
    ######## Function to get the next question............

    def next_ques(self):
        if self.q_num >= len(self.quiz_details["questions"]):
            messagebox.showwarning("Warning", "If completed the quiz, Press Submit to proceed")
        else:
            self.response[self.q_num] = self.opt_selected.get()
            self.q_num += 1
            self.opt_selected.set(self.response[self.q_num])

            self.display_q(self.q_num)

    ######## Function to submit the quiz............

    def submit(self):
        self.response[self.q_num]=self.opt_selected.get()
        self.end_quiz()

            


l = login()