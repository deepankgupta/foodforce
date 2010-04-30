import pickle
import os

def write_data():
    
    num_of_storyboards = 0
    output = open('storyboard_list.pkl','wb')
    
    for storyboard_name in os.listdir(os.path.join("storyboards")):
        if storyboard_name == '.svn':
            continue
        num_of_storyboards = num_of_storyboards + 1
    pickle.dump(num_of_storyboards,output)
    storyboard_no = 1
    for storyboard_name in os.listdir(os.path.join("storyboards")):
        if storyboard_name == '.svn':
            continue
        storyboard = [storyboard_no,str(storyboard_name)]
        pickle.dump(storyboard,output)
        storyboard_no +=1
        
        
    output.close()
    
write_data()