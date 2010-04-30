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
#
import gui
import pygame
#from threades import *
import threades
#from Foodforce2 import safe_exit
#from gui import *
import threading
#from model import *
import load_images
import model
import os
from pygame.locals import *

desktop_level=gui.Desktop()
#level=1
animation_obj=None


class change_level:
    
    
    def __init__(self):
        self.level_no=-1
    def new_level_stats(self,data_file,graphics_file,level_no=-1):
        #global total_update_flag 
        global animation_obj
        threades.pause_update_thread()           
        self.graphics()
        self.level_no=level_no
        self.data_file=data_file
        self.graphics_file=graphics_file
        self.run=True
        level_updater=threading.Thread(target=self.level_reinit,args=[]).start()
        
        pygame.display.set_caption('FoodForce2')
        threades.screen.fill((0,0,0))
        threades.screen.blit(self.ff_logo,threades.resize_pos((40,90)))
        
        desktop_level.update()
        desktop_level.draw()
        pygame.display.update()
            
        while 1 :
            
            for e in gui.setEvents(pygame.event.get()):
                if e.type == pygame.QUIT:
                    print 'in pygame.quit'                    
                    safe_exit()
                if e.type == QUIT:
                    print 'in quit'
                    safe_exit()

            #if level_updater.is_alive()==False:
               # self.run=False      GREAT THIS IS APPLICABLE ONLY WITH PYTHON 2.6, SO HAVE TO SEARCH SOME OTHER MEANS
            if self.run==False:
                break
           
        
            
        self.ff_logo = 0
        threades.initialize_facilities(True)
        threades.set_build_facility_placement_flag()
        threades.facility_placement_data_obj.clear_placement_data()
        #threades.current_level = proceduralFlow.storyboard_level
                
        threades.total_update_flag = True
        threades.resume_update_thread()

        
        
    def level_reinit(self):
        

        #emptying all the groups present in threads.py
        model.house_sprite_list = []
        model.hospital_sprite_list = []
        model.workshop_sprite_list = []
        model.school_sprite_list = []
        model.farm_sprite_list = []
        model.fountain_sprite_list = []

        model.facilities_list_sprites = { 'HOUSE':model.house_sprite_list, 'HOSPITAL':model.hospital_sprite_list, 'FARM':model.farm_sprite_list, 'SCHOOL':model.school_sprite_list, 'WORKSHOP':model.workshop_sprite_list, 'FOUNTAIN':model.fountain_sprite_list}

        
        
        local_list = threades.natural_calamities.sprites()
        #natural_calamities.clear()
        i=0
        for sprite in local_list:
            sprite.kill()
            i+=1
        threades.natural_calamities.empty()
        #print i
        
        i=0
        local_list = threades.villagers.sprites()
        #villagers.clear()
        for sprite in local_list:
            sprite.kill()
            i+=1 
        threades.villagers.empty()
        #print i
        
        
        local_list = threades.all.sprites()
        #all.clear()
        for sprite in local_list:
            sprite.kill()
        threades.all.empty()
        
        local_list = threades.facilities_group.sprites()
        #facilities_group.clear()
        for sprite in local_list:
            sprite.kill()
        threades.facilities_group.empty()
        
        local_list = threades.market.sprites()
        #market.clear()
        for sprite in local_list:
            sprite.kill()
        threades.market.empty()
        
        local_list = threades.all_drawable.sprites()
        #all_drawable.clear()
        for sprite in local_list:
            sprite.kill()
        threades.all_drawable.empty()
        
                
        model.init_cons(self.data_file)
        model.init_obj()
        load_images.graphics_layout(self.graphics_file)
        
        mkt = threades.Build('market.png',2800,2500)
        mkt.add(threades.all,threades.market)
    
        threades.images_obj.__init__()
        self.run=False
        #print 'reached at last'
        
        
        
        
        
        
    def graphics(self):
        logo = pygame.image.load(os.path.join('data', 'logo.png')).convert()
        self.ff_logo = pygame.transform.scale(logo,threades.resize_pos((1128,171)))
        threades.screen.fill((0,0,0))
        threades.screen.blit(self.ff_logo,threades.resize_pos((40,50)))

        # Font type
        myfont = pygame.font.Font("font.ttf", threades.resize_pt(17))

        
        #creating new label showing loading of level
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 1
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont
        labelStyleCopy['font-color'] = (0,200,0)
        
        text1='Loading....'
            
        #creating the label
        label = gui.Label(position = threades.resize_pos((500,600)), size = threades.resize_pos((250,50)), parent = desktop_level,style=labelStyleCopy,text=text1)
        
        #self.run=True
        
        