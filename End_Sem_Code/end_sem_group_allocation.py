import pandas as pd
import os

os.chdir('F:/Acads/5th sem/Python CS384/CS384_2020_skeleton/End_Sem_Code')

def branch_strength(filename):
    try:
        df = pd.read_csv(filename)
        df['branch'] = df['Roll'].apply(lambda x:x[4:6])
        branch_str = df['branch'].value_counts()
        strength = list(branch_str)
        branch = list(branch_str.index)
        data = {"BRANCH_CODE": branch,"STRENGTH": strength} 
        branch_df = pd.DataFrame(data).sort_values(by=['STRENGTH', 'BRANCH_CODE'],ascending = (False, True))
        branch_df.set_index('BRANCH_CODE',inplace=True) 
        print(branch_df)
        branch_df.to_csv('branch strength.csv')
    except:
        pass

def branch_files(filename):
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
    totals_list = []
    group_dist_list = []
    for i in matrix:
        if(i=='left'):
            continue
        totals_list.append(sum(list(matrix[i].values())))
        group_dist_list.append(matrix[i])
    df1 = pd.DataFrame({'group':groups_list,'total':totals_list})
    df2 = pd.DataFrame(group_dist_list)
    df_final = pd.concat([df1,df2],axis=1)
    df_final.set_index('group',inplace=True)
    df_final.to_csv('stats_grouping.csv')
    print(df_final)
    
    
def group_allocation(filename, number_of_groups):
    # Entire Logic 
	# You can add more functions, but in the test case, we will only call the group_allocation() method,
    #branch_strength(filename)
    #branch_files(filename)
    
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
    
    cnt_dict = {}
    columns = pd.read_csv(filename).columns
    groups_list=[]
    for i in matrix:
        if(i=='left'):
            continue
        d = matrix[i]
        grp_df = pd.DataFrame(columns = columns)
        grp_df.set_index(columns[0])
        for br in d:
            num = d[br]
            if br in cnt_dict.keys():
                cnt_dict[br] += num
            else:
                cnt_dict[br] = num
            count = cnt_dict[br]
            batch_df = pd.read_csv(br+'.csv')[count-num:count]
            grp_df = pd.concat([grp_df,batch_df])
            
        grp_df['branch'] = grp_df['Roll'].apply(lambda x:x[4:6])
        grp_df['roll_num'] = grp_df['Roll'].apply(lambda x:int(x[6:]))
        grp_df = grp_df.sort_values(by=['branch', 'roll_num'])
        grp_df.drop(columns = ['branch','roll_num'],inplace=True)
        
        if(i<10):
            grp_df.set_index('Roll',inplace=True) 
            grp_df.to_csv('Group_G0'+str(i)+'.csv')
            groups_list.append('Group_G0'+str(i))
        else:
            grp_df.set_index('Roll',inplace=True) 
            grp_df.to_csv('Group_G'+str(i)+'.csv')
            groups_list.append('Group_G'+str(i))
       
    stats_grouping(matrix,groups_list)        
            
    
filename = "Btech_2020_master_data.csv"
number_of_groups = 12 
group_allocation(filename, number_of_groups)