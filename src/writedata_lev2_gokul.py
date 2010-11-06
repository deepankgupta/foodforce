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
output = open('data2.pkl', 'wb')

# DICTIONARIES REGARDING RESOURCES REQD TO BUILD EACH FACILITY PER BUILDING

COST_HOUSE = {'BUILDING MATERIAL' : 5.0 , 'TOOLS' : 5.0 , 'WATER' :3.0 }
pickle.dump(COST_HOUSE, output)
COST_HOSPITAL = {'BUILDING MATERIAL' : 25.0 , 'TOOLS' : 20.0 , 'WATER' : 8.0 }
pickle.dump(COST_HOSPITAL, output)
COST_SCHOOL = {'BUILDING MATERIAL' : 20.0 , 'TOOLS' : 20.0 , 'WATER' : 8.0 }
pickle.dump(COST_SCHOOL, output)
COST_WORKSHOP = {'BUILDING MATERIAL' : 25.0 , 'TOOLS' : 10.0 , 'WATER' : 10.0 }
pickle.dump(COST_WORKSHOP, output)
COST_FARM = {'BUILDING MATERIAL' : 0.0 , 'TOOLS' : 5.0 , 'WATER' : 15.0 }
pickle.dump(COST_FARM, output)
COST_FOUNTAIN = {'BUILDING MATERIAL' : 10.0 , 'TOOLS' : 20.0 , 'WATER' : 0.0 }
pickle.dump(COST_FOUNTAIN, output)

# MANPOWER REQD TO BUILD EACH FACILITY PER BUILDING

MANP_REQD_BUILD_HOUSE = { 'EMPLOYED PEOPLE IN CONSTRUCTION' : 2.0 }
pickle.dump(MANP_REQD_BUILD_HOUSE, output)
MANP_REQD_BUILD_HOSPITAL = { 'EMPLOYED PEOPLE IN CONSTRUCTION' : 4.0 } #10.0 
pickle.dump(MANP_REQD_BUILD_HOSPITAL, output)
MANP_REQD_BUILD_SCHOOL = { 'EMPLOYED PEOPLE IN CONSTRUCTION' : 6.0 } #8.0
pickle.dump(MANP_REQD_BUILD_SCHOOL, output)
MANP_REQD_BUILD_WORKSHOP = { 'EMPLOYED PEOPLE IN CONSTRUCTION' : 4.0 }
pickle.dump(MANP_REQD_BUILD_WORKSHOP, output)
MANP_REQD_BUILD_FARM = { 'EMPLOYED PEOPLE IN CONSTRUCTION' : 2.0 }
pickle.dump(MANP_REQD_BUILD_FARM, output)
MANP_REQD_BUILD_FOUNTAIN = { 'EMPLOYED PEOPLE IN CONSTRUCTION' : 4.0 }
pickle.dump(MANP_REQD_BUILD_FOUNTAIN, output)
# DICTIONARY OF ALL THE MANPOWER DISTRIBUTION CHANGES WHEN SETTING A FACILITY

FACILITY_MANP_DICT_BUILD = { 'HOUSE' : MANP_REQD_BUILD_HOUSE , 'HOSPITAL' : MANP_REQD_BUILD_HOSPITAL , 'SCHOOL' : MANP_REQD_BUILD_SCHOOL , 'WORKSHOP' : MANP_REQD_BUILD_WORKSHOP , 'FARM' : MANP_REQD_BUILD_FARM , 'FOUNTAIN' : MANP_REQD_BUILD_FOUNTAIN }
pickle.dump(FACILITY_MANP_DICT_BUILD, output)


FACILITY_NAMES = {'HOUSE' : 'House' , 'HOSPITAL' : 'Hospital' , 'SCHOOL' : 'School' , 'WORKSHOP' : 'Workshop' , 'FARM' : 'Farm' , 'FOUNTAIN' : 'Well'}
pickle.dump(FACILITY_NAMES, output)



# DICTIONARIES OF RESOURCES REQD TO UPGRADE A FACILITY PER BUILDING  ( ASSUMPTION : NO MANPOWER IS REQD TO UPGRADE A FACILITY )

COST_LEVEL_HOUSE = {'BUILDING MATERIAL' : 2.0 , 'TOOLS' : 2.0 }
pickle.dump(COST_LEVEL_HOUSE, output)
COST_LEVEL_HOSPITAL = {'BUILDING MATERIAL' : 10.0 , 'TOOLS' : 5.0 }
pickle.dump(COST_LEVEL_HOSPITAL, output)
COST_LEVEL_SCHOOL = {'BUILDING MATERIAL' : 8.0 , 'TOOLS' : 5.0 }
pickle.dump(COST_LEVEL_SCHOOL, output)
COST_LEVEL_WORKSHOP = {'BUILDING MATERIAL' : 10.0 , 'TOOLS' : 5.0 }
pickle.dump(COST_LEVEL_WORKSHOP, output)
COST_LEVEL_FARM = {'BUILDING MATERIAL' : 0.0 , 'TOOLS' : 3.0 }
pickle.dump(COST_LEVEL_FARM, output)
COST_LEVEL_FOUNTAIN = {'BUILDING MATERIAL' : 2.0 , 'TOOLS' : 5.0 }
pickle.dump(COST_LEVEL_FOUNTAIN, output) 




# DICTIONARIES OF RESOURCES BEING CONSUMED BY EACH FACILITY PER BUILDING

CONS_HOUSE = { }                                                                                 # Remember that resources are being                                                                                                                     # consumed by manpower also so we need to                                                                                                                       # make that thing too... a TODO for 
pickle.dump(CONS_HOUSE, output)                                                                                                          # controller
CONS_HOSPITAL = { 'MEDICINE' : 2.0 , 'WATER' : 5.0 }
pickle.dump(CONS_HOSPITAL, output)
CONS_SCHOOL = { 'BOOKS' : 2.0 , 'WATER' : 2.0 }
pickle.dump(CONS_SCHOOL, output)
CONS_WORKSHOP = { }
pickle.dump(CONS_WORKSHOP, output)
CONS_FARM = { 'WATER' : 10.0 }
pickle.dump(CONS_FARM, output)
CONS_FOUNTAIN = { }
pickle.dump(CONS_FOUNTAIN, output)

# DICTIONARIES OF RESOURCES BEING PRODUCED BY THE FACILITY PER BUILDING

PROD_HOUSE = { }
pickle.dump(PROD_HOUSE, output)
PROD_HOSPITAL = { }
pickle.dump(PROD_HOSPITAL, output)  # WE CAN MAKE IT TO ZERO EVEN 
PROD_SCHOOL = { }
pickle.dump(PROD_SCHOOL, output)
PROD_WORKSHOP = { 'TOOLS' : 15.0 }
pickle.dump(PROD_WORKSHOP, output)
MAX_FOOD_PROD_PER_FARM = 70 #100
pickle.dump(MAX_FOOD_PROD_PER_FARM, output)
PROD_FARM = { 'RICE' : 0.0 , 'WHEAT' : 0.0 , 'BEANS' : 0.0 , 'SUGAR' : 0.0 , 'SALT' : 0.0 , 'OILS' : 0.0 }
pickle.dump(PROD_FARM, output)                                                                                                           #THIS HAS TO BE DECIDED BY THE USER, BY                                                                                                                         #DEFAULT THEIR VALUE HAS BEEN PUT EQUAL TO                                                                                                                      #ZERO, TODO: FOR CONTROLLER FILL IN THE                                                                                                                         #VALUES OF RICE ETC IN %
DEF_FARM_PROD = ('34','33','33')
pickle.dump(DEF_FARM_PROD, output)
PROD_FOUNTAIN = { 'WATER' : 13 } #{ 'WATER' : 25 }
pickle.dump(PROD_FOUNTAIN, output)



# MANPOWER DISTRIBUTION CHANGED BY EACH FACILITY TO RUN THE FACILITY, THIS WILL INCREASE OR DECREASE AT BUILDIN OR UPGRADATION OF A FACILITY AND NOT AT EVERY TURN

MANP_DIST_HOUSE = { }
pickle.dump(MANP_DIST_HOUSE, output)
MANP_DIST_HOSPITAL = { 'EMPLOYED PEOPLE IN HOSPITAL' : 10.0 }                            #BY HEALTHY PEOPLE I MEAN THE NUMBER OF                                                                                                                         #PEOPLE THAT CAN BE MADE HEALTHY BY A                                                                                                                           #HOSPITAL 
pickle.dump(MANP_DIST_HOSPITAL, output)
MANP_DIST_SCHOOL = { 'EMPLOYED PEOPLE IN SCHOOL' : 6.0 }
pickle.dump(MANP_DIST_SCHOOL, output)
MANP_DIST_WORKSHOP = { 'EMPLOYED PEOPLE IN WORKSHOP' : 10.0 }
pickle.dump(MANP_DIST_WORKSHOP, output)
MANP_DIST_FARM = { 'EMPLOYED PEOPLE IN FARM' : 10.0 }                                                            # PEOPLE FED = FOOD PRODUCED / 5 ,PEOPLE                                                                                                                        # FED NEEDS TO BE INCREMENTED BY THE                                                                                                                    # CONTROLLER AS FOOD CAN BE BOUGHT BY THE                                                                                                                       # MARKET ALSO , TODO : CONTROLLER
pickle.dump(MANP_DIST_FARM, output)
MANP_DIST_FOUNTAIN = { }
pickle.dump(MANP_DIST_FOUNTAIN, output)

# CHANGE IN MANPOWER DISTRIBUTION DUE TO THE FACILITIES
MANP_CH_HOUSE = { 'SHELTERED PEOPLE' : 8.0 } #4.0
pickle.dump(MANP_CH_HOUSE, output)
MANP_CH_HOSPITAL = { 'HEALTHY PEOPLE' : 30.0 } #25.0
pickle.dump(MANP_CH_HOSPITAL, output)
MANP_CH_SCHOOL = { 'EDUCATED PEOPLE' : 30.0 } #20.0
pickle.dump(MANP_CH_SCHOOL, output)
MANP_CH_WORKSHOP = { }
pickle.dump(MANP_CH_WORKSHOP, output)
MANP_CH_FARM = { }
pickle.dump(MANP_CH_FARM, output)
MANP_CH_FOUNTAIN = { }
pickle.dump(MANP_CH_FOUNTAIN, output)

# DICTIONARY OF ALL THE FACILITIES WITH THEIR MANPOWER DISTRIBUTION CHANGES

FACILITY_MANP_DICT_CH = { 'HOUSE' : MANP_CH_HOUSE , 'HOSPITAL' : MANP_CH_HOSPITAL , 'SCHOOL' : MANP_CH_SCHOOL , 'WORKSHOP' : MANP_CH_WORKSHOP , 'FARM' : MANP_CH_FARM , 'FOUNTAIN' : MANP_CH_FOUNTAIN }
pickle.dump(FACILITY_MANP_DICT_CH, output)
# DICTIONARY OF ALL THE FACILITIES WITH THEIR MANPOWER DISTRIBUTION CHANGES TO RUN FACILITY

FACILITY_MANP_DICT_RUN = { 'HOUSE' : MANP_DIST_HOUSE , 'HOSPITAL' : MANP_DIST_HOSPITAL , 'SCHOOL' : MANP_DIST_SCHOOL , 'WORKSHOP' : MANP_DIST_WORKSHOP , 'FARM' : MANP_DIST_FARM , 'FOUNTAIN' : MANP_DIST_FOUNTAIN }
pickle.dump(FACILITY_MANP_DICT_RUN, output)
# DICTIONARY OF ALL THE FACILITIES WITH THE RESOURCES THAT THEY CONSUME

FACILITY_RES_DICT_CONS = { 'HOUSE' : CONS_HOUSE , 'HOSPITAL' : CONS_HOSPITAL , 'SCHOOL' : CONS_SCHOOL , 'WORKSHOP' : CONS_WORKSHOP , 'FARM' : CONS_FARM , 'FOUNTAIN' : CONS_FOUNTAIN }
pickle.dump(FACILITY_RES_DICT_CONS, output)


# DICTIONARY FOR MANPOWER DISTRIBUTION WHICH IS USED IN MODEL.PY

MANP_DIST_DICT = { 'TOTAL POPULATION' : 0.0 , 'SHELTERED PEOPLE' : 0.0 , 'EDUCATED PEOPLE' : 0.0 , 'HEALTHY PEOPLE' : 0.0 , 'PEOPLE FED' : 0.0 , 'EMPLOYED PEOPLE IN CONSTRUCTION' : 0.0 , 'EMPLOYED PEOPLE IN HOSPITAL' : 0.0 , 'EMPLOYED PEOPLE IN SCHOOL' : 0.0 , 'EMPLOYED PEOPLE IN WORKSHOP' : 0.0 , 'EMPLOYED PEOPLE IN FARM' : 0.0 }
pickle.dump(MANP_DIST_DICT, output)
FOOD_DIST_DICT ={ 'RICE':0.0 , 'WHEAT':0.0 , 'BEANS':0.0 ,'SUGAR': 0.0 ,'SALT' : 0.0 , 'OILS' : 0.0}
pickle.dump(FOOD_DIST_DICT, output)
#with levels increase 
LEVEL_INCR_PROD = 0.4
pickle.dump(LEVEL_INCR_PROD, output)
LEVEL_INCR_CONS = 0.2
pickle.dump(LEVEL_INCR_CONS, output)

# INITIAL VALUES OF INDICATORS
INIT_HOUSING = 0.0
pickle.dump(INIT_HOUSING, output)
INIT_NUTRITION = 0.0
pickle.dump(INIT_NUTRITION, output)
INIT_HEALTH = 0.0
pickle.dump(INIT_HEALTH, output)
INIT_TRAINING = 0.0
pickle.dump(INIT_TRAINING, output)
INIT_EDUCATION = 0.0
pickle.dump(INIT_EDUCATION, output)





# FACILITIES
INIT_HOUSE = 3 #4
pickle.dump(INIT_HOUSE, output)
INIT_HOSPITAL = 1 #2
pickle.dump(INIT_HOSPITAL, output)
INIT_WORKSHOP = 1
pickle.dump(INIT_WORKSHOP, output)
INIT_SCHOOL= 1
pickle.dump(INIT_SCHOOL, output)
INIT_FARM = 1
pickle.dump(INIT_FARM, output)
INIT_FOUNTAIN = 1
pickle.dump(INIT_FOUNTAIN, output)




# MONEY
INIT_MONEY = 50 #10000
pickle.dump(INIT_MONEY, output)
MAX_MONEY=9999999999L
pickle.dump(MAX_MONEY, output)

# Level Of facility
INIT_LEVEL = 0
pickle.dump(INIT_LEVEL, output)

## VILLAGE QUANTITY
# RESOURCES
INIT_WATER = 100 #1000
pickle.dump(INIT_WATER, output)
INIT_BUILDMAT = 100 #1000
pickle.dump(INIT_BUILDMAT, output)
INIT_TOOLS = 100 #1000
pickle.dump(INIT_TOOLS, output)
INIT_MEDICINE = 50 #100
pickle.dump(INIT_MEDICINE, output)
INIT_BOOKS = 50
pickle.dump(INIT_BOOKS, output)

# FOOD RESOURCES
INIT_RICE = 100 #500
pickle.dump(INIT_RICE, output)
INIT_WHEAT = 100 #500
pickle.dump(INIT_WHEAT, output)
INIT_BEANS = 100 #500
pickle.dump(INIT_BEANS, output)
INIT_SUGAR = 50 #500
pickle.dump(INIT_SUGAR, output)
INIT_SALT = 50 #500
pickle.dump(INIT_SALT, output)
INIT_OILS = 50 #500
pickle.dump(INIT_OILS, output)



##MARKET QUANTITY
# RESOURCES
INIT_M_WATER = 10000
pickle.dump(INIT_M_WATER, output)
INIT_M_BUILDMAT = 10000
pickle.dump(INIT_M_BUILDMAT, output)
INIT_M_TOOLS = 10000
pickle.dump(INIT_M_TOOLS, output)
INIT_M_MEDICINE = 2000
pickle.dump(INIT_M_MEDICINE, output)
INIT_M_BOOKS = 2000
pickle.dump(INIT_M_BOOKS, output)

# FOOD RESOURCES
INIT_M_RICE = 2000
pickle.dump(INIT_M_RICE, output)
INIT_M_WHEAT = 2000
pickle.dump(INIT_M_WHEAT, output)
INIT_M_BEANS = 2000
pickle.dump(INIT_M_BEANS, output)
INIT_M_SUGAR = 2000
pickle.dump(INIT_M_SUGAR, output)
INIT_M_SALT = 2000
pickle.dump(INIT_M_SALT, output)
INIT_M_OILS = 2000
pickle.dump(INIT_M_OILS, output)







# INITIAL COST OF RESOURCES PER UNIT (ASSUMPTION : THE INITIAL COST OF RESOURCES IN MARKET AS WELL AS FOR THE VILLAGE IS SAME)
COST_WATER = 15
pickle.dump(COST_WATER, output)
COST_BUILDMAT = 15
pickle.dump(COST_BUILDMAT, output)
COST_TOOLS = 15
pickle.dump(COST_TOOLS, output)
COST_MEDICINE = 10
pickle.dump(COST_MEDICINE, output)
COST_BOOKS = 10
pickle.dump(COST_BOOKS , output)

COST_RICE = 10
pickle.dump(COST_RICE, output)
COST_WHEAT = 10
pickle.dump(COST_WHEAT, output)
COST_BEANS = 12
pickle.dump(COST_BEANS, output)
COST_SUGAR = 8
pickle.dump(COST_SUGAR, output)
COST_SALT = 8
pickle.dump(COST_SALT, output)
COST_OILS = 12
pickle.dump(COST_OILS, output)





# BOUNDS ON INDICATORS AND RESOURCES AND FACILITIES

MAX_INDICATOR = 100
pickle.dump(MAX_INDICATOR, output)
MAX_NO_INS_FACILITY = {'HOUSE':21 , 'HOSPITAL':3 , 'WORKSHOP':4, 'SCHOOL':3, 'FOUNTAIN':7, 'FARM':4} # MAXIMUM NO. OF INSTALLATIONS OF A FACILITY
pickle.dump(MAX_NO_INS_FACILITY, output)
MAX_LEVELS_FACILITY = 3  # MAXIMUM NO OF LEVELS OF A FACILITY
pickle.dump(MAX_LEVELS_FACILITY, output)
LEVEL_INCR_PROD = 0.4
pickle.dump(LEVEL_INCR_PROD, output)
LEVEL_INCR_CONS = 0.2
pickle.dump(LEVEL_INCR_CONS, output)

MAX_RES_VAL_VILLAGE = 10000
pickle.dump(MAX_RES_VAL_VILLAGE, output)
MAX_RES_VAL_MARKET = 1000000000L
pickle.dump(MAX_RES_VAL_MARKET, output)
PRICE_VARIATION = 10
pickle.dump(PRICE_VARIATION, output)

# INFORMATION REGARDING CLUSTERS

VILLAGE_LEVEL = [{ 'HOUSE':8 , 'HOSPITAL':1 , 'WORKSHOP':2, 'SCHOOL':1, 'FOUNTAIN':3, 'FARM':2}, { 'HOUSE':15 , 'HOSPITAL':2 , 'WORKSHOP':3, 'SCHOOL':2, 'FOUNTAIN':5, 'FARM':3}, { 'HOUSE':21 , 'HOSPITAL':3 , 'WORKSHOP':4, 'SCHOOL':3, 'FOUNTAIN':7, 'FARM':4}]
pickle.dump(VILLAGE_LEVEL, output)

# DICTIONARIES REGARDING NUTRITIVE VALUES OF FOOD ( THEY ARE IN % )

RICE_NUTRITION = { 'PROTIENS' : 0.30 , 'FATS' : 0.50 , 'VITAMINS' : 0.20 }
pickle.dump(RICE_NUTRITION, output)
WHEAT_NUTRITION = { 'PROTIENS' : 0.15 , 'FATS' : 0.70 , 'VITAMINS' : 0.15 }
pickle.dump(WHEAT_NUTRITION, output)
BEANS_NUTRITION = { 'PROTIENS' : 0.40 , 'FATS' : 0.20 , 'VITAMINS' : 0.40 }
pickle.dump(BEANS_NUTRITION, output)
SUGAR_NUTRITION = { 'PROTIENS' : 0.30 , 'FATS' : 0.55 , 'VITAMINS' : 0.15 }
pickle.dump(SUGAR_NUTRITION, output)
SALT_NUTRITION = { 'PROTIENS' : 0.40 , 'FATS' : 0.10 , 'VITAMINS' : 0.50 }
pickle.dump(SALT_NUTRITION, output)
OILS_NUTRITION = { 'PROTIENS' : 0.35 , 'FATS' : 0.20 , 'VITAMINS' : 0.45 }
pickle.dump(OILS_NUTRITION, output)


FOOD_DIST_DICT_INIT = {'RICE' : RICE_NUTRITION , 'WHEAT' : WHEAT_NUTRITION , 'BEANS' : BEANS_NUTRITION , 'SUGAR' : SUGAR_NUTRITION , 'SALT' : SALT_NUTRITION , 'OILS' : OILS_NUTRITION }
pickle.dump(FOOD_DIST_DICT_INIT, output)



#MANPOWER REGARDING CONSTANTS

INIT_PEOPLE = 40.0 #200.0
pickle.dump(INIT_PEOPLE, output)
FOOD_PP= 1 #1
pickle.dump(FOOD_PP, output)
MAX_PER_FOOD_CONS = 30 #30
pickle.dump(MAX_PER_FOOD_CONS, output)
POPULATION_CHANGE = 0.05
pickle.dump(POPULATION_CHANGE, output)

# DICTIONARY OF PARAMETERS ON WHICH THE INDICATORS DEPEND WITH THEIR WEIGHT (AS RATIO)

PDICT_HOUSING = { 'SHELTERED PEOPLE' : 1 }                                                    # AS NO. OF HOUSES AND LEVEL OF HOUSES ARE DIRECTLY    #  PROPORTIONAL TO NO OF PEOPLE SHELTERED
pickle.dump(PDICT_HOUSING, output)

PDICT_HEALTH = { 'HEALTHY PEOPLE' : 0.5 , 'NUTRITION' : 0.3 , 'WATER' : 0.2}                  # BY NUTRITION I MEAN THE NUTRITION INDICATOR
pickle.dump(PDICT_HEALTH, output)

PDICT_NUTRITION = { 'PEOPLE FED' : 0.3 , 'PROTIENS' : 0.3 , 'FATS' : 0.1 , 'VITAMINS' : 0.3 } # WE WOULD BE REQUIRED TO CALCULATE THE AMT OF PROTIENS ETC.                                                                                                    # FROM THE VALUE OF RICE ETC.
pickle.dump(PDICT_NUTRITION, output)
PDICT_EDUCATION = { 'EDUCATED PEOPLE' : 0.6 , 'LEVEL OF EDUCATION' : 0.4 }
pickle.dump(PDICT_EDUCATION, output)

PDICT_TRAINING = { 'LEVEL OF WORKSHOPS' : 0.4 , 'EMPLOYED PEOPLE IN WORKSHOP' : 0.25 , 'EMPLOYED PEOPLE IN FARM' : 0.2 , 'EMPLOYED PEOPLE IN HOSPITAL' : 0.1 , 'EMPLOYED PEOPLE IN CONSTRUCTION' : 0.05 }
pickle.dump(PDICT_TRAINING, output)


# WELL I SUPPOSE THAT THERE ISN'T ANY NEED FOR AN INDICATOR FOR FOOD ALSO AS WE HAVE ALREADY HAD TWO INDICATORS RELATED TO IT I.E. HEALTH AND NUTRITION 
# REGARDIN FORMULA TO CALCULATE VALUE OF AN INDICATOR = SUM OF ((ALL PARAMETERS MULTIPLIED BY THEIR RESPECTIVE WEIGHTS)/THEIR MAX VALUE)*1000
# REGARDIN THE MAX VALUE OF PROTIENS AND ALL WE CAN CALCULATE IT BY ASSUMING THAT WHAT WUD HAV BEEN THE VALUE OF PROTIENS IN THE DIET IF THE USER WUD HAV     # BEEN GROWIN ONLY THAT CROP WHICH HAS THE MAX PROTIEN CONTENT AND SO ON.............    


output.close()
