#! /usr/bin/env python
#
#   Author : Mohit Taneja (mohitgenii@gmail.com)
#   Date : 9/06/2008 
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#

import os
import pickle
storyboard_no = 1
storyboard_list_file = open('storyboard_list.pkl')
pickle.load(storyboard_list_file)
storyboard_name = None
while storyboard_name == None:
    storyboard = pickle.load(storyboard_list_file)
    if storyboard_no == storyboard[0]:
        storyboard_name = storyboard[1]
    
    
def write_data():

    output = open(os.path.join('storyboards',str(storyboard_name),'storyboard.pkl'),'wb')
    
    # Tutorial Mission
    
    text = '\n \n \n \nIn this beautiful country called India, there is a Gokul village. The village of gokul is governed by Kamat who is the Sarpanch(head) of the village. But Kamat is growing old and needs a successor. Can you, his younger son, take on the responsibilities of the village and make the village prosper.'
    
    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    chatText = ['Kamat','Son, I will teach you about the various aspects towards running a village today. Are you ready to learn? Let us go to the village of Abujamara.  ',
                'Son','Father, this is no village, it is just empty land.... ',
                'Kamat','Yes, this is the place where once stood the village of Abujamara. The village became a barren land when Ganga cursed the people of Abujamara by changing its course and flooding the Abujamara village. The people are homeless are we will help rebuild their village.']
    
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    text = 'Build a hut to shelter the people of Abujamara. You can build a hut by clicking on Build->Hut.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    condn1 = [True,1,'HOUSE','','==','',0]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'When you build a hut, some amount of your resources are utilized. For each Hut that you build, 10 units of bricks, 10 units of Tools and 3 units of Water are used. Also, people are required to build a hut. Similarly, anything you build will require materials such as bricks and labour. Try building another hut.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [True,1,'HOUSE','','==','',0]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'When you build a Hut the Housing bar on the lower right corner of your screen increases. The more this bar is filled the more number of people have houses available for them. High progress bars indicate a happy and prosperous village.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    text = 'At the lower left corner you can see the total population and total sheltered people. The total population increases with time. Building the Houses increases the sheltered population. You should always try to build enough houses to provide shelter to all the people.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    

    text = 'Water, the most basic necessity of life, must always be present to support any kind of habitation. Build a Well for people to get water from.'
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,1,'FOUNTAIN','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'The next basic necessity of a village is Food. To grow food, you will need to build farms. It is best to provide a healthy mix of Rice, Beans and Vegetables and Fruits. This will ensure healthy variety and nutrition.You can choose the type of production from the bar-chart for your farm. Click on Build>Farm and adjust the production'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,1,'FARM','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
 
    text = 'As you continue building you will require Tools and Bricks. If you run out of them you can buy them from the market.Buying anything requires money and you can see the amount of money available to you in the top right corner of the screen. '
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
      
    text = 'The settlement has grown, the children here need a place to study. Build a school for them. '
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,1,'SCHOOL','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    
    text = 'Well done. But there are no books in this school. Buy the books for the school from the market. The Market Window can be opened by clicking on the market button in the bottom. Once you open the market window, you can click on the thing you need to buy and sell. Then select the quantity in which it needs to be bought or sold'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [True,6,'','BOOKS','==','',0]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
   

    text = 'The upgrade button provides technological upgrades.Try upgrading the huts with bricks.Click on the Upgrade and then select Hut'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,2,'HOUSE','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'Technology upgrades provide better buildings with capacity to house more workers and produce more resources. Thus, they are usually helpful in increasing the prosperity of the village. Upgrade your school'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,2,'SCHOOL','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'You should notice that upgrading a facility increases its productivity. The number of children taught in the School have been increased considerable, also the quality of education is now better. The progress bars have also filled up more.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    text = 'People around are idyling in the village, you should build a workshop to create more work for them. Building a workshop also adds Tools to your village stockpile'

    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,1,'WORKSHOP','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)

    text = 'Your village has grown considerably now, hygiene and healthcare are the two the most important aspect of a healthy living. You must build a hosptial now for people to get good treatment and medicine.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,1,'HOSPITAL','','>=','',1]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = 'You will have to buy medicine from the market for hospital to run!'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [True,6,'','MEDICINE','==','',0]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
	
    text = 'Your village has now taken the first step towards prosperity. Congratulations!'
    
    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    action = [2,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    # Mission 1
    
    chatText = ['Kamat','Nice work with the setting up of the new village. I am really impressed.',
                'Son','Thanks',
                'Kamat','But I wonder, if you are capable enough to work without my guidance now that you have learnt the basics of building a village.',
                'Kamat','I will leave you the responsibility of the village for the next 3 months while I go out for your cousin sister wedding.']
    
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Do not let any of the progress bars drop below 35... or else Kamat will not be very pleased. Good Luck!'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HOUSING',35]
    condn2 = [False,3,'','','>=','HEALTH',35]
    condn3 = [False,3,'','','>=','EDUCATION',35]
    condn4 = [False,3,'','','>=','NUTRITION',35]
    condn5 = [False,3,'','','>=','TRAINING',35]
    condnlist = [condn1,condn2,condn3,condn4,condn5]
    condnGlobal = ['NOR',90,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    
    chatText = ['Kamat','Well done Son. It seems that you are capable of handling the village after me.']
    
    action = [1,[chatText,'prosper.png']]
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)

    action = [2,'']
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
 
    text = "You were not able to maintain the village properly. You were not able to complete the task given to you. You must retry this level to reach the next level."

    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)

    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    
    # Mission 2
    
    chatText = ['Kamat','Well done son, you have certainly not disappointed me. But our village is now running low on money.',
                'Kamat','I will give you four months to bring more cash into the village. A cash reserve always comes in handy in times of calamities.',
                'Kamat','Also, more cash reserves will enable us to setup more buildings and buy materials and food to improve the condition of our people.',
                'Kamat','As you have already learnt that Tools made in workshops can be traded in market to earn money, you should focus on that.']
    
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Earn Rs. 5000 more in the next 4 months. But remember, this should not come at the cost of village condition. Do not let the progress bars fall below 25. Good Luck!'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HOUSING',25]
    condn2 = [False,3,'','','>=','HEALTH',25]
    condn3 = [False,3,'','','>=','EDUCATION',25]
    condn4 = [False,3,'','','>=','NUTRITION',25]
    condn5 = [False,3,'','','>=','TRAINING',25]
    condnlist = [condn1,condn2,condn3,condn4,condn5]
    condnGlobal = ['NOR',120,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = "You were not able to maintain the village properly. You were not able to complete the task given to you. You must retry this level to reach the next level."

    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)

    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,5,'','','>=','',5000]
    
    condnlist = [condn1]
    condnGlobal = ['NOR',1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    action = [2,'']
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
 
    text = "You were not able to maintain the village properly. You were not able to complete the task given to you. You must retry this level to reach the next level."

    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)

    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    # Mission 3
    
    chatText = ['Kamat','Respected members of Panchayat, my son has brought Rs 5000 more into the village funds. Now, it is for us to decide what needs to be done with it.']
    
    
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    text = 'Panchayat discusses the matter in the village assembly....'
    
    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    chatText = ['Panch','The Panchayat has reached a decision. We will invest the money in building more schools.',
                'Kamat','Yes, children are the future of our village. We want to teach them so that they are able to stand on their feet and bring wealth and prosperity to the village later on.',
                'Panch','Yes, and since your son has proved himself adept in adminstering. We want him to take charge of the money earnt and use it to for educating the children of our village.',
                'Son','It will be my pleasure.']
                
    
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    text = 'Your mission is simple. Increase the progress bar of Education to 70 while not letting any of the other progress bars to fall below 30 within 3 months.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HOUSING',30]
    condn2 = [False,3,'','','>=','HEALTH',30]
    condn4 = [False,3,'','','>=','NUTRITION',30]
    condn5 = [False,3,'','','>=','TRAINING',30]
    condnlist = [condn1,condn2,condn4,condn5]
    condnGlobal = ['NOR',90,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    text = "You were not able to maintain the village properly. You were not able to complete the task given to you. You must retry this level to reach the next level."

    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)

    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    condn3 = [False,3,'','','>=','EDUCATION',70]
    
    condnlist = [condn1]
    condnGlobal = ['NOR',1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    action = [2,'']
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
 
    text = "You were not able to maintain the village properly. You were not able to complete the task given to you. You must retry this level to reach the next level."

    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)

    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    # Mission 4
    
    chatText = ['Kamat','Welcome Ajmal, my son. How have your studies been going on.',
                'Ajmal','Thanks father. I am a registered physician now... but what is this. The village hygiene is so poor. This village is a breeding ground for all the diseases.', 
                'Ajmal','With stagnant water and unhygenic market, diseases are bound to follow. All these diseases will soon take a form of an epidemic if nothing is done for this now.', 
                'Kamat','Can you work with your younger brother to help avert this situation.',
                'Ajmal','Sure father.',
                'Ajmal','For providing good health, we need to provide good nutritious food to the villagers. A nutritious diet consists of all the components such as Wheat, Fruits, vegetables and beans.',
                'Ajmal','Also we need to setup hospitals and educate people about good practices and simple measures to avoid diseases. Schools setup by you are already doing a good job of it. We just need to bring some good doctors here',
                'Ajmal','Can you do all this to avoid an epidemic']
                
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Yes, this mission is harder. Take the progress bars for health to 65 and nutrition above 45 and you will be termed as pass.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HEALTH',65]
    condn2 = [False,3,'','','>=','NUTRITION',45]
    condnlist = [condn1,condn2]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)


    
    text = "You were able to complete the task assigned to you. \nGood Going!!"

    action = [8,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    
    
    action = [2,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)

        
    # Mission 5
    
    chatText = ['Farmer','Save us save us ....',
                'Kamat','What happened. Where are you running from? Where are your cattle and belongings.',
                'Farmer','I have none sir.. I have ran away from my home with my kids and wife since there is a war going on.',
                'Farmer','There will be more like me coming. I will work hard, but please give me a place to live peacefully.']
                
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Kamat and the Panchayat discusses...'

    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    chatText = ['Panch','Panchayat has decided that we will let the incoming immigrants into our village and will treat them as our guests. Athiti Devo Bhav.']
    
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    text = 'It seems as if there are not enough huts for all the incoming immigrants. Build more huts and increase the progress bar for housing till 80. Also increase the progress for Nutrition upto 50.'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HOUSING',80]
    condn2 = [False,3,'','','>=','NUTRITION',50]
    condnlist = [condn1,condn2]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    

    
    text = "You were able to complete the task assigned to you. \nGood Going!!"

    action = [8,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    
    action = [2,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    # Mission 6
    
    chatText = ['Panch','Good day, members of the Panchayat. It has nearly been 4 months since the first immigrants came to our village.',
                'Panch','But most of them are sitting idle, since they were originally farmers and have no farms now.',
                'Kamat','So, what. We will train them in our workshops to produce bricks for our village. Also, we can train them as labourers and they will become a part and parcel of the village.']
                 
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Good job recovering from the calamity. Train your people so that they turn into useful resources. Increase the training progress bar to 70 to pass this mission.' 

    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    condn1 = [False,3,'','','>=','TRAINING',70]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)

    
    text = "You were able to complete the task assigned to you. \nGood Going!!"

    action = [8,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    
    
    action = [2,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    # Mission 7
    
    chatText = ['Farmer','Sarpanch ji, there is no water. The crops are dying. Help us',
                'Priest','How can Sarpanch ji help. It is the rain god: Indra who is displeased with us. Let us hold a pooja to please Indra.',
                'Kamat','I will do what I can.']
    
    action = [1,[chatText,'drought.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    chatText = ['Kamat','Son...',
                'Son','Yes father, is there anything I can do for you.',
                'Kamat','Yes son, the monsoon has deserted us. The crops are dying. Farmers believe it is the Indra god who is displeased, but you know better.',
                'Kamat','They will be holding a pooja soon. But we need to do more than that.',
                'Son','Yes Father.']
    
    action = [1,[chatText,'drought.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Do not let the nutrition progress drop below 50% and also donot let the water level fall below 500 for the next 2 months.'
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    condn1 = [False,3,'','','>=','NUTRITION',48]
    condn2 = [False,4,'','WATER','>=','',500]
    condnlist = [condn1,condn2]
    condnGlobal = ['NOR',60,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    
    


    chatText = ['Farmer','Thank you, Sarpanchji for bringing us out from such a grave problem. Without your help, we along with our families would have died of hunger.',
                'Kamat','Well this time it wasnt me. Its my son, who should be getting the credit of all this work.',
                'Son','Thanks, father. But it was all due to your guidance and support only that I am able to serve for the prosperity of the village.']


    action = [1,[chatText,'happy.png']]
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)

    text = "WFP has planned to teach the farmers of your village. \n\nThey would be helping the farmers in increasing the productivity by helping them in doing proper irrigation of the farms. They would help farmers in implementing techniques like Crop Rotation, using Fertilizers etc, so that the productivity of the farms increase and the fertility of the soil remains intact.\n\nGood Work!!"

    
    action = [6,text]
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)

    action = [2,'']
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
 

    text = "You were not able to maintain the village properly.\n\nYou were not able to complete the task given to you.\n\nYou must retry this level to reach the next level."
    
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)

    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
    
    
    # Mission 8
    
    chatText = ['Kamat','Son, I am getting old, but I have a faint feeling that something bad is about to happen.',
                'Son','Why do you think so, father?',
                'Kamat','The signs are there in the animals. Look how the cattle and the sheep are getting restless. They are the ones who know first that the Gods are angry.']
    
    action = [1,[chatText,'earthquake_st.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    action = [4,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)

    text = " An earthquake strikes the village.\n\nKamat dies during the Earthquake.\n\nAjmal also comes back to the village after getting this news."
    
    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    chatText = ['Ajmal','Brother, the responsibility to manage the village is up to you now. you must help the people of the village in recovering from this calamity.',
                'Son','But bhaiyya, I wouldnt  be able to do all this without Fathers help and support.',
                'Ajmal','Father had a vision for this village. It had taken him a lifetime to setup this village. You must work for his mission.',
                'Ajmal','You must re build everything and get the village back on the path to progress and prosperity.',
                'Son','Dont worry brother; I will rebuild the village to its former glory.']
    

    action = [1,[chatText,'earthquake_st.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = 'Mission Objective: Rebuild the village and bring the progress levels to 40%'
    
    action = [9,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    


    condn1 = [False,3,'','','>=','HOUSING',40]
    condn2 = [False,3,'','','>=','HEALTH',40]
    condn3 = [False,3,'','','>=','EDUCATION',40]
    condn4 = [False,3,'','','>=','NUTRITION',40]
    condn5 = [False,3,'','','>=','TRAINING',40]
    condnlist = [condn1,condn2,condn3,condn4,condn5]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)

 
    text = "The village Panchayat has decided to select you as the next Sarpanch of the village.Also, they have decided to make a new school in remembrance of the best Sarpanch this village had in years, your father, Kamat."
    
    
    action = [6,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    action = [10,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)


    output.close()
    
    
write_data()





























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
