import pandas as pd
import csv
import os

def individual():
    data = pd.read_csv('acad_res_stud_grades.csv')
    gp = data.groupby(['roll']) 
    
    for name,df in gp:
        
        if(os.path.exists('grades/'+name+'_individual.csv')):
            continue
    
        roll_df = df[['sub_code','total_credits','sub_type','credit_obtained','sem']]
        roll_df.rename(columns={'sub_code': 'Subject', 'total_credits': 'Credits', 'sub_type':'Type', 'credit_obtained':'Grade', 'sem':'Sem'},inplace=True)
        
        if(roll_df['Grade'].isnull().sum()!=0):
            with open(os.path.join('grades','misc.csv'), 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Roll: '+name])
                writer.writerow(['Semester Wise Details'])
                file.close()
            roll_df.to_csv(os.path.join('grades', 'misc.csv'),index=False,mode='a')
            continue
            
        with open(os.path.join('grades',name+'_individual.csv'), 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Roll: '+name])
            writer.writerow(['Semester Wise Details'])
            file.close()
        roll_df.to_csv(os.path.join('grades', name+'_individual.csv'),index=False,mode='a')
        
def overall():
    grades_to_int = {'AA':10,'AB':9,'BB':8,'BC':7,'CC':6,'CD':5,'DD':4,'F':0,'I':0}
    for i in os.listdir('grades'):
        roll = i.split('_')[0]
        if(roll=='misc.csv'):
            continue
        check = i.split('_')[1].split('.')[0]
        if(check!='individual' or os.path.exists(os.path.join('grades',roll+'_overall.csv'))):
            continue
        with open(os.path.join('grades',roll+'_overall.csv'), 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Roll: '+roll])
            file.close()
        
        data = pd.read_csv(os.path.join('grades',i),skiprows=2)
        data['Grade'] = data['Grade'].apply(lambda x:grades_to_int[x])    
        gp = data.groupby(['Sem'])
        CPI=[]
        tot_credits=[]
        sem_credits=[]
        semester=[]
        SPI=[]
        total_credits=0
        for sem,sem_df in gp:
            semester.append(sem)
            tot_sem_credits = sem_df['Credits'].astype(int).sum()
            sem_credits.append(tot_sem_credits)
            total_credits += tot_sem_credits
            spi = (sem_df['Credits'].astype('int')*sem_df['Grade']).sum()/tot_sem_credits
            if(len(CPI)==0):
                cpi=spi
            else:
                cpi = (cpi*tot_credits[-1] + spi*sem_credits[-1])/total_credits
            SPI.append(round(spi,2))
            CPI.append(round(cpi,2))
            tot_credits.append(total_credits)  
        details = {
                'Semester': semester,
                'Semester Credits': sem_credits,
                'Semester Credits Cleared':sem_credits,
                'SPI':SPI,
                'Total Credits':tot_credits,
                'Total Credits Cleared':tot_credits,
                'CPI':CPI
            }
        df = pd.DataFrame(details)
        df.to_csv(os.path.join('grades', roll+'_overall.csv'),index=False,mode='a')

# Function execution............


individual()
overall()

