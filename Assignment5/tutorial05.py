import os
import re

def rename_FIR(folder_name):
    # rename Logic
    pass
    

def rename_Game_of_Thrones(folder_name):
    # rename Logic 
    pass
    

def rename_Sherlock(folder_name):
    # rename Logic
    pass
    

def rename_Suits(folder_name):
    # rename Logic
    pass
    

def rename_How_I_Met_Your_Mother(folder_name):
    # rename Logic
    pass

print('Enter the Main Title of the Web Series : ')
series_name = input().lower()
if(series_name == 'FIR'.lower()):
    rename_FIR('FIR')
elif(series_name == 'Game of Thrones'.lower()):
    rename_Game_of_Thrones('Game of Thrones')
elif(series_name == 'How I Met Your Mother'.lower()):
    rename_How_I_Met_Your_Mother('How I Met Your Mother')
elif(series_name == 'Sherlock'.lower()):
    rename_Sherlock('Sherlock')
elif(series_name == 'Suits'.lower()):
    rename_Suits('Suits')
else:
    print('Entered series name is not present in the current database!!')