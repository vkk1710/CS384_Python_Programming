import csv
import os
import re


def course():
    # Read csv and process
    with open('studentinfo_cs384.csv','r') as file :
        dict_reader = csv.DictReader(file)
        field = ['id','full_name','country','email','gender','dob','blood_group','state']
        course_dict={'01':'btech','11':'mtech','12':'msc','21':'phd'}
        first=True
        for row in dict_reader:
            roll = row['id']
            year= roll[:2]
            course = roll[2:4]
            branch = roll[4:6].lower()
            temp = re.findall(r'\d+', roll)
            if(len(roll)!=8 or len(temp)!=2 or len(temp[0])!=4 or len(temp[1])!=2):
               with open('analytics\course\misc.csv','a',newline='') as f :
                   writer = csv.DictWriter(f, fieldnames = field)
                   if(first):
                       writer.writeheader()
                       first=False
                   writer.writerow({'id':row['id'],'full_name':row['full_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']})       
            
            elif(not(os.path.exists(os.path.join(r'analytics\course',branch,course_dict[course],year+'_'+branch+'_'+course_dict[course]+'.csv')))):
                path = os.path.join(r'analytics\course',branch,course_dict[course])
                try :
                    os.makedirs(path)
                except :
                    pass
                with open(os.path.join(path,year+'_'+branch+'_'+course_dict[course]+'.csv'),'a',newline='') as f :
                    writer = csv.DictWriter(f, fieldnames = field)
                    writer.writeheader()
                    writer.writerow({'id':row['id'],'full_name':row['full_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']})
                    
            else:
                path = os.path.join(r'analytics\course',branch,course_dict[course])
                with open(os.path.join(path,year+'_'+branch+'_'+course_dict[course]+'.csv'),'a',newline='') as f :
                        writer = csv.DictWriter(f, fieldnames = field)
                        writer.writerow({'id':row['id'],'full_name':row['full_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']})
                       
def country():
    # Read csv and process
    with open('studentinfo_cs384.csv','r') as file :
        dict_reader = csv.DictReader(file)
        field = ['id','full_name','country','email','gender','dob','blood_group','state']
        for row in dict_reader:
            country = row['country'].lower()
            if(not(os.path.exists(os.path.join(r'analytics\country',country+'.csv')))):
                with open(os.path.join(r'analytics\country',country+'.csv'),'a',newline='') as f :
                    writer = csv.DictWriter(f, fieldnames = field)
                    writer.writeheader()
                    writer.writerow({'id':row['id'],'full_name':row['full_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']})    
            else:
                with open(os.path.join(r'analytics\country',country+'.csv'),'a',newline='') as f:
                    writer = csv.DictWriter(f, fieldnames = field)
                    writer.writerow({'id':row['id'],'full_name':row['full_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']}) 

def email_domain_extract():
    # Read csv and process
    pass


def gender():
    # Read csv and process
     with open('studentinfo_cs384.csv','r') as file :
        dict_reader = csv.DictReader(file)
        field = ['id','full_name','country','email','gender','dob','blood_group','state']
        for row in dict_reader:
            Gender = row['gender'].lower()
            if(not(os.path.exists(os.path.join(r'analytics\gender',Gender+'.csv')))):
                with open(os.path.join(r'analytics\gender',Gender+'.csv'),'a',newline='') as f :
                    writer = csv.DictWriter(f, fieldnames = field)
                    writer.writeheader()
                    writer.writerow({'id':row['id'],'full_name':row['full_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']})    
            else:
                 with open(os.path.join(r'analytics\gender',Gender+'.csv'),'a',newline='') as f :
                    writer = csv.DictWriter(f, fieldnames = field)
                    writer.writerow({'id':row['id'],'full_name':row['full_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']})

def dob():
    # Read csv and process
    pass


def state():
    # Read csv and process
    pass


def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass
gender()