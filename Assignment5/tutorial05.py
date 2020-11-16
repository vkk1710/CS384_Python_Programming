import os
import re

os.chdir('F:/Acads/5th sem/Python CS384/CS384_1801CE31/Assignment5')
def rename_FIR(folder_name):
    print('Enter Season number padding : ')
    season_pad = int(input())
    print('Enter Episode number padding : ')
    episode_pad = int(input())
    
    i=0
    old_title=[]
    new_title=[]
    extension_list=[]
    for f in os.scandir('Subtitles/'+folder_name):
        if(f.is_file()):
            split=re.findall(r'\d+',f.name)
            episode_num = str(split[0])
            extension = f.name[-4:]
            extension_list.append(extension)
            if(episode_pad>len(episode_num)):
                for i in range(episode_pad-len(episode_num)):
                    episode_num = '0' + episode_num
            new_name = folder_name + ' - ' + 'Episode ' + episode_num
            old_title.append(f.name)
            new_title.append(new_name)
    for i in zip(old_title,new_title,extension_list):
        new_name = i[1]
        old_name = i[0]
        extension = i[2]
        if(os.path.exists('Subtitles/'+folder_name+'/'+new_name+extension)):
            os.rename('Subtitles/'+folder_name+'/'+old_name, 'Subtitles/'+folder_name+'/'+new_name+'_copy'+extension)
        else:
            os.rename('Subtitles/'+folder_name+'/'+old_name, 'Subtitles/'+folder_name+'/'+new_name+extension)            
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