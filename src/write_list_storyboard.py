import pickle
import os

def write_data():
    
    num_of_storyboards = 0
    output = open('storyboard_list.pkl','wb')
    
    for item in os.listdir(os.path.join("storyboards")):
        if item == '.svn':
            continue
        num_of_storyboards = num_of_storyboards + 1
    pickle.dump(num_of_storyboards,output)
    index = 1
    for item in os.listdir(os.path.join("storyboards")):
        if item == '.svn':
            continue
        storyboard = [index,str(item)]
        pickle.dump(storyboard,output)
        index +=1
        
        
    output.close()
    
write_data()