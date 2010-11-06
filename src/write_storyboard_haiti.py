import pickle
flag = 2
list_file = open('storyboard_list.pkl')
pickle.load(list_file)
storyboard_name = None
while storyboard_name == None:
    storyboard = pickle.load(list_file)
    if flag == storyboard[0]:
        storyboard_name = storyboard[1]

def write_data():
    
    output = open('storyboards/'+str(storyboard_name)+'/storyboard.pkl','wb')

    #Introduction data
    text = 'Haiti is a Carribbean country.Along with the Dominican Republic, it occupies the island of Hispaniola, in the Greater Antillean archipelago.The total area of Haiti is 27,750 square kilometres (10,714 sq mi) and its capital is Port-au-Prince. It was the first independent nation in Latin America and the first black-led republic in the world when it gained independence as part of a successful slave rebellion in 1804.'
    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    action = [4,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    chatText = ['Gilbert Fernandez','The city of Haiti has been struck by a catastrophic earthquake of magnitude 7.0',
                'Stevenson Gorbachev','Many notable landmarks such as Presidential Palace,National Assembly ,Port-au-Prince Cathedral,the main jail are completely destroyed.Many public figures are also the victims of this earthquake',
                'Gilbert Fernandez','Haiti is not self-sufficient to recover from this disaster',
                'Stevenson Gorbachev','We have asked for help from our neighbouring countries.I hope we will be able to get through these dark times with their support']
    
    action = [1,[chatText,str(storyboard_name)+'/images/chat images/earthquake_st.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    text = 'Haiti has been struck by an earthquake which has destroyed most of the buildings and severly deteriorated the condition of the city.Various teams has been sent by different countries to take care of the situation and help in any way they can.You being the head of the city have to work in collaboration with all the teams sent for your aid and ensure that the peace of the city is restored.'
    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    #Mission 1
    chatText = ['Stevenson Gorbachev','The earthquake has destroyed everything.',
                'Tony Peralta','At this point of time it is necessary that the survivors be located or people who cant be accessed due to blocking of roads be supplied with food and medicines.',
                'Ragnar Stefansson','The roads to major portions of the city are blocked and we have started working on it but it will take us some days to make a proper way',
                'Stevenson Gorbachev','Till then,something must be done for the survivors.',
                'Tony Peralta','The city also need more hospitals , as only two fully functional hospitals are left in the city and they are overcrowded.There are hundreds of injured people.']
    
    
    action = [1,[chatText,str(storyboard_name)+'/images/chat images/haiti.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'The mission is to provide food and medicinal facilities to the survivors.Increase the progress bars of nutrition and health to 30% within a time span of 2 weeks'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HEALTH',0]
    condnlist = [condn1]
    condnGlobal = ['NOR',14,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'You were not able to maintain the bars above 30%.You failed to save the people .You must retry this level to go to the next level'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HEALTH',30]
    condn2 = [False,3,'','','>=','NUTRITION',30]
    condnlist = [condn1,condn2]
    condnGlobal = ['NOR',1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'You have succeded in taking the first step towards resurrection of the town'
    
    action = [9,text]
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
    
    action = [2,'']
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
    
    text = 'You were not able to maintain the bars above 30%.You failed to save the people .You must retry this level to go to the next level'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    
    #Mission 2
    
    chatText = ['Tony Peralta','Large amounts of food supplies have been collected in Poet-au-prince and a large number of mobile health care facilities sent by various countries are working on the injured people',
                'Ragnar Stefansson','About 90% of the buildings in the city have been destroyed and people are living in overcrowded houses.Something must be done',
                'Stevenson Gorbachev','We must start building more houses for the people but we must also ensure that the progress made so far should be maintained and not be wasted.']
    
    action = [1,[chatText,str(storyboard_name)+'/images/chat images/haiti.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'The mission is to provide proper housing to the people of the village.Increase the progress bar housing to 40% ,keeping the progress bars for nutrition and health above 30 % .This mission should be completed in a span of 1 month.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','NUTRITION',30]
    condn2 = [False,3,'','','>=','HEALTH',30]
    condnlist = [condn1,condn2]
    condnGlobal = ['NOR',30,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'You failed to complete this mission.You have to complete this to go to the next level'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HOUSING',40]
    condnlist = [condn1]
    condnGlobal = ['NOR',1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
                
    text  = 'You have provided proper housing to the people of your town.'
    
    action = [2,'']
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
    
    text = 'You failed to complete this mission.You have to complete this to go to the next level '
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    
    #Mission 3
    
    chatText = ['Gilbert Fernandez','It is an essential part of the recovery plan that people should be employed and they should start earning again',
                'Ragnar Stefansson','People have started living in their own homes and the reconstruction process is proceeding at a fast pace',
                'Stevenson Gorbachev','The people of the city need to be trained, so that they can start feeding themselves.They should become independent as the food supplies will not last for a long time.',
                'Gilbert Fernandez','We are planning to launch a programme so as to provide employment to the people.']
    
    action  = [1,[chatText,str(storyboard_name)+'/images/chat images/haiti.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'This time you have to train the people so that they can start a normal life again.Increase the progress bar ,training to 40% by building workshops and also make sure that the nutrition and health bars are above 30% and housing bar above 40%.The time limit for this mission is 1 month'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HEALTH',30]
    condn2 = [False,3,'','','>=','NUTRITION',30]
    condn3 = [False,3,'','','>=','HOUSING',40]
    condnlist = [condn1,condn2,condn3]
    condnGlobal = ['NOR',30,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'You have lost this level.Try again'
    
    action = [8,text]
    actionData  = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','TRAINING',40]
    condnlist = [condn1]
    condnGlobal = ['NOR',1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'You have created employment for the people and have made them self-sufficient.Congratulations'
    
    action = [9,text]
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
    
    action = [2,'']
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
    
    text = 'You have lost this level.Try again'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    #Mission 4
    
    chatText = ['Stevenson Gorbachev','Due to this earthquake the education system of the city have totally collapsed.',
                'John Tremblay','It is very essential for the future that the children be trained and be taught from very beginning.',
                'Gilbert Fernandez','The city must also have sound monetary savings in order to ensure that these kind of calamities can be handled in a much effective way .']
    
    action = [1,[chatText,str(storyboard_name)+'/images/chat images/haiti.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Now all the basic services of the village has been restored ,so it is your job to keep them running.Increase the progress bar of education and training to 60% and in the next 1 month none of the bars should drop below 50% and you should have gathered Rs 4000 by the end of this time.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HEALTH',50]
    condn2 = [False,3,'','','>=','NUTRITION',50]
    condn3 = [False,3,'','','>=','HOUSING',50] 
    condnlist = [condn1,condn2,condn3]
    condnGlobal = ['NOR',30,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'You have not been able to complete the task.You must complete it to move on to the next level'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','EDUCATION',60]
    condn2 = [False,5,'','','>=','',4000]
    condn3 = [False,3,'','','>=','TRAINING',60]
    condnlist = [condn1,condn2,condn3]
    condnGlobal = ['NOR',1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'You have completed this step of taking the town towards full recovery'
    
    action = [9,text]
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
    
    action = [2,'']
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
    
    text = 'You have not been able to complete the task.You must complete it to move on to the next level'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    
    #Mission 5
    
    chatText = ['Stevenson Gorbachev','The situation of the city has improved considerably',
                'Gilbert Fernandez','Due to the rapid development of the education system, One Laptop Per Child (OLPC) has decided to donate free laptops to the schools.',
                'John Tremblay','This is a very good move as this will greatly help in the growth of the education system.Moreover, this kind of a thing will help all levels of society in an equal way and thus will develop society as a whole.',
                'Stevenson Gorbachev','The progress made so far would be for nothing if it is not maintained and the money earned be utilised for its further development.Do we have enough food and medicinal facilities for the people for the next few months?',
                'Tony Peralta','Our storage houses are full, we are fully prepared on that front',
                'Ragnar Stefansson','The housing area needs to be taken care of, we will need lot more houses to have proper shelters for all the people.']
    
    action = [1,[chatText,str(storyboard_name)+'/images/chat images/haiti.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Now you need to pay attention towards the development of the village.Every person in the village should have an appropriate house to itself.Your task is to increase the progress bar housing to 70% while keeping all other well above 30% for the first 10 days and above 50% for the next 20 days.The time limit is 1 months.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','EDUCATION',30]
    condn2 = [False,3,'','','>=','HEALTH',30]
    condn3 = [False,3,'','','>=','TRAINING',30]
    condn4 = [False,3,'','','>=','NUTRITION',30]
    condnlist = [condn1,condn2,condn3,condn4]
    condnGlobal = ['NOR',10,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output) 
    
    
    text = 'You have not been able to complete the task.You must complete it to move on to the next level'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','EDUCATION',40]
    condn2 = [False,3,'','','>=','HEALTH',40]
    condn3 = [False,3,'','','>=','TRAINING',40]
    condn4 = [False,3,'','','>=','NUTRITION',40]
    condnlist = [condn1,condn2,condn3,condn4]
    condnGlobal = ['NOR',20,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output) 
    
    
    text = 'You have not been able to complete the task.You must complete it to move on to the next level'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HOUSING',70]
    condnlist = [condn1]
    condnGlobal = ['NOR',1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = ['Gilbert Fernandez','You have completed this step of taking the town towards full recovery']
    
    action = [9,text]
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
    
    action = [2,'']
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
    
    text = 'You have not been able to complete the task.You must complete it to move on to the next level'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    
    #Mission 6
    
    chatText = ['Gilbert Fernandez','The people have once again started living a happy and prosperous life',
                'Tony Peralta','All our efforts have finally paid off, our work here in this city is done.',
                'Stevenson Gorbachev','Although the city has recovered from the shock of the earthquake but being the Governnor of the city it is my duty to keep on thriving for the betterment of the people.',
                'Ragnar Stefansson',' It is necessary that arrangements be made for a secure future and the standard of living of the people be increased.']
    
    
    action = [1,[chatText,str(storyboard_name)+'/images/chat images/haiti.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Your work now is to ensure that the city keeps on developing and as the representative of the people you are able to provide good facilities to them.Increase all the progress bars to 75% taking care that none of them should fall below 40% and manage to obtain an amount of Rs 3000 at the end of 1 month.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HOUSING',40]
    condn2 = [False,3,'','','>=','HEALTH',40]
    condn3 = [False,3,'','','>=','EDUCATION',40]
    condn4 = [False,3,'','','>=','NUTRITION',40]
    condn5 = [False,3,'','','>=','TRAINING',40]
    condnlist = [condn1,condn2,condn3,condn4,condn5]
    condnGlobal = ['NOR',30,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'You have not been able to complete the task.You must complete it to move on to the next level'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HOUSING',75]
    condn2 = [False,3,'','','>=','HEALTH',75]
    condn3 = [False,3,'','','>=','EDUCATION',75]
    condn4 = [False,3,'','','>=','NUTRITION',75]
    condn5 = [False,3,'','','>=','TRAINING',75]
    condn6 = [False,5,'','','>=','',3000]
    condnlist = [condn1,condn2,condn3,condn4,condn5,condn6]
    condnGlobal = ['NOR',1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'You have completed this step of taking the town towards full recovery'
    
    action = [9,text]
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
    
    text = 'Congratulations you have restored the peace and prosperity of yout town'
    
    action = [6,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    action = [10,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'You have not been able to complete the task.You must complete it to move on to the next level'
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    output.close()
    
write_data()