#! /usr/bin/env python
#

# ***** BEGIN LICENSE BLOCK *****
# Version: CPAL 1.0
#
# The contents of this file are subject to the Common Public Attribution
# License Version 1.0 (CPAL); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://opensource.org/licenses/cpal_1.0
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# ***** END LICENSE BLOCK ****
#

import pickle

# TODO Need to put delay actions at all the places

        

def write_data():

    output = open('storyboard.pkl','wb')
    
    # MISSION 1 
    
    text = 'Long ago in the massive lands of India, there used to be a village called Gokul. The village of Gokul had a wise and an honest man, Kamat, as its Sarpanch. After many years of service, Kamat realized that he had grown old. It was the time to retire and pass on his responsibilities to someone, who had the potential, mind and passion to manage the village. He and his close committee of advisers searched and searched for the ideal caretaker. Sometimes, when you keep on looking for the solution everywhere, you forget to look around your immediate environment. The person was right in Kamats house, his Son.'
    
    action = [7,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    chatText = ['Kamat','Hello Son. I hope your studies are going well in school. The studies done in the school give you a theoretical aspect of doing things; you need to learn about how to apply these learning in real life.',
                'Kamat','You need to know how to develop your village, as you might well become the Sarpanch after me. I will assist you in developing your skills...',
                'Kamat','Let us go to the village of AbuJamara.']
    
    action = [1,[chatText,'Wfpwork.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    chatText = ['Son','Father, this is no village, where are the villagers? A village without people is like lake without water.''',
    'Kamat','Yes, this is the place where the Abujamara people will move. The Abujmara village was situated on the banks of river Ganga. Mother Ganga cursed the people of Abujamara by changing its course of flow and flooding the Abujamara village.',
    'Kamat','The people of Abujamara are homeless right now. They came to our village seeking help and the Panchayat decided to clear this forest and provide the land to the poor people. It is our job to help them establish a village on this land.',
    'Kamat','If you had been at my place, how would you bring life back to this village?',
    'Son','Father, I feel that the first requirement of the people of the village is shelter.',
    'Kamat','Very rightly said son. Every person needs a house to live in. Shelter is among one of the most basic necessities of a person. Build 3 huts to shelter the people of Abujamara. You can setup a hut by clicking on Build Facility->house.']
    
    action = [1,[chatText,'Barren-Land.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,1,'HOUSE','','==','',3]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    chatText = ['Kamat','When you setup a hut, some amount of your resources are utilized. For each Hut that you setup, 10 units of Building Material, 8 units of Tools and 8 units of Water are used. Also, some of your manpower is employed in making the hut. Similarly, resources are used to setup each facility.',
    'Son','Okay, Father.',
    'Kamat','When you setup a Hut the Housing Indicator of the Village increases.The indicators are shown on the bottom right hand side of the screen. The indicators are a measure, which tell about the growth and prosperity of the village.',
    'Son','Okay, Father.']
    
    action = [1,[chatText,'thatched-huts.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    chatText = ['Kamat','Son, the next basic necessity of a village is Food. The people need food and water to survive. A well will draw water from the ground and provide fresh clean water to everybody. To setup a well click on Build Facility->Well. Build a well now.']

    action = [1,[chatText,'thatched-huts.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    
    condn1 = [True,1,'FOUNTAIN','','==','',0]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    chatText = ['Kamat','Well done son, You are going good.',
    'Kamat','To grow food, you will need to setup farms. Since the soil is fertile, we can grow any crop here. It is best to provide a healthy mix of Rice, Beans and Vegetables and Fruits. This will ensure healthy variety and nutrition. Build a farm now.']
    
    action = [1,[chatText,'farm2.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    condn1 = [True,1,'FARM','','==','',0]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)

    chatText = ['Kamat','Well done son. Let us go back and let the new village prosper.']
    
    action = [1,[chatText,'Happy.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    text = " Great Work!! \n\nLooking at the condition of the village and the rapid progress work done by you for the village. World Food Program has agreed to help the people for Abujamara by providing Food reserves to the village."
    
    action = [6,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    action = [2,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    # MISSION 2

    chatText = ['Kamat','The children of Abujamara have no place to study. Some of them are walking 10 miles and more to come to study at your school. Build a school for them.']
    
    action = [1,[chatText,'withbooks.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [True,1,'SCHOOL','','==','',0]
    condn2 = [True,3,'SCHOOL','','==','',0]
    condnlist = [condn1,condn2]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    chatText = ['Kamat','Son, the Schools require books to function properly. If there would be no books, the teachers would not be able to impart education to the children. Buy the books for the school from the market.',
    'Son','Okay, Father.']
    
    action = [1,[chatText,'withbooks.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [True,4,'SCHOOL','','==','',0]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    chatText = ['Kamat','Son, as the schools are functional now. You can see that the number of people educated in the Manpower Distribution table has increased. Also the education indicator in the Indicator table has increased.',
    'Son','Definitely father, it has. Now, I am able to realize the potential of education.',
    'Kamat','Good work son.']
    
    action = [1,[chatText,'withbooks.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    chatText = ['Kamat','Son all the facilities require water to function properly, you must setup a well for this purpose.',
                'Son','Okay, Father']
    
    action = [1,[chatText,'withbooks.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [True,1,'FOUNTAIN','','==','',0]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)

    chatText = ['Kamat','Son, as you can see a lot of people in the village are sitting idle. That is like a waste of their time and energy. You should setup workshops for the people who are not involved in agriculture. The workshop would provide craftsmen, potters and metal workers a place to work. Build a workshop for them to work.',
    'Son','Definitely father.']

    action = [1,[chatText,'cover09.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    

    condn1 = [True,1,'WORKSHOP','','==','',0]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    chatText = ['Kamat','Excellent, with the young learning and the grown-ups working, the village is on the path to prosperity. But can you spot something missing in this scheme. Yes, you are right. They do not have a hospital to care for the sick. Build a hospital now.']
    
    action = [1,[chatText,'hospital.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [True,1,'HOSPITAL','','==','',0]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)

    chatText = ['Kamat','We have done all we can. You are learning fast, someday you will take my place.']

    action = [1,[chatText,'sharpergirl.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)


    text = " Great Work!! \n\nLooking at the Rapid progress of the village. WFP has planned to start Food for Work program in Abujamara village.\n\nIn Food for Work program WFP involves People of the village in Development Work. \n\nWorkers are paid not with money but with food rations to \nbuild vital new infrastructure that will increase the food \nsecurity of households or communities."

    action = [6,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    action = [2,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    # MISSION 3
    
    chatText = ['Kamat','How are your studies going? I see, you do not seem to have enough books at school. It is all caused when trading is neglected. Let us analyze the village stocks and I will help you learn the basics of trading.',
    'Kamat','You can see the buy/sell button in the highlighted portion in the lower panel of the screen. This provides information on the number of every resource present in the village. When you find yourself running low on a certain resource, you should go to the market to buy more of it.',
    'Kamat','Let us buy more books. Click on the Buy/Sell button, select books and enter the quantity in the box. Finally click the BUY button to buy the books.']

    action = [1,[chatText,'trading.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)


    condn1 = [True,6,'','BOOKS','==','',0]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)


    chatText = ['Kamat','Excellent Work , Son.',
    'Kamat','Son you would have noticed that the money present with the village, shown in the right hand top corner, decreases when you buy any resources from the market. You must maintain a good amount of money in the village account.',
    'Kamat','To increase money in the village account you can sell resources to the market.',
    'Kamat','Like, we have an excess of Tools and since we are not doing any new construction these days, we can safely sell it in the market. Sell 20 units of Tools.']
    
    action = [1,[chatText,'trading.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)



    condn1 = [True,7,'','TOOLS','==','',0]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)

    chatText = ['Kamat','Good work son. This is all you need to know about trading. You need to buy the resources when you are falling short of them and sell them when there is an excess of a resource in your village. The prices are governed by the amount of supply in the market.', 
    'Kamat','Let us head back to a nice dinner at home.']
    

    action = [1,[chatText,'trading.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)


    action = [2,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    # MISSION 4
    
    chatText = ['Kamat','Meet Sukhdev, sarpanch of Abujamara. He has come to thank us for all we did for the village.',
    'Sukhdev','Yes, after you and your sons initial start, our village has prospered. How can I ever thank you for the wonderful work you did for my people.',
    'Kamat','It was our pleasure, Sukhdev. If men wont help fellow men in need, then who will.',
    'Sukhdev','This is your modesty, Kamat. I am really impressed with your village, your village has better building and efficient workers.',
    'Kamat','This is because we have kept up with the technology Sukhdev. My son and me will accompany you to your village to help install better technology in buildings.',
    'Sukhdev','Thanks a lot, Kamat. We will hold a grand feast on your coming there.']
    
    action = [1,[chatText,'tech.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    chatText = ['Kamat','You must know son, technology upgrades provide better buildings with capacity to house more workers and produce more resources. Thus, they are usually helpful in increasing the prosperity of the village. Do an upgrade of the workshop to level 2. Click on the Upgrade Button and then select Workshop and click upgrade.']

    action = [1,[chatText,'tech.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [True,2,'WORKSHOP','','==','',0]
    condnlist = [condn1]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    chatText = ['Kamat','Good work Son. You should notice that upgrading a facility increases its productivity. The amount of resources produced by the Workshop have been increased considerable, also the people working in workshop would get better working conditions.',
    'Son','Yes father, I can notice the changes. The indicators level has also increased.',
    'Kamat','Yes Son, upgrading a facility affects the overall prosperity of the village.']
    
    action = [1,[chatText,'tech.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    chatText = ['Kamat','Son, now upgrade every facility type to level 1. You can also notice that information related to the upgrade is given in the upgrade window whenever you select any facility.',
    'Kamat','When you will upgrade all the facilities, you will notice a considerable change in the indicators of the village.',
    'Son','Okay, father.']
    
    action = [1,[chatText,'tech.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    condn1 = [False,2,'HOSPITAL','','>=','',1]
    condn2 = [False,2,'HOUSE','','>=','',1]
    condn3 = [False,2,'SCHOOL','','>=','',1]
    condn4 = [False,2,'FARM','','>=','',1]
    condn5 = [False,2,'FOUNTAIN','','>=','',1]
    condnlist = [condn1,condn2,condn3,condn4,condn5]
    condnGlobal = ['AND',-1,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)
    
    chatText = ['Kamat','Excellent work. Let us join Sukhdev for the feast.']
    
    action = [1,[chatText,'tech.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    text = "The people of Abujamara are very much pleased with all the work you have done for the prosperity of the village.\n\n They have sent you the first harvest from their Farms, as\na symbol of Honor to you. You must accept it."
    
    action = [6,text]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    action = [2,'']
    actionData = ['action',action]
    pickle.dump(actionData,output)
 

    
    # MISSION 5
    
    chatText = ['Kamat','I am really impressed with your work.',
    'Son','Thank you, father.',
    'Kamat','But I wonder, if you are capable enough to work without my guidance now that you have learnt the basics of building a village.',
    'Son','I think I will be father.',
    'Kamat','I will be leaving the village for the next 3 months to go to your Cousins wedding.',
    'Son','Will I not be accompanying you?',
    'Kamat','No son, I need someone to take care of the village.',
    'Kamat','Here is your mission: Take good care of our village for the next 3 months.',
    'Kamat','Do not let the indicator levels fall below 20% for the next three months.',
    'Son','Ok Father. I will not disappoint you.']

    
    action = [1,[chatText,'prosper.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)
    
    condn1 = [False,3,'','','>=','HOUSING',20]
    condn2 = [False,3,'','','>=','HEALTH',20]
    condn3 = [False,3,'','','>=','EDUCATION',20]
    condn4 = [False,3,'','','>=','NUTRITION',20]
    condn5 = [False,3,'','','>=','TRAINING',20]
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
 
    text = "You were not able to maintain the village properly. Your indicators fell below 20%.\n\n You must retry this level to reach the next level."
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)

    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)
 

    # MISSION 6
    
    chatText = ['Kamat','Welcome Ajmal, welcome. How did you find time to visit this small village again.',
    'Son','Welcome home bhaiyya.',
    'Ajmal','It is so good to see you again Father, brother. All the comforts in the city are nowhere near the comfort of the home! I am so happy to be back again.',
    'Kamat','I am glad to hear this. So finally, you are going to stay for long.',
    'Ajmal','No father, I am afraid not. I am leaving tomorrow but I bring terrible news from the city.',
    'Kamat','So soon... but what news troubles you Ajmal?',
    'Ajmal','The economy is in recession. Big companies have become bankrupt; traders are losing all their money, prices of the basic commodities falling...',
    'Kamat','Ajmal, as a part of the government, it is your job to improve the economy.',
    'Ajmal','We are trying hard father, but the recession is here for some time. And you should prepare...',
    'Kamat','Prepare for what?',
    'Ajmal','The prices will fall and trade will decrease in a few days.',
    'Kamat','Our treasury is already low due to bad trade these days, I did not know, it was due to the mistakes of the city people.',
    'Son','I will handle it father. I will sail us through these bad times.',
    'Kamat','I have full faith in your capabilities son. I will leave the management of the village resources to you.',
    'Ajmal','I did not know, that you have stepped into our fathers shoes so soon.',
    'Son','I have bhaiyya, and I will do well.',
    'Ajmal','Father, come with me to the city once. You will be able to appreciate the crisis better. Moreover, your grandchildren are eager to meet you.',
    'Kamat','Thats a good idea, it has been years since I saw them.',
    'Ajmal','Thank you father.',
    'Son','Bhaiyya, what do you reckon will happen in the coming days.',
    'Ajmal','Prices of the commodities will fall, do not try to setup new things during this period and focus on trading well.',
    'Ajmal','Smart trading will ensure that you do not lose the money in your treasury. According to my calculations, things will improve in the next year.',
    'Ajmal','So at the end of 4 months, do not allow the indicator values to below 20%. Also, maintain atleast Rs. 5,000 In the treasury at all times.',
    'Ajmal','Farewell brother, hope you will do well.']
    
    action = [1,[chatText,'rec2.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    chatText = ['Son','The prices of all the commodities have dropped. The resources required for proper functioning of the facilities are drying up .',
    'Son','It is indeed a tough time for the village. I wish father had been here to accompany me.']

    action = [1,[chatText,'rec2.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    condn1 = [False,3,'','','>=','HOUSING',20]
    condn2 = [False,3,'','','>=','HEALTH',20]
    condn3 = [False,3,'','','>=','EDUCATION',20]
    condn4 = [False,3,'','','>=','NUTRITION',20]
    condn5 = [False,3,'','','>=','TRAINING',20]
    condn6 = [False,5,'','','>=','',5000]
    condnlist = [condn1,condn2,condn3,condn4,condn5,condn6]
    condnGlobal = ['NOR',120,condnlist]
    condnData = ['condition',condnGlobal]
    pickle.dump(condnData,output)

    chatText = ['Kamat','Well done Son. You have proved your capabilities once again.',
    'Son','Thank you, father.']

    action = [1,[chatText,'happy2.png']]
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)

    text = "Looking at the present economical conditions, the government has planned to give bailout to the companies affected by recession.\n\n The prices of crops will rise again, and the farmers will be able to get the right value for their hardwork.\n\n Good Work!!"
    
    action = [6,text]
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)

    action = [2,'']
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)
 

    text = "You were not able to maintain the village properly. Your indicators fell below 20% or the money in your bank is less than Rs. 5000.\n\nYou must retry this level to reach the next level."
    
    
    action = [8,text]
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)

    action = [3,'']
    actionData = ['actionFalse',action]
    pickle.dump(actionData,output)

    # MISSION 7
    
    chatText = ['Farmer','Sarpanch ji, there is no water. The crops are dying. Help us',
    'Farmer','Help us Sarpanch ji, otherwise whole village will die due to hunger.',
    'Farmer',' Is it the rain god: Indra who is displeased with us.',
    'Kamat','No it is not the gods, but the failing monsoon.',
    'Kamat','Due to recent ecological disturbances, monsoon has not come this year. But dont worry I will handle it.',
    'Farmer','Thank you sarpanch ji. We are also holding a pooja[prayers] for Indra.']
    
    action = [1,[chatText,'drought.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    chatText = ['Kamat','Son...',
                'Son','Yes father, is there anything I can do for you.',
                'Kamat','Yes son, the monsoon has deserted us. The crops are dying. Farmers believe it is the Indra god who is displeased, but you know better.',
                'Son','Yes father.',
                'Kamat','They will be holding a pooja soon. But we need to do more than that.',
                'Son','Yes Father.',
                'Kamat','Due to lack of water, the productivity of farms have decreased. People are dying of hunger.',
                'Kamat','Hospitals and Workshops are also not able to work properly due to shortage of water.',
                'Kamat','Build up some wells and take good care of crops. Do not let the nutrition indicator drop below 20% and also donot let the water level fall below 100.',
                'Kamat','Good luck son.']
    
    
    action = [1,[chatText,'drought.png']]
    actionData = ['action',action]
    pickle.dump(actionData,output)

    condn1 = [False,3,'','','>=','NUTRITION',20]
    condn2 = [False,4,'','WATER','>=','',100]
    condnlist = [condn1,condn2]
    condnGlobal = ['NOR',120,condnlist]
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



    # MISSION 8
    
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
    
    text = 'Mission Objective: \n\nRebuild the village and bring the indicators to 40% within\nnext 2 years.'
    
    action = [7,text]
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

 
    text = "The village Panchayat has decided to select you as the next Sarpanch of the village.\n\nAlso, they have decided to make a new school in remembrance of the best Sarpanch this village had in years, your father, Kamat."
    
    
    action = [6,text]
    actionData = ['actionTrue',action]
    pickle.dump(actionData,output)


    output.close()
    
    
write_data()