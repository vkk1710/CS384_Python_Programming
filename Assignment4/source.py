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
    pass

# Function execution............

individual()

