import sqlite3
import csv
import hashlib
import pandas as pd
import re

class database:
    def __init__(self):
        self.conn = sqlite3.connect("project1_quiz_cs384")
        self.conn.execute('''CREATE TABLE IF NOT EXISTS project1_registration(username VARCHAR(10),password VARCHAR(45),name VARCHAR(30),whatsapp_number VARCHAR(10))''')
        self.conn.commit()
        
    def get_user(self,roll):
        found = True
        self.cur = self.conn.cursor()
        data = self.cur.execute('''SELECT * FROM project1_registration WHERE username=:roll''',{"roll":roll}).fetchone()
        if data == None:
            found = False
        self.cur.close()
        return {"found" : found,"data" : data}
    
    def register(self,roll,text_password,name,whatsapp_number):
        if self.get_user(roll)["found"]:
            return False
        self.pass_hash = hashlib.md5(text_password.encode()).hexdigest()
        self.conn.execute('''INSERT INTO project1_registration(username,password,name,whatsapp_number) VALUES(?,?,?,?)''',
        [
            (roll),
            (self.pass_hash),
            (name),
            (whatsapp_number)
        ])
        self.conn.commit()
        return True
    
    def check_cred(self,roll,password):
        found = True
        msg = "Logged in"
        hash_pass = hashlib.md5(password.encode()).hexdigest()
        res = self.get_user(roll)
        if res['found'] == False:
            found = False
            msg = "{} not found".format(roll)
        if found and res['data'][1] != hash_pass:
            msg = "invalid Password"
            found = False
        return {"success" : found,"msg" : msg}

def get_quiz(file):
    reader = csv.DictReader(open(f'quiz_wise_questions/{file}',"r"))
    q_time = float(reader.fieldnames[-1].split("time=")[1][:-1])
    quiz_df = pd.read_csv(f'quiz_wise_questions/{file}')
    questions_dict = {}
    question = quiz_df['question']
    choices = quiz_df[['option1','option2','option3','option4']]
    correct_opt = quiz_df['correct_option']
    marks_correct = quiz_df['marks_correct_ans']
    marks_wrong = quiz_df['marks_wrong_ans']
    compulsion = quiz_df['compulsory']
    ind = list(quiz_df.index)
    for i in ind:
        d = {}
        d['question'] = question[i]
        d['choices'] = list(choices.iloc[i])
        d['correct_option'] = correct_opt[i]
        d['marks_correct_ans'] = marks_correct[i]
        d['marks_wrong_ans'] = marks_wrong[i]
        d['compulsion'] = compulsion[i]
        questions_dict[i+1] = d
    return {"questions" : questions_dict,"time" : q_time*60}