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
    pass

def stats_grouping(matrix,groups_list):
    # function to generate the stats_grouping.csv
    pass
    
    
def group_allocation(filename, number_of_groups):
    # Entire Logic 
	# You can add more functions, but in the test case, we will only call the group_allocation() method,
    
    # calling function to generate branch_strength.csv file........
    branch_strength(filename)
          
            
    
filename = "Btech_2020_master_data.csv"
number_of_groups = 12 
group_allocation(filename, number_of_groups)