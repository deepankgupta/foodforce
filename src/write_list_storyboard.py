import pickle
import os

def write_data():
    
    num_of_storyboards = 0
    output = open('storyboard_list.pkl','wb')
    
    for item in os.listdir(os.path.join("storyboards")):
        num_of_storyboards = num_of_storyboards + 1
    pickle.dump(num_of_storyboards,output)
    
    for item in os.listdir(os.path.join("storyboards")):
        pickle.dump(str(item),output)
        
    output.close()
    
write_data()