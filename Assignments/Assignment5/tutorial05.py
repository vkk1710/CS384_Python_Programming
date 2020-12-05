import os
import re

def rename_FIR(folder_name):
    print('Enter Season number padding : ')
    season_pad = int(input())
    print('Enter Episode number padding : ')
    episode_pad = int(input())
    
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


def rename_Game_of_Thrones(folder_name):
    print('Enter Season number padding : ')
    season_pad = int(input())
    print('Enter Episode number padding : ')
    episode_pad = int(input())
    
    old_title=[]
    new_title=[]
    extension_list=[]
    for f in os.scandir('Subtitles/'+folder_name):
        if(f.is_file()):
            split=re.findall(r'\d+',f.name)
            season_num = str(split[0])
            episode_num = str(int(split[1]))
            pattern = re.compile(r'- [A-Za-z ]+')
            episode_name = re.search(pattern, f.name)[0][2:]
            extension = f.name[-4:]
            extension_list.append(extension)
            if(episode_pad>len(episode_num)):
                for i in range(episode_pad-len(episode_num)):
                    episode_num = '0' + episode_num
            if(season_pad>len(season_num)):
                for i in range(season_pad-len(season_num)):
                    season_num = '0' + season_num
            new_name = folder_name + ' - ' + 'Season ' + season_num + ' Episode ' + episode_num + ' - ' + episode_name
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
            

def rename_Sherlock(folder_name):
    print('Enter Season number padding : ')
    season_pad = int(input())
    print('Enter Episode number padding : ')
    episode_pad = int(input())
    
    old_title=[]
    new_title=[]
    extension_list=[]
    for f in os.scandir('Subtitles/'+folder_name):
        if(f.is_file()):
            split=re.findall(r'\d+',f.name)
            season_num = str(split[0])
            episode_num = str(split[1])
            extension = f.name[-4:]
            extension_list.append(extension)
            if(episode_pad>len(episode_num)):
                for i in range(episode_pad-len(episode_num)):
                    episode_num = '0' + episode_num
            if(season_pad>len(season_num)):
                for i in range(season_pad-len(season_num)):
                    season_num = '0' + season_num
            if(season_pad==1):
                season_num = int(season_num)
                season_num = str(season_num)
            if(episode_pad==1):
                episode_num = int(episode_num)
                episode_num = str(episode_num)
            new_name = folder_name + ' - ' + 'Season ' + season_num + ' Episode ' + episode_num
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
    

def rename_Suits(folder_name):
    print('Enter Season number padding : ')
    season_pad = int(input())
    print('Enter Episode number padding : ')
    episode_pad = int(input())
    
    old_title=[]
    new_title=[]
    extension_list=[]
    for f in os.scandir('Subtitles/'+folder_name):
        if(f.is_file()):
            split=re.findall(r'\d+',f.name)
            season_num = str(split[0])
            episode_num = str(int(split[1]))
            episode_name = re.split(r'\.720p|\.480p|\.en|\.HDTV|TBA',f.name)[0]
            episode_name = re.split(r'- ',episode_name)[-1]
            extension = f.name[-4:]
            extension_list.append(extension)
            
            if(episode_pad>len(episode_num)):
                for i in range(episode_pad-len(episode_num)):
                    episode_num = '0' + episode_num
            if(season_pad>len(season_num)):
                for i in range(season_pad-len(season_num)):
                    season_num = '0' + season_num
                
            new_name = folder_name + ' - ' + 'Season ' + season_num + ' Episode ' + episode_num 
            if(episode_name!=''):
               new_name = folder_name + ' - ' + 'Season ' + season_num + ' Episode ' + episode_num  + ' - ' + episode_name
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


def rename_How_I_Met_Your_Mother(folder_name):
    print('Enter Season number padding : ')
    season_pad = int(input())
    print('Enter Episode number padding : ')
    episode_pad = int(input())
    
    old_title=[]
    new_title=[]
    extension_list=[]
    repeat_dict = {}
    for f in os.scandir('Subtitles/'+folder_name):
        if(f.is_file()):
            split = re.split(r'\s[-]\s',f.name)[1]
            split = re.split(r'x',split)
            season_num = split[0]
            episode_num = split[1]
            episode_name = re.split(r'\.720p|\.1080p|\.en|\.HDTV|\.480p',f.name)[0]
            episode_name = re.split(r'- ',episode_name)[-1].strip()
            extension = f.name[-4:]
            extension_list.append(extension)
            
            if(season_pad>len(season_num)):
                for i in range(season_pad-len(season_num)):
                    season_num = '0' + season_num
            if(len(episode_num.split('-'))==1):
                episode_num = str(int(episode_num))
                if(episode_pad>len(episode_num)):
                    for i in range(episode_pad-len(episode_num)):
                        episode_num = '0' + episode_num 
            else:
                p1 = str(int(episode_num.split('-')[0]))
                p2 = str(int(episode_num.split('-')[1]))
                if(episode_pad>len(p1)):
                    for i in range(episode_pad-len(p1)):
                        p1 = '0' + p1
                if(episode_pad>len(p2)):
                    for i in range(episode_pad-len(p2)):
                        p2 = '0' + p2
                episode_num = p1+'-'+p2
                
            new_name = folder_name + ' - ' + 'Season ' + season_num + ' Episode ' + episode_num + ' - ' + episode_name
            old_title.append(f.name)
            new_title.append(new_name)
            
            if(new_name+extension in repeat_dict):
                repeat_dict[new_name+extension] += 1
            else:
                repeat_dict[new_name+extension] = 1
      
    for i in zip(old_title,new_title,extension_list):
        new_name = i[1]
        old_name = i[0]
        extension = i[2]
        if(os.path.exists('Subtitles/'+folder_name+'/'+new_name+extension)):
            os.rename('Subtitles/'+folder_name+'/'+old_name, 'Subtitles/'+folder_name+'/'+new_name+'('+str(repeat_dict[new_name+extension]-1)+')'+extension)
            repeat_dict[new_name+extension] -= 1
        else:
            os.rename('Subtitles/'+folder_name+'/'+old_name, 'Subtitles/'+folder_name+'/'+new_name+extension)                    


########### Calling the series renaming functions according to the user input...........

########### Please set the current working directory to this assignment 5 directory before running the code

series_list = os.listdir('Subtitles')

print('Menu of Series :\n')

series_dict = {}
for i,name in enumerate(series_list):
    print(f'{i+1}. {name}')  
    series_dict[i+1] = name
print('\n')


print('Please choose an option from the menu above : ')

series_num =  int(input())
while(series_num not in [1,2,3,4,5]):
    print('Please choose a valid option!!')
    print('Please choose an option from the menu above : ')
    series_num =  int(input())

series_name = series_dict[series_num].lower()

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
