import csv
import os
import re
import shutil

def del_create_analytics_folder():
    # del the analytics folder including subfolder
    # mkdir the analytics folder (only mkdir)
    shutil.rmtree(r'.\analytics')
    os.mkdir(r'.\analytics')
    pass

def course():
    # Read csv and process
    try:
        shutil.rmtree(r'.\analytics\course')
    except:
        pass
    try:
        os.mkdir(r'.\analytics\course')
    except:
        pass
    with open(r'.\studentinfo_cs384.csv','r') as file :
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
               with open(r'.\analytics\course\misc.csv','a',newline='') as f :
                   writer = csv.DictWriter(f, fieldnames = field)
                   if(first):
                       writer.writeheader()
                       first=False
                   writer.writerow({'id':row['id'],'full_name':row['full_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']})       
            
            elif(not(os.path.exists(os.path.join(r'.\analytics\course',branch,course_dict[course],year+'_'+branch+'_'+course_dict[course]+'.csv')))):
                path = os.path.join(r'.\analytics\course',branch,course_dict[course])
                try :
                    os.makedirs(path)
                except :
                    pass
                with open(os.path.join(path,year+'_'+branch+'_'+course_dict[course]+'.csv'),'a',newline='') as f :
                    writer = csv.DictWriter(f, fieldnames = field)
                    writer.writeheader()
                    writer.writerow({'id':row['id'],'full_name':row['full_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']})
                    
            else:
                path = os.path.join(r'.\analytics\course',branch,course_dict[course])
                with open(os.path.join(path,year+'_'+branch+'_'+course_dict[course]+'.csv'),'a',newline='') as f :
                        writer = csv.DictWriter(f, fieldnames = field)
                        writer.writerow({'id':row['id'],'full_name':row['full_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']})
                       
def country():
    # Read csv and process
    try:
        shutil.rmtree(r'.\analytics\country')
    except:
        pass
    try:
        os.mkdir(r'.\analytics\country')
    except:
        pass
    with open(r'.\studentinfo_cs384.csv','r') as file :
        dict_reader = csv.DictReader(file)
        field = ['id','full_name','country','email','gender','dob','blood_group','state']
        for row in dict_reader:
            country = row['country'].lower()
            if(not(os.path.exists(os.path.join(r'.\analytics\country',country+'.csv')))):
                with open(os.path.join(r'.\analytics\country',country+'.csv'),'a',newline='') as f :
                    writer = csv.DictWriter(f, fieldnames = field)
                    writer.writeheader()
                    writer.writerow({'id':row['id'],'full_name':row['full_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']})    
            else:
                with open(os.path.join(r'.\analytics\country',country+'.csv'),'a',newline='') as f:
                    writer = csv.DictWriter(f, fieldnames = field)
                    writer.writerow({'id':row['id'],'full_name':row['full_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']}) 


def email_domain_extract():
    # Read csv and process
    try:
        shutil.rmtree(r'.\analytics\email_domain')
    except:
        pass
    try:
        os.mkdir(r'.\analytics\email_domain')
    except:
        pass
    with open(r'.\studentinfo_cs384.csv','r') as file :
        dict_reader = csv.DictReader(file)
        field = ['id','full_name','country','email','gender','dob','blood_group','state']
        for row in dict_reader:
            email = row['email'].lower()
            email_domain=re.search(r'@(.+)[.]',email).group(0)
            email_domain=email_domain.split('.')[0][1:]
            if(not(os.path.exists(os.path.join(r'.\analytics\email_domain',email_domain+'.csv')))):
                with open(os.path.join(r'.\analytics\email_domain',email_domain+'.csv'),'a',newline='') as f :
                    writer = csv.DictWriter(f, fieldnames = field)
                    writer.writeheader()
                    writer.writerow({'id':row['id'],'full_name':row['full_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']})    
            else:
                with open(os.path.join(r'.\analytics\email_domain',email_domain+'.csv'),'a',newline='') as f :
                    writer = csv.DictWriter(f, fieldnames = field)
                    writer.writerow({'id':row['id'],'full_name':row['full_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']})

def gender():
    # Read csv and process
    try:
        shutil.rmtree(r'.\analytics\gender')
    except:
        pass
    try:
        os.mkdir(r'.\analytics\gender')
    except:
        pass
    with open(r'.\studentinfo_cs384.csv','r') as file :
        dict_reader = csv.DictReader(file)
        field = ['id','full_name','country','email','gender','dob','blood_group','state']
        for row in dict_reader:
            Gender = row['gender'].lower()
            if(not(os.path.exists(os.path.join(r'.\analytics\gender',Gender+'.csv')))):
                with open(os.path.join(r'.\analytics\gender',Gender+'.csv'),'a',newline='') as f :
                    writer = csv.DictWriter(f, fieldnames = field)
                    writer.writeheader()
                    writer.writerow({'id':row['id'],'full_name':row['full_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']})    
            else:
                 with open(os.path.join(r'.\analytics\gender',Gender+'.csv'),'a',newline='') as f :
                    writer = csv.DictWriter(f, fieldnames = field)
                    writer.writerow({'id':row['id'],'full_name':row['full_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']})

def dob():
    # Read csv and process
    pass            

def state():
    # Read csv and process
    try:
        shutil.rmtree(r'.\analytics\state')
    except:
        pass
    try:
        os.mkdir(r'.\analytics\state')
    except:
        pass
    with open(r'.\studentinfo_cs384.csv','r') as file :
        dict_reader = csv.DictReader(file)
        field = ['id','full_name','country','email','gender','dob','blood_group','state']
        for row in dict_reader:
            State = row['state'].lower()
            if(not(os.path.exists(os.path.join(r'.\analytics\state',State+'.csv')))):
                with open(os.path.join(r'.\analytics\state',State+'.csv'),'a',newline='') as f :
                    writer = csv.DictWriter(f, fieldnames = field)
                    writer.writeheader()
                    writer.writerow({'id':row['id'],'full_name':row['full_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']})    
            else:
                 with open(os.path.join(r'.\analytics\state',State+'.csv'),'a',newline='') as f :
                    writer = csv.DictWriter(f, fieldnames = field)
                    writer.writerow({'id':row['id'],'full_name':row['full_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']})


def blood_group():
    # Read csv and process
    try:
        shutil.rmtree(r'.\analytics\blood_group')
    except:
        pass
    try:
        os.mkdir(r'.\analytics\blood_group')
    except:
        pass
    with open(r'.\studentinfo_cs384.csv','r') as file :
        dict_reader = csv.DictReader(file)
        field = ['id','full_name','country','email','gender','dob','blood_group','state']
        for row in dict_reader:
            blood = row['blood_group'].lower()
            if(not(os.path.exists(os.path.join(r'.\analytics\blood_group',blood+'.csv')))):
                with open(os.path.join(r'.\analytics\blood_group',blood+'.csv'),'a',newline='') as f :
                    writer = csv.DictWriter(f, fieldnames = field)
                    writer.writeheader()
                    writer.writerow({'id':row['id'],'full_name':row['full_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']})    
            else:
                 with open(os.path.join(r'.\analytics\blood_group',blood+'.csv'),'a',newline='') as f :
                    writer = csv.DictWriter(f, fieldnames = field)
                    writer.writerow({'id':row['id'],'full_name':row['full_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']})


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    try:
        os.remove(r'.\analytics\studentinfo_cs384_names_split.csv')
    except:
        pass
    try:
        os.remove(r'.\analytics\studentinfo_cs384_names_split_sorted_first_name.csv')
    except:
        pass
    dict_list=[]
    with open(r'.\studentinfo_cs384.csv','r') as file :
        dict_reader = csv.DictReader(file)
        field = ['id','first_name','last_name','country','email','gender','dob','blood_group','state']
        for row in dict_reader:
            if(not(os.path.exists(os.path.join(r'.\analytics','studentinfo_cs384_names_split.csv')))):
                with open(os.path.join(r'.\analytics','studentinfo_cs384_names_split.csv'),'a',newline='') as f :
                    writer = csv.DictWriter(f, fieldnames = field)
                    writer.writeheader()
                    new_dict = {'id':row['id'],'first_name':row['full_name'].split(' ')[0],'last_name':' '.join(row['full_name'].split(' ')[1:]),'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']}
                    dict_list.append(new_dict)
                    writer.writerow(new_dict)    
            else:
                 with open(os.path.join(r'.\analytics','studentinfo_cs384_names_split.csv'),'a',newline='') as f :
                    writer = csv.DictWriter(f, fieldnames = field)
                    new_dict = {'id':row['id'],'first_name':row['full_name'].split(' ')[0],'last_name':' '.join(row['full_name'].split(' ')[1:]),'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']}
                    dict_list.append(new_dict)
                    writer.writerow(new_dict)
    
    dict_list.sort(key = lambda t : t['first_name'])
    with open(os.path.join(r'.\analytics','studentinfo_cs384_names_split_sorted_first_name.csv'),'a',newline='') as f :
        writer = csv.DictWriter(f, fieldnames = field)
        writer.writeheader()
        row = dict_list[0]
        writer.writerow({'id':row['id'],'first_name':row['first_name'],'last_name':row['last_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']})    
    for row in dict_list[1:]:
        with open(os.path.join(r'.\analytics','studentinfo_cs384_names_split_sorted_first_name.csv'),'a',newline='') as f :
            writer = csv.DictWriter(f, fieldnames = field)
            writer.writerow({'id':row['id'],'first_name':row['first_name'],'last_name':row['last_name'],'country':row['country'],'email':row['email'],'gender':row['gender'],'dob':row['dob'],'blood_group':row['blood_group'],'state':row['state']})    

