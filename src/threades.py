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

#from model import *
import model
import Exceptions                 
import threading   
import random   
from time import sleep,time,ctime
#import texts_spa
#import texts_eng

# import statements for animation classes
import pygame
import os
from pygame.locals import *
pygame.init()
pygame.mixer.init()
#from load_images import *
import game_events
import load_images
import pickle
import glob
from texts_spa import setup_text, upgrade_fac_text, buysell_exceptions, setup_fac_exceptions, upgrade_fac_exceptions, fac_running_exceptions, setup_format_text, upgrade_format_text
from texts_eng import setup_text, upgrade_fac_text, buysell_exceptions, setup_fac_exceptions, upgrade_fac_exceptions, fac_running_exceptions, setup_format_text, upgrade_format_text
#import proceduralFlow


original_screen_size = [1200.0,900.0]

import gui
#from gui import *
import defaultStyle


pygame.display.init()

try:

    display_info = pygame.display.Info()
    new_screen_size = [display_info.current_w,display_info.current_h]
    
except:
    
    new_screen_size = [800,600]
    
new_screen_size = [800,600]

global screen   
if model.FLAG_XO:
    global screen
    new_screen_size[1] -= 80.0/900.0*new_screen_size[1]
    screen = pygame.display.set_mode(new_screen_size,SRCALPHA,32)
else:
    
    #screen = pygame.display.set_mode(new_screen_size,FULLSCREEN|SRCALPHA,32)
    screen = pygame.display.set_mode(new_screen_size,SRCALPHA,32)


defaultStyle.init(gui)

desktop = gui.Desktop()

###### FLAGS ####

GAME_EXIT_FLAG = False
# Facility placement flag
buildFacilityPlacementFlag = ""

# Level start Facility build flag 
levelStartFacilityBuildFlag = 0
levelStartUpdateFlag = True

#Screen Initialization Flags
total_update_flag = True
panel_update_flag = True
map_update_flag = True
top_update_flag = True
facilities_update_flag = True   
game_save_flag = False

PLACING_LIST_TEMP = []
current_level = 0
SOUND_PATH = os.path.join('sounds','effects')
SOUND_VOLUME = [1,1]  #max Vol is [1,1] i.e [left,right]

def initialize_facilities(autobuild_flag = True):
    
    model.ppl.change_total_population(1000)
    global levelStartFacilityBuildFlag
    global levelStartUpdateFlag
    levelStartUpdateFlag = False
    global PLACING_LIST_TEMP

    PLACING_DATA_LIST = PLACING_LIST_TEMP
    new_list = []

    HOUSE_NO = model.INIT_HOUSE
    HOSP_NO = model.INIT_HOSPITAL
    SCHOOL_NO = model.INIT_SCHOOL
    FARM_NO = model.INIT_FARM
    FOUNTAIN_NO = model.INIT_FOUNTAIN
    WORKS_NO = model.INIT_WORKSHOP
    
    
    for i in range(len(PLACING_DATA_LIST)):
        if PLACING_DATA_LIST[i][0] == 'HOUSE' and HOUSE_NO>0:
            build_facility(model.House,PLACING_DATA_LIST = PLACING_DATA_LIST[i], autobuild_flag = autobuild_flag)
            HOUSE_NO = HOUSE_NO -1
            levelStartFacilityBuildFlag +=1
            new_list.append(PLACING_DATA_LIST[i])
            
        if PLACING_DATA_LIST[i][0] == 'HOSPITAL' and HOSP_NO>0:
            build_facility(model.Hospital,PLACING_DATA_LIST[i], autobuild_flag = autobuild_flag)
            HOSP_NO = HOSP_NO -1
            levelStartFacilityBuildFlag +=1
            new_list.append(PLACING_DATA_LIST[i])
            
        if PLACING_DATA_LIST[i][0] == 'SCHOOL' and SCHOOL_NO>0:
            build_facility(model.School,PLACING_DATA_LIST[i], autobuild_flag = autobuild_flag)
            SCHOOL_NO = SCHOOL_NO -1
            levelStartFacilityBuildFlag +=1
            new_list.append(PLACING_DATA_LIST[i])
            
        if PLACING_DATA_LIST[i][0] == 'FARM' and FARM_NO>0:
            build_facility(model.Farm,PLACING_DATA_LIST[i], autobuild_flag = autobuild_flag)
            FARM_NO = FARM_NO -1
            levelStartFacilityBuildFlag +=1
            new_list.append(PLACING_DATA_LIST[i])
            
        if PLACING_DATA_LIST[i][0] == 'FOUNTAIN' and FOUNTAIN_NO>0:
            build_facility(model.Fountain,PLACING_DATA_LIST[i], autobuild_flag = autobuild_flag)
            FOUNTAIN_NO = FOUNTAIN_NO -1
            levelStartFacilityBuildFlag +=1
            new_list.append(PLACING_DATA_LIST[i])
            
        if PLACING_DATA_LIST[i][0] == 'WORKSHOP' and WORKS_NO>0:
            build_facility(model.Workshop,PLACING_DATA_LIST[i], autobuild_flag = autobuild_flag)
            WORKS_NO = WORKS_NO -1
            levelStartFacilityBuildFlag +=1
            new_list.append(PLACING_DATA_LIST[i])
  
    #reload_placing_data_list()
    model.ppl.change_total_population(-1000)
    
    PLACING_LIST_TEMP = new_list
    transform_obj.focus_at((1000,2000))
    transform_obj.set_ratio(0.5)
    calculate_indicators_starting()

# A Switch for pausing the update thread
update_thread_pause = True


''' Utility Functions '''

def stop_facility(facility_obj,name_res = ''):
    ''' Thread to stop a facility it resumes the facility when the village
    has enough model.resources to run the facility
    '''
    text = fac_running_exceptions['insufficient_res']%{'facility':model.FACILITY_NAMES[facility_obj.get_name()],'resource':str(name_res).lower()}
    message.push_message(text,'high')
    event = game_events.Event(type = game_events.STOPFACILITYEVENT, facility_name = facility_obj.get_name())
    game_events.EventQueue.add(event)
    res_cost = facility_obj.get_consumption()
    facility_obj.stop_facility()
    a=1
    while True:
        a=0
        for i in range(len(model.resources)):
            name = model.resources[i].get_name()
            if res_cost.has_key(name):
                if model.resources[i].get_vquantity() < res_cost[name]:
                    a=1
        if a==0:
            break
        if GAME_EXIT_FLAG:
            return
        sleep(1)
        if GAME_EXIT_FLAG:
            return
        sleep(1)
        if GAME_EXIT_FLAG:
            return
        
    facility_obj.resume_facility()
    text = fac_running_exceptions['resume']%{'facility':model.FACILITY_NAMES[facility_obj.get_name()]}
    message.push_message(text,'low')
    event = game_events.Event(type = game_events.RESUMEFACILITYEVENT, facility_name = facility_obj.get_name())
    game_events.EventQueue.add(event)
    
def get_setup_text(facility_obj):
    
    ty = model.text_file.setup_format_text[0]
    
    _name_dic = {'WATER':model.text_file.list_gen_res[0]
                 ,'BUILDING MATERIAL':model.text_file.list_gen_res[1]
                 ,'TOOLS':model.text_file.list_gen_res[2]
                 ,'MEDICINE':model.text_file.list_gen_res[3]
                 ,'BOOKS':model.text_file.list_gen_res[4]
                 ,'HOUSE':model.text_file.facilities_list[0]
                 ,'HOSPITAL':model.text_file.facilities_list[1]
                 ,'WORKSHOP':model.text_file.facilities_list[2]
                 ,'SCHOOL':model.text_file.facilities_list[3]
                 ,'FOUNTAIN':model.text_file.facilities_list[4]
                 ,'FARM':model.text_file.facilities_list[5]
                  }
    
    
    facility=_name_dic[str(facility_obj.get_name())]
    number = str(int(facility_obj.get_original_number()))
    costbuild = facility_obj.get_cost_build() or model.text_file.resources_text[1]
    costrun = facility_obj.get_cons_dict() or model.text_file.resources_text[1]
    manbuild = str(int(model.FACILITY_MANP_DICT_BUILD[facility_obj.get_name()]['EMPLOYED PEOPLE IN CONSTRUCTION']))
    try:
        manrun = model.FACILITY_MANP_DICT_RUN[facility_obj.get_name()]['EMPLOYED PEOPLE IN %(facility)s'%{'facility':facility}]
    except:
        manrun = '0'
    rem_build_mat = int(model.resources[1].get_vquantity()) - int(costbuild['BUILDING MATERIAL'])
    rem_tools = int(model.resources[2].get_vquantity()) - int(costbuild['TOOLS'])
    rem_water = int(model.resources[0].get_vquantity()) - int(costbuild['WATER'])
    
    if rem_build_mat < 0:
        resafter = model.text_file.setup_fac_exceptions['low_resource']%{'resource':'bricks'}
    elif rem_tools < 0:
        resafter = model.text_file.setup_fac_exceptions['low_resource']%{'resource':'tools'}
    elif rem_water < 0:
        resafter = model.text_file.setup_fac_exceptions['low_resource']%{'resource':'water'}
    else:
        resafter = model.text_file.list_gen_res[1]+':'+ str(rem_build_mat)+ model.text_file.list_gen_res[2]+':'+str(rem_tools)+model.text_file.list_gen_res[0]+':'+str(rem_water)
    
    strcostbuild = ''
    strcostrun = ''
     
    
    if type(costbuild) != str:
        for cost in costbuild.iteritems():
            strcostbuild+=' '+str(cost[1]).lower()+' '+str(_name_dic[cost[0]])
    else:
        strcostbuild=costbuild
    if type(costrun) != str:
        for cost in costrun.iteritems():
            strcostrun+=' '+str(cost[1]).lower()+' '+str(_name_dic[cost[0]])
    else:
        strcostrun=costrun
    
    return ty%{'facility':facility,'number':number,'costbuild':strcostbuild,'costrun':strcostrun,'manbuild':manbuild,'manrun':manrun,'resafter':resafter}

def get_upgrade_text(facility_obj):
    
    ty = model.text_file.upgrade_format_text[0]
    
    _name_dic = {'WATER':model.text_file.list_gen_res[0]
                 ,'BUILDING MATERIAL':model.text_file.list_gen_res[1]
                 ,'TOOLS':model.text_file.list_gen_res[2]
                 ,'MEDICINE':model.text_file.list_gen_res[3]
                 ,'BOOKS':model.text_file.list_gen_res[4]
                 ,'HOUSE':model.text_file.facilities_list[0]
                 ,'HOSPITAL':model.text_file.facilities_list[1]
                 ,'WORKSHOP':model.text_file.facilities_list[2]
                 ,'SCHOOL':model.text_file.facilities_list[3]
                 ,'FOUNTAIN':model.text_file.facilities_list[4]
                 ,'FARM':model.text_file.facilities_list[5]
                  }
    try:
        assert (facility_obj.get_level()<3)
        text = model.text_file.upgrade_text[facility_obj.get_name()][facility_obj.get_level()]
        facility=_name_dic[facility_obj.get_name()]
        number = str(int(facility_obj.get_original_number()))
        cost_upgrade = facility_obj.get_cost_inc_level()
        rem_build_mat = int(model.resources[1].get_vquantity()) - int(cost_upgrade['BUILDING MATERIAL'])
        rem_tools = int(model.resources[2].get_vquantity()) - int(cost_upgrade['TOOLS'])
        if rem_build_mat < 0:
            resafter = model.text_file.setup_fac_exceptions['low_resource']%{'resource':'bricks'}
        if rem_tools < 0 :
            resafter = model.text_file.setup_fac_exceptions['low_resource']%{'resource':'tools'}
        else:
            resafter = model.text_file.list_gen_res[1]+':'+ str(rem_build_mat)+ model.text_file.list_gen_res[2]+':'+str(rem_tools)
        strcostupgrade=''
        
        for cost in cost_upgrade.iteritems():
            strcostupgrade+=' '+str(cost[1])+' '+_name_dic[str(cost[0])]

    except:
        resafter=model.text_file.upgrade_fac_exceptions['max_level']
        return resafter
  
    return ty%{'text':text,'number':number,'facility':facility,'costupgrade':strcostupgrade,'resafter':resafter}

def set_build_facility_placement_flag(facility_obj = None):
    global buildFacilityPlacementFlag
    if facility_obj:
        buildFacilityPlacementFlag = facility_obj.get_name()
    else :
        buildFacilityPlacementFlag = ""
    
def build_placed_facility(facility_name, autobuild_flag, PLACING_DATA_LIST):
    '''Builds the placed facility according to placed position
    Args:
     facility_obj: The to be built facility object
     place_facility_thread: Thread for placing facility
    '''
    global PLACING_LIST_TEMP
    PLACING_LIST_TEMP.append(PLACING_DATA_LIST)
    
    facility_name = PLACING_DATA_LIST[0]
    rect_obj = PLACING_DATA_LIST[1]
    
    place_pos_x = rect_obj[0]
    place_pos_y = rect_obj[1]
        
    if autobuild_flag == False:
        audio.play_sound('build')       
        
    if facility_name == 'HOUSE':
        images_obj.initialize_facility('HOUSE')
        sprite = House_sprite((place_pos_x,place_pos_y))
        model.house_sprite_list.append(sprite)
        
    if facility_name == 'HOSPITAL':
        images_obj.initialize_facility('HOSPITAL')
        sprite = Hospital_sprite((place_pos_x,place_pos_y))
        model.hospital_sprite_list.append(sprite)
        
    if facility_name == 'WORKSHOP':
        images_obj.initialize_facility('WORKSHOP')
        sprite = Workshop_sprite((place_pos_x,place_pos_y))
        model.workshop_sprite_list.append(sprite)
        
    if facility_name == 'SCHOOL':
        images_obj.initialize_facility('SCHOOL')
        sprite = School_sprite((place_pos_x,place_pos_y))
        model.school_sprite_list.append(sprite)
        
    if facility_name == 'FARM':
        images_obj.initialize_facility('FARM')
        sprite = Farm_sprite((place_pos_x,place_pos_y))
        model.farm_sprite_list.append(sprite)
        
    if facility_name == 'FOUNTAIN':
        images_obj.initialize_facility('FOUNTAIN')
        sprite = Fountain_sprite((place_pos_x,place_pos_y))
        model.fountain_sprite_list.append(sprite)
    add_sprite_all(sprite)
    add_sprite_facilities(sprite)
    
    # Generating villagers for each facility
    speeds = [[2,0],[-2,0],[0,2],[0,-2]]
    facility_obj = model.facilities_list[0]
    for i in range(len(model.facilities_list)):
        if model.facilities_list[i].get_name() == facility_name:
            facility_obj = model.facilities_list[i]
    for i in range(int(random.random()*5)):
        #print attribute
        dir = int(random.random()*4)
        villager = Villager((place_pos_x-500,place_pos_y-500,place_pos_x+500,place_pos_y+500))
        villager.set_speed(speeds[dir])
        villager.add(villagers,all)
        
    check_collide_villager(sprite) # Function to check if a sprite collides with the position of a villager
    
        
def place_facility_collide_check(rect_obj):
    FACILITY_RECT_LIST = []
    
    (rect_obj[0],rect_obj[1]) = transform_obj.inverse_transform_cordinate((rect_obj[0],rect_obj[1]))

    market_rect = pygame.Rect(int(2800*(1200.0/new_screen_size[0])),int(2500*(900.0/new_screen_size[1])),int(516*(1200.0/new_screen_size[0])),int(600*(900.0/new_screen_size[1])))  
    
    for key in model.facilities_list_sprites.values():
        for i in range(len(key)):
            FACILITY_RECT_LIST.append(transform_obj.inverse_transform_rect(key[i].rect))
            
    result = rect_obj.collidelist(FACILITY_RECT_LIST)
    if rect_obj.colliderect(market_rect):
        result = 1
        
    if result == -1:
        return False
    else:
        return True
                                        
    
def build_facility(facility_obj, PLACING_DATA_LIST = [], list_food = model.DEF_FARM_PROD, autobuild_flag = False):
    ''' Thread to build a new building of any facility
    Args:
     facility_obj:Facility object to be built
     list_food:
    '''
    
    if facility_obj.get_number() == 0:
        
        if facility_obj.get_original_number() > 0:
            text = model.text_file.setup_fac_exceptions['stopped']
            message.push_message(text,'high')
            return text
    try:
        
        if facility_obj.check_manp_res(model.ppl)<0:
            raise Exceptions.Low_Manpower_Resources_Exception
    
        model.resources=facility_obj.build_start(model.resources,model.ppl)
        
        if facility_obj.get_name() == 'FARM':

            qrice = int(list_food[0])*model.MAX_FOOD_PROD_PER_FARM/100
            qwheat = int(list_food[1])*model.MAX_FOOD_PROD_PER_FARM/100
            qbeans = int(list_food[2])*model.MAX_FOOD_PROD_PER_FARM/100
            prod = facility_obj.get_prod_dict()
            prod['RICE'] = (prod['RICE']*facility_obj.get_number() + qrice)/(facility_obj.get_number() + 1)
            prod['WHEAT'] = (prod['WHEAT']*facility_obj.get_number() + qwheat)/(facility_obj.get_number() + 1)
            prod['BEANS'] = (prod['BEANS']*facility_obj.get_number() + qbeans)/(facility_obj.get_number() + 1)
            facility_obj.set_production(prod)
               
        model.ppl = facility_obj.update_manp_res(model.ppl)
        
        
    except Exceptions.Resources_Underflow_Exception,args:
        res = str(args).lower()
        text = model.text_file.setup_fac_exceptions['low_resource']%{'resource':res}
        return text
    except Exceptions.Low_Manpower_Resources_Exception:
        text = model.text_file.setup_fac_exceptions['low_manpower']
        return text
    except Exceptions.Maximum_Number_Reached:
        text = model.text_file.setup_fac_exceptions['max_limit']
        return text
    if autobuild_flag == False:
        set_build_facility_placement_flag(facility_obj)
    else:
        build_placed_facility("",True,PLACING_DATA_LIST)
    
    return model.text_file.setup_text[4]

def check_collide_villager(sprite):
    ''' Checks if an installation collides with a position of a villager, If yes, then it deletes 
    the villager sprite and create similar villager sprites at safe positions
    '''
    
    while True:
        
        sprites_list = pygame.sprite.spritecollide(sprite,villagers,False)
        if sprites_list:
            for sprites in sprites_list:
                new_sprite = Villager(sprites.get_attributes())
                sprites.remove(all,villagers)
                sprites.kill()
                
                new_sprite.add(villagers,all)    
        else:
            break
        
def build_end_facility(facility_obj):
    global levelStartFacilityBuildFlag
    model.ppl = facility_obj.build_end(model.ppl)
    event = game_events.Event(type = game_events.BUILDFACILITYEVENT, facility_name = facility_obj.get_name())
    game_events.EventQueue.add(event)
    if levelStartFacilityBuildFlag > 0:
        levelStartFacilityBuildFlag -= 1
        if levelStartFacilityBuildFlag == 0:
            model.resources = model.ppl.update_turn(model.resources,model.facilities_list)
    calculate_indicators_starting()
    

def upgrade_facility(facility_obj):
    ''' Upgrades a facility
    COMMENT : change the view of facility if you want to do so
    '''
    if facility_obj.get_number() == 0:
        
        if facility_obj.get_original_number() > 0:
            text = model.text_file.upgrade_fac_exceptions['stopped']
            message.push_message(text,'high')
            return text
        text = model.text_file.upgrade_fac_exceptions['none_setup']
        return text
        
    #global model.resources
    try:
        model.resources = facility_obj.update_level(model.resources,model.ppl)
    except Exceptions.Resources_Underflow_Exception,args:
        res = str(args).lower()
        text = model.text_file.upgrade_fac_exceptions['low_resource']%{'resource':res}
        return text
    except Exceptions.Maximum_Level_Reached:
        text =  model.text_file.upgrade_fac_exceptions['max_level']
        return text
    
    if facility_obj.get_name() == 'HOUSE':
        images_obj.House_flag = False
        images_obj.initialize_facility(facility_obj.get_name())
    if facility_obj.get_name() == 'HOSPITAL':
        images_obj.Hospital_flag = False
        images_obj.initialize_facility(facility_obj.get_name())
    if facility_obj.get_name() == 'WORKSHOP':
        images_obj.Workshop_flag = False
        images_obj.initialize_facility(facility_obj.get_name())
    if facility_obj.get_name() == 'SCHOOL':
        images_obj.School_flag = False
        images_obj.initialize_facility(facility_obj.get_name())
    for i in range(len(model.facilities_list_sprites[facility_obj.get_name()])):
        model.facilities_list_sprites[facility_obj.get_name()][i].upgrade_level()
    
    event = game_events.Event(type = game_events.UPGRADEFACILITYEVENT, facility_name = facility_obj.get_name())
    game_events.EventQueue.add(event)
    
    text = model.text_file.upgrade_fac_text[4]
    return text


def pause_update_thread():
    global update_thread_pause
    update_thread_pause = False


def resume_update_thread():
    global update_thread_pause
    update_thread_pause = True


def calculate_indicators_starting():
    
    # updation of indicators
    
    # housing
    ratio_people_sheltered = model.ppl.get_no_of_ppl_sheltered()/model.ppl.get_total_population()
    model.Housing.turn({'SHELTERED PEOPLE' : ratio_people_sheltered})

    # nutrition
    ppl_fed_ratio = model.ppl.get_no_of_ppl_fed()/model.ppl.get_total_population()
    temp = model.FOOD_DIST_DICT_INIT
    protiens = 0.0
    vitamins = 0.0
    fats = 0.0
    for resource in model.food_resources:
        name = resource.get_name()
        if temp.has_key(name):
            quantity = int(resource.get_vquantity())
            protiens += temp[name]['PROTIENS'] * quantity
            vitamins += temp[name]['VITAMINS'] * quantity
            fats += temp[name]['FATS'] * quantity
        
    
    food = protiens + vitamins + fats
    if food:
            protiens /= food*0.6
            if protiens>1:
                protiens = 1
            vitamins /= food*0.4
            if vitamins>1:
                vitamins = 1
            fats /= food*0.6
            if fats>1:
                fats = 1

    model.Nutrition.turn({'PEOPLE FED' : ppl_fed_ratio , 'PROTIENS' : protiens , 'FATS' : fats , 'VITAMINS' : vitamins})

    # health
    healthy_ppl_ratio = model.ppl.get_no_of_ppl_healthy()/model.ppl.get_total_population()
    nutrition = model.Nutrition.get_value()
    nutrition /= model.MAX_INDICATOR
    water = model.Water.get_vquantity()/1000.0
    if water>1:
        water =1

    model.Health.turn({'HEALTHY PEOPLE' : healthy_ppl_ratio , 'NUTRITION' : nutrition , 'WATER' : water})

    # education
    educated_ppl = model.ppl.get_no_of_ppl_educated()/model.ppl.get_total_population()
    level = model.School.get_level()/model.MAX_LEVELS_FACILITY
    model.Education.turn({'EDUCATED PEOPLE' : educated_ppl , 'LEVEL OF EDUCATION' : level })

    # training
    level = model.Workshop.get_level()/model.MAX_LEVELS_FACILITY
    ppl_workshop = model.ppl.get_no_of_ppl_emp_in_workshop()/model.ppl.get_total_population()
    ppl_farm = model.ppl.get_no_of_ppl_emp_in_farm()/model.ppl.get_total_population()    
    ppl_hospital = model.ppl.get_no_of_ppl_emp_in_hospital()/model.ppl.get_total_population()
    ppl_construction = model.ppl.get_no_of_ppl_emp_in_cons()/model.ppl.get_total_population()
    ppl_emp = model.ppl.get_total_no_of_ppl_emp()/model.ppl.get_total_population()
    model.Training.turn({ 'LEVEL OF WORKSHOPS' : level , 'EMPLOYED PEOPLE IN WORKSHOP' : ppl_emp , 'EMPLOYED PEOPLE IN FARM' : ppl_emp , 'EMPLOYED PEOPLE IN HOSPITAL' : ppl_emp , 'EMPLOYED PEOPLE IN CONSTRUCTION' : ppl_emp })

update_turn_time = 0         
def update_turn(delay = 0):
    ''' Updates the model.resources, facilities, manpower model.resources and indicators
    at each turn
    '''
    global food_resources
    global Housing
    global Nutrition
    global Health
    global Water
    global School
    global update_turn_time
    
    update_turn_time += delay
    #print "Delay :" + str(delay)
    #print "turn time :" + str(update_turn_time)
    if update_turn_time>10000:
        
        if update_thread_pause == True:

            # updation of all facilities
            global levelStartUpdateFlag
            levelStartUpdateFlag = True
    
            for i in range(len(model.facilities_list)):
                try:
                    model.resources = model.facilities_list[i].turn(model.resources)
                except Exceptions.Resources_Underflow_Exception,args:
                    
                    t = threading.Thread(target = stop_facility , args = [model.facilities_list[i],str(args)])
                    t.start()
                except Exceptions.Resources_Overflow_Exception:
                    pass 
    
            # Increase of population
            popul = model.ppl.get_total_population()
            model.POPULATION_FACTOR+=0.05
            model.ppl.change_total_population((popul * model.POPULATION_CHANGE/model.POPULATION_FACTOR))
            model.ppl.update_total_no_of_ppl_employed()
            
            # updation of manpower model.resources
            
            model.resources = model.ppl.update_turn(model.resources,model.facilities_list)

            # updation of prices of model.resources and the check on model.resources if their market value decreases a certain value then it should increase it
            
            for i in range(len(model.resources)):
                model.resources[i].update_price()
                if model.resources[i].get_mquantity < 500:
                    model.resources[i].change_mquantity(8000)
    
            # housing
            ratio_people_sheltered = model.ppl.get_no_of_ppl_sheltered()/model.ppl.get_total_population()
            model.Housing.turn({'SHELTERED PEOPLE' : ratio_people_sheltered})
    
            # nutrition
            ppl_fed_ratio = model.ppl.get_no_of_ppl_fed()/model.ppl.get_total_population()
            #print "ppl_fed_ratio",ppl_fed_ratio
            temp = model.FOOD_DIST_DICT_INIT
            protiens = 0.0
            vitamins = 0.0
            fats = 0.0
            for resource in model.food_resources:
                name = resource.get_name()
                if temp.has_key(name):
                    quantity = int(resource.get_vquantity())
                    #print "name, quantity of food resource",name,quantity
                    protiens += temp[name]['PROTIENS'] * quantity
                    vitamins += temp[name]['VITAMINS'] * quantity
                    fats += temp[name]['FATS'] * quantity
                
            #print "value of protiens,vitamins,fats",protiens,vitamins,fats
            food = protiens + vitamins + fats
            if food:
                protiens /= food*0.6
                if protiens>1:
                    protiens = 1
                vitamins /= food*0.4
                if vitamins>1:
                    vitamins = 1
                fats /= food*0.6
                if fats>1:
                    fats = 1
            #print "protiens,vitamins,fats",protiens,vitamins,fats
    
            model.Nutrition.turn({'PEOPLE FED' : ppl_fed_ratio , 'PROTIENS' : protiens , 'FATS' : fats , 'VITAMINS' : vitamins})
    
            # health
            healthy_ppl_ratio = model.ppl.get_no_of_ppl_healthy()/model.ppl.get_total_population()
            #print "healthy_ppl_ratio",healthy_ppl_ratio
            nutrition = model.Nutrition.get_value()
            nutrition /= model.MAX_INDICATOR
            #print "nutrition",nutrition
            water = model.Water.get_vquantity()/1000.0
            if water>1:
                water =1
            #print "water",water
    
            model.Health.turn({'HEALTHY PEOPLE' : healthy_ppl_ratio , 'NUTRITION' : nutrition , 'WATER' : water})
    
            # education
            educated_ppl = model.ppl.get_no_of_ppl_educated()/model.ppl.get_total_population()
            level = model.School.get_level()/model.MAX_LEVELS_FACILITY
            model.Education.turn({'EDUCATED PEOPLE' : educated_ppl , 'LEVEL OF EDUCATION' : level })
    
            # training
            level = model.Workshop.get_level()/model.MAX_LEVELS_FACILITY
            ppl_workshop = model.ppl.get_no_of_ppl_emp_in_workshop()/model.ppl.get_total_population()
            ppl_farm = model.ppl.get_no_of_ppl_emp_in_farm()/model.ppl.get_total_population()    
            ppl_hospital = model.ppl.get_no_of_ppl_emp_in_hospital()/model.ppl.get_total_population()
            ppl_construction = model.ppl.get_no_of_ppl_emp_in_cons()/model.ppl.get_total_population()
            ppl_emp = model.ppl.get_total_no_of_ppl_emp()/model.ppl.get_total_population()
            model.Training.turn({ 'LEVEL OF WORKSHOPS' : level , 'EMPLOYED PEOPLE IN WORKSHOP' : ppl_emp , 'EMPLOYED PEOPLE IN FARM' : ppl_emp , 'EMPLOYED PEOPLE IN HOSPITAL' : ppl_emp , 'EMPLOYED PEOPLE IN CONSTRUCTION' : ppl_emp })

            update_turn_time =0

# Functions for making the code resolution independent

def resize_pos(original_pos,original_size = original_screen_size,new_size = new_screen_size):
    ratio_x = (original_pos[0]+0.0)/(original_size[0]+0.0) 
    ratio_y = original_pos[1]/(original_size[1] +0.0)
    new_pos = (int(new_size[0]*ratio_x),int(new_size[1]*ratio_y))
    return new_pos

def resize_pt(point,original_size = original_screen_size,new_size = new_screen_size):
    ratio_x = new_size[0]/(original_size[0]+0.0) 
    ratio_y = new_size[1]/(original_size[1] +0.0)
    ratio = (ratio_x + ratio_y)/2
    point *= ratio
    return int(point)

def resize_pt_x(point,original_size = original_screen_size,new_size = new_screen_size):
    ratio_x = new_size[0]/(original_size[0]+0.0) 
    point *= ratio_x
    return int(point)

def resize_pt_y(point,original_size = original_screen_size,new_size = new_screen_size):
    ratio_y = new_size[1]/(original_size[1] +0.0)
    point *= ratio_y
    return int(point)
    
def resize_rect(original_rect,original_size = original_screen_size,new_size = new_screen_size):
    ratio_x = new_size[0]/(original_size[0]+0.0) 
    ratio_y = new_size[1]/(original_size[1] +0.0)
    new_rect = (int(original_rect[0]*ratio_x),int(original_rect[1]*ratio_y),int(original_rect[2]*ratio_x),int(original_rect[3]*ratio_y))
    return new_rect


# Functions to perform various game operations
def buy_res(res,res_quantity):
    ''' This method allows a user to buy model.resources
    '''
    #global model.resources
    #global model.money
    
    
    try:
        quantity=int(res_quantity)
        model.money = res.buy(quantity , model.money)
    except Exceptions.Money_Underflow_Exception:
        text = model.text_file.buysell_exceptions['low_money']
        return text
    except Exceptions.Resources_Underflow_Exception,args:
        text = model.text_file.buysell_exceptions['low_mkt_qty']
        return text
    except Exceptions.Resources_Overflow_Exception:
        text = model.text_file.buysell_exceptions['overflow']
        return text
        
    text = model.text_file.buysell_exceptions['no_exception']
    
    event = game_events.Event(type = game_events.BUYRESOURCESEVENT, res_name = res.get_name(), res_quantity = res_quantity)
    game_events.EventQueue.add(event)
    
    return text
        

def sell_res(res,res_quantity):
    ''' This method allows a user to sell model.resources
    '''
    try:
        quantity=int(res_quantity)
        model.money = res.sell(quantity , model.money)       
    except Exceptions.Resources_Underflow_Exception,args:
        text = model.text_file.buysell_exceptions['low_qty']
        return text
    except Exceptions.Resources_Overflow_Exception:
        text = model.text_file.buysell_exceptions['no_exception']
        return text
    text = model.text_file.buysell_exceptions['no_exception']
    
    event = game_events.Event(type = game_events.SELLRESOURCESEVENT, res_name = res.get_name(), res_quantity = res_quantity)
    game_events.EventQueue.add(event)
    
    return text
    
    
# Functions for calamities
def demolish_facility(facility_name):
    ''' Function to demolish a facility
    '''
    
    if (facility_name == 'House') and (model.House.get_number()>0):
        
        model.ppl = model.House.demolish(model.ppl)
        sprite = model.house_sprite_list.pop(0)
        event = game_events.Event(type = game_events.DEMOLISHFACILITYEVENT, facility_name = model.House.get_name())
        game_events.EventQueue.add(event)
        sprite.kill()
    
    if (facility_name == 'Hospital') and (model.Hospital.get_number()>0):
        model.ppl = model.Hospital.demolish(model.ppl)
        sprite = model.hospital_sprite_list.pop(0)
        event = game_events.Event(type = game_events.DEMOLISHFACILITYEVENT, facility_name = model.Hospital.get_name())
        game_events.EventQueue.add(event)
        sprite.kill()
    
    if (facility_name == 'Workshop') and (model.Workshop.get_number()>0):
        model.ppl = model.Workshop.demolish(model.ppl)
        sprite = model.workshop_sprite_list.pop(0)
        event = game_events.Event(type = game_events.DEMOLISHFACILITYEVENT, facility_name = model.Workshop.get_name())
        game_events.EventQueue.add(event)
        sprite.kill()
    
    if (facility_name == 'School') and (model.School.get_number()>0):
        model.ppl = model.School.demolish(model.ppl)
        sprite = model.school_sprite_list.pop(0)
        event = game_events.Event(type = game_events.DEMOLISHFACILITYEVENT, facility_name = model.School.get_name())
        game_events.EventQueue.add(event)
        sprite.kill()
    
    if (facility_name == 'Farm') and (model.Farm.get_number()>0):
        model.ppl = model.Farm.demolish(model.ppl)
        sprite = model.farm_sprite_list.pop(0)
        event = game_events.Event(type = game_events.DEMOLISHFACILITYEVENT, facility_name = model.Farm.get_name())
        game_events.EventQueue.add(event)
        sprite.kill()
    
    if (facility_name == 'Fountain') and (model.Fountain.get_number()>0):
        model.ppl = model.Fountain.demolish(model.ppl)
        sprite = model.fountain_sprite_list.pop(0)
        event = game_events.Event(type = game_events.DEMOLISHFACILITYEVENT, facility_name = model.Fountain.get_name())
        game_events.EventQueue.add(event)
        sprite.kill()
    
def flood():
    '''This method needs to be called when there is an flood in the village
    It will increase the quantity of water with the village and stop the operation of
    all facilities for some time
    '''
    global Hospital 
    global House
    global School
    global Workshop
    #global model.ppl
    global Water
    global Farm
    
    
    try :
        model.Water.change_vquantity(1000)
    except :
        pass
    
    model.Hospital.stop_facility()
    model.House.stop_facility()  # we can comment it out even....
    model.School.stop_facility()
    model.Workshop.stop_facility()
    model.Farm.stop_facility()
     
    sleep(90)                   # that means for five turns
    
    model.Hospital.resume_facility()
    model.House.resume_facility()
    model.School.resume_facility()
    model.Workshop.resume_facility()
    model.Farm.resume_facility()
    
    
def famine():
    '''This method needs to be called when there is an famine in the village
    It will stop the production of farms for some time, five turns
    '''
    
    global Farm
    
    model.Farm.stop_facility()
    sleep(90)
    model.Farm.resume_facility()
    
if model.FLAG_XO or model.FLAG_SOAS:
    import olpcgames.util
    import subprocess
    list_file = open('storyboard_list.pkl')
    for i in range(pickle.load(list_file)):
        item = pickle.load(list_file)
        subprocess.call(['mkdir', os.path.join(olpcgames.util.get_activity_root(),'storyboards',str(item))])
    save_game_file = os.path.join(olpcgames.util.get_activity_root(),'storyboards',str(model.storyboard_file),'save_game.pkl')
else:
    save_game_file = os.path.join('storyboards',str(model.storyboard_file),'save_game.pkl')

def save_game():
    '''Used to save current level'''
    global PLACING_LIST_TEMP
    global current_level
    global game_save_flag
    global storyboard_file
    game_save_flag = True
    
    data_file = os.path.join('storyboards',str(model.storyboard_file),'save_game.pkl')
    output = open(data_file,'wb')
    pickle.dump(current_level,output)
    pickle.dump(model.game_controller.get_global_time(),output)
    pickle.dump(PLACING_LIST_TEMP,output)
    output.close()
    
def delete_saved_game(data_file = save_game_file):
    '''Used to delete saved game data'''
    global game_saved_flag
    game_save_flag = False
    output = open(data_file,'wb')
    output.close()
    


def resume_game():
    '''Used to resume a saved game'''
    global PLACING_LIST_TEMP
    global level_save_time
    global game_save_flag
    global current_level
    
    data_file = os.path.join('storyboards',str(model.storyboard_file),'save_game.pkl')
    output = open(data_file,'rb')
    level = pickle.load(output)
    current_level = level
    level_save_time = pickle.load(output)
    model.game_controller.resume_game_time_update(level_save_time)
    #print model.global_time
    while True:
        try:
            PLACING_LIST_TEMP = pickle.load(output)
            #print PLACING_LIST_TEMP
        except EOFError:
            break
    output.close()
    game_save_flag = False
    
def check_saved_game_level():
    '''Used to check the status of game, saved or unsaved'''
 
    global game_save_flag
    storyboard_list_file = open('storyboard_list.pkl')
    for i in range(pickle.load(storyboard_list_file)):
        storyboard_name = pickle.load(storyboard_list_file)
        if os.path.exists(os.path.join('storyboards',str(storyboard_name[1]),'save_game.pkl')):
            game_save_flag = True       
            break
    
def load_initial_facilities():
    global PLACING_LIST_TEMP
    PLACING_LIST_TEMP = []
    fac_load_file = open(os.path.join('storyboards',str(model.storyboard_file),'init_fac.pkl'),'rb')
    while True:
        try:
            PLACING_LIST_TEMP.append(pickle.load(fac_load_file))
        except EOFError:
            break
    fac_load_file.close()
        
    
# The messages Classes    
class Messages:
    ''' Class which handles the messaging system
    '''
    def __init__(self):
        self.queue = []
        self.queue_color = []
        
    
    def push_message(self,text,priority):
        ''' Used to push a message in the message queue
        '''
        if priority == 'low':
            color = (0,250,0) # Green
        if priority == 'medium':
            color = (0,0,250) # Blue
        if priority == 'high':
            color = (250,0,0) # Red
        
        self.queue_color.append(color)
        self.queue.append(text)
    
    def pop_message(self):
        ''' Used to pop a message from the message queue
        '''
        
        text = None
        color = None
        if self.queue:
            text = self.queue.pop(0)
            color = self.queue_color.pop(0)
        return (text,color)
    
    
message = Messages()   # the Mesages class object 


# NOW there are classes of animation and sprites here

class Workshop_sprite(pygame.sprite.Sprite):
    
    def __init__(self,(x,y)):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.ratio = transform_obj.ratio
        self.level = model.Workshop.get_level()
        self.built_flag = 0
        self.image = load_images.Workshop_tiles_list[self.level][self.frame]
        self.rect = self.image.get_rect()
        self.position = (x,y)
        self.position_rect = self.rect.move(self.position)
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        self.tile_time = 0
        self.update_flag = True

    def update(self):
        if self.tile_time < 2000:
            self.tile_time += model.iteration_time
        else:
            self.tile_time = 0
            
            if (self.frame >= 2 and self.level ==0) :
                if (self.frame == 2 and self.built_flag == 0) :
                    build_end_facility(model.Workshop)
                    self.built_flag = 1
            elif (self.frame >= 2 and self.level ==1) :
                if (self.frame == 2 and self.built_flag == 0) :
                    build_end_facility(model.Workshop)
                    self.built_flag = 1
            elif (self.frame >= 2 and self.level ==2) :
                if (self.frame == 2 and self.built_flag == 0) :
                    build_end_facility(model.Workshop)
                    self.built_flag = 1
            elif (self.frame >= 2 and self.level ==3) :
                if (self.frame == 2 and self.built_flag == 0) :
                    build_end_facility(model.Workshop)
                    self.built_flag = 1
            else:
                self.frame += 1
                self.update_flag = True
        if not self.ratio == transform_obj.ratio:
            self.update_flag = True
            self.ratio = transform_obj.ratio
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
            
        
    def set_frame(self):
        if transform_obj.check_update_condition() or self.update_flag:
            self.image = load_images.Workshop_tiles_list[self.level][self.frame]
            self.update_flag = False
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        
    def get_position(self):
        ''' Returns the position rect of the sprite
        '''
        return self.position_rect
    
    def upgrade_level(self):
        
        transform_obj.focus_at(self.position)
        self.level +=1
        self.counter = 4
        self.frame = 0
        self.update_flag = True

  
class House_sprite(pygame.sprite.Sprite):
    
    def __init__(self,(x,y)):
        pygame.sprite.Sprite.__init__(self)
        # Saving tiles of all the upgrades in tiles_list
        self.frame = 0
        self.level = model.House.get_level()
        self.built_flag = 0
        self.ratio = transform_obj.ratio
        self.image = load_images.House_tiles_list[self.level][self.frame]
        self.rect = self.image.get_rect()
        self.position = (x,y)
        self.position_rect = self.rect.move(self.position)
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        self.tile_time = 0
        self.update_flag = True

    def update(self):
        if self.tile_time < 2000:
            self.tile_time += model.iteration_time
        else:
            self.tile_time = 0
            
            if (self.frame >= 3 and self.level ==0) :
                if (self.frame == 3 and self.built_flag == 0) :
                    build_end_facility(model.House)
                    self.built_flag = 1
            elif (self.frame >= 2 and self.level ==1) :
                if (self.frame == 2 and self.built_flag == 0) :
                    build_end_facility(model.House)
                    self.built_flag = 1
            elif (self.frame >= 2 and self.level ==2) :
                if (self.frame == 2 and self.built_flag == 0) :
                    build_end_facility(model.House)
                    self.built_flag = 1
            elif (self.frame >= 2 and self.level ==3) :
                if (self.frame == 2 and self.built_flag == 0) :
                    build_end_facility(model.House)
                    self.built_flag = 1
            else:
                self.frame += 1
                self.update_flag = True
        if not self.ratio == transform_obj.ratio:
            self.update_flag = True
            self.ratio = transform_obj.ratio
        
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
            
        
    def set_frame(self):
        if transform_obj.check_update_condition() or self.update_flag:
            self.image = load_images. House_tiles_list[self.level][self.frame]
            self.update_flag = False
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        
    def get_position(self):
        ''' Returns the position rect of the sprite
        '''
        return self.position_rect
    
    def upgrade_level(self):
        transform_obj.focus_at(self.position)
        self.level +=1
        self.counter = 4
        self.frame = 0
        self.update_flag = True

        
class Hospital_sprite(pygame.sprite.Sprite):
    
    def __init__(self,(x,y)):
        pygame.sprite.Sprite.__init__(self)
        # Saving tiles of all the upgrades in tiles_list
        self.frame = 0
        self.ratio = transform_obj.ratio
        self.level = model.Hospital.get_level()
        self.built_flag = 0
        self.image = load_images.Hospital_tiles_list[self.level][self.frame]
        self.rect = self.image.get_rect()
        self.position = (x,y)
        self.position_rect = self.rect.move(self.position)
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        self.tile_time = 0
        self.update_flag = True

    def update(self):
        
        if self.tile_time < 2000:
            self.tile_time += model.iteration_time
        else:
            self.tile_time = 0
            
            if (self.frame >= 3 and self.level ==0) :
                if (self.frame == 3 and self.built_flag == 0) :
                    build_end_facility(model.Hospital)
                    self.built_flag = 1
            elif (self.frame >= 2 and self.level ==1) :
                if (self.frame == 2 and self.built_flag == 0) :
                    build_end_facility(model.Hospital)
                    self.built_flag = 1
            elif (self.frame >= 2 and self.level ==2) :
                if (self.frame == 2 and self.built_flag == 0) :
                    build_end_facility(model.Hospital)
                    self.built_flag = 1
            elif (self.frame >= 2 and self.level ==3) :
                if (self.frame == 2 and self.built_flag == 0) :
                    build_end_facility(model.Hospital)
                    self.built_flag = 1
            else:
                self.frame += 1
                self.update_flag = True
        if not self.ratio == transform_obj.ratio:
            self.update_flag = True
            self.ratio = transform_obj.ratio
        
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
            
        
    def set_frame(self):
        if transform_obj.check_update_condition() or self.update_flag:
            self.image = load_images.Hospital_tiles_list[self.level][self.frame]
            self.update_flag = False
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        
    def get_position(self):
        ''' Returns the position rect of the sprite
        '''
        return self.position_rect
        
    def upgrade_level(self):
        transform_obj.focus_at(self.position)
        self.level +=1
        self.counter = 4
        self.frame = 0
        self.update_flag = True
        
        
class School_sprite(pygame.sprite.Sprite):
    
    def __init__(self,(x,y)):
        pygame.sprite.Sprite.__init__(self)
       # Saving tiles of all the upgrades in tiles_list
        
        
        self.frame = 0
        self.level = model.School.get_level()
        self.built_flag =0
        self.ratio = transform_obj.ratio
        self.image = load_images.School_tiles_list[self.level][self.frame]
        self.rect = self.image.get_rect()
        self.position = (x,y)
        self.position_rect = self.rect.move(self.position)
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        self.tile_time =0
        self.update_flag = True
        

    def update(self):
        
        if self.tile_time < 2000:
            self.tile_time += model.iteration_time
        else:
            self.tile_time = 0
            
            if (self.frame >= 3 and self.level ==0) :
                if (self.frame == 3 and self.built_flag == 0) :
                    build_end_facility(model.School)
                    self.built_flag = 1
            elif (self.frame >= 2 and self.level ==1) :
                if (self.frame == 2 and self.built_flag == 0) :
                    build_end_facility(model.School)
                    self.built_flag = 1
            elif (self.frame >= 2 and self.level ==2) :
                if (self.frame == 2 and self.built_flag == 0) :
                    build_end_facility(model.School)
                    self.built_flag = 1
            elif (self.frame >= 2 and self.level ==3) :
                if (self.frame == 2 and self.built_flag == 0) :
                    build_end_facility(model.School)
                    self.built_flag = 1
            else:
                self.frame += 1
                self.update_flag = True
        if not self.ratio == transform_obj.ratio:
            self.update_flag = True
            self.ratio = transform_obj.ratio
        
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
            
        
    def set_frame(self):
        if transform_obj.check_update_condition() or self.update_flag:
            self.image = load_images.School_tiles_list[self.level][self.frame]
            self.update_flag = False
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        
    def get_position(self):
        ''' Returns the position rect of the sprite
        '''
        return self.position_rect
        
    def upgrade_level(self):
        transform_obj.focus_at(self.position)
        self.level +=1
        self.counter = 4
        self.frame = 0
        self.update_flag = True

 
class Farm_sprite(pygame.sprite.Sprite):
    
    def __init__(self,(x,y)):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.built_flag = 0
        self.ratio = transform_obj.ratio
        self.image = load_images.Farm_tiles[0][self.frame]
        self.rect = self.image.get_rect()
        self.position = (x,y)
        self.position_rect = self.rect.move(self.position)
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        self.tile_time = 0
        self.update_flag = True
        

    def update(self):
        
        
        if self.tile_time < 2000:
            self.tile_time += model.iteration_time
        else:
            self.tile_time = 0
            
            if (self.frame >= 2) :
                if (self.frame == 2 and self.built_flag == 0) :
                    build_end_facility(model.Farm)
                    self.built_flag = 1
            else:
                self.frame += 1
                self.update_flag = True
        
        if not self.ratio == transform_obj.ratio:
            self.update_flag = True
            self.ratio = transform_obj.ratio
        
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        
  

    def set_frame(self):
        if transform_obj.check_update_condition() or self.update_flag:
            self.image = load_images.Farm_tiles[0][self.frame]
            self.update_flag = False
        
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        
    def get_position(self):
        ''' Returns the position rect of the sprite
        '''
        return self.position_rect
    
    def upgrade_level(self):
        transform_obj.focus_at(self.position)
        self.update_flag = True
        

    
class Fountain_sprite(pygame.sprite.Sprite):
    
    def __init__(self,(x,y)):
        pygame.sprite.Sprite.__init__(self)
        # Saving tiles of all the upgrades in tiles_list
        self.frame = 0
        self.built_flag = 0
        self.ratio = transform_obj.ratio
        self.image = load_images.Fountain_tiles[0][self.frame]
        self.rect = self.image.get_rect()
        self.position = (x,y)
        self.position_rect = self.rect.move(self.position)
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        self.tile_time = 0
        self.update_flag = True
        

    def update(self):
        
        
        if self.tile_time < 2000:
            self.tile_time += model.iteration_time
        else:
            self.tile_time = 0
            
            if (self.frame >= 3) :
                if (self.frame == 3 and self.built_flag == 0) :
                    build_end_facility(model.Fountain)
                    self.built_flag = 1
            else:
                self.frame += 1
                self.update_flag = True
        if not self.ratio == transform_obj.ratio:
            self.update_flag = True
            self.ratio = transform_obj.ratio
        
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        
    def set_frame(self):
        if transform_obj.check_update_condition() or self.update_flag:
            self.image = load_images.Fountain_tiles[0][self.frame]
            self.update_flag = False
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        
    def get_position(self):
        ''' Returns the position rect of the sprite
        '''
        return self.position_rect
    
    def upgrade_level(self):
        transform_obj.focus_at(self.position)
        self.update_flag = True
        


# The work for drawing the background
#global back_image_level1

if not model.FLAG_XO:

    global image_to_scale
    image_to_scale = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    global image_pos
    image_pos = []
    for num_ver in range(10):
        for num_hor in range(12):
            rect = Rect(num_hor*250 + 10, num_ver*250 + 10, 230, 230)
            image_pos.append(rect)


#Class to initialise the background
class Environment2:
    
    def __init__(self):
        self.sheet = pygame.image.load(os.path.join('data','tileset2.png')).convert()
        #self.sheet = pygame.transform.scale(self.sheet,(3010,2260))
            
        self.dis_image = {}
        for image_no in image_to_scale:
            self.surf = pygame.Surface((230,230)).convert()
            self.rect = image_pos[image_no]
            self.surf.blit(self.sheet,(0,0),self.rect)
            self.surf = pygame.transform.scale(self.surf,resize_pos((230,230)))
            self.dis_image[image_no] = self.surf
        
        self.dis_image_trans = {}
        for self.dis_image_key in self.dis_image.keys():
            self.dis_image_trans[self.dis_image_key] = transform_obj.transform_surface(self.dis_image.get(self.dis_image_key))

           
    def update_background(self):
        #self.dis_image_trans = {}
        if transform_obj.check_update_condition():
            for self.dis_image_key in self.dis_image.keys():
                self.dis_image_trans[self.dis_image_key] = transform_obj.transform_surface(self.dis_image.get(self.dis_image_key))

        rect = self.dis_image_trans[self.dis_image_key].get_rect()
        (self.x_inc ,self.y_inc) = rect.size 

        self.img_x_init = int(transform_obj.pos_x/self.x_inc)
        self.img_y_init = int(transform_obj.pos_y/self.y_inc)
        self.ratio = transform_obj.ratio
        self.pos_x_init = (self.x_inc*self.img_x_init) - transform_obj.pos_x
        self.pos_y_init = (self.y_inc*self.img_y_init) - transform_obj.pos_y
        self.pos_x = self.pos_x_init  
        self.pos_y = self.pos_y_init  
        self.img_x = self.img_x_init
        self.img_y = self.img_y_init
        
        while self.pos_x < resize_pt_x(1000):
            self.img_y = self.img_y_init
            self.pos_y = self.pos_y_init
            while self.pos_y < resize_pt_y(600):
                screen.blit(self.dis_image_trans[load_images.back_image_level1[self.img_y][self.img_x]],(self.pos_x,self.pos_y),rect)
       
                self.img_y += 1
                self.pos_y += self.y_inc
            self.img_x += 1
            self.pos_x += self.x_inc


class Environment(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        spritesheet = load_images.Spritesheet('tileset.png')
        self.tiles = spritesheet.imgat((0,0,930,560))
        self.tiles = pygame.transform.scale(self.tiles,resize_pos((930,560)))
        
    def update_background(self):
        
        screen.blit(self.tiles,(0,resize_pt_y(40)))
    


class Build(pygame.sprite.Sprite):
    
    def __init__(self, filename, x, y, colorkey=None):
        pygame.sprite.Sprite.__init__(self)
        self.market_image = pygame.image.load(os.path.join('data', filename)).convert_alpha()
        self.image = transform_obj.transform_surface(self.market_image)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = self.image.get_at((0, 0))
            self.image.set_colorkey(colorkey, RLEACCEL)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.update_flag = True
        self.ratio = transform_obj.ratio
        self.rect = self.rect.move(transform_obj.transform_cordinates((x, y)))
        
    def update(self):
        if not self.ratio == transform_obj.ratio:
            self.update_flag = True
            self.ratio = transform_obj.ratio
        
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates((self.x, self.y)))
        
    def set_frame(self):
        
        if transform_obj.check_update_condition() or self.update_flag:
            self.image = transform_obj.transform_surface(self.market_image)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates((self.x, self.y)))
        
    



# Functions to add sprites to groups
def add_sprite_all(sprite):
    sprite.add(all)    
    
def add_sprite_facilities(sprite):
    sprite.add(facilities_group)    





# The screen sprite to clip all the sprites which are not in the drawable region
class screen_sprite(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.surface.Surface(resize_pos((1200,560)))
        self.rect = Rect(resize_rect((0,40,930,560)))
  



# The villager class
class Villager(pygame.sprite.Sprite):
    
    def __init__(self,range_rect):
        pygame.sprite.Sprite.__init__(self)
        names = ['Man','Woman','Boy','Girl']
        name = names[int(random.random()*4)]
        self.dx = 2
        self.dy = 2
        self.update_flag = True
        self.ratio = transform_obj.ratio
        self.speed = [2, 0]
        self.speed_time = 0
        self.tile_time =0
        self.name = name
        self.dtiles_final = [0,0,0,0]
        self.range = range_rect
        if self.name == 'Man':
            self.tiles = load_images.Man_tiles[0]
        
        if self.name == 'Woman':
            self.tiles = load_images.Woman_tiles[0]
        
        if self.name == 'Boy':
            self.tiles = load_images.Boy_tiles[0]
        
        if self.name == 'Girl':
            self.tiles = load_images.Girl_tiles[0]
        
        self.frame = 0
        self.set_direction()
        self.dtiles_final = self.dtiles
            
        self.image = self.dtiles_final[self.frame]
        self.rect = self.image.get_rect()
        
        flag =True
        while flag:
            flag = False
            self.initial_position = [self.range[0]+int(random.random()*self.range[2]), self.range[1]+int(random.random()*self.range[3])]
            self.position = self.initial_position
            self.position_rect = self.rect.move(self.position)
            for key in model.facilities_list_sprites.keys(): 
                sprite_list = model.facilities_list_sprites[key]
                for sprite in sprite_list:
                    self.test_rect = sprite.get_position()
                    if self.test_rect.colliderect(self.position_rect):
                        
                        flag = True
        
        self.prev_disp = transform_obj.transform_cordinates(self.position)
        self.rect = self.rect.move(self.prev_disp)
        
    
    def set_direction(self):
        
        
        if self.name == 'Man':
            self.tiles = load_images.Man_tiles[0]
        
        if self.name == 'Woman':
            self.tiles = load_images.Woman_tiles[0]
        
        if self.name == 'Boy':
            self.tiles = load_images.Boy_tiles[0]
        
        if self.name == 'Girl':
            self.tiles = load_images.Girl_tiles[0]
        
        sp = self.speed
        if sp[0] > 0  and sp[1] == 0:
            self.dtiles = self.tiles[0:4]
        elif sp[0] < 0  and sp[1] == 0:
            self.dtiles = self.tiles[4:8]
        elif sp[0] == 0  and sp[1] < 0:
            self.dtiles = self.tiles[8:12]
        elif sp[0] == 0  and sp[1] > 0:
            self.dtiles = self.tiles[12:16]
            
        self.dtiles_final = self.dtiles
            
    def collide_build(self):
        
        self.set_speed(map(lambda x: -x, self.speed))
        
        self.position = [self.position[0] + 5, self.position[1] + 5]
        self.position = [self.position[0] + 5, self.position[1] + 5]
        
        self.update()
        self.set_direction()

    
    def set_speed(self, speed):
        
        
        self.speed = speed
        self.set_direction()
    
    def update(self):
    
        self.speed_time += model.iteration_time
        self.tile_time +=model.iteration_time
        
        ANIMRECT = Rect(0,0,9000,6000)
        if self.tile_time >= 500:
            self.tile_time =0 
            self.frame  += 1
            if self.frame >3:
                self.frame = 0
        
        if self.speed_time >= 6000:
            self.speed_time = 0
            temp = self.speed[0]
            self.speed[0] = self.speed[1]
            self.speed[1] = temp
            
        
        self.rect = self.image.get_rect()
        self.position = [self.position[0] + (self.speed[0]*model.iteration_time/100.0), self.position[1] + (self.speed[1]*model.iteration_time/100.0)]
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        
        if self.position[0] <= 0 or (self.position[0]+100) >= ANIMRECT.width or self.position[0] <= (self.range[0]) or self.position[0] >= (self.range[0]+self.range[2]):
            self.speed[0] = -self.speed[0]
            
            self.rect = self.image.get_rect()
            self.position[0] += self.speed[0]*model.iteration_time/100.0
            self.position[1] += self.speed[1]*model.iteration_time/100.0
            self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
            
        elif self.position[1] <= 0 or (self.position[1]-100) >= ANIMRECT.height or self.position[1] <= (self.range[1]) or self.position[1] >= (self.range[1]+self.range[3]):
            self.speed[1] = -self.speed[1]
            
            self.rect = self.image.get_rect()
            self.position[0] += self.speed[0]*model.iteration_time/100.0
            self.position[1] += self.speed[1]*model.iteration_time/100.0
            self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        self.set_direction()
        if not self.ratio == transform_obj.ratio:
            self.update_flag = True
            self.ratio = transform_obj.ratio
        
        #self.rect.clamp_ip(ANIMRECT)    
    def set_frame(self):
        
        self.set_direction()
        if transform_obj.check_update_condition() or self.update_flag:
            self.dtiles_final = self.dtiles
        self.image = self.dtiles_final[self.frame]
        
    def get_attributes(self):
        return self.range
    def get_name(self):
        return self.name
    



# Function to check for villagers collision
def check_villagers_self_collision():
    
    villagers_sprite_list = []
    for sprite in villagers.sprites():
        sprite.remove(villagers)
        sprites_list = pygame.sprite.spritecollide(sprite,villagers,False)
        if sprites_list:
            for villager in sprites_list:
                villager.collide_build()
        villagers_sprite_list.append(sprite)
    while villagers_sprite_list:
        villager = villagers_sprite_list.pop()
        villager.add(villagers)
         



class Transform:
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.MAX_RATIO = 0.9
        self.MIN_RATIO = 0.4
        self.ratio = 0.4
        self.motion_up = 0
        self.motion_down = 0
        self.motion_left = 0
        self.motion_right = 0
        self.mouse_move_flag = True
        self.prev_ratio = 0.2
    
    def check_update_condition(self):
        ''' Checks Whether to update an image or not
        '''
        
        if self.prev_ratio == self.ratio:
            return False
        else : 
            return True
        
    def move_up(self,dist = 10):
        
        self.pos_y -= dist
    
    def stop_mouse_move(self):
        self.mouse_move_flag = False
        
    def resume_mouse_move(self):
        self.mouse_move_flag = True
    
    def start_move(self,dir):    
        
        if dir == 'up':
            self.motion_up = 1
        elif dir == 'down':
            self.motion_down = 1
        elif dir == 'right':
            self.motion_right = 1
        elif dir == 'left':
            self.motion_left = 1
  
    def stop_move(self,dir):    
        
        if dir == 'up':
            self.motion_up = 0
        elif dir == 'down':
            self.motion_down = 0
        elif dir == 'right':
            self.motion_right = 0
        elif dir == 'left':
            self.motion_left = 0
  
    def move(self):
        speed = 200
        if self.motion_up:
            self.pos_y -= speed*model.iteration_time/1000
        if self.motion_down:
            self.pos_y += speed*model.iteration_time/1000
        if self.motion_right:
            self.pos_x+= speed*model.iteration_time/1000
        if self.motion_left:
            self.pos_x -= speed*model.iteration_time/1000
  
    def move_mouse(self,(x,y)):
    
        if self.mouse_move_flag == True:
            self.pos_x -= x
            self.pos_y -=y
 
    def move_down(self):
        
        self.pos_y += 10
  
    def move_right(self,dist = 10):
        
        self.pos_x += dist    
  
    def move_left(self,dist = 10):
        
        self.pos_x -= dist    
    
    def move_free(self,(x,y)):
    
        self.pos_x -= x
        self.pos_y -=y
    
    def check_pos(self):
        if self.pos_x < 0:
            self.pos_x = 0
        if self.pos_x > (int(self.ratio*6000) - 930):
            self.pos_x = (int(self.ratio*6000) - 930)
        if self.pos_y < 0:
            self.pos_y = 0
        if self.pos_y > (int(self.ratio*5000) - 560):
            self.pos_y = (int(self.ratio*5000) - 560)
            
    
    def focus(self):
        ''' Used to focus or zoom in'''
        self.ratio = self.ratio + 0.10
        if self.ratio >= 0.9:
            self.ratio = 0.9
        else:
            a = self.pos_x +600
            b = self.pos_y + 280
            a *= self.ratio/(self.ratio - 0.10)
            b *= self.ratio/(self.ratio - 0.10)
            self.pos_x = int(a - 600)
            self.pos_y = int(b - 280)
    
    
    def defocus(self):
        ''' Used to defocus or zoom out'''
        self.ratio = self.ratio - 0.10
        if self.ratio <= 0.2:
            self.ratio = 0.2
        else:
            a = self.pos_x +600
            b = self.pos_y + 280
            a *= self.ratio/(self.ratio + 0.10)
            b *= self.ratio/(self.ratio + 0.10)
            self.pos_x = int(a - 600)
            self.pos_y = int(b - 280)
    
    
    def focus_at(self,(x,y)):
        '''Used to focus at a particular position'''
        #self.ratio = 0.6
        self.pos_x = int(x*self.ratio) -500
        self.pos_y = int(y*self.ratio) - 80
  
    def transform_cordinates(self,(x,y)):
        newx = x*self.ratio - self.pos_x
        newy = y*self.ratio - self.pos_y + resize_pt_y(40)
        return (int(newx),int(newy))
 
    def inverse_transform_cordinate(self,(x,y)):
        ''' Transform the Screen Cordinates to Village Cordinates
        
        Args:
         x:int:x cordinate
         y:int:y cordinate
        Return:
         newx:int:new x cordinate
         newy:int:new y cordinate
        '''
        newx = ((x + self.pos_x)/self.ratio)*(1200.0/new_screen_size[0])
        newy = ((y + self.pos_y - 40)/self.ratio)*(900.0/new_screen_size[1])
        return(int(newx),int(newy))
    
    
    def inverse_trans_cordinate(self,(x,y)):
        ''' Transform the Screen Cordinates to Village Cordinates
        
        Args:
         x:int:x cordinate
         y:int:y cordinate
        Return:
         newx:int:new x cordinate
         newy:int:new y cordinate
        '''
        newx = ((x + self.pos_x)/self.ratio)
        newy = ((y + self.pos_y - resize_pt_y(40))/self.ratio)
        return(int(newx),int(newy))
    
    def inverse_transform_rect(self,(x,y,w,z)):
        ''' Transform the Screen Cordinates to Village Cordinates
        
        Args:
         x:int:x cordinate
         y:int:y cordinate
        Return:
         newx:int:new x cordinate
         newy:int:new y cordinate
        '''
        newx = ((x + self.pos_x)/self.ratio)*(1200.0/new_screen_size[0])
        newy = ((y + self.pos_y - 40)/self.ratio)*(900.0/new_screen_size[1])
        neww = (w/self.ratio)*(1200.0/new_screen_size[0])
        newz = (z/self.ratio)*(900.0/new_screen_size[1])
        return(int(newx),int(newy),int(neww),int(newz))

    
    def set_ratio(self,ratio):
        self.ratio = ratio
  
    def transform_surface(self,surface):
        (x,y) = surface.get_size()
        x *= self.ratio
        y *= self.ratio
        surface = pygame.transform.scale(surface, (int(x),int(y)))
        return surface
    
    def village_boundary_covered(self):
        min_x =  int(self.pos_x/self.ratio)
        min_y = int(self.pos_y/self.ratio)
        max_x = int((self.pos_x+930) /self.ratio)
        max_y = int((self.pos_y+560) /self.ratio)
        return [min_x, min_y, max_x, max_y]
    
  
   
class update_images:
    
    def __init__(self):

        self.House_flag = False
        self.Workshop_flag = False
        self.School_flag = False
        self.Hospital_flag = False
        self.Fountain_flag = False
        self.Farm_flag = False
        
    def update_images(self):
        
        if transform_obj.check_update_condition():
            if transform_obj.prev_ratio > transform_obj.ratio:
                for i in range(len(load_images.House_tiles_list)):
                    for j in range(len(load_images.House_tiles_list[i])):
                        (x,y) = load_images.House_tiles_list[i][j].get_size()
                        x *= transform_obj.ratio/transform_obj.prev_ratio
                        y *= transform_obj.ratio/transform_obj.prev_ratio
                        load_images.House_tiles_list[i][j] = pygame.transform.scale(load_images.House_tiles_list[i][j],(int(x),int(y)))
                
                for i in range(len(load_images.Hospital_tiles_list)):
                    for j in range(len(load_images.Hospital_tiles_list[i])):
                        (x,y) = load_images.Hospital_tiles_list[i][j].get_size()
                        x *= transform_obj.ratio/transform_obj.prev_ratio
                        y *= transform_obj.ratio/transform_obj.prev_ratio
                        load_images.Hospital_tiles_list[i][j] = pygame.transform.scale(load_images.Hospital_tiles_list[i][j],(int(x),int(y)))

                for i in range(len(load_images.Workshop_tiles_list)):
                    for j in range(len(load_images.Workshop_tiles_list[i])):
                        (x,y) = load_images.Workshop_tiles_list[i][j].get_size()
                        x *= transform_obj.ratio/transform_obj.prev_ratio
                        y *= transform_obj.ratio/transform_obj.prev_ratio
                        load_images.Workshop_tiles_list[i][j] = pygame.transform.scale(load_images.Workshop_tiles_list[i][j],(int(x),int(y)))

                for i in range(len(load_images.School_tiles_list)):
                    for j in range(len(load_images.School_tiles_list[i])):
                        (x,y) = load_images.School_tiles_list[i][j].get_size()
                        x *= transform_obj.ratio/transform_obj.prev_ratio
                        y *= transform_obj.ratio/transform_obj.prev_ratio
                        load_images.School_tiles_list[i][j] = pygame.transform.scale(load_images.School_tiles_list[i][j],(int(x),int(y)))
                
                for i in range(len(load_images.Fountain_tiles)):
                    for j in range(len(load_images.Fountain_tiles[i])):
                        (x,y) = load_images.Fountain_tiles[i][j].get_size()
                        x *= transform_obj.ratio/transform_obj.prev_ratio
                        y *= transform_obj.ratio/transform_obj.prev_ratio
                        load_images.Fountain_tiles[i][j] = pygame.transform.scale(load_images.Fountain_tiles[i][j],(int(x),int(y)))

                for i in range(len(load_images.Farm_tiles)):
                    for j in range(len(load_images.Farm_tiles[i])):
                        (x,y) = load_images.Farm_tiles[i][j].get_size()
                        x *= transform_obj.ratio/transform_obj.prev_ratio
                        y *= transform_obj.ratio/transform_obj.prev_ratio
                        load_images.Farm_tiles[i][j] = pygame.transform.scale(load_images.Farm_tiles[i][j],(int(x),int(y)))
                
                for i in range(len(load_images.Man_tiles)):
                    for j in range(len(load_images.Man_tiles[i])):
                        (x,y) = load_images.Man_tiles[i][j].get_size()
                        x *= transform_obj.ratio/transform_obj.prev_ratio
                        y *= transform_obj.ratio/transform_obj.prev_ratio
                        load_images.Man_tiles[i][j] = pygame.transform.scale(load_images.Man_tiles[i][j],(int(x),int(y)))
                
                for i in range(len(load_images.Woman_tiles)):
                    for j in range(len(load_images.Woman_tiles[i])):
                        (x,y) = load_images.Woman_tiles[i][j].get_size()
                        x *= transform_obj.ratio/transform_obj.prev_ratio
                        y *= transform_obj.ratio/transform_obj.prev_ratio
                        load_images.Woman_tiles[i][j] = pygame.transform.scale(load_images.Woman_tiles[i][j],(int(x),int(y)))
                
                for i in range(len(load_images.Boy_tiles)):
                    for j in range(len(load_images.Boy_tiles[i])):
                        (x,y) = load_images.Boy_tiles[i][j].get_size()
                        x *= transform_obj.ratio/transform_obj.prev_ratio
                        y *= transform_obj.ratio/transform_obj.prev_ratio
                        load_images.Boy_tiles[i][j] = pygame.transform.scale(load_images.Boy_tiles[i][j],(int(x),int(y)))
                
                for i in range(len(load_images.Girl_tiles)):
                    for j in range(len(load_images.Girl_tiles[i])):
                        (x,y) = load_images.Girl_tiles[i][j].get_size()
                        x *= transform_obj.ratio/transform_obj.prev_ratio
                        y *= transform_obj.ratio/transform_obj.prev_ratio
                        load_images.Girl_tiles[i][j] = pygame.transform.scale(load_images.Girl_tiles[i][j],(int(x),int(y)))
                
                        
                        
            else:
                if self.House_flag:
                    load_images.load_images_facility('HOUSE',model.House.get_level())
    
                    for i in range(len(load_images.House_tiles_list)):
                        for j in range(len(load_images.House_tiles_list[i])):
                            (x,y) = resize_pos(load_images.House_tiles_list[i][j].get_size())
                            x *= transform_obj.ratio
                            y *= transform_obj.ratio
                            load_images.House_tiles_list[i][j] = pygame.transform.scale(load_images.House_tiles_list[i][j],(int(x),int(y)))
                    
                if self.Hospital_flag:
                    load_images.load_images_facility('HOSPITAL',model.Hospital.get_level())
                    
                    for i in range(len(load_images.Hospital_tiles_list)):
                        for j in range(len(load_images.Hospital_tiles_list[i])):
                            (x,y) = resize_pos(load_images.Hospital_tiles_list[i][j].get_size())
                            x *= transform_obj.ratio
                            y *= transform_obj.ratio
                            load_images.Hospital_tiles_list[i][j] = pygame.transform.scale(load_images.Hospital_tiles_list[i][j],(int(x),int(y)))

                if self.Workshop_flag:
                    load_images.load_images_facility('WORKSHOP',model.Workshop.get_level())
    
                    for i in range(len(load_images.Workshop_tiles_list)):
                        for j in range(len(load_images.Workshop_tiles_list[i])):
                            (x,y) = resize_pos(load_images.Workshop_tiles_list[i][j].get_size())
                            x *= transform_obj.ratio
                            y *= transform_obj.ratio
                            load_images.Workshop_tiles_list[i][j] = pygame.transform.scale(load_images.Workshop_tiles_list[i][j],(int(x),int(y)))

                if self.School_flag:                
                    load_images.load_images_facility('SCHOOL',model.School.get_level())
    
                    for i in range(len(load_images.School_tiles_list)):
                        for j in range(len(load_images.School_tiles_list[i])):
                            (x,y) = resize_pos(load_images.School_tiles_list[i][j].get_size())
                            x *= transform_obj.ratio
                            y *= transform_obj.ratio
                            load_images.School_tiles_list[i][j] = pygame.transform.scale(load_images.School_tiles_list[i][j],(int(x),int(y)))

                if self.Fountain_flag:
                    load_images.load_images_facility('FOUNTAIN',model.Fountain.get_level())
                    
                    for i in range(len(load_images.Fountain_tiles)):
                        for j in range(len(load_images.Fountain_tiles[i])):
                            (x,y) = resize_pos(load_images.Fountain_tiles[i][j].get_size())
                            x *= transform_obj.ratio
                            y *= transform_obj.ratio
                            load_images.Fountain_tiles[i][j] = pygame.transform.scale(load_images.Fountain_tiles[i][j],(int(x),int(y)))
                            
                if self.Farm_flag:
                    load_images.load_images_facility('FARM',model.Farm.get_level())
                    
                    for i in range(len(load_images.Farm_tiles)):
                        for j in range(len(load_images.Farm_tiles[i])):
                            (x,y) = resize_pos(load_images.Farm_tiles[i][j].get_size())
                            x *= transform_obj.ratio
                            y *= transform_obj.ratio
                            load_images.Farm_tiles[i][j] = pygame.transform.scale(load_images.Farm_tiles[i][j],(int(x),int(y)))
                    
                load_images.load_images_ppl()
                
                for i in range(len(load_images.Man_tiles)):
                    for j in range(len(load_images.Man_tiles[i])):
                        (x,y) = resize_pos(load_images.Man_tiles[i][j].get_size())
                        x *= transform_obj.ratio
                        y *= transform_obj.ratio
                        load_images.Man_tiles[i][j] = pygame.transform.scale(load_images.Man_tiles[i][j],(int(x),int(y)))
                
                for i in range(len(load_images.Woman_tiles)):
                    for j in range(len(load_images.Woman_tiles[i])):
                        (x,y) = resize_pos(load_images.Woman_tiles[i][j].get_size())
                        x *= transform_obj.ratio
                        y *= transform_obj.ratio
                        load_images.Woman_tiles[i][j] = pygame.transform.scale(load_images.Woman_tiles[i][j],(int(x),int(y)))
                
                for i in range(len(load_images.Boy_tiles)):
                    for j in range(len(load_images.Boy_tiles[i])):
                        (x,y) = resize_pos(load_images.Boy_tiles[i][j].get_size())
                        x *= transform_obj.ratio
                        y *= transform_obj.ratio
                        load_images.Boy_tiles[i][j] = pygame.transform.scale(load_images.Boy_tiles[i][j],(int(x),int(y)))
                
                for i in range(len(load_images.Girl_tiles)):
                    for j in range(len(load_images.Girl_tiles[i])):
                        (x,y) = resize_pos(load_images.Girl_tiles[i][j].get_size())
                        x *= transform_obj.ratio
                        y *= transform_obj.ratio
                        load_images.Girl_tiles[i][j] = pygame.transform.scale(load_images.Girl_tiles[i][j],(int(x),int(y)))
                
            
    def initialize_facility(self,facility_name = '',level = 0):
        
        if facility_name == 'HOUSE' and (not self.House_flag):
            
            load_images.load_images_facility('HOUSE',model.House.get_level())
            self.House_flag = True    
            for i in range(len(load_images.House_tiles_list)):
                for j in range(len(load_images.House_tiles_list[i])):
                    (x,y) = resize_pos(load_images.House_tiles_list[i][j].get_size())
                    x *= transform_obj.ratio
                    y *= transform_obj.ratio
                    load_images.House_tiles_list[i][j] = pygame.transform.scale(load_images.House_tiles_list[i][j],(int(x),int(y)))
            
        if facility_name == 'HOSPITAL' and (not self.Hospital_flag):
            
            load_images.load_images_facility('HOSPITAL',model.Hospital.get_level())
            self.Hospital_flag = True        
            for i in range(len(load_images.Hospital_tiles_list)):
                for j in range(len(load_images.Hospital_tiles_list[i])):
                    (x,y) = resize_pos(load_images.Hospital_tiles_list[i][j].get_size())
                    x *= transform_obj.ratio
                    y *= transform_obj.ratio
                    load_images.Hospital_tiles_list[i][j] = pygame.transform.scale(load_images.Hospital_tiles_list[i][j],(int(x),int(y)))

        
        if facility_name == 'WORKSHOP' and (not self.Workshop_flag):
            
            load_images.load_images_facility('WORKSHOP',model.Workshop.get_level())
            self.Workshop_flag = True
            for i in range(len(load_images.Workshop_tiles_list)):
                for j in range(len(load_images.Workshop_tiles_list[i])):
                    (x,y) = resize_pos(load_images.Workshop_tiles_list[i][j].get_size())
                    x *= transform_obj.ratio
                    y *= transform_obj.ratio
                    load_images.Workshop_tiles_list[i][j] = pygame.transform.scale(load_images.Workshop_tiles_list[i][j],(int(x),int(y)))

        
        if facility_name == 'SCHOOL' and (not self.School_flag):
            
            load_images.load_images_facility('SCHOOL',model.School.get_level())
            self.School_flag = True
            for i in range(len(load_images.School_tiles_list)):
                for j in range(len(load_images.School_tiles_list[i])):
                    (x,y) = resize_pos(load_images.School_tiles_list[i][j].get_size())
                    x *= transform_obj.ratio
                    y *= transform_obj.ratio
                    load_images.School_tiles_list[i][j] = pygame.transform.scale(load_images.School_tiles_list[i][j],(int(x),int(y)))

        
        if facility_name == 'FOUNTAIN' and (not self.Fountain_flag):
            
            load_images.load_images_facility('FOUNTAIN',model.Fountain.get_level())
            self.Fountain_flag = True
            for i in range(len(load_images.Fountain_tiles)):
                for j in range(len(load_images.Fountain_tiles[i])):
                    (x,y) = resize_pos(load_images.Fountain_tiles[i][j].get_size())
                    x *= transform_obj.ratio
                    y *= transform_obj.ratio
                    load_images.Fountain_tiles[i][j] = pygame.transform.scale(load_images.Fountain_tiles[i][j],(int(x),int(y)))
                    
            
        if facility_name == 'FARM' and (not self.Farm_flag):
            
            load_images.load_images_facility('FARM',model.Farm.get_level())
            self.Farm_flag = True            
            for i in range(len(load_images.Farm_tiles)):
                for j in range(len(load_images.Farm_tiles[i])):
                    (x,y) = resize_pos(load_images.Farm_tiles[i][j].get_size())
                    x *= transform_obj.ratio
                    y *= transform_obj.ratio
                    load_images.Farm_tiles[i][j] = pygame.transform.scale(load_images.Farm_tiles[i][j],(int(x),int(y)))
            

images_obj = update_images()

class Animation:
    
    def __init__(self):
       
        
        
        global env
        if model.FLAG_XO:
            env = Environment()
        else:
            env = Environment2()
        env.update_background()
        mkt = Build('market.png',2800,2500)
        mkt.add(all,market)
    
    
    
    def update(self):
        ''' Creates the final surface with the background and all and with the sprites too '''
        
        transform_obj.move()
        transform_obj.check_pos() 
        if natural_calamities:
            #natural_calamities.clear(screen,self.background)
            natural_calamities.update()
        
        images_obj.update_images()
        check_sprite = screen_sprite()
        #screen.blit(self.background,(0,resize_pt_y(40)))
        #all_drawable.clear(screen,self.background)
        env.update_background()
        
        all_drawable.empty()
        all.update()
        drawable_sprites = pygame.sprite.spritecollide(check_sprite,all,False)
        for sprite in drawable_sprites:
            sprite.set_frame()
            sprite.add(all_drawable)
            
        
        # Checking for collision of villagers nd other facilities and the market
        collide = pygame.sprite.groupcollide(villagers, facilities_group, False, False)
        for villager in collide.keys():
            villager.collide_build()
        collide = pygame.sprite.groupcollide(villagers, market, False, False)
        for villager in collide.keys():
            villager.collide_build()
        collide = pygame.sprite.groupcollide(villagers, facilities_group, False, False)
        for villager in collide.keys():
            new_sprite = Villager(villager.get_attributes())
            villager.remove(all,villagers)
            villager.kill()
            new_sprite.add(villagers,all)
        collide = pygame.sprite.groupcollide(villagers, market, False, False)
        for villager in collide.keys():
            new_sprite = Villager(villager.get_attributes())
            villager.remove(all,villagers)
            villager.kill()
            new_sprite.add(villagers,all)
        check_villagers_self_collision()
        
        
        all_drawable.draw(screen)       
        if natural_calamities:
            natural_calamities.draw(screen)
        transform_obj.prev_ratio = transform_obj.ratio
 

class Sounds:
    '''Controls the sounds'''
    def __init__(self):
        self.SOUND_PATH = SOUND_PATH
        self.SOUND_DIC = {}
        self.SOUND_DIC = self.load_sound()
        self.volume = SOUND_VOLUME
    
    def load_sound(self,sound_path = SOUND_PATH):
        '''Gets a dictionary of sounds with just their names from SOUND_PATH and loads them into buffer'''
        sound_list = glob.glob(os.path.join(SOUND_PATH,'*.ogg'))
        sound_dic = {}
        for sound_name in sound_list:
            try:
                sound_dic[sound_name] = pygame.mixer.Sound(sound_name)
            except Exception is e:
                sound_dic[sound_name] = None
                print "Error Loading Sound: " + str(e)+ '\n ' + sound_name
        return sound_dic
    
    def play_sound(self,sound_name,volume = SOUND_VOLUME):
        '''Plays the requested sound effect
        The function shuffles between the available sound effects
        volume: [0.0 to 1.0] :volume [left, right]
        '''
        sound_set = []
        for key in self.SOUND_DIC:
            if sound_name in key:
                sound_set.append(key)
        sound_name = sound_set[random.randrange(0,len(sound_set))]
        sound_object = self.SOUND_DIC[sound_name]
        
        if sound_object:
            channel = sound_object.play()
            channel.set_volume(volume[0],volume[1])
            
    def play_music(self,storyboard_music_enabled,sound_name):
        if storyboard_music_enabled:
            if sound_name != 'soundtrack':
                loop = 1
            else:
                loop = -1
            if pygame.mixer.get_busy():
                pygame.mixer.music.stop()
            pygame.mixer.music.load(os.path.join('storyboards',str(model.storyboard_file),sound_name+'.ogg'))
            pygame.mixer.music.play(loop)
            pygame.mixer.music.set_volume((self.volume[0]+self.volume[1])/2)
        else:
            if pygame.mixer.get_busy():
                pygame.mixer.music.stop()
            pygame.mixer.music.load(os.path.join('sounds','soundtrack.ogg'))
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume((self.volume[0]+self.volume[1])/2)
              
    def stop_soundtrack(self):
        pygame.mixer.music.stop()
            
    def safe_exit(self):
        pygame.mixer.stop()
        
    def pause_music(self):
        pygame.mixer.pause()
            
natural_calamities = pygame.sprite.RenderUpdates()
villagers = pygame.sprite.Group()
all = pygame.sprite.RenderUpdates() 
facilities_group = pygame.sprite.Group()
market = pygame.sprite.Group()

transform_obj = Transform()
audio = Sounds()
all_drawable = pygame.sprite.RenderUpdates()
