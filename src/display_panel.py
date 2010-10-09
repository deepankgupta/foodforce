#! /usr/bin/env python
# -*- coding: ISO-8859-1 -*-
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

from sys import exit
import os
from time import *
#from threades import *
import threades
import threading

import gui
#from gui import *
#from gui_buttons import *
import gui_buttons
import model
#from model import *
import pygame
import load_images
import texts_spa
import texts_eng

class bar:

    color_bar = (47,47,255)

    def __init__(self, (x_value, y_value)):
        ''' Draws a bar on the surface at posn x,y
        '''
        self.x = x_value
        self.y = y_value

        pygame.draw.rect(threades.screen,self.color_bar,threades.resize_rect((self.x,self.y,250,18)),2)

        pygame.draw.rect(threades.screen,(255,255,255),threades.resize_rect((self.x+2,self.y+2,246,14)))



    def update_value(self,value):
        '''Updates the value of the bar
        '''

        max_value = 100.0
        max_pixel = 246.0
        colour = (177,135,73)           
        pygame.draw.rect(threades.screen,self.color_bar,threades.resize_rect((self.x,self.y,250,18)),2)        
        pygame.draw.rect(threades.screen,colour,threades.resize_rect((self.x+2,self.y+2,value/max_value*max_pixel,14)))
        pygame.draw.rect(threades.screen,(255,255,255),threades.resize_rect((self.x+2+value/max_value*max_pixel,self.y+2,max_pixel-value/max_value*max_pixel,14)))







class indicator_panel:

    ##global threades.desktop
    font_bg_color = (0,0,0)       # This should be same as  the background colour for the label
    font_color = (255,214,150)    # This should be same as that for the font to be written on the label
    color_grey = (160,160,160)
    def __init__(self):
        ''' Draws the indicator panel on the surface
        '''
        self.update_flag = True
        
        self.name_labels = []
        myfont1 = pygame.font.Font("font.ttf", threades.resize_pt(30))   # For main heading

        myfont2 = pygame.font.Font("font.ttf", threades.resize_pt(20))   # For indicators name
        myfont3 = pygame.font.Font("font.ttf", threades.resize_pt(16))
        # Creating a custom label style
        self.labelstyle1 = gui.defaultLabelStyle.copy()
        self.labelstyle1['border-width'] = 1
        self.labelstyle1['wordwrap'] = True
        self.labelstyle1['autosize'] = False
        self.labelstyle1['font'] = myfont1
        self.labelstyle1['font-color'] = self.font_color
        self.labelstyle1['border-color'] = self.color_grey
        # Drawing main Indicator label
        label = gui.Label(position = threades.resize_pos((900,600)),size = threades.resize_pos((300,45)), parent = threades.desktop, text = "  "+model.text_file.indicators_text[0], style = self.labelstyle1)
        self.name_labels.append(label)
        #print " deawing indicator panel"
        
        # Creating second custom label
        self.labelstyle2 = gui.defaultLabelStyle.copy()
        self.labelstyle2['border-width'] = 0
        self.labelstyle2['wordwrap'] = True
        self.labelstyle2['autosize'] = False
        self.labelstyle2['font'] = myfont2
        self.labelstyle2['font-color'] = self.font_color
        self.labelstyle2['border-color'] = self.color_grey
        
        
        # Drawing all the indicators

        # Creating second custom label
        self.labelstyle3 = gui.defaultLabelStyle.copy()
        self.labelstyle3['border-width'] = 0
        self.labelstyle3['wordwrap'] = False
        self.labelstyle3['autosize'] = True
        self.labelstyle3['font'] = myfont3
        self.labelstyle3['font-color'] = self.font_color
        self.labelstyle3['border-color'] = self.color_grey
        
        # Empty Dictionary for bar
        self.bar_dict = []
        
        name_label_size = threades.resize_pos((300,25))
        self.value_labels = []
        for i in range(5):
            label = gui.Label(position = threades.resize_pos((900,650+50*i)),size = name_label_size, parent = threades.desktop, text = model.text_file.ind_namelist[i], style = self.labelstyle2)
            self.name_labels.append(label)
            self.bar_dict.append(bar((902,677+50*i)))
            label = gui.Label(position = threades.resize_pos((1160,677+50*i)), parent = threades.desktop, text = str(0), style = self.labelstyle3)
            self.value_labels.append(label)
            

    
    def update_name(self):
        
        self.name_labels[0].text = model.text_file.indicators_text[0]
        for i in range(1,6):
            self.name_labels[i].text = model.text_file.ind_namelist[i-1]
            


    def update_value(self):
        ''' Updates the values of all the indicators
        '''
        
        for i in range(5):

            self.bar_dict[i].update_value(model.indicators_list[i].get_value())
            if not (self.value_labels[i].text == str(int(model.indicators_list[i].get_value()))+'%'):
                self.update_flag = True
                
        #print 'update flag is',self.update_flag,'panel flag is',threades.panel_update_flag,'total is',threades.total_update_flag
        
        if self.update_flag or threades.panel_update_flag or threades.total_update_flag:
            pygame.draw.line(threades.screen,self.color_grey,threades.resize_pos((900,645)),threades.resize_pos((900,900)),1)
        
            for i in range(5):
    
                self.bar_dict[i].update_value(model.indicators_list[i].get_value())
                if not (self.value_labels[i].text == str(int(model.indicators_list[i].get_value()))+'%'):
                    self.value_labels[i].text = str(int(model.indicators_list[i].get_value()))+'%'

        self.update_flag = False
        




class resources_panel:


    ##global threades.desktop
    font_bg_color = (0,0,0)             # This should be same as  the background colour for the label
    font_color = (255,214,150)      # This should be same as that for the font to be written on the label
    color_grey = (160,160,160)
    def __init__(self):
        ''' Draws the model.resources panel on the surface
        '''
        
        self.update_flag = True
        self.money_flag = True
        self.time_flag = False
        self.time_help_value=0
        myfont1 = pygame.font.Font("font.ttf", threades.resize_pt(30))   # For main heading
        myfont2 = pygame.font.Font("font.ttf", threades.resize_pt(20))   # For model.resources name and their value
        myfont3 = pygame.font.Font("font.ttf", threades.resize_pt(16))
        myfont4 = pygame.font.Font("font.ttf", threades.resize_pt(18))   # For the display of model.money
        
        # Creating a custom label style
        self.labelstyle1 = gui.defaultLabelStyle.copy()
        self.labelstyle1['border-width'] = 1
        self.labelstyle1['wordwrap'] = True
        self.labelstyle1['autosize'] = False
        self.labelstyle1['font'] = myfont1
        self.labelstyle1['font-color'] = self.font_color
        self.labelstyle1['border-color'] = self.color_grey
        
        self.name_labels = []
        # Drawing main Resources rectangle
        label = gui.Label(position = threades.resize_pos((400,600)),size = threades.resize_pos((500,45)), parent = threades.desktop, text = "                    "+model.text_file.resources_text[0], style = self.labelstyle1)
        self.name_labels.append(label)
        # Creating second label style
        self.labelstyle2 = gui.defaultLabelStyle.copy()
        self.labelstyle2['border-width'] = 0
        self.labelstyle2['wordwrap'] = True
        self.labelstyle2['autosize'] = False
        self.labelstyle2['font'] = myfont2
        self.labelstyle2['font-color'] = self.font_color
        
        self.labelstyle3 = gui.defaultLabelStyle.copy()
        self.labelstyle3['border-width'] = 0
        self.labelstyle3['wordwrap'] = False
        self.labelstyle3['autosize'] = True
        self.labelstyle3['font'] = myfont3
        self.labelstyle3['font-color'] = self.font_color
        
        self.labelstyle4 = gui.defaultLabelStyle.copy()
        self.labelstyle4['border-width'] = 0
        self.labelstyle4['wordwrap'] = False
        self.labelstyle4['autosize'] = True
        self.labelstyle4['font'] = myfont4
        self.labelstyle4['font-color'] = (160,160,160)
        self.money_label = gui.Label(position = threades.resize_pos((850,10)), parent = threades.desktop, text = model.text_file.money_text[0]+' -:   '+str(int(model.money.get_money()))+'      ', style = self.labelstyle4)
        self.name_labels.append(self.money_label)
        self.time_label= gui.Label(position = threades.resize_pos((300,10)), parent = threades.desktop, text = model.text_file.time_text[0]+' -:   '+model.text_file.time_text[1]+'      ', style = self.labelstyle4)
        self.name_labels.append(self.time_label)
        self.value_labels = []
        # Drawing general model.resources list
        
        for i in range(5):
            label = gui.Label(position = threades.resize_pos((400,645+35*i)),size = threades.resize_pos((200,35)), parent = threades.desktop, text = model.text_file.list_gen_res[i], style = self.labelstyle2)
            self.name_labels.append(label)
            label = gui.Label(position = threades.resize_pos((605,649+35*i)), parent = threades.desktop, text = str(int(model.resources[i].get_vquantity())), style = self.labelstyle3)
            self.value_labels.append(label)
            
        # Drawing food model.resources list
        
        for i in range(6):
            label = gui.Label(position = threades.resize_pos((650,645+35*i)),size = threades.resize_pos((200,35)), parent = threades.desktop, text = model.text_file.list_food_res[i], style = self.labelstyle2)
            self.name_labels.append(label)
            label = gui.Label(position = threades.resize_pos((855,649+35*i)), parent = threades.desktop, text = str(int(model.resources[i+5].get_vquantity())), style = self.labelstyle3)
            self.value_labels.append(label)
            
            
    def update_name(self):
        
        self.name_labels[0].text = "                    "+model.text_file.resources_text[0]
        self.name_labels[1].text = model.text_file.money_text[0]+' -: '+str(int(model.money.get_money()))+'      '
        self.name_labels[2].text = model.text_file.time_text[0]+' -: '+model.text_file.time_text[1]+'      '
        for i in range(3,8):
            self.name_labels[i].text = model.text_file.list_gen_res[i-3]
            
        for i in range(8,14):
            self.name_labels[i].text = model.text_file.list_food_res[i-8]
            

    def update_value(self):
        ''' Updates the model.resources panel
        '''

        self.money_flag = False
        for i in range(11):
            if not (self.value_labels[i].text == str(int(model.resources[i].get_vquantity()))):
                self.update_flag = True
        
        if self.update_flag or threades.panel_update_flag or threades.total_update_flag:
           
            
            pygame.draw.line(threades.screen,self.color_grey,threades.resize_pos((400,645)),threades.resize_pos((400,855)),1)
            pygame.draw.line(threades.screen,self.color_grey,threades.resize_pos((650,645)),threades.resize_pos((650,855)),1)
    
            for i in range(11):
                if not (self.value_labels[i].text == str(int(model.resources[i].get_vquantity()))):
                    self.value_labels[i].text = str(int(model.resources[i].get_vquantity()))
        
        if not (self.money_label.text == model.text_file.money_text[0] +' -:   '+str(int(model.money.get_money()))+'      '):
            self.money_flag = True
            self.money_label.text = model.text_file.money_text[0] +' -:   '+str(int(model.money.get_money()))+'      '
         
        #print 'no of days is',model.game_controller.get_days()
        if self.time_flag==True:
            #self.time_label.text=''
            #NOTE: Here, I am not adding as if years is not 0 , then only it will be blitted becoz if do like that the things will keep on changing, not a nice view
            self.time_label.text= model.text_file.time_text[0]+' -:   '+model.text_file.time_text[2]+': '+str(model.game_controller.get_years())+'  '+model.text_file.time_text[3]+': '+str(model.game_controller.get_months()) +'  '+model.text_file.time_text[4]+': '+str(model.game_controller.get_days()) 
            self.time_flag=True
            
        #to update the money flag
        
        #print 'global_time is',model.game_controller.get_global_time(),'while the time_help_value is',self.time_help_value
        if (model.game_controller.get_global_time()>((model.game_controller.conversion_factor)+self.time_help_value)):
            self.time_flag=True
            self.time_help_value=model.game_controller.get_global_time()
            
            
        self.update_flag = False
        
    
    
    


class manpower_panel:

    ##global threades.desktop
    font_bg_color = (0,0,0)       # This should be same as  the background colour for the label
    font_color = (255,214,150)    # This should be same as that for the font to be written on the label
    color_grey = (160,160,160)
    def __init__(self):
        ''' Draws the manpower panel
        '''
        
        self.update_flag = True
        myfont1 = pygame.font.Font("font.ttf", threades.resize_pt(30))   # For main heading
        myfont2 = pygame.font.Font("font.ttf", threades.resize_pt(20))   # For model.resources name and their value
        myfont3 = pygame.font.Font("font.ttf", threades.resize_pt(16))   # For model.resources name and their value

        # Creating a custom label style
        self.labelstyle1 = gui.defaultLabelStyle.copy()
        self.labelstyle1['border-width'] = 1
        self.labelstyle1['wordwrap'] = True
        self.labelstyle1['autosize'] = False
        self.labelstyle1['font'] = myfont1
        self.labelstyle1['font-color'] = self.font_color
        self.labelstyle1['border-color'] = self.color_grey
        self.name_labels = []
        # Drawing main Manpower Resources rectangle
        label = gui.Label(position = threades.resize_pos((0,600)),size = threades.resize_pos((400,45)), parent = threades.desktop, text = "  "+model.text_file.mpwr_resources_text[0], style = self.labelstyle1)
        self.name_labels.append(label)
        # Creating second label style
        self.labelstyle2 = gui.defaultLabelStyle.copy()
        self.labelstyle2['border-width'] = 0
        self.labelstyle2['wordwrap'] = True
        self.labelstyle2['autosize'] = False
        self.labelstyle2['font'] = myfont2
        self.labelstyle2['font-color'] = self.font_color
        self.labelstyle2['border-color'] = self.color_grey

        self.labelstyle3 = gui.defaultLabelStyle.copy()
        self.labelstyle3['border-width'] = 0
        self.labelstyle3['wordwrap'] = False
        self.labelstyle3['autosize'] = True
        self.labelstyle3['font'] = myfont3
        self.labelstyle3['font-color'] = self.font_color
        self.labelstyle3['border-color'] = self.color_grey

        # Drawing Manpower model.resources list
        list_names = model.text_file.mpwr_list_names
        list_values = (model.ppl.get_total_population(),model.ppl.get_no_of_ppl_sheltered(),model.ppl.get_no_of_ppl_educated(),model.ppl.get_no_of_ppl_healthy(),model.ppl.get_no_of_ppl_fed(),model.ppl.get_total_no_of_ppl_emp())
        
        self.value_labels = []
        for i in range(6):
            label = gui.Label(position = threades.resize_pos((0,645+35*i)),size = threades.resize_pos((350,35)), parent = threades.desktop, text = list_names[i], style = self.labelstyle2)
            self.name_labels.append(label)
            label = gui.Label(position = threades.resize_pos((355,649+35*i)), parent = threades.desktop, text = str(int(list_values[i])), style = self.labelstyle3)
            self.value_labels.append(label)

    def update_name(self):
        
        self.name_labels[0].text = model.text_file.mpwr_resources_text[0]
        for i in range(1,7):
            self.name_labels[i].text = model.text_file.mpwr_list_names[i-1]
            
    def update_value(self):
        ''' Updates the Manpower panel
        '''
        list_values = (model.ppl.get_total_population(),model.ppl.get_no_of_ppl_sheltered(),model.ppl.get_no_of_ppl_educated(),model.ppl.get_no_of_ppl_healthy(),model.ppl.get_no_of_ppl_fed(),model.ppl.get_total_no_of_ppl_emp())
        for i in range(6):

            if not (self.value_labels[i].text == str(int(list_values[i]))):
                self.update_flag = True
        
        if self.update_flag or threades.panel_update_flag or threades.total_update_flag:

            pygame.draw.line(threades.screen,self.color_grey,threades.resize_pos((900,645)),threades.resize_pos((900,855)),1)
            pygame.draw.rect(threades.screen,self.color_grey,threades.resize_rect((0,855,300,45)),2)        
            pygame.draw.rect(threades.screen,self.color_grey,threades.resize_rect((300,855,300,45)),2)        
            pygame.draw.rect(threades.screen,self.color_grey,threades.resize_rect((600,855,300,45)),2)        
    
            for i in range(6):
    
                if not (self.value_labels[i].text == str(int(list_values[i]))):
                    self.value_labels[i].text = str(int(list_values[i]))
        
        self.update_flag = False
        
    
class facilities_panel:

    #global threades.desktop
    font_bg_color = (255,255,255)       # This should be same as  the background colour for the label
    font_color = (255,214,150)    # This should be same as that for the font to be written on the label
    color_grey = (160,160,160)
    def __init__(self):
        ''' Draws the Facilities panel
        '''
        self.update_flag = True
        myfont1 = pygame.font.Font("font.ttf", threades.resize_pt(20))   # For model.resources name and their value
        self.name_labels = []
        self.labelstyle1 = gui.defaultLabelStyle.copy()
        self.labelstyle1['border-width'] = 0
        self.labelstyle1['wordwrap'] = False
        self.labelstyle1['autosize'] = False
        self.labelstyle1['font'] = myfont1
        self.labelstyle1['font-color'] = self.font_color
        #self.labelstyle1['bg-color'] = self.font_bg_color
        
        self.list_titles = model.text_file.facilities_list
        self.list_names = [model.text_file.num_text+': ']
        self.list_values1 = (model.House.get_number(),model.School.get_number(),model.Hospital.get_number(),model.Workshop.get_number(),model.Farm.get_number(),model.Fountain.get_number())
        self.list_values2 = (model.House.get_level(),model.School.get_level(),model.Hospital.get_level(),model.Workshop.get_level(),model.Farm.get_level(),model.Fountain.get_level())
        self.value_labels = []
        for i in range(6):
            label = gui.Label(position = threades.resize_pos((950,50+55*i)),size = threades.resize_pos((300,30)), parent = threades.desktop, text = self.list_titles[i], style = self.labelstyle1)
            self.name_labels.append(label)
            label = gui.Label(position = threades.resize_pos((950,75+55*i)),size = threades.resize_pos((300,30)), parent = threades.desktop, text = self.list_names[0]+str(int(self.list_values1[i]))+model.text_file.level_text+':'+str(int(self.list_values2[i])), style = self.labelstyle1)
            self.name_labels.append(label)
            label.surf.set_alpha(200)
            self.value_labels.append(label)

            
    def update_name(self):
        
        self.name_labels[0].text = model.text_file.mpwr_resources_text[0]
        for i in range(1,7):
            self.name_labels[i].text = model.text_file.mpwr_list_names[i-1]
            
    def update_value(self):
        ''' Updates the Facilities panel
        '''
        for i in range(6):

            if not (self.value_labels[i].text == self.list_names[0]+str(int(self.list_values1[i]))+' '+model.text_file.level_text+': '+str(int(self.list_values2[i]))):
                self.update_flag = False
        
        if self.update_flag or threades.facilities_update_flag or threades.total_update_flag:
            
            self.list_values1 = (model.House.get_original_number(),model.School.get_original_number(),model.Hospital.get_original_number(),model.Workshop.get_original_number(),model.Farm.get_original_number(),model.Fountain.get_original_number())
            self.list_values2 = (model.House.get_level(),model.School.get_level(),model.Hospital.get_level(),model.Workshop.get_level(),model.Farm.get_level(),model.Fountain.get_level())
            pygame.draw.rect(threades.screen,(0,0,0),threades.resize_rect((930,40,270,350))) 
            for i in range(6):
    
                if not (self.value_labels[i].text == self.list_names[0]+str(int(self.list_values1[i]))+' '+model.text_file.level_text+': '+str(int(self.list_values2[i]))):
                    self.value_labels[i].text = self.list_names[0]+str(int(self.list_values1[i]))+' '+model.text_file.level_text+': '+str(int(self.list_values2[i]))
        
        self.update_flag = False
        


class mini_map:

    def __init__(self):
        
        self.update_flag = True
        for i in range(6):
            load_images.Map_images[i] = pygame.transform.scale(load_images.Map_images[i],threades.resize_pos((15,15)))
        self.map = pygame.image.load(os.path.join('data', 'map.png')).convert()
        self.map = pygame.transform.scale(self.map,threades.resize_pos((270,210)))
        self.list_num_fac = []
        for i in range(len(model.facilities_list)):
            self.list_num_fac.append(model.facilities_list[i].get_original_number())
    
    def update(self):
        
        for i in range(len(model.facilities_list)):
            if not (self.list_num_fac[i] == model.facilities_list[i].get_original_number()):
                self.update_flag = True
    
        if self.update_flag or threades.map_update_flag or threades.total_update_flag:
            threades.screen.blit(self.map,threades.resize_pos((930,390)))
            posn = threades.resize_pos((930+int(3200/23.22),390+int(2600/24.80)))
            threades.screen.blit(load_images.Map_images[6],posn)
            for i in range(len(model.facilities_list)):
                for j in range(model.facilities_list[i].get_original_number()):
                    posn = threades.resize_pos((930+int(model.facilities_list_sprites[model.facilities_list[i].get_name()][j].position[0]/23.22),390+int(model.facilities_list_sprites[model.facilities_list[i].get_name()][j].position[1]/24.80)))
                    threades.screen.blit(load_images.Map_images[i],posn)
        rect_draw = threades.transform_obj.village_boundary_covered()
        rect_final = threades.resize_rect((930+rect_draw[0]/23.22, 390 + rect_draw[1]/24.80, (rect_draw[2]-rect_draw[0])/23.22, (rect_draw[3]-rect_draw[1])/24.80))
        pygame.draw.rect(threades.screen, (47, 47, 255, 180), rect_final, 2)
        self.update_flag = False
    



class display_panel:

    def __init__(self):
        self.ind = indicator_panel()
        self.res = resources_panel()
        self.man = manpower_panel()
        self.fac = facilities_panel()
        self.map = mini_map()
    
    
    

    def update(self):
        self.ind.update_value()
        self.res.update_value()
        self.map.update()
        self.man.update_value()
        self.fac.update_value()

    def change_labels(self):
        self.ind.update_name()
        self.res.update_name()
        self.man.update_name()
        self.man.update_name()