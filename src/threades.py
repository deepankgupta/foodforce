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

from model import *
import model
import Exceptions                 
import threading   
import random   
from time import sleep,time,ctime
from texts import *

# import statements for animation classes
import pygame
import os
from pygame.locals import *
pygame.init()
from load_images import *


original_screen_size = (1200.0,900.0)

import gui
from gui import *
import defaultStyle
# Detecting the maximum resolution the machine can support
resolution_list = pygame.display.list_modes()
resolution_list.sort()
max_resolution = resolution_list.pop()
new_screen_size = max_resolution
# Max resolution detected and the screen size is set to it
new_screen_size = (950,700)
screen = pygame.display.set_mode(new_screen_size,0,32)

# For initialising the style of the guI
defaultStyle.init(gui)

desktop = Desktop()
# initializing values for constant
init_cons('data.pkl')

#initializing objects
init_obj()


def initialize_facilities():
    
    for i in range(INIT_HOUSE):
        build_facility(House)
    for i in range(INIT_HOSPITAL):
        build_facility(Hospital)
    for i in range(INIT_SCHOOL):
        build_facility(School)
    for i in range(INIT_FARM):
        build_facility(Farm)
    for i in range(INIT_FOUNTAIN):
        build_facility(Fountain)
    for i in range(INIT_WORKSHOP):
        build_facility(Workshop)
        
    Water.set_variables('WATER',INIT_WATER,INIT_M_WATER,COST_WATER)
    Buildmat.set_variables('BUILDING MATERIAL',INIT_BUILDMAT,INIT_M_BUILDMAT,COST_BUILDMAT)
    Tools.set_variables('TOOLS',INIT_TOOLS,INIT_M_TOOLS,COST_TOOLS)
    transform_obj.focus_at((1000,2000))
    transform_obj.set_ratio(0.5)



# A Switch for pausing the update thread
update_thread_pause = True



''' Definition of threads'''

def stop_facility(facility_obj):
    ''' Thread to stop a facility it resumes the facility when the village
    has enough resources to run the facility
    '''
    global resources
    message.push_message('Facility '+FACILITY_NAMES[facility_obj.get_name()]+' has been temporarily stopped due to insufficient resources to run the facility','high')
    res_cost = facility_obj.get_consumption()
    facility_obj.stop_facility()
    a=1
    while True:
        a=0
        
        for i in range(len(resources)):
            name = resources[i].get_name()
            if res_cost.has_key(name):
                if resources[i].get_vquantity() < res_cost[name]:
                    a=1
        if a==0:
            break
        sleep(2)

    facility_obj.resume_facility()
    message.push_message('Facility '+FACILITY_NAMES[facility_obj.get_name()]+' has been resumed','low')
    



def get_setup_text(facility_obj):
    
    text = ''
    text += 'Number :'
    text += str(int(facility_obj.get_original_number()))
    text += '   Level :'
    text += str(int(facility_obj.get_level()))
    text +='\n'
    cost_build = facility_obj.get_cost_build()
    text +='Resources required to build :  BUILDING MATERIAL:'+str(int(cost_build['BUILDING MATERIAL']))+' TOOLS :'+str(int(cost_build['TOOLS']))+' WATER :'+str(int(cost_build['WATER']))+'\n'
    cost_run = facility_obj.get_cons_dict()
    if cost_run:
        text +='Resources required to run : '
        for key in cost_run.keys():
            text +=key+': '+str(int(cost_run[key]))+' '
        text +='\n'
    text +='Manpower required : To build: '+str(int(FACILITY_MANP_DICT_BUILD[facility_obj.get_name()]['EMPLOYED PEOPLE IN CONSTRUCTION']))+' To run: '
    if FACILITY_MANP_DICT_RUN[facility_obj.get_name()]:
        for key in FACILITY_MANP_DICT_RUN[facility_obj.get_name()].keys():
            text +=str(int(FACILITY_MANP_DICT_RUN[facility_obj.get_name()][key]))
    else:
        text += '0'
    
    return text

def get_upgrade_text(facility_obj):
    
    text = ''
    if facility_obj.get_level() < 3:
        text += upgrade_text[facility_obj.get_name()][facility_obj.get_level()]
    else:
        text = 'You cannot upgrade the facility anymore, it has reached its maximum level'
    
    return text

def build_facility(facility_obj, list_food = ('0')):
    ''' Thread to build a new building of any facility
    '''
    global resources
    global ppl
    
    
    '''if not check_level(facility_obj):
        text = ' All the installations of ' + facility_obj.get_name() +' of this level have been made. Try setting up some other facilities'
        return text
    '''    
    if facility_obj.get_number() == 0:
        
        if facility_obj.get_original_number() > 0:
            text = 'You cannot build a facility when it has been temporarily stopped, try building it when it is resumed'
            return text
    
    try:
        
        resources=facility_obj.build_start(resources,ppl)
        
        if facility_obj.get_name() == 'FARM':
         
            
            qrice = list_food[0]*MAX_FOOD_PROD_PER_FARM/100
            qwheat = list_food[1]*MAX_FOOD_PROD_PER_FARM/100
            qbeans = list_food[2]*MAX_FOOD_PROD_PER_FARM/100
            prod = facility_obj.get_prod_dict()
            prod['RICE'] = (prod['RICE']*facility_obj.get_number() + qrice)/(facility_obj.get_number() + 1)
            prod['WHEAT'] = (prod['WHEAT']*facility_obj.get_number() + qwheat)/(facility_obj.get_number() + 1)
            prod['BEANS'] = (prod['BEANS']*facility_obj.get_number() + qbeans)/(facility_obj.get_number() + 1)
            facility_obj.set_production(prod)
           
            
        ppl = facility_obj.update_manp_res(ppl)
        
        
    except Exceptions.Resources_Underflow_Exception:
        return 'You dont have enough resources to build the facility,  please try later'
    except Exceptions.Low_Manpower_Resources_Exception:
        return 'You dont have enough manpower to build the facility, please try later'
    except Exceptions.Maximum_Number_Reached:
        return 'You cannot setup more buildings of this facility, try setting up some other facility'
    
    
    #ppl = facility_obj.build_end(ppl)
    if facility_obj.get_name() == 'HOUSE':
        sprite = House_sprite()
        house_sprite_list.append(sprite)
        
    if facility_obj.get_name() == 'HOSPITAL':
        sprite = Hospital_sprite()
        hospital_sprite_list.append(sprite)
        
    if facility_obj.get_name() == 'WORKSHOP':
        sprite = Workshop_sprite()
        workshop_sprite_list.append(sprite)
        
    if facility_obj.get_name() == 'SCHOOL':
        sprite = School_sprite()
        school_sprite_list.append(sprite)
        
    if facility_obj.get_name() == 'FARM':
        sprite = Farm_sprite()
        farm_sprite_list.append(sprite)
        
    if facility_obj.get_name() == 'FOUNTAIN':
        sprite = Fountain_sprite()
        fountain_sprite_list.append(sprite)
    add_sprite_all(sprite)
    add_sprite_facilities(sprite)
    
    # Generating villagers for each facility
    speeds = [[2,0],[-2,0],[0,2],[0,-2]]
    for attribute in facility_villagers[facility_obj.get_name()][facility_obj.get_original_number()-1]:
        print attribute
        dir = int(random.random()*4)
        villager = Villager(attribute)
        villager.set_speed(speeds[dir])
        villager.add(villagers,all)
    
    
    check_collide_villager(sprite) # Function to check if a sprite collides with the position of a villager

    return 'Facility has been build'

    
    
def check_level(facility_obj):
    ''' Function that checks whether a level has been completed or not and takes an appropriable action.
    Returns True if the facility can be built in the prsent cluster else returns False. Sends a message to 
    message queue when a level is completed.
    '''
    level_list = []
    level = 0
    for facility in facilities_list:
        if facility.get_original_number() < VILLAGE_LEVEL[0][facility.get_name()]:
            level = 0
        elif facility.get_original_number() < VILLAGE_LEVEL[1][facility.get_name()]:
            level = 1
        elif facility.get_original_number() <= VILLAGE_LEVEL[2][facility.get_name()]:
            level = 2
        level_list.append(level)
    level_list.sort()
    level = level_list.pop(0)
    if (facility_obj.get_original_number() +1) < VILLAGE_LEVEL[level][facility_obj.get_name()]:
        return True
    
    if (facility_obj.get_original_number() +1) == VILLAGE_LEVEL[level][facility_obj.get_name()]:
        flag = True
        for facility in facilities_list:
            if (not (facility == facility_obj)) and (not (facility.get_original_number() == VILLAGE_LEVEL[level][facility.get_name()])):
                flag = False
        if flag:
            message.push_message(' You have completed level ' + str(level+1),'high')
        return True
    
    if facility_obj.get_original_number() == VILLAGE_LEVEL[level][facility_obj.get_name()] and level < 2:
        return False
    
    
    
    
    

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
    global ppl
    ppl = facility_obj.build_end(ppl)




def upgrade_facility(facility_obj):
    ''' Upgrades a facility
    COMMENT : change the view of facility if you want to do so
    '''
    if facility_obj.get_number() == 0:
        
        if facility_obj.get_original_number() > 0:
            text = 'You cannot upgrade a facility when it has been temporarily stopped, try upgrading it when it is resumed'
            return text
        text = 'You need to setup a facility first to upgrade it'
        return text
        
    global resources
    try:
        resources = facility_obj.update_level(resources,ppl)
    except Exceptions.Resources_Underflow_Exception:
        text =  "You don't have enough resources to upgrade the facility please try later"
        return text
    except Exceptions.Maximum_Level_Reached:
        text =  'Facility has reached its maximum level you cant upgrade it now'
        return text
    
    
    
    # Updation of sprites
    for i in range(len(facilities_list_sprites[facility_obj.get_name()])):
        facilities_list_sprites[facility_obj.get_name()][i].upgrade_level()
    
    text = 'Facility has been upgraded'
    return text


def pause_update_thread():
    global update_thread_pause
    update_thread_pause = False


def resume_update_thread():
    global update_thread_pause
    update_thread_pause = True


def update_turn():
    ''' Updates the resources, facilities, manpower resources and indicators
    at each turn
    '''
    global resources
    global facilities_list
    global ppl
    global food_resources
    global Housing
    global Nutrition
    global Health
    global Water
    global School


    
    while True:
        
        if update_thread_pause == True:

            # updation of all facilities
            for i in range(len(facilities_list)):
                try:
                    resources = facilities_list[i].turn(resources)
                except Exceptions.Resources_Underflow_Exception:
                    
                    t = threading.Thread(target = stop_facility , args = [facilities_list[i]])
                    t.start()
                except Exceptions.Resources_Overflow_Exception:
                    pass 
    
            # updation of manpower resources
            
            resources = ppl.update_turn(resources,facilities_list)
    
        
    
            # updation of prices of resources and the check on resources if their market value decreases a certain value then it should increase it
            
            for i in range(len(resources)):
                resources[i].update_price()
                if resources[i].get_mquantity < 500:
                    resources[i].change_mquantity(8000)
    
    
    
    
    
            # updation of indicators
    
            # housing
            ratio_people_sheltered = ppl.get_no_of_ppl_sheltered()/ppl.get_total_population()
            Housing.turn({'SHELTERED PEOPLE' : ratio_people_sheltered})
    
            # nutrition
            ppl_fed_ratio = ppl.get_no_of_ppl_fed()/ppl.get_total_population()
            temp = FOOD_DIST_DICT_INIT
            protiens = 0
            vitamins = 0
            fats = 0
            for resource in food_resources:
                name = resource.get_name()
                if temp.has_key(name):
                    protiens += temp[name]['PROTIENS'] * resource.get_vquantity()
                    vitamins += temp[name]['VITAMINS'] * resource.get_vquantity()
                    fats += temp[name]['FATS'] * resource.get_vquantity()
                
            
            food = protiens + vitamins + fats
            protiens /= food
            vitamins /= food
            fats /= food
    
            Nutrition.turn({'PEOPLE FED' : ppl_fed_ratio , 'PROTIENS' : protiens , 'FATS' : fats , 'VITAMINS' : vitamins})
    
            # health
            healthy_ppl_ratio = ppl.get_no_of_ppl_healthy()/ppl.get_total_population()
            nutrition = Nutrition.get_value()
            nutrition /= MAX_INDICATOR
            water = Water.get_vquantity()/MAX_RES_VAL_VILLAGE
    
            Health.turn({'HEALTHY PEOPLE' : healthy_ppl_ratio , 'NUTRITION' : nutrition , 'WATER' : water})
    
            # education
            educated_ppl = ppl.get_no_of_ppl_educated()/ppl.get_total_population()
            level = School.get_level()/MAX_LEVELS_FACILITY
            Education.turn({'EDUCATED PEOPLE' : educated_ppl , 'LEVEL OF EDUCATION' : level })
    
            # training
            level = Workshop.get_level()/MAX_LEVELS_FACILITY
            ppl_workshop = ppl.get_no_of_ppl_emp_in_workshop()/ppl.get_total_population()
            ppl_farm = ppl.get_no_of_ppl_emp_in_farm()/ppl.get_total_population()    
            ppl_hospital = ppl.get_no_of_ppl_emp_in_hospital()/ppl.get_total_population()
            ppl_construction = ppl.get_no_of_ppl_emp_in_cons()/ppl.get_total_population()
            Training.turn({ 'LEVEL OF WORKSHOPS' : level , 'EMPLOYED PEOPLE IN WORKSHOP' : ppl_workshop , 'EMPLOYED PEOPLE IN FARM' : ppl_farm , 'EMPLOYED PEOPLE IN HOSPITAL' : ppl_hospital , 'EMPLOYED PEOPLE IN CONSTRUCTION' : ppl_construction })
    
        sleep(15)
            




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







    





def buy_res(res,res_quantity):
    ''' This method allows a user to buy resources
    '''
    global resources
    global money
    
    
    try:
        #print "The initial value of resources with the village is" , resources[i].get_vquantity()
        #print "The initial value of resources with the market is" , resources[i].get_mquantity()
        quantity=res_quantity
        #print 'initial money is'
        #print money.get_money()
        money = res.buy(quantity , money)
        #print 'final money is'
        #print money.get_money()
        #print "The final value of resources with the village is" , resources[i].get_vquantity()
        #print "The final value of resources with the market is" , resources[i].get_mquantity()
    except Exceptions.Money_Underflow_Exception:
        text ='You dont have enough money to buy this resource. Please change the quantity or try later'
        return text
    except Exceptions.Resources_Underflow_Exception:
        text ='The market doesnot have enough quantity to sell this resource to village'
        return text
    except Exceptions.Resources_Overflow_Exception:
        text ='The Village cannot store so much amount of resources you should try and use the money to buy some other resources '
        return text
        
    text = 'The Village has bought the resource you demanded'
    return text
        

    

    


def sell_res(res,res_quantity):
    ''' This method allows a user to sell resources
    '''
    global resources
    global money
    
    
    

    try:
        #print "The initial value of resources with the village is" , resources[i].get_vquantity()
        #print "The initial value of resources with the market is" , resources[i].get_mquantity()
        quantity=res_quantity
        money = res.sell(quantity , money)        
        #print "The final value of resources with the village is" , resources[i].get_vquantity()
        #print "The final value of resources with the market is" , resources[i].get_mquantity()
    except Exceptions.Resources_Underflow_Exception:
        text = 'The village doesnot have enough quantity to sell this resource to market'
        return text
    except Exceptions.Resources_Overflow_Exception:
        text = 'The Village has sold the resource you demanded'
        return text
    text = 'The Village has sold the resource you demanded'
    return text
    
    
    

def demolish_facility(facility_name):
    ''' Function to demolish a facility
    '''
    # Calls the demolish function of the facility and removes its sprite from all groups
    global ppl
    
    if (facility_name == 'House') and (House.get_number()>0):
        
        ppl = House.demolish(ppl)
        sprite = house_sprite_list.pop(0)
        sprite.kill()
    
    if (facility_name == 'Hospital') and (Hospital.get_number()>0):
        ppl = Hospital.demolish(ppl)
        sprite = hospital_sprite_list.pop(0)
        sprite.kill()
    
    if (facility_name == 'Workshop') and (Workshop.get_number()>0):
        ppl = Workshop.demolish(ppl)
        sprite = workshop_sprite_list.pop(0)
        sprite.kill()
    
    if (facility_name == 'School') and (School.get_number()>0):
        ppl = School.demolish(ppl)
        sprite = school_sprite_list.pop(0)
        sprite.kill()
    
    if (facility_name == 'Farm') and (Farm.get_number()>0):
        ppl = Farm.demolish(ppl)
        sprite = farm_sprite_list.pop(0)
        sprite.kill()
    
    if (facility_name == 'Fountain') and (House.get_number()>0):
        ppl = Fountain.demolish(ppl)
        sprite = fountain_sprite_list.pop(0)
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
    global ppl
    global Water
    global Farm
    
    
    try :
        Water.change_vquantity(1000)
    except :
        pass
    
    Hospital.stop_facility()
    House.stop_facility()  # we can comment it out even....
    School.stop_facility()
    Workshop.stop_facility()
    Farm.stop_facility()
     
    sleep(90)                   # that means for five turns
    
    Hospital.resume_facility()
    House.resume_facility()
    School.resume_facility()
    Workshop.resume_facility()
    Farm.resume_facility()
    
    
def famine():
    '''This method needs to be called when there is an famine in the village
    It will stop the production of farms for some time, five turns
    '''
    
    global Farm
    
    Farm.stop_facility()
    sleep(90)
    Farm.resume_facility()
    
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
            color = (0,127,0) # Green
        if priority == 'medium':
            color = (0,0,127) # Blue
        if priority == 'high':
            color = (127,0,0) # Red
        
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
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.level = Workshop.get_level()
        self.built_flag = 0
        transform_obj.focus_at(workshop_posn_list[Workshop.get_number()-1])
        self.image = transform_obj.transform_surface(Workshop_tiles_list[self.level][self.frame])
        self.rect = self.image.get_rect()
        self.position = workshop_posn_list[Workshop.get_number()-1]
        self.position_rect = self.rect.move(self.position)
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        self.tile_time = 0

    def update(self):
        if self.tile_time < 2000:
            self.tile_time += iteration_time
        else:
            self.tile_time = 0
            
            if (self.frame >= 2 and self.level ==0) :
                if (self.frame == 2 and self.built_flag == 0) :
                    build_end_facility(Workshop)
                    self.built_flag = 1
            elif (self.frame >= 2 and self.level ==1) :
                pass
            elif (self.frame >= 2 and self.level ==2) :
                pass
            elif (self.frame >= 2 and self.level ==3) :
                pass
            else:
                self.frame += 1
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
            
        
    def set_frame(self):
        self.image = transform_obj.transform_surface(Workshop_tiles_list[self.level][self.frame])
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

  
class House_sprite(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Saving tiles of all the upgrades in tiles_list
        self.frame = 0
        self.level = House.get_level()
        self.built_flag = 0
        transform_obj.focus_at(house_posn_list[House.get_number()-1])
        self.image = transform_obj.transform_surface(House_tiles_list[self.level][self.frame])
        self.rect = self.image.get_rect()
        self.position = house_posn_list[House.get_number()-1]
        self.position_rect = self.rect.move(self.position)
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        self.tile_time = 0

    def update(self):
        if self.tile_time < 2000:
            self.tile_time += iteration_time
        else:
            self.tile_time = 0
            
            if (self.frame >= 3 and self.level ==0) :
                if (self.frame == 3 and self.built_flag == 0) :
                    build_end_facility(House)
                    self.built_flag = 1
            elif (self.frame >= 2 and self.level ==1) :
                pass
            elif (self.frame >= 2 and self.level ==2) :
                pass
            elif (self.frame >= 2 and self.level ==3) :
                pass
            else:
                self.frame += 1
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
            
        
    def set_frame(self):
        self.image = transform_obj.transform_surface(House_tiles_list[self.level][self.frame])
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

        
class Hospital_sprite(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Saving tiles of all the upgrades in tiles_list
        self.frame = 0
        self.level = Hospital.get_level()
        self.built_flag = 0
        transform_obj.focus_at(hospital_posn_list[Hospital.get_number()-1])
        self.image = transform_obj.transform_surface(Hospital_tiles_list[self.level][self.frame])
        self.rect = self.image.get_rect()
        self.position = hospital_posn_list[Hospital.get_number()-1]
        self.position_rect = self.rect.move(self.position)
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        self.tile_time = 0

    def update(self):
        if self.tile_time < 2000:
            self.tile_time += iteration_time
        else:
            self.tile_time = 0
            
            if (self.frame >= 3 and self.level ==0) :
                if (self.frame == 3 and self.built_flag == 0) :
                    build_end_facility(Hospital)
                    self.built_flag = 1
            elif (self.frame >= 2 and self.level ==1) :
                pass
            elif (self.frame >= 2 and self.level ==2) :
                pass
            elif (self.frame >= 2 and self.level ==3) :
                pass
            else:
                self.frame += 1
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
            
        
    def set_frame(self):
        self.image = transform_obj.transform_surface(Hospital_tiles_list[self.level][self.frame])
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
        
        
class School_sprite(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
       # Saving tiles of all the upgrades in tiles_list
        
        
        self.frame = 0
        self.level = School.get_level()
        self.built_flag =0
        transform_obj.focus_at(school_posn_list[School.get_number()-1])
        self.image = transform_obj.transform_surface(School_tiles_list[self.level][self.frame])
        self.rect = self.image.get_rect()
        self.position = school_posn_list[School.get_number()-1]
        self.position_rect = self.rect.move(self.position)
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        self.tile_time =0
        

    def update(self):
        if self.tile_time < 2000:
            self.tile_time += iteration_time
        else:
            self.tile_time = 0
            
            if (self.frame >= 3 and self.level ==0) :
                if (self.frame == 3 and self.built_flag == 0) :
                    build_end_facility(School)
                    self.built_flag = 1
            elif (self.frame >= 2 and self.level ==1) :
                pass
            elif (self.frame >= 2 and self.level ==2) :
                pass
            elif (self.frame >= 2 and self.level ==3) :
                pass
            else:
                self.frame += 1
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
            
        
    def set_frame(self):
        self.image = transform_obj.transform_surface(School_tiles_list[self.level][self.frame])
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

 
class Farm_sprite(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Saving tiles of all the upgrades in tiles_list
        self.frame = 0
        self.built_flag = 0
        transform_obj.focus_at(farm_posn_list[Farm.get_number()-1])
        self.image = transform_obj.transform_surface(Farm_tiles[0][self.frame])
        self.rect = self.image.get_rect()
        self.position = farm_posn_list[Farm.get_number()-1]
        self.position_rect = self.rect.move(self.position)
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        self.tile_time = 0
        

    def update(self):
        
        if self.tile_time < 2000:
            self.tile_time += iteration_time
        else:
            self.tile_time = 0
            
            if (self.frame >= 2) :
                if (self.frame == 2 and self.built_flag == 0) :
                    build_end_facility(Farm)
                    self.built_flag = 1
            else:
                self.frame += 1
            
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        
  

    def set_frame(self):
        self.image = transform_obj.transform_surface(Farm_tiles[0][self.frame])
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        
    def get_position(self):
        ''' Returns the position rect of the sprite
        '''
        return self.position_rect
    
    def upgrade_level(self):
        transform_obj.focus_at(self.position)

    
class Fountain_sprite(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Saving tiles of all the upgrades in tiles_list
        self.frame = 0
        self.built_flag = 0
        transform_obj.focus_at(fountain_posn_list[Fountain.get_number()-1])
        
        self.image = transform_obj.transform_surface(Fountain_tiles[0][self.frame])
        self.rect = self.image.get_rect()
        self.position = fountain_posn_list[Fountain.get_number()-1]
        self.position_rect = self.rect.move(self.position)
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        self.tile_time = 0
        

    def update(self):
        
        if self.tile_time < 2000:
            self.tile_time += iteration_time
        else:
            self.tile_time = 0
            
            if (self.frame >= 3) :
                if (self.frame == 3 and self.built_flag == 0) :
                    build_end_facility(Fountain)
                    self.built_flag = 1
            else:
                self.frame += 1
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        
    def set_frame(self):
        self.image = transform_obj.transform_surface(Fountain_tiles[0][self.frame])
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        
    def get_position(self):
        ''' Returns the position rect of the sprite
        '''
        return self.position_rect
    
    def upgrade_level(self):
        transform_obj.focus_at(self.position)

class Environment(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        spritesheet = Spritesheet('tileset.png')
        self.tiles = spritesheet.imgat((0,0,930,560))
        self.tiles = pygame.transform.scale(self.tiles,resize_pos((930,560)))
        
    def get_background(self):
        
        background = pygame.Surface(resize_pos((930,560))).convert()
        
        background.blit(self.tiles, (0,0))     
        
        return background
        
        
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
        self.rect = self.rect.move(transform_obj.transform_cordinates((x, y)))
        
    def update(self):
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates((self.x, self.y)))
        
    def set_frame(self):
        
        self.image = transform_obj.transform_surface(self.market_image)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(transform_obj.transform_cordinates((self.x, self.y)))
        
    
def add_sprite_all(sprite):
    sprite.add(all)    
    
def add_sprite_facilities(sprite):
    sprite.add(facilities_group)    

class screen_sprite(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.surface.Surface(resize_pos((1200,560)))
        self.rect = Rect(resize_rect((0,40,1000,560)))
        
#def check_villagers_collide_facility():
class Villager(pygame.sprite.Sprite):
    
    def __init__(self,(name,range_rect)):
        pygame.sprite.Sprite.__init__(self)
        self.dx = 2
        self.dy = 2
        self.speed = [2, 0]
        self.speed_time = 0
        self.tile_time =0
        self.name = name
        self.range = range_rect
        if name == 'Man':
            self.tiles = Man_tiles[0]
        
        if name == 'Woman':
            self.tiles = Woman_tiles[0]
        
        if name == 'Boy':
            self.tiles = Boy_tiles[0]
        
        if name == 'Girl':
            self.tiles = Girl_tiles[0]
        
        self.frame = 0
        self.set_direction()
        self.image = transform_obj.transform_surface(self.dtiles[self.frame])
        self.rect = self.image.get_rect()
        
        flag =True
        while flag:
            flag = False
            self.initial_position = [self.range[0]+int(random.random()*self.range[2]), self.range[1]+int(random.random()*self.range[3])]
            self.position = self.initial_position
            self.position_rect = self.rect.move(self.position)
            for key in facilities_list_sprites.keys(): 
                sprite_list = facilities_list_sprites[key]
                for sprite in sprite_list:
                    self.test_rect = sprite.get_position()
                    if self.test_rect.colliderect(self.position_rect):
                        
                        flag = True
        
        self.prev_disp = transform_obj.transform_cordinates(self.position)
        self.rect = self.rect.move(self.prev_disp)
        
    
    def set_direction(self):
        
        
        sp = self.speed
        if sp[0] > 0  and sp[1] == 0:
            self.dtiles = self.tiles[0:4]
        elif sp[0] < 0  and sp[1] == 0:
            self.dtiles = self.tiles[4:8]
        elif sp[0] == 0  and sp[1] < 0:
            self.dtiles = self.tiles[8:12]
        elif sp[0] == 0  and sp[1] > 0:
            self.dtiles = self.tiles[12:16]
            
    def collide_build(self):
        #self.rect = self.rect.move([-2*self.speed[0], -2*self.speed[1]])
        
        self.set_speed(map(lambda x: -x, self.speed))
        self.update()
        self.set_direction()

    '''
    def collide_build(self):
        print 'collide build called'
        sp = self.speed
        dx = self.dx
        dy = self.dy
        if sp[0] < 0  and sp[1] == 0:
            self.speed = [dx, 0]
        elif sp[0] > 0  and sp[1] == 0:
            self.speed = [-dx, 0]
        elif sp[0] == 0  and sp[1] < 0:
            self.speed = [0, dy]
        elif sp[0] == 0  and sp[1] > 0:
            self.speed = [0, -dy]  
            
        self.set_direction()
    '''
    def set_speed(self, speed):
        
        
        self.speed = speed
        self.set_direction()
    
    def update(self):
    
        self.speed_time += iteration_time
        self.tile_time +=iteration_time
        
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
        self.position = [self.position[0] + (self.speed[0]*iteration_time/100.0), self.position[1] + (self.speed[1]*iteration_time/100.0)]
        self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        
        if self.position[0] <= 0 or (self.position[0]+100) >= ANIMRECT.width or self.position[0] <= (self.range[0]) or self.position[0] >= (self.range[0]+self.range[2]):
            self.speed[0] = -self.speed[0]
            
            self.rect = self.image.get_rect()
            self.position[0] += self.speed[0]*iteration_time/100.0
            self.position[1] += self.speed[1]*iteration_time/100.0
            self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
            
        elif self.position[1] <= 0 or (self.position[1]-100) >= ANIMRECT.height or self.position[1] <= (self.range[1]) or self.position[1] >= (self.range[1]+self.range[3]):
            self.speed[1] = -self.speed[1]
            
            self.rect = self.image.get_rect()
            self.position[0] += self.speed[0]*iteration_time/100.0
            self.position[1] += self.speed[1]*iteration_time/100.0
            self.rect = self.rect.move(transform_obj.transform_cordinates(self.position))
        self.set_direction()
        #self.rect.clamp_ip(ANIMRECT)    
    def set_frame(self):
        self.image = transform_obj.transform_surface(self.dtiles[self.frame])
        
    def get_attributes(self):
        return (self.name,self.range)
    def get_name(self):
        return self.name

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
        self.ratio = 0.4
        self.motion_up = 0
        self.motion_down = 0
        self.motion_left = 0
        self.motion_right = 0
        self.mouse_move_flag = True
    
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
        speed = 50
        if self.motion_up:
            self.pos_y -= speed*iteration_time/1000
        if self.motion_down:
            self.pos_y += speed*iteration_time/1000
        if self.motion_right:
            self.pos_x+= speed*iteration_time/1000
        if self.motion_left:
            self.pos_x -= speed*iteration_time/1000
  
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
        if self.pos_x > (int(self.ratio*9000) - 1200):
            self.pos_x = (int(self.ratio*9000) - 1200)
        if self.pos_y < 0:
            self.pos_y = 0
        if self.pos_y > (int(self.ratio*6000) - 560):
            self.pos_y = (int(self.ratio*6000) - 560)
            
    
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
        self.ratio = 0.7
        self.pos_x = int(x*self.ratio) -500
        self.pos_y = int(y*self.ratio) - 80
  
    def transform_cordinates(self,(x,y)):
        newx = x*self.ratio - self.pos_x
        newy = y*self.ratio - self.pos_y + resize_pt_y(40)
        return (int(newx),int(newy))
 
    def set_ratio(self,ratio):
        self.ratio = ratio
  
    def transform_surface(self,surface):
        (x,y) = surface.get_size()
        x *= self.ratio
        y *= self.ratio
        surface = pygame.transform.scale(surface, (int(x),int(y)))
        return surface
    
    
  
   

class Animation:
    
    def __init__(self):
        global surface3
        
        env = Environment()
        self.background = env.get_background()
        screen.blit(self.background,(0,40))
        mkt = Build('market.png',2800,2500)
        mkt.add(all,market)
    
    
    def update(self):
        ''' Creates the final surface with the background and all and with the sprites too '''
        
        global surface3
        transform_obj.move()
        transform_obj.check_pos() 
        if natural_calamities:
            natural_calamities.clear(screen,self.background)
            natural_calamities.update()
        
        check_sprite = screen_sprite()
        screen.blit(self.background,(0,resize_pt_y(40)))
        #all_drawable.clear(screen,self.background)
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
 

natural_calamities = pygame.sprite.RenderUpdates()
villagers = pygame.sprite.Group()
all = pygame.sprite.RenderUpdates() 
facilities_group = pygame.sprite.Group()
market = pygame.sprite.Group()
transform_obj = Transform()
#surface3 = pygame.surface.Surface((1200,560))
all_drawable = pygame.sprite.RenderUpdates() 
    

