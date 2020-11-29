import pandas as pd
import os

# save this .py file along with Btech_2020_master_data.csv in the current working directory

def branch_strength(filename):
    # function that generates the branch_strength.csv
    try:
        df = pd.read_csv(filename)
        df['branch'] = df['Roll'].apply(lambda x:x[4:6])
        branch_str = df['branch'].value_counts()
        strength = list(branch_str)
        branch = list(branch_str.index)
        data = {"BRANCH_CODE": branch,"STRENGTH": strength} 
        branch_df = pd.DataFrame(data).sort_values(by=['STRENGTH', 'BRANCH_CODE'],ascending = (False, True))
        branch_df.set_index('BRANCH_CODE',inplace=True) 
        branch_df.to_csv('branch strength.csv')
    except:
        pass

def branch_files(filename):
    # function to generate branch wise csv files
    df = pd.read_csv(filename)
    df['branch'] = df['Roll'].apply(lambda x:x[4:6])
    df['roll_num'] = df['Roll'].apply(lambda x:int(x[6:]))
    branches = list(df['branch'].value_counts().index)
    for branch in branches:
        br_df = df.loc[df['branch']==branch]
        br_df.sort_values(by='roll_num')
        br_df = br_df[['Roll','Name','Email']]
        br_df.set_index('Roll',inplace=True)
        br_df.to_csv(branch+'.csv')

def stats_grouping(matrix,groups_list):
    # function to generate the stats_grouping.csv
    pass
    
    
def group_allocation(filename, number_of_groups):
    # Entire Logic 
	# You can add more functions, but in the test case, we will only call the group_allocation() method,
    
    # calling function to generate branch_strength.csv file........
    branch_strength(filename)
    
    # calling function to generate branch wise csv files........
    branch_files(filename)
    
    # code for generating the matrix........
    df = pd.read_csv('branch strength.csv')
    branch = list(df['BRANCH_CODE'])
    strength = list(df['STRENGTH'])
    matrix={}
    for i in range(number_of_groups):
        d = {}
        for br,st in zip(branch,strength):
            d[br] = st//number_of_groups
        matrix[i+1] = d
    d={}
    for br,st in zip(branch,strength):
        d[br] = st%number_of_groups
    matrix['left'] = d
    left_dict = matrix['left']
    count = 0
    for i in left_dict :
        rem = left_dict[i]
        for n in range(rem):
            matrix[(count%number_of_groups)+1][i] += 1
            count += 1
            left_dict[i] -= 1     
            
    
filename = "Btech_2020_master_data.csv"
number_of_groups = 12 
group_allocation(filename, number_of_groups)