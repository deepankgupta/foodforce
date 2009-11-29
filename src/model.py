#! /usr/bin/env python
#
#   Author : Mohit Taneja (mohitgenii@gmail.com)
#   Date : 3/06/08
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

import Exceptions
import pickle
import pygame
import os
#import gui_buttons

#Flag to check the operating system
FLAG_XO = False



if os.path.exists('/sys/power/olpc-pm'):
       
    FLAG_XO = True
else:
    FLAG_XO = False

FLAG_SOAS = False

if os.path.exists('/home/liveuser/Activities') and (FLAG_XO == False):
       
    FLAG_SOAS = True
else:
    FLAG_SOAS = False

#facility size values
Facility_Size = [['HOUSE',360,360],['HOSPITAL',370,300],['FARM',516,500],['FOUNTAIN',197,192],['SCHOOL',420,450],['WORKSHOP',600,750]]

#Facility_Size = [['HOUSE',360],['HOSPITAL',370],['FARM',516],['FOUNTAIN',197],['SCHOOL',420],['WORKSHOP',600]]


def init_cons(file_name):
    """ used to read the values of constant from data file file_name
    @ivar file_name data file containing values of constant
    @type file_name string
    """
    data_file = open(file_name,'rb')
    # DICTIONARIES REGARDING RESOURCES REQD TO BUILD EACH FACILITY PER BUILDING
    global COST_HOUSE, COST_HOSPITAL, COST_SCHOOL, COST_WORKSHOP, COST_FARM, COST_FOUNTAIN
    COST_HOUSE = pickle.load(data_file)
    COST_HOSPITAL = pickle.load(data_file)
    COST_SCHOOL = pickle.load(data_file)
    COST_WORKSHOP = pickle.load(data_file)
    COST_FARM = pickle.load(data_file)
    COST_FOUNTAIN = pickle.load(data_file)

    # MANPOWER REQD TO BUILD EACH FACILITY PER BUILDING
    global MANP_REQD_BUILD_HOUSE, MANP_REQD_BUILD_HOSPITAL, MANP_REQD_BUILD_SCHOOL, MANP_REQD_BUILD_WORKSHOP, MANP_REQD_BUILD_FARM, MANP_REQD_BUILD_FOUNTAIN
    MANP_REQD_BUILD_HOUSE = pickle.load(data_file)
    MANP_REQD_BUILD_HOSPITAL = pickle.load(data_file)
    MANP_REQD_BUILD_SCHOOL = pickle.load(data_file)
    MANP_REQD_BUILD_WORKSHOP = pickle.load(data_file)
    MANP_REQD_BUILD_FARM = pickle.load(data_file)
    MANP_REQD_BUILD_FOUNTAIN = pickle.load(data_file)

    # DICTIONARY OF ALL THE MANPOWER DISTRIBUTION CHANGES WHEN SETTING A FACILITY
    global FACILITY_MANP_DICT_BUILD, FACILITY_NAMES
    FACILITY_MANP_DICT_BUILD = pickle.load(data_file)
    FACILITY_NAMES = pickle.load(data_file)

    # DICTIONARIES OF RESOURCES REQD TO UPGRADE A FACILITY PER BUILDING  ( ASSUMPTION : NO MANPOWER IS REQD TO UPGRADE A FACILITY )
    global COST_LEVEL_HOUSE, COST_LEVEL_HOSPITAL, COST_LEVEL_SCHOOL, COST_LEVEL_WORKSHOP, COST_LEVEL_FARM, COST_LEVEL_FOUNTAIN
    COST_LEVEL_HOUSE = pickle.load(data_file)
    COST_LEVEL_HOSPITAL = pickle.load(data_file)
    COST_LEVEL_SCHOOL = pickle.load(data_file)
    COST_LEVEL_WORKSHOP = pickle.load(data_file)
    COST_LEVEL_FARM = pickle.load(data_file)
    COST_LEVEL_FOUNTAIN = pickle.load(data_file)

    # DICTIONARIES OF RESOURCES BEING CONSUMED BY EACH FACILITY PER BUILDING
    global CONS_HOUSE, CONS_HOSPITAL, CONS_SCHOOL, CONS_WORKSHOP, CONS_FARM, CONS_FOUNTAIN
    CONS_HOUSE = pickle.load(data_file)
    CONS_HOSPITAL = pickle.load(data_file)
    CONS_SCHOOL = pickle.load(data_file)
    CONS_WORKSHOP = pickle.load(data_file)
    CONS_FARM = pickle.load(data_file)
    CONS_FOUNTAIN = pickle.load(data_file)

    # DICTIONARIES OF RESOURCES BEING PRODUCED BY THE FACILITY PER BUILDING
    global PROD_HOUSE, PROD_HOSPITAL, PROD_SCHOOL, PROD_WORKSHOP, MAX_FOOD_PROD_PER_FARM, PROD_FARM,DEF_FARM_PROD,PROD_FOUNTAIN
    PROD_HOUSE = pickle.load(data_file)
    PROD_HOSPITAL = pickle.load(data_file)
    PROD_SCHOOL = pickle.load(data_file)
    PROD_WORKSHOP = pickle.load(data_file)
    MAX_FOOD_PROD_PER_FARM = pickle.load(data_file)
    PROD_FARM = pickle.load(data_file)
    DEF_FARM_PROD = pickle.load(data_file)
    PROD_FOUNTAIN = pickle.load(data_file)

    # MANPOWER DISTRIBUTION CHANGED BY EACH FACILITY TO RUN THE FACILITY, THIS WILL INCREASE OR DECREASE AT BUILDIN OR UPGRADATION OF A FACILITY AND NOT AT EVERY TURN
    global MANP_DIST_HOUSE, MANP_DIST_HOSPITAL, MANP_DIST_SCHOOL, MANP_DIST_WORKSHOP, MANP_DIST_FARM, MANP_DIST_FOUNTAIN
    MANP_DIST_HOUSE = pickle.load(data_file)
    MANP_DIST_HOSPITAL = pickle.load(data_file)
    MANP_DIST_SCHOOL = pickle.load(data_file)
    MANP_DIST_WORKSHOP = pickle.load(data_file)
    MANP_DIST_FARM = pickle.load(data_file)
    MANP_DIST_FOUNTAIN = pickle.load(data_file)

    # CHANGE IN MANPOWER DISTRIBUTION DUE TO THE FACILITIES
    global MANP_CH_HOUSE, MANP_CH_HOSPITAL, MANP_CH_SCHOOL, MANP_CH_WORKSHOP, MANP_CH_FARM, MANP_CH_FOUNTAIN
    MANP_CH_HOUSE = pickle.load(data_file)
    MANP_CH_HOSPITAL = pickle.load(data_file)
    MANP_CH_SCHOOL = pickle.load(data_file)
    MANP_CH_WORKSHOP = pickle.load(data_file)
    MANP_CH_FARM = pickle.load(data_file)
    MANP_CH_FOUNTAIN = pickle.load(data_file)

    # DICTIONARY OF ALL THE FACILITIES WITH THEIR MANPOWER DISTRIBUTION CHANGES
    global FACILITY_MANP_DICT_CH
    FACILITY_MANP_DICT_CH = pickle.load(data_file)

    # DICTIONARY OF ALL THE FACILITIES WITH THEIR MANPOWER DISTRIBUTION CHANGES TO RUN FACILITY
    global FACILITY_MANP_DICT_RUN
    FACILITY_MANP_DICT_RUN = pickle.load(data_file)

    # DICTIONARY OF ALL THE FACILITIES WITH THE RESOURCES THAT THEY CONSUME
    global FACILITY_RES_DICT_CONS
    FACILITY_RES_DICT_CONS = pickle.load(data_file)

    # DICTIONARY FOR MANPOWER DISTRIBUTION WHICH IS USED IN PY
    global MANP_DIST_DICT, FOOD_DIST_DICT
    MANP_DIST_DICT = pickle.load(data_file)
    FOOD_DIST_DICT = pickle.load(data_file)

    #with levels increase
    global LEVEL_INCR_PROD, LEVEL_INCR_CONS
    LEVEL_INCR_PROD = pickle.load(data_file)
    LEVEL_INCR_CONS = pickle.load(data_file)

    # INITIAL VALUES OF INDICATORS
    global INIT_HOUSING, INIT_NUTRITION, INIT_HEALTH, INIT_TRAINING, INIT_EDUCATION 
    INIT_HOUSING = pickle.load(data_file)
    INIT_NUTRITION = pickle.load(data_file)
    INIT_HEALTH = pickle.load(data_file)
    INIT_TRAINING = pickle.load(data_file)
    INIT_EDUCATION = pickle.load(data_file)

    # FACILITIES
    global INIT_HOUSE, INIT_HOSPITAL, INIT_WORKSHOP, INIT_SCHOOL, INIT_FARM, INIT_FOUNTAIN 
    INIT_HOUSE = pickle.load(data_file)
    INIT_HOSPITAL = pickle.load(data_file)
    INIT_WORKSHOP = pickle.load(data_file)
    INIT_SCHOOL= pickle.load(data_file)
    INIT_FARM = pickle.load(data_file)
    INIT_FOUNTAIN = pickle.load(data_file)

    # MONEY
    global INIT_MONEY, MAX_MONEY
    INIT_MONEY = pickle.load(data_file)
    MAX_MONEY = pickle.load(data_file)

    #Initial Level
    global INIT_LEVEL
    INIT_LEVEL = pickle.load(data_file)
    
    ## VILLAGE QUANTITY
    # RESOURCES
    global INIT_WATER, INIT_BUILDMAT, INIT_TOOLS, INIT_MEDICINE, INIT_BOOKS 
    INIT_WATER = pickle.load(data_file)
    INIT_BUILDMAT = pickle.load(data_file)
    INIT_TOOLS = pickle.load(data_file)
    INIT_MEDICINE = pickle.load(data_file)
    INIT_BOOKS = pickle.load(data_file)

    # FOOD RESOURCES
    global INIT_RICE, INIT_WHEAT, INIT_BEANS, INIT_SUGAR, INIT_SALT, INIT_OILS 
    INIT_RICE = pickle.load(data_file)
    INIT_WHEAT = pickle.load(data_file)
    INIT_BEANS = pickle.load(data_file)
    INIT_SUGAR = pickle.load(data_file)
    INIT_SALT = pickle.load(data_file)
    INIT_OILS = pickle.load(data_file)

    ##MARKET QUANTITY
    # RESOURCES
    global INIT_M_WATER, INIT_M_BUILDMAT, INIT_M_TOOLS, INIT_M_MEDICINE, INIT_M_BOOKS 
    INIT_M_WATER = pickle.load(data_file)
    INIT_M_BUILDMAT = pickle.load(data_file)
    INIT_M_TOOLS = pickle.load(data_file)
    INIT_M_MEDICINE = pickle.load(data_file)
    INIT_M_BOOKS = pickle.load(data_file)

    # FOOD RESOURCES
    global INIT_M_RICE, INIT_M_WHEAT, INIT_M_BEANS, INIT_M_SUGAR, INIT_M_SALT, INIT_M_OILS 
    INIT_M_RICE = pickle.load(data_file)
    INIT_M_WHEAT = pickle.load(data_file)
    INIT_M_BEANS = pickle.load(data_file)
    INIT_M_SUGAR = pickle.load(data_file)
    INIT_M_SALT = pickle.load(data_file)
    INIT_M_OILS = pickle.load(data_file)

    # INITIAL COST OF RESOURCES PER UNIT (ASSUMPTION : THE INITIAL COST OF RESOURCES IN MARKET AS WELL AS FOR THE VILLAGE IS SAME)
    global COST_WATER, COST_BUILDMAT, COST_TOOLS, COST_MEDICINE, COST_BOOKS, COST_RICE, COST_WHEAT, COST_BEANS, COST_SUGAR, COST_SALT, COST_OILS 
    COST_WATER = pickle.load(data_file)
    COST_BUILDMAT = pickle.load(data_file)
    COST_TOOLS = pickle.load(data_file)
    COST_MEDICINE = pickle.load(data_file)
    COST_BOOKS = pickle.load(data_file)
    COST_RICE = pickle.load(data_file)
    COST_WHEAT = pickle.load(data_file)
    COST_BEANS = pickle.load(data_file)
    COST_SUGAR = pickle.load(data_file)
    COST_SALT = pickle.load(data_file)
    COST_OILS = pickle.load(data_file)

    # BOUNDS ON INDICATORS AND RESOURCES AND FACILITIES
    global MAX_INDICATOR, MAX_NO_INS_FACILITY, MAX_LEVELS_FACILITY, MAX_RES_VAL_VILLAGE, MAX_RES_VAL_MARKET, PRICE_VARIATION 
    MAX_INDICATOR = pickle.load(data_file)
    MAX_NO_INS_FACILITY = pickle.load(data_file)
    MAX_LEVELS_FACILITY = pickle.load(data_file)  # MAXIMUM NO OF LEVELS OF A FACILITY
    LEVEL_INCR_PROD = pickle.load(data_file)
    LEVEL_INCR_CONS = pickle.load(data_file)
    MAX_RES_VAL_VILLAGE = pickle.load(data_file)
    MAX_RES_VAL_MARKET = pickle.load(data_file)
    PRICE_VARIATION = pickle.load(data_file)

    # INFORMATION REGARDING CLUSTERS
    global VILLAGE_LEVEL 
    VILLAGE_LEVEL = pickle.load(data_file)

    # DICTIONARIES REGARDING NUTRITIVE VALUES OF FOOD ( THEY ARE IN % )
    global RICE_NUTRITION, WHEAT_NUTRITION, BEANS_NUTRITION, SUGAR_NUTRITION, SALT_NUTRITION, OILS_NUTRITION, FOOD_DIST_DICT_INIT
    RICE_NUTRITION = pickle.load(data_file)
    WHEAT_NUTRITION = pickle.load(data_file)
    BEANS_NUTRITION = pickle.load(data_file)
    SUGAR_NUTRITION = pickle.load(data_file)
    SALT_NUTRITION = pickle.load(data_file)
    OILS_NUTRITION = pickle.load(data_file)
    FOOD_DIST_DICT_INIT = pickle.load(data_file)

    #MANPOWER REGARDING CONSTANTS
    global INIT_PEOPLE, FOOD_PP, MAX_PER_FOOD_CONS,POPULATION_CHANGE
    INIT_PEOPLE = pickle.load(data_file)
    FOOD_PP= pickle.load(data_file)
    MAX_PER_FOOD_CONS = pickle.load(data_file)
    POPULATION_CHANGE = pickle.load(data_file)

    # DICTIONARY OF PARAMETERS ON WHICH THE INDICATORS DEPEND WITH THEIR WEIGHT (AS RATIO)
    global PDICT_HOUSING, PDICT_HEALTH, PDICT_NUTRITION, PDICT_EDUCATION, PDICT_TRAINING 
    PDICT_HOUSING = pickle.load(data_file)
    PDICT_HEALTH = pickle.load(data_file)
    PDICT_NUTRITION = pickle.load(data_file)
    PDICT_EDUCATION = pickle.load(data_file)
    PDICT_TRAINING = pickle.load(data_file)
    
init_cons('data.pkl')
def save_cons():
    ''' Used to save constants
    '''
    COST_HOUSE = House.get_cost_build()
    pickle.dump(COST_HOUSE, output)
    COST_HOSPITAL = Hospital.get_cost_build()
    pickle.dump(COST_HOSPITAL, output)
    COST_SCHOOL = School.get_cost_build()
    pickle.dump(COST_SCHOOL, output)
    COST_WORKSHOP = Workshop.get_cost_build()
    pickle.dump(COST_WORKSHOP, output)
    COST_FARM = Farm.get_cost_build()
    COST_FOUNTAIN = Fountain.get_cost_build()
    pickle.dump(COST_FOUNTAIN, output)
    
    # MANPOWER REQD TO BUILD EACH FACILITY PER BUILDING
    
    MANP_REQD_BUILD_HOUSE = House.get_manp_req_build()
    pickle.dump(MANP_REQD_BUILD_HOUSE, output)
    MANP_REQD_BUILD_HOSPITAL = Hospital.get_manp_req_build()
    pickle.dump(MANP_REQD_BUILD_HOSPITAL, output)
    MANP_REQD_BUILD_SCHOOL = School.get_manp_req_build()
    pickle.dump(MANP_REQD_BUILD_SCHOOL, output)
    MANP_REQD_BUILD_WORKSHOP = Workshop.get_manp_req_build()
    pickle.dump(MANP_REQD_BUILD_WORKSHOP, output)
    MANP_REQD_BUILD_FARM = Farm.get_manp_req_build()
    pickle.dump(MANP_REQD_BUILD_FARM, output)
    MANP_REQD_BUILD_FOUNTAIN = Fountain.get_manp_req_build()
    pickle.dump(MANP_REQD_BUILD_FOUNTAIN, output)
    # DICTIONARY OF ALL THE MANPOWER DISTRIBUTION CHANGES WHEN SETTING A FACILITY
    
    FACILITY_MANP_DICT_BUILD = { 'HOUSE' : MANP_REQD_BUILD_HOUSE , 'HOSPITAL' : MANP_REQD_BUILD_HOSPITAL , 'SCHOOL' : MANP_REQD_BUILD_SCHOOL , 'WORKSHOP' : MANP_REQD_BUILD_WORKSHOP , 'FARM' : MANP_REQD_BUILD_FARM , 'FOUNTAIN' : MANP_REQD_BUILD_FOUNTAIN }
    pickle.dump(FACILITY_MANP_DICT_BUILD, output)
    
    
    FACILITY_NAMES = {'HOUSE' : 'House' , 'HOSPITAL' : 'Hospital' , 'SCHOOL' : 'School' , 'WORKSHOP' : 'Workshop' , 'FARM' : 'Farm' , 'FOUNTAIN' : 'Well'}
    pickle.dump(FACILITY_NAMES, output)
    
    
    
    # DICTIONARIES OF RESOURCES REQD TO UPGRADE A FACILITY PER BUILDING  ( ASSUMPTION : NO MANPOWER IS REQD TO UPGRADE A FACILITY )
    
    COST_LEVEL_HOUSE = House.get_cost_inc_level()
    pickle.dump(COST_LEVEL_HOUSE, output)
    COST_LEVEL_HOSPITAL = Hospital.get_cost_inc_level()
    pickle.dump(COST_LEVEL_HOSPITAL, output)
    COST_LEVEL_SCHOOL = School.get_cost_inc_level()
    pickle.dump(COST_LEVEL_SCHOOL, output)
    COST_LEVEL_WORKSHOP = Workshop.get_cost_inc_level()
    pickle.dump(COST_LEVEL_WORKSHOP, output)
    COST_LEVEL_FARM = Farm.get_cost_inc_level()
    pickle.dump(COST_LEVEL_FARM, output)
    COST_LEVEL_FOUNTAIN = Fountain.get_cost_inc_level()
    pickle.dump(COST_LEVEL_FOUNTAIN, output) 
    
    
    
    
    # DICTIONARIES OF RESOURCES BEING CONSUMED BY EACH FACILITY PER BUILDING
    
    CONS_HOUSE = { }                                                                                 # Remember that resources are being                                                                                                                     # consumed by manpower also so we need to                                                                                                                       # make that thing too... a TODO for 
    pickle.dump(CONS_HOUSE, output)                                                                                                          # controller
    CONS_HOSPITAL = Hospital.get_cons_dict()
    pickle.dump(CONS_HOSPITAL, output)
    CONS_SCHOOL = School.get_cons_dict()
    pickle.dump(CONS_SCHOOL, output)
    CONS_WORKSHOP = Workshop.get_cons_dict()
    pickle.dump(CONS_WORKSHOP, output)
    CONS_FARM = Farm.get_cons_dict()
    pickle.dump(CONS_FARM, output)
    CONS_FOUNTAIN = Fountain.get_cons_dict()
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
    MANP_DIST_SCHOOL = { 'EMPLOYED PEOPLE IN SCHOOL' : 8.0 }
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
    INIT_HOUSE = 0 #4
    pickle.dump(INIT_HOUSE, output)
    INIT_HOSPITAL = 0 #2
    pickle.dump(INIT_HOSPITAL, output)
    INIT_WORKSHOP = 0
    pickle.dump(INIT_WORKSHOP, output)
    INIT_SCHOOL= 0
    pickle.dump(INIT_SCHOOL, output)
    INIT_FARM = 0
    pickle.dump(INIT_FARM, output)
    INIT_FOUNTAIN = 0
    pickle.dump(INIT_FOUNTAIN, output)
    
    
    
    
    # MONEY
    INIT_MONEY = 100 #10000
    pickle.dump(INIT_MONEY, output)
    MAX_MONEY=9999999999L
    pickle.dump(MAX_MONEY, output)
    
    # Level Of facility
    INIT_LEVEL = 0
    pickle.dump(INIT_LEVEL, output)
    
    ## VILLAGE QUANTITY
    # RESOURCES
    INIT_WATER = 25 #1000
    pickle.dump(INIT_WATER, output)
    INIT_BUILDMAT = 30 #1000
    pickle.dump(INIT_BUILDMAT, output)
    INIT_TOOLS = 45 #1000
    pickle.dump(INIT_TOOLS, output)
    INIT_MEDICINE = 0 #100
    pickle.dump(INIT_MEDICINE, output)
    INIT_BOOKS = 0
    pickle.dump(INIT_BOOKS, output)
    
    # FOOD RESOURCES
    INIT_RICE = 40 #500
    pickle.dump(INIT_RICE, output)
    INIT_WHEAT = 40 #500
    pickle.dump(INIT_WHEAT, output)
    INIT_BEANS = 10 #500
    pickle.dump(INIT_BEANS, output)
    INIT_SUGAR = 30 #500
    pickle.dump(INIT_SUGAR, output)
    INIT_SALT = 30 #500
    pickle.dump(INIT_SALT, output)
    INIT_OILS = 20 #500
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
    
    INIT_PEOPLE = 10.0 #200.0
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

def init_obj():
    """ used to initialize objects
    """
    # Initialisation of GUI elements with the desktop
    global global_time, iteration_time
    global_time = 0
    iteration_time = 0
    '''initialization of money '''
    global money
    money = Money(INIT_MONEY)
    '''facility initializaion '''
    #house
    global House, School, Hospital, Farm, Workshop, Fountain
    House = Facility('HOUSE',COST_HOUSE,COST_LEVEL_HOUSE,PROD_HOUSE,CONS_HOUSE,level = INIT_LEVEL)
    #school
    School = Facility('SCHOOL',COST_SCHOOL,COST_LEVEL_SCHOOL,PROD_SCHOOL,CONS_SCHOOL,level = INIT_LEVEL)
    #hospital
    Hospital = Facility('HOSPITAL',COST_HOSPITAL,COST_LEVEL_HOSPITAL,PROD_HOSPITAL,CONS_HOSPITAL,level = INIT_LEVEL)
    #farm
    Farm = Facility('FARM',COST_FARM,COST_LEVEL_FARM,PROD_FARM,CONS_FARM,level = INIT_LEVEL)
    #workshop
    Workshop = Facility('WORKSHOP',COST_WORKSHOP,COST_LEVEL_WORKSHOP,PROD_WORKSHOP,CONS_WORKSHOP,level = INIT_LEVEL)
    #fountain
    Fountain = Facility('FOUNTAIN',COST_FOUNTAIN,COST_LEVEL_FOUNTAIN,PROD_FOUNTAIN,CONS_FOUNTAIN,level = INIT_LEVEL)

    ''' initialization of resources   '''
    global Water, Buildmat, Tools, Medicine, Book, Rice, Wheat, Beans, Sugar, Salt, Oil
    #water
    Water=Resource('WATER',INIT_WATER,INIT_M_WATER,COST_WATER,MAX_RES_VAL_VILLAGE, MAX_RES_VAL_MARKET, PRICE_VARIATION)
    #building material
    Buildmat=Resource('BUILDING MATERIAL',INIT_BUILDMAT,INIT_M_BUILDMAT,COST_BUILDMAT)
    #tools
    Tools=Resource('TOOLS',INIT_TOOLS,INIT_M_TOOLS,COST_TOOLS)
    #medicines
    Medicine=Resource('MEDICINE',INIT_MEDICINE,INIT_M_MEDICINE,COST_MEDICINE)
    #books
    Book=Resource('BOOKS',INIT_BOOKS,INIT_M_BOOKS,COST_BOOKS)
    #rice
    Rice=Resource('RICE',INIT_RICE,INIT_M_RICE,COST_RICE)
    #wheat
    Wheat=Resource('WHEAT',INIT_WHEAT,INIT_M_WHEAT,COST_WHEAT)
    #beans
    Beans=Resource('BEANS',INIT_BEANS,INIT_M_BEANS,COST_BEANS)
    #sugar
    Sugar=Resource('SUGAR',INIT_SUGAR,INIT_M_SUGAR,COST_SUGAR)
    #salt
    Salt=Resource('SALT',INIT_SALT,INIT_M_SALT,COST_SALT)
    #oil
    Oil=Resource('OILS',INIT_OILS,INIT_M_OILS,COST_OILS)

    ''' initialization of indicators  '''
    global Housing, Health, Education, Nutrition, Training 
    #housing
    Housing=Indicator('HOUSING',INIT_HOUSING,PDICT_HOUSING)
    #health
    Health=Indicator('HEALTH',INIT_HEALTH,PDICT_HEALTH)
    #education
    Education=Indicator('EDUCATION',INIT_EDUCATION,PDICT_EDUCATION)
    #nutrition
    Nutrition=Indicator('NUTRITION',INIT_NUTRITION,PDICT_NUTRITION)
    #training
    Training=Indicator('TRAINING',INIT_TRAINING,PDICT_TRAINING)
    '''initialisation of manpower resources'''
    global ppl
    ppl = People(INIT_PEOPLE, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)



    '''initialisation of lists'''
    global resources, food_resources, facilities_list, indicators_list
    resources=(Water,Buildmat,Tools,Medicine,Book,Rice,Wheat,Beans,Sugar,Salt,Oil)  # resources list
    food_resources=(Rice,Wheat,Beans,Sugar,Salt,Oil)  #food resources list
    facilities_list=(House,School,Hospital,Workshop,Farm,Fountain) #facilities list
    indicators_list=(Housing,Nutrition,Health,Education,Training) #indicators list


    ''' List of all the sprites '''
    global house_sprite_list, hospital_sprite_list, workshop_sprite_list, school_sprite_list, farm_sprite_list, fountain_sprite_list
    house_sprite_list = []
    hospital_sprite_list = []
    workshop_sprite_list = []
    school_sprite_list = []
    farm_sprite_list = []
    fountain_sprite_list = []

    global facilities_list_sprites
    facilities_list_sprites = { 'HOUSE':house_sprite_list, 'HOSPITAL':hospital_sprite_list, 'FARM':farm_sprite_list, 'SCHOOL':school_sprite_list, 'WORKSHOP':workshop_sprite_list, 'FOUNTAIN':fountain_sprite_list}



class Indicator:
    """ A base class for one of the game indicators such as health, nutrition,
    and so on. Each indicator has a value e.g if health is 25% its value is 250
    and a dictionary of parameters->weight, which are
    responsible for indicator value. By parameter we mean the facilities and
    resources which affect the value of the indicator.
    @ivar maximum_value stores the maximum value of the indictor
    @type maximum_value integer
    """

    global MAX_INDICATOR
    maximum_value = MAX_INDICATOR
    def __init__(self, name, value, pdict):
        """ Constructor which takes the name, initial value of the indicator in variable value
        and pdict as a dictionary of parameters affecting the indicator
        it is assumed that the weights are the ratios i.e they are b/w 0and 1
        @ivar name contains the name of the indicator
        @type string
        @ivar value contains the initial value of the indicator
        @type integer
        @ivar pdict dictonary of parameters affecting the indicator
        @type pdict dictonary
        """                                                                         
        
        self.name = name
        self.set_value(value)
        self.set_parameters(pdict)
        
        
 

    def set_max(self, max_value):  
        """methods to assign maximum value that can be assigned to a indicator
        @ivar max_value contains the maximum value of the indicator
        @type integer
        """
     
        self.maximum_value = max_value


    # value methods

    def get_name(self):
        """method to get the name of the indicator
        @return name of an indicator
        @returntype string
        """

        return self.name

    def get_value(self):
        """ method to get the value of an indicator
        @return value of an indicator
        @return type real
        """

        return self._value

    def set_value(self, value):
        """ Sets the value of the indicator if its greater than the maximum value
        it makes it equal to the maximum value and if it is less than 0 than makes it 0
        @ivar value contains the value of an indicator
        @type real
        """
    
        if(value <=self.maximum_value and value >= 0):
            self._value = value
        
        elif(value<0):
            self._value=0
        
        elif(value>self.maximum_value):
            self._value=self.maximum_value

    # parameter  methods

    def set_parameters(self, pdict):
        """ Initializes the parameters dictionary that affects the value of an indicator
        @ivar pdict dictinary that affects the value of an indicator
        @type pdict dictonary
        """
    
        self._parameters = pdict

    def get_parameters(self):
        """ method to get parameters that affect the value of an indicator
        @return parameters that affect the value of an indicator
        @returntype dictonary 
        """
        return self._parameters

   
    def add_parameter(self, parameter, weight):                                
        """adds a new parameter to the dictionary, if a parameter and its value is passed
        to the function
        @ivar parameter parameter affecting the value of an indicator
        @itype prameter string
        @ivar weight value of the parameter
        @type real
        """
    
        self._parameters[parameter] = weight
  

    def rem_parameter(self, parameter):
        """method to remove a parameter from the dictionary
        @ivar parameter parameter affecting the value of an indicator
        @type parameter string
        """
    
        del self._parameters[parameter]


    def change_weight(self, parameter, weight):
        """This function is called to change the weight of a particular parameter.
        @ivar parameter parameter affecting the value of an indicator
        @type prameter string
        @ivar weight value of the parameter
        @type real 
        """
     
        self._parameters[parameter] = weight
        
 
    def turn(self, parameter_values):
        """This function is called to update the value after a turn.
        parameter_values is a dictionary of parameters and there values.
        The value of an indicator depends only on the instantaneous value of the parameters.
        The values that are passed in this dictionary should be the
        (value of the parameter)/(maximum value of parameter)
        @ivar parameter_values dictonary of parameters and their values.
        @type parameter_values dictonary
        @return updated value of the indicator
        @returntype integer
        """            
                                                              # ASSUMPTION
        
        self._value = 0
        for key in parameter_values.keys():

            if(self._parameters.has_key(key)):
                self._value += parameter_values[key] * self._parameters[key] * self.maximum_value

            if(self._value>self.maximum_value):
                self._value = self.maximum_value

            if(self._value<0):
                self._value=0
            
        return self._value


class Facility:
    """ A base class for game facilities as school, hospital and so on.
    * Each facility can have one or more buildings. 
    * Each facility has levels of building, that uses differents amounts of
    resources to be achieved.
    * Each facility spends a resource list on each turn
    * Each facility produces a resource list on each turn
    level : The level of the buildings of a particular type
    number : The number of buildings of that facility type.
    cost_build : list of amount of resources used to build a building
    cost_inc_level : list of amount of resources required to increase the
    level of building.
    production : list of amount of resources produced by the facility
    consumption : list of amount of resources consumed by the facility
    LEVEL_INCR_PROD : Percentage of increase in production with each level
    wrt base_production.
    LEVEL_INCR_CONS : Percentage of increase in consumption with each level
    wrt base_production.
    """
    global LEVEL_INCR_PROD, LEVEL_INCR_CONS
  

    def __init__(self, name, cost_build, cost_inc_level, base_production, base_consumption, _LEVEL_INCREASE_PROD = LEVEL_INCR_PROD, _LEVEL_INCREASE_CONS = LEVEL_INCR_CONS, level = 0, number = 0):
        """ Constructor that takes parameters as name of the facility, cost to build that
        facility, cost to increase the level of an already settled facility, base
        production as a dictionary of the resources being produced by the facility
        and base consumption as the resources being consumed by the facility. level is by
        default initialised to 0 and number of installations to 0.
        @ivar name facility name
        @type string
        @ivar cost_build dictionary of resources and their corresponding values required to setup facilty
        @type cost_build dictionary
        @ivar cost_inc_level dictionary of resources required to increase the level of already settled facility
        @type cost_inc_level dictionary
        @ivar base_production dictionary of resources produced by the facility
        @type base_production dictionary
        @ivar base_consumption dictionary of resources consumed by the facility
        @type dictionary
        @ivar level level of the facility of a particular type
        @type integer
        @ivar number number of the facility of a particular type
        @type integer
        @ivar LEVEL_INCR_PROD percentage of increase in production with each level
        @type LEVEL_INCR_PROD integer
        @ivar LEVEL_INCR_CONS Percentage of increase in consumption with each level wrt base_production
        @type LEVEL_INCR_CONS integer
        """

        self._name = name
        self._level = level
        self._number = number
        self.set_cost_build(cost_build)
        self.set_cost_inc_level(cost_inc_level)
        self.set_production(base_production)
        self.set_consumption(base_consumption)
        self.level_incr_prod = _LEVEL_INCREASE_PROD
        self.level_incr_cons = _LEVEL_INCREASE_CONS
        self.temp_number = 0
        self.temp_level = 0
        

    def get_name(self):
        """ method which returns the name of the facility
        THE NAME OF THE FACILITY SHOULD BE THE SAME AS THATS GIVEN IN facilities_constants.py
        IN DICTIONARY THATS GIVEN IN FACILITY_MANP_DICT A TODO OR AN ASSUMPTION FOR CONTROLLER
        @return name of the facility
        @returntype string
        """                                                                   

        return self._name
    
    def get_number(self):
        """method used to get number of facility of a particular type
        @return number of facility of a particular type
        @returntype integer
        """
        return self._number

    def change_number(self, change):
        """ changes the number of installations of a facility
        @ivar change contains the change in number of insallations of a facility
        @type change integer
        @raises Maximum_Number_Reached raised when the number of installations exceed the MAX_NO_INS_FACILITY
        """
        global MAX_NO_INS_FACILITY
        if self._number+change < 0:
            self._number = 0
        elif self._number+change > MAX_NO_INS_FACILITY[self._name]:
            self._number = MAX_NO_INS_FACILITY[self._name]
            raise Exceptions.Maximum_Number_Reached
        else :
            self._number += change

    def change_level (self,change):
        """ Changes level of a facility
        @ivar change cnatains the change in level of a facility
        @itype integer
        @raises Maximum_Level_Reached raised when the level of a facility exceeds the MAX_LEVELS_FACILITY
        """
        global MAX_LEVELS_FACILITY
        if self._level+change < 0:
            self._level = 0
        elif self._level+change > MAX_LEVELS_FACILITY:
            self._level = MAX_LEVELS_FACILITY
            raise Exceptions.Maximum_Level_Reached
        else :
            self._level += change 

    def get_level(self):
        """ method used to get level of facility
        @return level of a facility
        @returntype integer
        """
        return self._level   

    def get_level_incr_prod(self):
        """ method used to get realtive increase in level of production
        @return relative increase in level of production
        @returntype real
        """
        return self.level_incr_prod

    def get_level_incr_cons(self):
        """ method used to get relative increse in level of consumption
        @return relative increse in level of consumption
        @returntype real
        """
        return self.level_incr_cons

    def set_cost_build(self, cost_build):
        """ Sets the cost to build a facility if one needs to change the value that has
        been initialised by the constructor
        @ivar cost_build dictionary of resources to build a facility
        @type cost_build dictionary
        """

        self.cost_build = cost_build
    
    def get_cost_build(self):
        """ get cost of building a facility
        @return cost of building a facility
        @returntype dictionary
        """
        return self.cost_build

    def set_manp_req_build(self, manp_req_build):
        """ Sets the manpower requirement to build a facility
        @ivar manp_req_build manpower required to build a facility
        @type manp_req_build integer
        """

        self.manp_req_build = manp_req_build
        
    def get_manp_req_build(self):
        """Gets the manpower required to build
        """
        return self.manp_req_build

    def set_manp_rq_run(self, manp_req_run):
        """ Sets the manpower requirement to run a facility
        @ivar manp_req_run manpower required to run a facility
        @type manp_req_run integer
        """

        self.manp_req_run = manp_req_run

    def set_cost_inc_level(self, cost_inc_level):
        """ Sets the cost to increase the level of a facility that has been installed
        if one needs to change the value that has been initialised by the constructor
        @ivar cost_inc_level dictionary of resources required to increase the level of facility
        @type cost_inc_level dictionary
        """
        
        self.cost_inc_level = cost_inc_level
    
    def get_cost_inc_level(self):
        """method used to get increase in cost with updation in level
        @return increase in cost with updation in level
        @returntype dictionary
        """
        return self.cost_inc_level

    #Production and consumption methods. 

    def set_production(self, base_production):
        """ initialises the base production value of resources due to a facility
        @ivar base_production dictionary of resources produced by a facility
        @type base_production dictionary
        """
        
        self.base_production = base_production

    def set_consumption(self, base_consumption):
        """ initialises the base consumption value of a resource due to a facility
        @ivar base_consumption dictionary of resources comsumed by a facility
        @type base_consumption dictionary
        """

        self.base_consumption = base_consumption

    def add_production(self, name, value):
        """ adds a new key to the dictionary of resources being produced by the facility
        @ivar name name of resource being produced by the facility
        @typr name string
        @ivar value value of resources produced by the facility
        @type value integer
        """
        
        self.base_production[name] = value

    def rem_production(self, name):
        """ removes a key from the dictionary of resources being produced by the facility
        @ivar name name of resurce to be removed from the dictionary of resources being produced
        @type name string
        """
        
        del self.base_production[name]

    def get_prod_dict(self):
        """ method used to get production dictionary
        @return base production dictionary of a facility
        @returntype dictionary 
        """
        return self.base_production
    
    def get_cons_dict(self):
        """ method used to get consumption dictionary
        @return base consumption of a facility
        @returntype dictionary
        """ 
        return self.base_consumption

    def get_production(self):
        """ method used to get the resourceas produecd by a facility.
        Multiply base_production with number of installations and add to it the
        extra amountt of resources produced due to upgradation of the level of facility
        Multiply level * base_consumption * self. level_inr_prod
        @return dictionary of resurces produced by the facility
        @returntype dictioanry
        """
        
        production = {}
        
        for key in self.base_production.keys():
            production[key]=self._number * self.base_production[key] + (self.base_production[key] * self._number * self.level_incr_prod * self._level)
        return production

    def add_consumption(self, name, value):
        """ adds a new key to the dictionary of resources being consumed by the facility
        @ivar name name of resource being consumed by the facility
        @type name string
        @ivar value value of resource being consumed
        @type value integer
        """

        self.base_consumption[name] = value

    def rem_consumption(self, name):
        """ removes a key from the dictionary of resources being consumed by the facility
        @ivar name name of resource to be removed
        @type string
        """
        
        del self.base_consumption[name]

    def get_consumption(self):
        """ Returns the amount of resources consumed by the facility.
        Multiply base_consumption with number of installations and add to it the
        extra amt of resources being produced due to the upgradation of level of facility
        Multiply level * base_consumption * self.level_incr_cons
        @return amount of resources consumed by the facility
        @returntype dictionary
        """
        consumption = {}
        for key in self.base_consumption.keys():
            consumption[key]=self._number * self.base_consumption[key] + (self.base_consumption[key] * self._number * self.level_incr_cons * self._level)
        return consumption


    #Other Methods

    def check_resources_reqd_upgrade(self, resources):
        ''' Checks if the village has the reqd resources to build a facility
        '''
        for i in range(len(resources)):
            name = resources[i].get_name()
            if self.cost_inc_level.has_key(name):
                if resources[i].get_vquantity() < self.cost_inc_level[name]:
                    raise Exceptions.Resources_Underflow_Exception,name
        
    def update_level(self, resources,people_obj):
        """ Updates the level of facility installed, all the buildings of a facility installed
        are upgraded at the same time. First check whether the resources are sufficient. If yes
        then upgrade and return the dictionary of the resources that are required for upgradation.
        If not then raises an exception.
        @ivar resources dictionary of resources currently available
        @type resources dictionary
        @ivar people_obj object of class PEOPLE used to change populatin distribution
        @type people_obj object
        @raises Resources_Underflow_Exception when village resources are less than required resources to build a facility
        @raises Maximum_Level_Reached when maximum level of facility is reached
        @return quantity of rsources after updation
        @returnttype dictionary 
        """
        global MAX_LEVELS_FACILITY, MANP_DIST_DICT, FACILITY_MANP_DICT_CH

        self.change_level(1)
        self.change_level(-1)
        self.check_resources_reqd_upgrade(resources)
        
        for i in range(len(resources)):
            name = resources[i].get_name()
            if self.cost_inc_level.has_key(name):
                if resources[i].get_vquantity() < self.cost_inc_level[name]:
                    raise Exceptions.Resources_Underflow_Exception,args
                else:
                    resources[i].change_vquantity(-self.cost_inc_level[name])
        if self._level == MAX_LEVELS_FACILITY:
            raise Exceptions.Maximum_Level_Reached
        self.change_level(1)
        
        # Generating the change in manpower due to upgradation
        self.manp_dist_dict = MANP_DIST_DICT
        self.dict_res_change = FACILITY_MANP_DICT_CH[self._name]
        for keying in self.manp_dist_dict.keys():
            if self.dict_res_change.has_key(keying):
                self.manp_dist_dict[keying] +=  self.level_incr_prod*self._number*self.dict_res_change[keying]
        people_obj.change_population_dist(self.manp_dist_dict['TOTAL POPULATION'], self.manp_dist_dict['SHELTERED PEOPLE'], self.manp_dist_dict['EDUCATED PEOPLE'], self.manp_dist_dict['HEALTHY PEOPLE'], self.manp_dist_dict['PEOPLE FED'], self.manp_dist_dict['EMPLOYED PEOPLE IN CONSTRUCTION'], self.manp_dist_dict['EMPLOYED PEOPLE IN HOSPITAL'], self.manp_dist_dict['EMPLOYED PEOPLE IN SCHOOL'], self.manp_dist_dict['EMPLOYED PEOPLE IN WORKSHOP'], self.manp_dist_dict['EMPLOYED PEOPLE IN FARM'])
        MANP_DIST_DICT = { 'TOTAL POPULATION' : 0.0 , 'SHELTERED PEOPLE' : 0.0 , 'EDUCATED PEOPLE' : 0.0 , 'HEALTHY PEOPLE' : 0.0 , 'PEOPLE FED' : 0.0 , 'EMPLOYED PEOPLE IN CONSTRUCTION' : 0.0 , 'EMPLOYED PEOPLE IN HOSPITAL' : 0.0 , 'EMPLOYED PEOPLE IN SCHOOL' : 0.0 , 'EMPLOYED PEOPLE IN WORKSHOP' : 0.0 , 'EMPLOYED PEOPLE IN FARM' : 0.0 }
        return resources

    def check_resources_reqd_build(self, resources):
        ''' Checks if the village has the reqd resources to build a facility
        '''
        for i in range(len(resources)):
            name = resources[i].get_name()
            if self.cost_build.has_key(name):
                if resources[i].get_vquantity() < self.cost_build[name]:
                    raise Exceptions.Resources_Underflow_Exception,name
        
        
    def build_start(self, resources , people_obj):
        """ Starts Building a new installation of a facility. Check whether the resources are sufficient.
        If yes than adds one to the number of installations.If not then raises an exception
        also it returns a dictionary of resources with their values that are required to build the facility
        @ivar resources dictionary of resources currently available
        @type resources dictionary
        @ivar people_obj object of class PEOPLE used to change populatin distribution
        @type people_obj object
        @raises Resources_Underflow_Exception when village resources are less than required resources to build a facility
        @raises Low_Manpower_Resources_Exception when number of people available are less than people required to build a facility  
        @return quantity of rsources after updation
        @returnttype dictionary
        """
        self.change_number(1)
        self.change_number(-1)
        self.check_resources_reqd_build(resources)
        for i in range(len(resources)):
            name = resources[i].get_name()
            if self.cost_build.has_key(name):
                if resources[i].get_vquantity() < self.cost_build[name]:
                    raise Exceptions.Resources_Underflow_Exception,name
                else:
                    resources[i].change_vquantity(-self.cost_build[name])
        if self.check_manp_res(people_obj) < 0:
            raise Exceptions.Low_Manpower_Resources_Exception
        
        return resources

    def build_end(self, people_obj):
        """ Changes the manpower distribution that occurs when a building has been finished its construction.
        It takes an object of class people and returns the same object with the updated population distribution.
        @ivar people_obj object of class PEOPLE used to update manpower distribution
        @type people_obj object
        @return object of class people
        @returntype object
        """
        global FACILITY_MANP_DICT_BUILD
        self.dict_res_build = FACILITY_MANP_DICT_BUILD[self._name]
        change = -self.dict_res_build['EMPLOYED PEOPLE IN CONSTRUCTION']
        people_obj.change_no_of_ppl_emp_in_cons(change)
        self._number +=1
        
        return people_obj

    def stop_facility(self):
        """ Used to temporarily stop a facility in case the resources that are required to run a facility
        are low, the facility can be resumed when sufficient resources are available using resume_facility()
        """

        self.temp_number = self._number
        self.temp_level = self._level
        self._number = 0
        self._level = 0

    def resume_facility(self):
        """ Used to resume a facility that was temporarily stopped using stop_facility()
        """

        self._number = self.temp_number
        self._level = self.temp_level
        self.temp_number = 0
        self.temp_level = 0
        
    def get_original_number(self):
        """ used to get the number of a particular facility currently available
        @return number of facility
        @returntype integer
        """
        if self._number<self.temp_number:
            return self.temp_number
        else:
            return self._number

        
    def demolish(self , people_obj):
        """ Note that the demolish function is not taking any resources but releases the manpower
        allocated to run the facility. It takes an object of class people and returns the same object
        with the updated population distribution.
        @ivar people_obj object of class PEOPLE used to update manpower distribution
        @type people_obj object
        @return object of class people
        @returntype object
        """
        global FACILITY_MANP_DICT_RUN, MANP_DIST_DICT
        self.change_number(-1)
        
        self.dict_res_run = FACILITY_MANP_DICT_RUN[self._name]
        self.manp_dist_dict = MANP_DIST_DICT

        for keying in self.manp_dist_dict.keys():
            if self.dict_res_run.has_key(keying):
                self.manp_dist_dict[keying] = -self.dict_res_run[keying]

        people_obj.change_population_dist(self.manp_dist_dict['TOTAL POPULATION'], self.manp_dist_dict['SHELTERED PEOPLE'], self.manp_dist_dict['EDUCATED PEOPLE'], self.manp_dist_dict['HEALTHY PEOPLE'], self.manp_dist_dict['PEOPLE FED'], self.manp_dist_dict['EMPLOYED PEOPLE IN CONSTRUCTION'], self.manp_dist_dict['EMPLOYED PEOPLE IN HOSPITAL'], self.manp_dist_dict['EMPLOYED PEOPLE IN SCHOOL'], self.manp_dist_dict['EMPLOYED PEOPLE IN WORKSHOP'], self.manp_dist_dict['EMPLOYED PEOPLE IN FARM'])
        MANP_DIST_DICT = { 'TOTAL POPULATION' : 0.0 , 'SHELTERED PEOPLE' : 0.0 , 'EDUCATED PEOPLE' : 0.0 , 'HEALTHY PEOPLE' : 0.0 , 'PEOPLE FED' : 0.0 , 'EMPLOYED PEOPLE IN CONSTRUCTION' : 0.0 , 'EMPLOYED PEOPLE IN HOSPITAL' : 0.0 , 'EMPLOYED PEOPLE IN SCHOOL' : 0.0 , 'EMPLOYED PEOPLE IN WORKSHOP' : 0.0 , 'EMPLOYED PEOPLE IN FARM' : 0.0 }
        return people_obj

    def turn(self, resources):
        """ Updates the resources allocated to the village by increasing the value of resources that
        have been produced in the current turn and decreasing the value of the resources that have
        been consumed by the facility
        @ivar resources dictionary of resources currently available
        @type resources dictionary
        @raises Resources_Underflow_Exception when any of the available resources is less than resources required to run a faclity
        @return resources after updation
        @returntype dictionary
        """

        production = self.get_production()
        consumption = self.get_consumption()
        
        for i in range(len(resources)):
            name = resources[i].get_name()
            if production.has_key(name):
                resources[i].change_vquantity(production[name])
            if consumption.has_key(name):
                if resources[i].get_vquantity() >= consumption[name]:
                    resources[i].change_vquantity(-consumption[name])
                else:
                    raise Exceptions.Resources_Underflow_Exception,name

        return resources

    def update_manp_res(self, people_obj):
        """ Updates the manpower resources if available to build a facility.
        It takes an object of class people and returns the same object with the
        updated population distribution
        @ivar people_obj object of class PEOPLE used to update manpower distribution
        @type people_obj object
        @return object of class people
        @returntype object
        """
        global FACILITY_MANP_DICT_BUILD, FACILITY_MANP_DICT_RUN, MANP_DIST_DICT, FACILITY_MANP_DICT_CH
        self.dict_res_build = FACILITY_MANP_DICT_BUILD[self._name]
        self.dict_res_run = FACILITY_MANP_DICT_RUN[self._name]
        self.manp_dist_dict = MANP_DIST_DICT
        self.dict_res_change = FACILITY_MANP_DICT_CH[self._name]
        for keying in self.manp_dist_dict.keys():

            if self.dict_res_build.has_key(keying):
                self.manp_dist_dict[keying] = self.dict_res_build[keying]

            if self.dict_res_run.has_key(keying):
                self.manp_dist_dict[keying] = self.dict_res_run[keying]

            if self.dict_res_change.has_key(keying):
                self.manp_dist_dict[keying] = self.dict_res_change[keying] + self.level_incr_prod*self._level*self.dict_res_change[keying]

        people_obj.change_population_dist(self.manp_dist_dict['TOTAL POPULATION'], self.manp_dist_dict['SHELTERED PEOPLE'], self.manp_dist_dict['EDUCATED PEOPLE'], self.manp_dist_dict['HEALTHY PEOPLE'], self.manp_dist_dict['PEOPLE FED'], self.manp_dist_dict['EMPLOYED PEOPLE IN CONSTRUCTION'], self.manp_dist_dict['EMPLOYED PEOPLE IN HOSPITAL'], self.manp_dist_dict['EMPLOYED PEOPLE IN SCHOOL'], self.manp_dist_dict['EMPLOYED PEOPLE IN WORKSHOP'], self.manp_dist_dict['EMPLOYED PEOPLE IN FARM'])
        MANP_DIST_DICT = { 'TOTAL POPULATION' : 0.0 , 'SHELTERED PEOPLE' : 0.0 , 'EDUCATED PEOPLE' : 0.0 , 'HEALTHY PEOPLE' : 0.0 , 'PEOPLE FED' : 0.0 , 'EMPLOYED PEOPLE IN CONSTRUCTION' : 0.0 , 'EMPLOYED PEOPLE IN HOSPITAL' : 0.0 , 'EMPLOYED PEOPLE IN SCHOOL' : 0.0 , 'EMPLOYED PEOPLE IN WORKSHOP' : 0.0 , 'EMPLOYED PEOPLE IN FARM' : 0.0 }
        return people_obj

    def check_manp_res(self, people_obj):
        """ Checks whether there are enough manpower resources to build a facility
        It takes an object of class people which stores the current population distribution
        it returns value >= 0 if the facility can be settled else returns value < 0
        @ivar people_obj object of class PEOPLE used to check manpower to build facility
        @type people_obj object
        @return difference between total unemployed people and people required for the facility
        @returntype integer
        """
        global FACILITY_MANP_DICT_BUILD, FACILITY_MANP_DICT_RUN
        people_req = 0
        self.dict_res_build = FACILITY_MANP_DICT_BUILD[self._name]
        self.dict_res_run = FACILITY_MANP_DICT_RUN[self._name]

        for keying in self.dict_res_build.keys():
            people_req += self.dict_res_build[keying]

        for keying in self.dict_res_run.keys():
            people_req += self.dict_res_run[keying]

        return people_obj.get_total_no_of_ppl_un_emp() - people_req








    
class Resource:
    """A class for game resources such as food, books and so on. 
    The game will contain two quanitities of resources. One for the market.
    Other for the village. The market quantity will also determine
    buying and selling prices for every resource.
    MAX_RES_VAL : It is the maximum amount/quantity of resource that a
    village can hold. Market can hold any amount of any resource
    PRICE_VARIATION : It is the amount of variation that can occur in prices.
    Note that buying price and selling price are wrt village and not market. 
    """


    global MAX_RES_VAL_VILLAGE, MAX_RES_VAL_MARKET, PRICE_VARIATION
    def __init__(self, name, v_quantity, m_quantity, price, _MAX_RESOURCE_VAL_VILLAGE = MAX_RES_VAL_VILLAGE,_MAX_RESOURCE_VAL_MARKET = MAX_RES_VAL_MARKET,_PRICE_VAR = PRICE_VARIATION):
        """ Constructor that takes parameters as name of the resource, quantity in vilage, quantity in village,
        price of quantity and maximum limit of quantity.
        @ivar name name of the resource
        @type name string
        @ivar v_quantity quantity of resource present in the village
        @type v_quantity integer
        @ivar m_quantity quantity of resource present in the market
        @type m_quantity integer
        @ivar MAX_RESOURCE_VAL_VILLAGE maximum quantity of resource in village
        @type MAX_RESOURCE_VAL_VILLAGE integer
        @ivar MAX_RESOURCE_VAL_MARKET maximum quantity of resource in market
        @type MAX_RESOURCE_VAL_MARKET integer
        @ivar PRICE_VAR contains price variation due to change in resource quantity in village
        @type PRICE_VAR integer
        """
        
        self._name = name
        self.vquantity = v_quantity
        self.mquantity = m_quantity
        self.price = price
        self.initial_price = price
        self.max_res_value_village = _MAX_RESOURCE_VAL_VILLAGE
        self.max_res_value_market = _MAX_RESOURCE_VAL_MARKET
        self.max_price_variation = _PRICE_VAR
        
    def set_variables(self, name, v_quantity, m_quantity, price, _MAX_RESOURCE_VAL_VILLAGE = MAX_RES_VAL_VILLAGE, _MAX_RESOURCE_VAL_MARKET = MAX_RES_VAL_MARKET,_PRICE_VAR = PRICE_VARIATION ):
        """ used to set the quantity of resources present in market and village
        @ivar name name of the resource
        @type name string
        @ivar v_quantity quantity of resource present in the village
        @type v_quantity integer
        @ivar m_quantity quantity of resource present in the market
        @type m_quantity integer
        @ivar MAX_RESOURCE_VAL_VILLAGE maximum quantity of resource in village
        @type MAX_RESOURCE_VAL_VILLAGE integer
        @ivar MAX_RESOURCE_VAL_MARKET maximum quantity of resource in market
        @type MAX_RESOURCE_VAL_MARKET integer
        @ivar PRICE_VAR contains price variation due to change in resource quantity in village
        @type PRICE_VAR integer
        """
        self._name = name
        self.vquantity = v_quantity
        self.mquantity = m_quantity
        self.price = price
        self.initial_price = price
        self.max_res_value_village = _MAX_RESOURCE_VAL_VILLAGE
        self.max_res_value_market = _MAX_RESOURCE_VAL_MARKET
        self.max_price_variation = _PRICE_VAR
        
        
    def get_name(self):
        """ used to get the name of the resource
        @return name of the resource
        @returntype string
        """
        
        return self._name

    #Quantity related methods.  

    def set_vquantity(self, quantity):
        """ Sets the quantity of the resource present in the village
        @ivar quantity quatity of resources present in village
        @type quantity integer
        @raises Resources_Overflow_Exception when resource quantity exceeds the maximum limit
        @raises Resources_Underflow_Exception when resource quantity becomes negative
        """

        if quantity > self.max_res_value_village:
            self.vquantity = self.max_res_value_village
            raise Exceptions.Resources_Overflow_Exception
        if quantity < 0:
            raise Exceptions.Resources_Underflow_Exception,self._name
        
        self.vquantity = quantity

    def get_vquantity(self):
        """used to the quantity of resource present in the village
        @return quatity of resource present in village
        @returntype integer
        """
        
        return self.vquantity

    def set_mquantity(self, quantity):
        """ Sets the quantity of the resource present in the market
        @ivar quantity quntity for resource present in market
        @type quantity integer
        @raises Resources_Underflow_Exception when quantity becomes negative
        @raises Resources_Overflow_Exception when quantity exceeds maximum limit
        """

        if quantity > self.max_res_value_market:
            self.mquantity = self.max_res_value_market
            raise Exceptions.Resources_Overflow_Exception
        if quantity < 0:
            raise Exceptions.Resources_Underflow_Exception,self._name
        
        self.mquantity = quantity

    def get_mquantity(self):
        """ used to get the quantity of the resource present in the market
        @return quantity of the resource present in the market
        """
        
        return self.mquantity

    def change_vquantity(self, change):
        """ Changes the quantity of resource present in the village
        @ivar change contains the change in resource present in the village
        @type change integer
        @raises Resources_Underflow_Exception when quantity becomes negative
        @raises Resources_Overflow_Exception when quantity exceeds maximum limit
        """

        if (self.vquantity + change) > self.max_res_value_village:
            self.vquantity = self.max_res_value_village
            raise Exceptions.Resources_Overflow_Exception
        if (self.vquantity + change) < 0:
            raise Exceptions.Resources_Underflow_Exception,self._name
        
        self.vquantity = self.vquantity + change

    def change_mquantity(self, change):
        """ Changes the quantity of resource present in the market
        @ivar change contains the change in resource present in the market
        @type change integer
        @raises Resources_Underflow_Exception when quantity becomes negative
        @raises Resources_Overflow_Exception when quantity exceeds maximum limit
        """
        
        if (self.mquantity + change) > self.max_res_value_market:
            self.mquantity = self.max_res_value_market
            raise Exceptions.Resources_Overflow_Exception
        if (self.mquantity + change) < 0:
            raise Exceptions.Resources_Underflow_Exception,self._name
        
        self.mquantity = self.mquantity + change

    #Price related methods
        
    def get_price(self):
        """ used to get the price of the resource
        @return the price of the resource
        @returntype integer
        """

        return self.price

    def set_price(self, new_price):
        """ Sets a new price for the resource
        @ivar new_price price of the resource
        @type integer
        """

        self.price = new_price

    def change_price(self, change):
        """ Changes the price of a resource
        @ivar change contains the change in price of resource
        @type integer
        """

        if change > self.max_price_variation:
            change = self.max_price_variation
        self.price += change

    def update_price(self):
        """ Updates the price of a resource in accordance with the market forces
        """

        self.price = self.initial_price + (((self.max_res_value_village/2 - self.vquantity)/self.max_res_value_village) * self.max_price_variation) + (((self.max_res_value_market/2 - self.mquantity)/self.max_res_value_market) * self.max_price_variation)           
        
        if self.price < 0:
            self.price = 0
        
    #Buy and sell methods

    def buy(self, quantity, money):
        """ This method is used to buy resources from the market.
        It takes quantity that is to be bought and the total money present
        with the village as parameters. It generates exception when the market
        resources are less than that to be bought or if the village doesnot have
        enough money to buy the resources. returns the cost to buy the resources
        @ivar quantity quantity of resource to be bought from the market
        @type quantity integer
        @ivar money object of class MONEY 
        @type money object
        @raises Resources_Underflow_Exception when quantity in market is less than demand
        @raises Money_Underflow_Exception when money is not enough to buy the quantity
        """
        
        if quantity > self.mquantity:
            raise Exceptions.Resources_Underflow_Exception
        buy_price = int(self.price)
        cost = quantity * buy_price
        if cost < money.get_money():
            self.change_vquantity(quantity)
            self.change_mquantity(-quantity)
            money.change_money(-cost)
            return money
        else:
            raise Exceptions.Money_Underflow_Exception

    def sell(self, quantity, money):
        """ This method is used to sell resources to the market
        It generates an exeption when the village has less resources
        than what is demanded to sell. returns the cost that the village
        gets by selling the resources
        @ivar quantity quantity of resource to sell in the market
        @type quantity integer
        @ivar money object of class MONEY 
        @type money object
        @raises Resources_Underflow_Exception when quantity in market is less than demand
        @return money object of class MONEY
        @returntype object
        """
        if quantity > self.vquantity:
            raise Exceptions.Resources_Underflow_Exception
        sell_price = int(self.price)
        cost = quantity * sell_price
        self.change_vquantity(-quantity)
        self.change_mquantity(quantity)
        money.change_money(cost)
        return money



class People:
    """ A Class which manages the population of the village. The population has been
    classified on the basis of educated/or not, whether the person is provided food or
    not i.e he is fed or not , also on the basis of whther the person is employed or not
    and if he is employed than in which profession is he employed
    """

    def __init__(self, total_population, no_of_ppl_sheltered, no_of_ppl_educated, no_of_ppl_healthy, no_of_ppl_fed, no_of_ppl_emp_in_cons, no_of_ppl_emp_in_hospital, no_of_ppl_emp_in_school, no_of_ppl_emp_in_workshop, no_of_ppl_emp_in_farm):
        """ Constructor which initialises the initial population distribution
        @ivar total_population total population of the village
        @type total_population integer
        @ivar no_of_ppl_sheltered number of sheltered people 
        @type no_of_ppl_sheltered integer
        @ivar no_of_ppl_educated number of educated people
        @type no_of_ppl_educated integer
        @ivar no_of_ppl_healthy number of healthy people
        @type no_of_ppl_healthy integer
        @ivar no_of_ppl_fed number of people fed
        @type no_of_ppl_fed integer
        @ivar no_of_ppl_emp_in_cons number of people employed in construction
        @type no_of_ppl_emp_in_cons integer
        @ivar no_of_ppl_emp_in_hospital number of people employed in hospital
        @type no_of_ppl_emp_in_hospital integer
        @ivar no_of_ppl_emp_in_school number of people employed in school
        @type no_of_ppl_emp_in_school integer
        @ivar no_of_ppl_emp_in_workshop number of people employed in workshop
        @type no_of_ppl_emp_in_workshop integer
        @ivar no_of_ppl_emp_in_farm number of people employed in farm
        @type no_of_ppl_emp_in_farm integer
        """

        self.total_population = total_population
        self.no_of_ppl_sheltered = no_of_ppl_sheltered
        self.no_of_ppl_educated = no_of_ppl_educated
        self.no_of_ppl_healthy = no_of_ppl_healthy
        self.no_of_ppl_fed = no_of_ppl_fed
        self.no_of_ppl_emp_in_cons = no_of_ppl_emp_in_cons
        self.no_of_ppl_emp_in_hospital = no_of_ppl_emp_in_hospital
        self.no_of_ppl_emp_in_school = no_of_ppl_emp_in_school
        self.no_of_ppl_emp_in_workshop = no_of_ppl_emp_in_workshop
        self.no_of_ppl_emp_in_farm = no_of_ppl_emp_in_farm
        self.total_no_of_ppl_emp = self.no_of_ppl_emp_in_cons + self.no_of_ppl_emp_in_hospital + self.no_of_ppl_emp_in_school + self.no_of_ppl_emp_in_workshop + self.no_of_ppl_emp_in_farm
        self.total_no_of_ppl_un_emp = self.total_population - self.total_no_of_ppl_emp
        self.check_bounds()
    # Methods to assign a value to the population distribution

    def set_population_dist(self, total_population , no_of_ppl_sheltered , no_of_ppl_educated , no_of_ppl_healthy , no_of_ppl_fed , no_of_ppl_emp_in_cons , no_of_ppl_emp_in_hospital , no_of_ppl_emp_in_school , no_of_ppl_emp_in_workshop , no_of_ppl_emp_in_farm ):
        """ Changes the population distribution
        @ivar total_population total population of the village
        @type total_population integer
        @ivar no_of_ppl_sheltered number of sheltered people 
        @type no_of_ppl_sheltered integer
        @ivar no_of_ppl_educated number of educated people
        @type no_of_ppl_educated integer
        @ivar no_of_ppl_healthy number of healthy people
        @type no_of_ppl_healthy integer
        @ivar no_of_ppl_fed number of people fed
        @type no_of_ppl_fed integer
        @ivar no_of_ppl_emp_in_cons number of people employed in construction
        @type no_of_ppl_emp_in_cons integer
        @ivar no_of_ppl_emp_in_hospital number of people employed in hospital
        @type no_of_ppl_emp_in_hospital integer
        @ivar no_of_ppl_emp_in_school number of people employed in school
        @type no_of_ppl_emp_in_school integer
        @ivar no_of_ppl_emp_in_workshop number of people employed in workshop
        @type no_of_ppl_emp_in_workshop integer
        @ivar no_of_ppl_emp_in_farm number of people employed in farm
        @type no_of_ppl_emp_in_farm integer
        """
               
        self.total_population = total_population
        self.no_of_ppl_sheltered = no_of_ppl_sheltered
        self.no_of_ppl_educated = no_of_ppl_educated
        self.no_of_ppl_healthy = no_of_ppl_healthy
        self.no_of_ppl_fed = no_of_ppl_fed
        self.no_of_ppl_emp_in_cons = no_of_ppl_emp_in_cons
        self.no_of_ppl_emp_in_hospital = no_of_ppl_emp_in_hospital
        self.no_of_ppl_emp_in_school = no_of_ppl_emp_in_school
        self.no_of_ppl_emp_in_workshop = no_of_ppl_emp_in_workshop
        self.no_of_ppl_emp_in_farm = no_of_ppl_emp_in_farm
        self.total_no_of_ppl_emp = self.no_of_ppl_emp_in_cons + self.no_of_ppl_emp_in_hospital + self.no_of_ppl_emp_in_school + self.no_of_ppl_emp_in_workshop + self.no_of_ppl_emp_in_farm
        self.total_no_of_ppl_un_emp = self.total_population - self.total_no_of_ppl_emp
        self.check_bounds()

    def set_total_population(self, total_population):
        """ Changes the total population to a new value
        @ivar total_population total population of the village
        @type total_population integer
        """

        self.total_population = total_population
        self.check_bounds()

    def set_no_of_ppl_sheltered(self, no_of_ppl_sheltered):
        """ Changes the number of people sheltered to a new value
        @ivar no_of_ppl_sheltered number of sheltered people 
        @type no_of_ppl_sheltered integer
        """
    
        self.no_of_ppl_sheltered = no_of_ppl_sheltered
        self.check_bounds()

    def set_no_of_ppl_educated(self, no_of_ppl_educated):
        """ Changes the no of people educated to a new value
        @ivar no_of_ppl_educated number of educated people
        @type no_of_ppl_educated integer
        """

        self.no_of_ppl_educated = no_of_ppl_educated
        self.check_bounds()

    def set_no_of_ppl_healthy(self, no_of_ppl_healthy):
        """ Changes the no of people healthy to a new value
        @ivar no_of_ppl_healthy number of healthy people
        @type no_of_ppl_healthy integer
        """
 
        self.no_of_ppl_healthy = no_of_ppl_healthy
        self.check_bounds()

    def set_no_of_ppl_fed(self, no_of_ppl_fed):
        """ Changes the no of people fed to a new value
        @ivar no_of_ppl_fed number of people fed
        @type no_of_ppl_fed integer
        """

        self.no_of_ppl_fed = no_of_ppl_fed
        self.check_bounds()

    def set_no_of_ppl_emp_in_cons(self, no_of_ppl_emp_in_cons):
        """ Changes the no of people employed in construction to a new value
        @ivar no_of_ppl_emp_in_cons number of people employed in construction
        @type no_of_ppl_emp_in_cons integer
        """

        self.no_of_ppl_emp_in_cons = no_of_ppl_emp_in_cons
        self.update_total_no_of_ppl_employed()
        self.check_bounds()

    def set_no_of_ppl_emp_in_hospital(self, no_of_ppl_emp_in_hospital):
        """ Changes the no of people employed in hospitals to a new value
        @ivar no_of_ppl_emp_in_hospital number of people employed in hospital
        @type no_of_ppl_emp_in_hospital integer
        """
 
        self.no_of_ppl_emp_in_hospital = no_of_ppl_emp_in_hospital
        self.update_total_no_of_ppl_employed()
        self.check_bounds()

    def set_no_of_ppl_emp_in_school(self, no_of_ppl_emp_in_school):
        """ Changes the no of people employed in school to a new value
        @ivar no_of_ppl_emp_in_school number of people employed in school
        @type no_of_ppl_emp_in_school integer
        """

        self.no_of_ppl_emp_in_school = no_of_ppl_emp_in_school
        self.update_total_no_of_ppl_employed()
        self.check_bounds()

    def set_no_of_ppl_emp_in_workshop(self, no_of_ppl_emp_in_workshop):
        """ Changes the no of people employed in workshop to a new value
        @ivar no_of_ppl_emp_in_workshop number of people employed in workshop
        @type no_of_ppl_emp_in_workshop integer
        """

        self.no_of_ppl_emp_in_workshop = no_of_ppl_emp_in_workshop
        self.update_total_no_of_ppl_employed()
        self.check_bounds()

    def set_no_of_ppl_emp_in_farm(self, no_of_ppl_emp_in_farm):
        """ Changes the no of people employed in farm to a new value
        @ivar no_of_ppl_emp_in_farm number of people employed in farm
        @type no_of_ppl_emp_in_farm integer
        """

        self.no_of_ppl_emp_in_farm = no_of_ppl_emp_in_farm
        self.update_total_no_of_ppl_employed()
        self.check_bounds()

    def set_total_no_of_ppl_emp(self, total_no_of_ppl_emp):
        """ Changes the total no of people employed to a new value
        @ivar total_no_of_ppl_emp total number of people employed
        @type total_no_of_ppl_emp total integer
        """

        self.total_no_of_ppl_emp = total_no_of_ppl_emp
        self.total_no_of_ppl_un_emp = self.total_population - self.total_no_of_ppl_emp
        self.check_bounds()

    # Method definitions to change the value of population distribution


    def change_population_dist(self, change_in_total_population = 0, change_in_no_of_ppl_sheltered = 0, change_in_no_of_ppl_educated = 0, change_in_no_of_ppl_healthy = 0, change_in_no_of_ppl_fed = 0, change_in_no_of_ppl_emp_in_cons = 0, change_in_no_of_ppl_emp_in_hospital = 0, change_in_no_of_ppl_emp_in_school = 0, change_in_no_of_ppl_emp_in_workshop = 0, change_in_no_of_ppl_emp_in_farm = 0):
        """ Changes the population distribution
        @ivar change_in_total_population change in total population
        @type change_in_total_population integer
        @ivar change_in_no_of_ppl_sheltered change in number of sheltered people 
        @type change_in_no_of_ppl_sheltered integer
        @ivar change_in_no_of_ppl_educated change in number of educated people 
        @type change_in_no_of_ppl_educated integer
        @ivar change_in_no_of_ppl_healthy change in number of healthy people 
        @type change_in_no_of_ppl_healthy integer
        @ivar change_in_no_of_ppl_fed change in number of people fed 
        @type change_in_no_of_ppl_fed integer 
        @ivar change_in_no_of_ppl_emp_in_cons change in number of people employed in construction 
        @type change_in_no_of_ppl_emp_in_cons integer
        @ivar change_in_no_of_ppl_emp_in_hospital change in number of people employed in hospital 
        @type change_in_no_of_ppl_emp_in_hospital integer
        @ivar change_in_no_of_ppl_emp_in_school change in number of people employed in school 
        @type change_in_no_of_ppl_emp_in_school integer
        @ivar change_in_no_of_ppl_emp_in_workshop change in number of people employed in workshop 
        @type change_in_no_of_ppl_emp_in_workshop integer
        @ivar change_in_no_of_ppl_emp_in_farm change in number of people employed in farm 
        @type change_in_no_of_ppl_emp_in_farm integer
        """
        self.total_population += change_in_total_population
        self.no_of_ppl_sheltered += change_in_no_of_ppl_sheltered
        self.no_of_ppl_educated += change_in_no_of_ppl_educated
        self.no_of_ppl_healthy += change_in_no_of_ppl_healthy
        self.no_of_ppl_fed += change_in_no_of_ppl_fed
        self.no_of_ppl_emp_in_cons += change_in_no_of_ppl_emp_in_cons
        self.no_of_ppl_emp_in_hospital += change_in_no_of_ppl_emp_in_hospital
        self.no_of_ppl_emp_in_school += change_in_no_of_ppl_emp_in_school
        self.no_of_ppl_emp_in_workshop += change_in_no_of_ppl_emp_in_workshop
        self.no_of_ppl_emp_in_farm += change_in_no_of_ppl_emp_in_farm
        self.total_no_of_ppl_emp = self.no_of_ppl_emp_in_cons + self.no_of_ppl_emp_in_hospital + self.no_of_ppl_emp_in_school + self.no_of_ppl_emp_in_workshop + self.no_of_ppl_emp_in_farm
        self.total_no_of_ppl_un_emp = self.total_population - self.total_no_of_ppl_emp
        self.check_bounds()



    def change_total_population(self, change_in_total_population):
        """ Changes the total population 
        @ivar change_in_total_population change in total population
        @type change_in_total_population integer
        """

        self.total_population += change_in_total_population
        self.check_bounds()

    def change_no_of_ppl_sheltered(self, change_in_no_of_ppl_sheltered):
        """ Changes the number of people sheltered 
        @ivar change_in_no_of_ppl_sheltered change in number of sheltered people 
        @type change_in_no_of_ppl_sheltered integer
        """
    
        self.no_of_ppl_sheltered += change_in_no_of_ppl_sheltered
        self.check_bounds()

    def change_no_of_ppl_educated(self, change_in_no_of_ppl_educated):
        """ Changes the no of people educated 
        @ivar change_in_no_of_ppl_educated change in number of educated people 
        @type change_in_no_of_ppl_educated integer
        """

        self.no_of_ppl_educated += change_in_no_of_ppl_educated
        self.check_bounds()

    def change_no_of_ppl_healthy(self, change_in_no_of_ppl_healthy):
        """ Changes the no of people healthy 
        @ivar change_in_no_of_ppl_healthy change in number of healthy people 
        @type change_in_no_of_ppl_healthy integer
        """

        self.no_of_ppl_healthy += change_in_no_of_ppl_healthy
        self.check_bounds()

    def change_no_of_ppl_fed(self, change_in_no_of_ppl_fed):
        """ Changes the no of people fed 
        @ivar change_in_no_of_ppl_fed change in number of people fed 
        @type change_in_no_of_ppl_fed integer 
        """

        self.no_of_ppl_fed += change_in_no_of_ppl_fed
        self.check_bounds()

    def change_no_of_ppl_emp_in_cons(self, change_in_no_of_ppl_emp_in_cons):
        """ Changes the no of people employed in construction 
        @ivar change_in_no_of_ppl_emp_in_cons change in number of people employed in construction 
        @type change_in_no_of_ppl_emp_in_cons integer
        """
 
        self.no_of_ppl_emp_in_cons += change_in_no_of_ppl_emp_in_cons
        self.update_total_no_of_ppl_employed()
        self.check_bounds()

    def change_no_of_ppl_emp_in_hospital(self, change_in_no_of_ppl_emp_in_hospital):
        """ Changes the no of people employed in hospitals 
        @ivar change_in_no_of_ppl_emp_in_hospital change in number of people employed in hospital 
        @type change_in_no_of_ppl_emp_in_hospital integer
        """

        self.no_of_ppl_emp_in_hospital += change_in_no_of_ppl_emp_in_hospital
        self.update_total_no_of_ppl_employed()
        self.check_bounds()

    def change_no_of_ppl_emp_in_school(self, change_in_no_of_ppl_emp_in_school):
        """ Changes the no of people employed in school 
        @ivar change_in_no_of_ppl_emp_in_school change in number of people employed in school 
        @type change_in_no_of_ppl_emp_in_school integer
        """

        self.no_of_ppl_emp_in_school += change_in_no_of_ppl_emp_in_school
        self.update_total_no_of_ppl_employed()
        self.check_bounds()

    def change_no_of_ppl_emp_in_workshop(self, change_in_no_of_ppl_emp_in_workshop):
        """ Changes the no of people employed in workshop 
        @ivar change_in_no_of_ppl_emp_in_workshop change in number of people employed in workshop 
        @type change_in_no_of_ppl_emp_in_workshop integer
        """

        self.no_of_ppl_emp_in_workshop += change_in_no_of_ppl_emp_in_workshop
        self.update_total_no_of_ppl_employed()
        self.check_bounds()

    def change_no_of_ppl_emp_in_farm(self, change_in_no_of_ppl_emp_in_farm):
        """ Changes the no of people employed in farm 
        @ivar change_in_no_of_ppl_emp_in_farm change in number of people employed in farm 
        @type change_in_no_of_ppl_emp_in_farm integer
        """

        self.no_of_ppl_emp_in_farm += change_in_no_of_ppl_emp_in_farm
        self.update_total_no_of_ppl_employed()
        self.check_bounds()

    def change_total_no_of_ppl_emp(self, change_in_total_no_of_ppl_emp):
        """ Changes the total no of people employed
        @ivar change_in_total_no_of_ppl_emp change in total number of people employed
        @type change_in_total_no_of_ppl_emp integer
        """
 
        self.total_no_of_ppl_emp += total_no_of_ppl_emp
        self.check_bounds()


    def update_total_no_of_ppl_employed(self):
        """ Updates the total number of people employed 
        """

        self.total_no_of_ppl_emp = self.no_of_ppl_emp_in_cons + self.no_of_ppl_emp_in_hospital + self.no_of_ppl_emp_in_school + self.no_of_ppl_emp_in_workshop + self.no_of_ppl_emp_in_farm
        self.total_no_of_ppl_un_emp = self.total_population - self.total_no_of_ppl_emp
        self.check_bounds()

    # Method definitions that return the population distribution

    def get_total_population(self):
        """ used to get the value of total population
        @return value of total population
        @returntype integer
        """

        return self.total_population 

    def get_no_of_ppl_sheltered(self):
        """ used to get the number of people sheltered 
        @return number of people sheltered 
        @returntype integer
        """
    
        return self.no_of_ppl_sheltered 

    def get_no_of_ppl_educated(self):
        """ used to get the number of people educated 
        @return number of people educated
        @returntype integer
        """

        return self.no_of_ppl_educated 

    def get_no_of_ppl_healthy(self):
        """ used to get the number of people healthy
        @return
        @returntype integer
        """

        return self.no_of_ppl_healthy 

    def get_no_of_ppl_fed(self):
        """ used to get the number of people fed
        @return number of people healthy
        @returntype integer
        """

        return self.no_of_ppl_fed 

    def get_no_of_ppl_emp_in_cons(self):
        """ used to get the number of people employed in construction 
        @return number of people employed in construction 
        @returntype integer
        """

        return self.no_of_ppl_emp_in_cons 
        
    def get_no_of_ppl_emp_in_hospital(self):
        """ used to get the number of people employed in hospitals 
        @return number of people employed in hospitals 
        @returntype integer
        """

        return self.no_of_ppl_emp_in_hospital 
        
    def get_no_of_ppl_emp_in_school(self):
        """ used to get the number of people employed in school 
        @return number of people employed in school 
        @returntype integer
        """

        return self.no_of_ppl_emp_in_school 
        
    def get_no_of_ppl_emp_in_workshop(self):
        """ used to get the number of people employed in workshop 
        @return number of people employed in workshop
        @returntype integer
        """

        return self.no_of_ppl_emp_in_workshop 
        
    def get_no_of_ppl_emp_in_farm(self):
        """ used to get the number of people employed in farm 
        @return number of people employed in farm 
        @returntype integer
        """

        return self.no_of_ppl_emp_in_farm 
        
    def get_total_no_of_ppl_emp(self):
        """ used to get the total number of people employed 
        @return total number of people employed
        @returntype integer
        """

        return self.total_no_of_ppl_emp

    def get_total_no_of_ppl_un_emp(self):
        """ used to get total number of people unemployed
        @return total number of people unemployed
        @returntype integer
        """

        return self.total_no_of_ppl_un_emp
    
    # Method to check Bounds
    
    def check_bounds(self):
        """ Method to check bounds on all the variables regarding population distribution
        """
        if(self.no_of_ppl_sheltered > self.total_population):
            self.no_of_ppl_sheltered = self.total_population
        if(self.no_of_ppl_sheltered < 0):
            self.no_of_ppl_sheltered = 0
    
        if(self.no_of_ppl_educated > self.total_population):
            self.no_of_ppl_educated = self.total_population
        if(self.no_of_ppl_educated < 0):
            self.no_of_ppl_educated = 0
    
        if(self.no_of_ppl_healthy > self.total_population):
            self.no_of_ppl_healthy = self.total_population
        if(self.no_of_ppl_healthy < 0):
            self.no_of_ppl_healthy = 0
    
        if(self.no_of_ppl_fed > self.total_population):
            self.no_of_ppl_fed = self.total_population
        if(self.no_of_ppl_fed < 0):
            self.no_of_ppl_fed = 0
    
        if(self.no_of_ppl_emp_in_cons > self.total_population):
            self.no_of_ppl_emp_in_cons = self.total_population
        if(self.no_of_ppl_emp_in_cons < 0):
            self.no_of_ppl_emp_in_cons = 0
    
        if(self.no_of_ppl_emp_in_hospital > self.total_population):
            self.no_of_ppl_emp_in_hospital = self.total_population
        if(self.no_of_ppl_emp_in_hospital < 0):
            self.no_of_ppl_emp_in_hospital = 0
    
        if(self.no_of_ppl_emp_in_school > self.total_population):
            self.no_of_ppl_emp_in_school = self.total_population
        if(self.no_of_ppl_emp_in_school < 0):
            self.no_of_ppl_emp_in_school = 0
    
        if(self.no_of_ppl_emp_in_workshop > self.total_population):
            self.no_of_ppl_emp_in_workshop = self.total_population
        if(self.no_of_ppl_emp_in_workshop < 0):
            self.no_of_ppl_emp_in_workshop = 0

        if(self.no_of_ppl_emp_in_farm > self.total_population):
            self.no_of_ppl_emp_in_farm = self.total_population
        if(self.no_of_ppl_emp_in_farm < 0):
            self.no_of_ppl_emp_in_farm = 0
            
        if(self.total_no_of_ppl_emp > self.total_population):
            self.total_no_of_ppl_emp = self.total_population
        if(self.total_no_of_ppl_emp < 0):
            self.total_no_of_ppl_emp = 0

        if(self.total_no_of_ppl_un_emp > self.total_population):
            self.total_no_of_ppl_un_emp = self.total_population
        if(self.total_no_of_ppl_un_emp < 0):
            self.total_no_of_ppl_un_emp = 0
   
    def update_turn(self,resources,facilities_list):
        """ Method to calculate the amount of food items consumed by the manpower and the
        water consumption make the changes in resources and then return resources only
        @ivar resources dictionary of resource present in the village
        @type resources dictionary
        @ivar facilities_list dictionary of facilities available
        @type facilities_list dictionary
        @return resources after updation
        @returntype dictionary
        """
        global MAX_PER_FOOD_CONS, FOOD_PP, FOOD_DIST_DICT, MANP_CH_HOUSE, MANP_CH_HOSPITAL, MANP_CH_SCHOOL
        food = 0.0                    

        for i in range(len(resources)):
            name = resources[i].get_name()
            temp=FOOD_DIST_DICT
            if temp.has_key(name):
                temp[name]=resources[i].get_vquantity()
                food+=temp[name]
        
        food_temp = food*MAX_PER_FOOD_CONS/100
        
        if food_temp > (FOOD_PP * self.total_population):
            food_temp = (FOOD_PP) * self.total_population

        self.no_of_ppl_fed = int(food_temp/FOOD_PP)
        food_temp = self.no_of_ppl_fed*FOOD_PP
        ratio = food_temp/food

        for key in temp.keys():
            temp[key] -= ratio*temp[key]
        
            for i in range(len(resources)):
                name = resources[i].get_name()
                if temp.has_key(name):   
                    resources[i].set_vquantity(temp[name])

        for i in range(len(resources)):
            name = resources[i].get_name()
            if name == 'WATER':
                resources[i].change_vquantity(-ratio*resources[i].get_vquantity())

        for i in range(len(facilities_list)):
            name = facilities_list[i].get_name()
            if name == 'HOUSE':
                self.no_of_ppl_sheltered = facilities_list[i].get_number() * MANP_CH_HOUSE['SHELTERED PEOPLE']*(1+facilities_list[i].get_level()*facilities_list[i].level_incr_prod)

        
        for i in range(len(facilities_list)):
            name = facilities_list[i].get_name()
            if name == 'HOSPITAL':
                self.no_of_ppl_healthy = facilities_list[i].get_number() * MANP_CH_HOSPITAL['HEALTHY PEOPLE']*(1+facilities_list[i].get_level()*facilities_list[i].level_incr_prod)


        for i in range(len(facilities_list)):
            name = facilities_list[i].get_name()
            if name == 'SCHOOL':
                self.no_of_ppl_educated = facilities_list[i].get_number() * MANP_CH_SCHOOL['EDUCATED PEOPLE']*(1+facilities_list[i].get_level()*facilities_list[i].level_incr_prod)

        self.check_bounds()
        return resources


   

    

    


class Money:
    """ Class to manage the money present with the village
    """
    def __init__(self,money):
        """ Initialises the variable money with the initial amount which is
        to be given to the Village
        @ivar money amount of money for village
        @type money integer
        """
        self.money = money
        self.check_bounds()

    def set_money(self, money):
        """ set the amount of money
        @ivar money amount of money to be updated
        @type money integer
        """
        self.money=money
        self.check_bounds()

    def change_money(self,mchange):
        """ change the value of the money
        @ivar mchange change in amount of money present in the village
        @type mchange integer
        """
        self.money +=mchange
        self.check_bounds()

    def get_money(self):
        """ used to get money in village
        @return money present in the village
        """
        return self.money
    
    def check_bounds(self):
        """ method t check the bound on variable money
        @raises Money_Underflow_Exception when money becomes negative
        """
        global MAX_MONEY 
        if(self.money > MAX_MONEY):
            self.money = MAX_MONEY
        if(self.money < 0):
            raise Exceptions.Money_Underflow_Exception
        
class game_time:
    def __init__(self,conversion_factor=3000):
        self.level_iteration_time=0
        self.level_global_time=0
        self.clock = pygame.time.Clock()
        self.years=0
        self.months=0
        self.total_days = 0
        self.days=0
        self.time_help=0                                 #this is not of any use right now, I have put it for future use, so no need to worry now
        self.conversion_factor= conversion_factor       #this variable allows you to decide how many seconds(in milli) should be counted as a day      
        self.help_update_value=0                    #it is used while updating the value of days etc
        
    def update_level_time(self,check_flag=True):
        if check_flag==True:
            #print self.level_global_time
            #print global_time
            #print "help ",self.time_help
            #print "inter",self.level_iteration_time
            if True:
                self.level_iteration_time=self.clock.tick()
                if self.level_iteration_time<1000:
                    #print 'global time updated'
                    self.level_global_time+=self.level_iteration_time
        
                
        self.update_converted_global_time()
                
    def get_global_time(self):
        return self.level_global_time
    
    def get_iteration_time(self):
        return self.level_iteration_time
            
    def reset_time(self):
        self.level_iteration_time=0
        self.level_global_time=0
        self.years=0
        self.total_days = 0
        self.months=0
        self.days=0
        self.help_update_value=0
        
    def update_converted_global_time(self):
        self.time_help=self.level_global_time-self.help_update_value
        
        #self.years=(self.level_global_time/(3000*365))
        #self.time_help=int(self.level_global_time%(3000*365))
        #print 'time_help is ', self.time_help
        #print 'conversion factor is',self.conversion_factor
        if self.time_help>=self.conversion_factor:
            self.days=int(self.days+(self.time_help/self.conversion_factor))
            self.total_days += int((self.time_help/self.conversion_factor))
            self.help_update_value=self.level_global_time
        #print 'days in updated part is', self.days
        if self.days>31:
            self.months=int(self.months+(self.days/31))
            self.days=int(self.days%31)
        if self.months>12:
            self.years=int(self.years+(self.months/12))
            self.months=int(self.months%12)
            
    def forced_game_time_update(self,new_global_time):
        self.level_global_time = new_global_time
        
            
    def get_days(self):
        return self.days
    def get_total_days(self):
        return self.total_days
    def get_months(self):
        return self.months
    def get_years(self):
        return self.years
        
game_controller=game_time()


init_obj()
