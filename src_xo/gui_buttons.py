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

from sys import exit
import os
from time import *
from threades import *
import threades
import threading

import gui
from gui import *
from game_sharing import *


class marketBarChart:
    '''Class which displays the bar chart in the market window
    '''
    color1 = (255,214,150)
    color2 = (170,142,100)
    #color3 = (85,71,50)
    color_rect = (50,100,150)
    
    def drawValueChart(self,surface,initial_value = 10,maximum_value = 1000.0):
        ''' Draws a barchart on the screen
        '''
        
        self.price_flag = False
        self.surf = surface
        self.bar1Val = initial_value
        self.bar2Val = 0
        self.bar1ValMax = maximum_value
        pygame.draw.rect(surface,self.color1,resize_rect((440,200,200*self.bar1Val/self.bar1ValMax,30)))
        
        pygame.draw.rect(surface,self.color_rect,resize_rect((440,200,200,30)),2)
        
    def drawPriceChart(self,surface,initial_price = 10, maximum_value = 50):
        ''' Draws a barchart on the screen
        '''
        if self.price_flag == False:
            self.price_flag = True
            self.bar2Val = initial_price
            self.bar2ValMax = maximum_value
            pygame.draw.rect(surface,self.color2,resize_rect((440,280,200*self.bar2Val/self.bar2ValMax,30)))
        
            pygame.draw.rect(surface,self.color_rect,resize_rect((440,280,200,30)),2)
        
      
    def updateChart(self,(x,y)):
        ''' Updates the bar chart on the basis of the mouse click
        '''
        surface = self.surf
        if (x>resize_pt_x(640)) and (x<resize_pt_x(840)) and (y>resize_pt_y(250)) and (y<resize_pt_y(280)):
            pygame.draw.rect(surface,(0,0,0),resize_rect((440,200,200,50)))
            
            self.bar1Val = (x-resize_pt_x(640))*self.bar1ValMax/resize_pt_x(200)
            
            if self.bar1Val > self.bar1ValMax:
                self.bar1Val = self.bar1ValMax
            if self.bar1Val < 0:
                self.bar1Val = 0
            
            pygame.draw.rect(surface,self.color1,resize_rect((440,200,200*self.bar1Val/self.bar1ValMax,30)))
        
            pygame.draw.rect(surface,self.color_rect,resize_rect((440,200,200,30)),2)
            gui_obj.buysell_obj.updateMarketLabelValues()
        
        if self.price_flag:
            if (x>resize_pt_x(640)) and (x<resize_pt_x(840)) and (y>resize_pt_y(330)) and (y<resize_pt_y(360)):
                pygame.draw.rect(surface,(0,0,0),resize_rect((440,280,200,30)))
                
                self.bar2Val = (x-resize_pt_x(640))*self.bar2ValMax/resize_pt_x(200)
                
                if self.bar2Val > self.bar2ValMax:
                    self.bar2Val = self.bar2ValMax
                if self.bar2Val < 0:
                    self.bar2Val = 0
                
                pygame.draw.rect(surface,self.color2,resize_rect((440,280,200*self.bar2Val/self.bar2ValMax,30)))
        
                pygame.draw.rect(surface,self.color_rect,resize_rect((440,280,200,30)),2)
                gui_obj.buysell_obj.updateMarketLabelValues()
        
        #gui_obj.buysell_obj.drawPriceChart()
        
    def deletePriceChart(self):
        
        if self.price_flag:
            pygame.draw.rect(self.surf,(0,0,0),resize_rect((438,278,234,34)))
            self.price_flag = False
            #gui_obj.buysell_obj.label_res_price_flag = False
            gui_obj.buysell_obj.label_res_price.text = ''
            gui_obj.buysell_obj.label_price.text = ''
            self.bar2Val = 10
                
      
    
class barChart:
    
    ''' Class which displays the bar chart and handles it
    '''
    color1 = (255,214,150)
    color2 = (170,142,100)
    color3 = (85,71,50)
    color_rect = (50,100,150)
    
    def drawChart(self,surface,rice,vegetables,beans):
        ''' Draws a barchart on the screen
        '''
        
        self.surf = surface
        self.bar1Val = rice
        self.bar2Val = vegetables
        self.bar3Val = beans
        
        
        pygame.draw.rect(surface,self.color1,resize_rect((100,50.0+200*(100-self.bar1Val)/100,50,200*self.bar1Val/100.0)))
        pygame.draw.rect(surface,self.color2,resize_rect((250,50.0+200*(100-self.bar2Val)/100,50,200*self.bar2Val/100.0)))
        pygame.draw.rect(surface,self.color3,resize_rect((400,50.0+200*(100-self.bar3Val)/100,50,200*self.bar3Val/100.0)))
        
        pygame.draw.rect(surface,self.color_rect,resize_rect((100,50,50,200)),2)
        pygame.draw.rect(surface,self.color_rect,resize_rect((250,50,50,200)),2)
        pygame.draw.rect(surface,self.color_rect,resize_rect((400,50,50,200)),2)
        
    def updateChart(self,(x,y)):
        ''' Updates the bar chart on the basis of the mouse click
        '''
        surface = self.surf
        if (x>resize_pt_x(400)) and (x<resize_pt_x(450)) and (y>resize_pt_y(200)) and (y<resize_pt_y(400)):
            pygame.draw.rect(surface,(0,0,0),resize_rect((100,50,350,200)))
            change = self.bar1Val - (resize_pt_y(400)-y)*100/resize_pt_y(200.0)
            self.bar1Val = self.bar1Val - change
            self.bar2Val = self.bar2Val +change/2
            self.bar3Val = self.bar3Val +change/2
            
            if self.bar1Val > 100:
                self.bar1Val = 100
            if self.bar1Val < 0:
                self.bar1Val = 0
            if self.bar2Val > 100:
                self.bar2Val = 100
            if self.bar2Val < 0:
                self.bar2Val = 0
            if self.bar3Val > 100:
                self.bar3Val = 100
            if self.bar3Val < 0:
                self.bar3Val = 0
            
            pygame.draw.rect(surface,self.color1,resize_rect((100,50.0+200*(100-self.bar1Val)/100,50,200*self.bar1Val/100.0)))
            pygame.draw.rect(surface,self.color2,resize_rect((250,50.0+200*(100-self.bar2Val)/100,50,200*self.bar2Val/100.0)))
            pygame.draw.rect(surface,self.color3,resize_rect((400,50.0+200*(100-self.bar3Val)/100,50,200*self.bar3Val/100.0)))

            pygame.draw.rect(surface,self.color_rect,resize_rect((100,50,50,200)),2)
            pygame.draw.rect(surface,self.color_rect,resize_rect((250,50,50,200)),2)
            pygame.draw.rect(surface,self.color_rect,resize_rect((400,50,50,200)),2)
            
            
            
        if (x>resize_pt_x(550)) and (x<resize_pt_x(600)) and (y>resize_pt_y(200)) and (y<resize_pt_y(400)):
            pygame.draw.rect(surface,(0,0,0),resize_rect((100,50,350,200)))
            change = self.bar2Val - (resize_pt_y(400)-y)*100/resize_pt_y(200.0)
            self.bar2Val = self.bar2Val - change
            self.bar1Val = self.bar1Val + change/2
            self.bar3Val = self.bar3Val + change/2
            
            if self.bar1Val > 100:
                self.bar1Val = 100
            if self.bar1Val < 0:
                self.bar1Val = 0
            if self.bar2Val > 100:
                self.bar2Val = 100
            if self.bar2Val < 0:
                self.bar2Val = 0
            if self.bar3Val > 100:
                self.bar3Val = 100
            if self.bar3Val < 0:
                self.bar3Val = 0
            
            pygame.draw.rect(surface,self.color1,resize_rect((100,50.0+200*(100-self.bar1Val)/100,50,200*self.bar1Val/100.0)))
            pygame.draw.rect(surface,self.color2,resize_rect((250,50.0+200*(100-self.bar2Val)/100,50,200*self.bar2Val/100.0)))
            pygame.draw.rect(surface,self.color3,resize_rect((400,50.0+200*(100-self.bar3Val)/100,50,200*self.bar3Val/100.0)))

            pygame.draw.rect(surface,self.color_rect,resize_rect((100,50,50,200)),2)
            pygame.draw.rect(surface,self.color_rect,resize_rect((250,50,50,200)),2)
            pygame.draw.rect(surface,self.color_rect,resize_rect((400,50,50,200)),2)
            
            
            
        if (x>resize_pt_x(700)) and (x<resize_pt_x(750)) and (y>resize_pt_y(200)) and (y<resize_pt_y(400)):
            pygame.draw.rect(surface,(0,0,0),resize_rect((100,50,350,200)))
            change = self.bar3Val - (resize_pt_y(400)-y)*100/resize_pt_y(200.0)
            self.bar3Val = self.bar3Val - change
            self.bar2Val = self.bar2Val + change/2
            self.bar1Val = self.bar1Val + change/2
            
            if self.bar1Val > 100:
                self.bar1Val = 100
            if self.bar1Val < 0:
                self.bar1Val = 0
            if self.bar2Val > 100:
                self.bar2Val = 100
            if self.bar2Val < 0:
                self.bar2Val = 0
            if self.bar3Val > 100:
                self.bar3Val = 100
            if self.bar3Val < 0:
                self.bar3Val = 0
            
            pygame.draw.rect(surface,self.color1,resize_rect((100,50.0+200*(100-self.bar1Val)/100,50,200*self.bar1Val/100.0)))
            pygame.draw.rect(surface,self.color2,resize_rect((250,50.0+200*(100-self.bar2Val)/100,50,200*self.bar2Val/100.0)))
            pygame.draw.rect(surface,self.color3,resize_rect((400,50.0+200*(100-self.bar3Val)/100,50,200*self.bar3Val/100.0)))
            
            pygame.draw.rect(surface,self.color_rect,resize_rect((100,50,50,200)),2)
            pygame.draw.rect(surface,self.color_rect,resize_rect((250,50,50,200)),2)
            pygame.draw.rect(surface,self.color_rect,resize_rect((400,50,50,200)),2)
            
            
       
        


class setup_button:

    ''' Class which handles the windows when the setup button is clicked
    '''
    rect_color = (255,214,150)
    color_grey = (160,160,160)
    
    def __init__(self):
        
        self.win_flag = False
        self.child_win_flag = False
        
    
    def setup(self,button=None):
        ''' Initiated when the button for setting up a facility is clicked
        '''
        
        
        gui_obj.disable_buttons()
        myfont = pygame.font.Font("font.ttf", resize_pt(20))

        # Custom Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont
        win_style['font-color'] = self.rect_color
        win_style['bg-color'] = (0,0,0)

        # Calculating position and size of window from the size of the desktop        
        position_win =resize_pos((200.0,50.0))
        size_win =resize_pos((800.0,600.0))

        # Creating window
        self.win = Window(position = position_win, size = size_win, parent = desktop, text = "Set up a facility for your village " ,style = win_style,shadeable = False)
        #self.win.surf.blit(School_tiles_list[3][2],(0,0))
        self.win.surf.set_alpha(140) 
        self.win.onClose = lambda button: self.close_win_safe()
        self.win_flag = True
        
        # Pausing the update thread
        pause_update_thread()
        
        #  Creating Custom label style
        myfont2 = pygame.font.Font("font.ttf", resize_pt(16))
        myfont3 = pygame.font.Font("font.ttf", resize_pt(14))
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 1
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont2
        labelStyleCopy['font-color'] = self.rect_color
        labelStyleCopy['border-color'] = self.color_grey
        default_text = 'What would you like to set up? Choose a facility from the list and press the Set Up button.'
        self.message_label = Label(position = resize_pos((450,120),(800.0,600.0),self.win.size),size = resize_pos((250,100),(800.0,600.0),self.win.size), parent = self.win, text = default_text, style = labelStyleCopy)
        text ='Please select a Facility to see its status and Requirements' 
        labelStyleCopy2 = gui.defaultLabelStyle.copy()
        labelStyleCopy2['border-width'] = 1
        labelStyleCopy2['wordwrap'] = True
        labelStyleCopy2['autosize'] = False
        labelStyleCopy2['font'] = myfont3
        labelStyleCopy2['font-color'] = self.rect_color
        labelStyleCopy2['border-color'] = self.color_grey

        self.message_label2 = Label(position = resize_pos((20,400),(800.0,600.0),self.win.size),size = resize_pos((570,120),(800.0,600.0),self.win.size), parent = self.win, text = text, style = labelStyleCopy2)

        # creating custom style for option box
        op_style = gui.defaultOptionBoxStyle.copy()
        op_style['font'] = myfont
        op_style['font-color'] = self.rect_color
        op_style['autosize'] = True
        op_style['word wrap'] = False
        # Creating option boxes for all the facilities
        position_optionbox = resize_pos((200.0,150.0),(800.0,600.0),size_win)        
        self.housing_box = OptionBox(position = position_optionbox, parent = self.win, style = op_style, text = 'House')
        self.housing_box.onClick =  self.on_select_setup_option_box
        self.hospital_box = OptionBox(position = self.win.nextPosition(resize_pt_y(10)), parent = self.win, style = op_style, text = 'Hospital')
        self.hospital_box.onClick = self.on_select_setup_option_box
        self.workshop_box = OptionBox(position = self.win.nextPosition(resize_pt_y(10)), parent = self.win, style = op_style, text = 'Workshop')
        self.workshop_box.onClick = self.on_select_setup_option_box
        self.school_box = OptionBox(position = self.win.nextPosition(resize_pt_y(10)), parent = self.win, style = op_style, text = 'School')
        self.school_box.onClick = self.on_select_setup_option_box
        self.farm_box = OptionBox(position = self.win.nextPosition(resize_pt_y(10)), parent = self.win, style = op_style, text = 'Farm')
        self.farm_box.onClick = self.on_select_setup_option_box
        self.fountain_box = OptionBox(position = self.win.nextPosition(resize_pt_y(10)), parent = self.win, style = op_style, text = 'Well')
        self.fountain_box.onClick = self.on_select_setup_option_box

        self.win.surf.set_alpha(255)
        background = self.win.surf.subsurface(pygame.Rect(resize_rect((400,180,200,200))))
        self.background_pic = background.copy()
        self.win.surf.set_alpha(140)

        # Creating buttons for Setting up the facility and closing the setup window
        button_style = gui.defaultButtonStyle.copy()
        button_style['font'] = myfont2

        self.button_setup = Button(position = resize_pos((600.0,420.0),(800.0,600.0),size_win), size = resize_pos((120.0,50.0),(800.0,600.0),size_win), parent = self.win, text = "Set Up",style = button_style)
        #self.button_close = Button(position = resize_pos((600.0,460.0),(800.0,600.0),size_win), size = resize_pos((120.0,50.0),(800.0,600.0),size_win), parent = self.win, text = "Close",style = button_style)
        #self.button_close.onClick  = self.close_win
        self.button_setup.onClick = self.setup_facility

    def on_select_setup_option_box(self,button):

        self.win.surf.set_alpha(255)
        self.win.surf.blit(self.background_pic,resize_pos((450,250)))
        self.win.surf.set_alpha(140)

        if button.text == 'House':
            text = 'House: '
            image = House_tiles_list[2][2]
            text += get_setup_text(House)
        if button.text == 'Hospital':
            text = 'Hospital: '
            image = Hospital_tiles_list[2][2]
            text += get_setup_text(Hospital)
        if button.text == 'School':
            text = 'School: '
            image = School_tiles_list[2][2]
            text += get_setup_text(School)
        if button.text == 'Workshop':
            text = 'Workshop: '
            image = Workshop_tiles_list[2][2]
            text += get_setup_text(Workshop)
        if button.text == 'Farm':
            text = 'Farm: '
            image = Farm_tiles[0][1]
            text += get_setup_text(Farm)
        if button.text == 'Well':
            text = 'Well: '
            image = Fountain_tiles[0][3]
            text += get_setup_text(Fountain)
        display_image = pygame.transform.scale(image,resize_pos((140,140)))
        self.win.surf.blit(display_image,resize_pos((450,250)))
        self.message_label2.text = text



    def close_win(self,button=None):
        self.win.close()
        self.win_flag = False
        gui_obj.enable_buttons()

    def close_win_safe(self,button = None):
        self.win_flag = False
        gui_obj.enable_buttons()


    def setup_facility(self,button=None):
        ''' Sets up the facility
        '''


        if self.housing_box.value:
            label_text =  build_facility(House)
        elif self.hospital_box.value:
            label_text =  build_facility(Hospital)
        elif self.workshop_box.value:
            label_text =  build_facility(Workshop)
        elif self.fountain_box.value:
            label_text =  build_facility(Fountain)
        elif self.school_box.value:
            label_text =  build_facility(School)
        elif self.farm_box.value:
            label_text =  self.build_facility_farm()
        else:
            label_text = ' Please select a Facility for building'
        self.message_label.text = label_text
        if label_text== 'Facility has been build':
            self.close_win()

    def build_facility_farm(self):

        myfont = pygame.font.Font("font.ttf",resize_pt(22))

        # Custom Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont
        win_style['font-color'] = self.rect_color
        win_style['bg-color'] = (0,0,0)

        # Calculating position and size of window from the size of the desktop        
        position_win =resize_pos((300.0,150.0))
        size_win =resize_pos((600.0,400.0))

        # Creating window
        self.child_win = Window(position = position_win, size = size_win, parent = desktop, text = "Setup Farm " ,style = win_style,shadeable = False,moveable = False)
        #self.child_win.surf.set_alpha(190) 
        self.win.enabled = False
        self.child_win_flag = True
        self.child_win.onClose = lambda button: self.enable_parent_win()

        self.bardisplay = barChart()
        self.bardisplay.drawChart(self.child_win.surf,33,33,34)
        
        # Creating custom label style1
        myfont2 = pygame.font.Font("font.ttf",resize_pt(16))
        labelstyle1 = gui.defaultLabelStyle.copy()
        labelstyle1['border-width'] = 0
        labelstyle1['wordwrap'] = False
        labelstyle1['autosize'] = True
        labelstyle1['font'] = myfont2
        labelstyle1['font-color'] = self.rect_color

        label_rice = Label(position = resize_pos((100.0,260.0),(600.0,400.0),self.child_win.size), parent = self.child_win, text = 'Rice', style = labelstyle1)
        label_veg = Label(position = resize_pos((250.0,260.0),(600.0,400.0),self.child_win.size), parent = self.child_win, text = 'Fruit and \nVegetables', style = labelstyle1)
        label_beans = Label(position = resize_pos((400.0,260.0),(600.0,400.0),self.child_win.size), parent = self.child_win, text = 'Beans', style = labelstyle1)

        # Creating second custom label style
        labelStyleCopy2 = gui.defaultLabelStyle.copy()
        labelStyleCopy2['border-width'] = 0
        labelStyleCopy2['wordwrap'] = True
        labelStyleCopy2['autosize'] = False
        labelStyleCopy2['font'] = myfont2
        labelStyleCopy2['border-color'] = self.rect_color
        labelStyleCopy2['font-color'] = self.rect_color
        
        text = 'Balance the bar chart to select the percentages of different food items you want to grow in your farm'
        self.message_label2 = Label(position = resize_pos((20,320),(600.0,400.0),self.child_win.size),size = resize_pos((470,70),(600.0,400.0),self.child_win.size), parent = self.child_win, text = text, style = labelStyleCopy2)

        '''
        # Creating custom text box style
        textbox_style = gui.defaultTextBoxStyle.copy()
        textbox_style['font'] = myfont2
        textbox_style['font-color'] = self.rect_color
        self.textbox_rice = TextBox(position = resize_pos((300.0, 70.0),(600.0,400.0),self.child_win.size), size = resize_pos((50,20),(600.0,400.0),self.child_win.size), parent = self.child_win, style = textbox_style) 
        self.textbox_veg = TextBox(position = resize_pos((300.0, 110.0),(600.0,400.0),self.child_win.size), size = resize_pos((50,20),(600.0,400.0),self.child_win.size), parent = self.child_win, style = textbox_style) 
        self.textbox_beans = TextBox(position = resize_pos((300.0, 150.0),(600.0,400.0),self.child_win.size), size = resize_pos((50,20),(600.0,400.0),self.child_win.size), parent = self.child_win, style = textbox_style) 
        '''
        
        # Custom button style        
        button_style = gui.defaultButtonStyle.copy()
        button_style['font'] = myfont2

        self.button_setup_farm = Button(position = resize_pos((500.0,320.0),(600.0,400.0),size_win), size = resize_pos((80.0,50.0),(600.0,400.0),size_win), parent = self.child_win, text = "Set Up",style = button_style)
        self.button_setup_farm.onClick = self.setup_facility_farm

        self.return_text_farm = ' '
        return self.return_text_farm


    def setup_facility_farm(self,button=None):

        # Finally setting up the facility after the button is clicked
        quantity1 = self.bardisplay.bar1Val
        quantity2 = self.bardisplay.bar2Val
        quantity3 = self.bardisplay.bar3Val
        list_food = [quantity1,quantity2,quantity3]
        label_text = build_facility(Farm,list_food)
        self.child_win.close()
        self.enable_parent_win()
        self.close_win()
        return

    def enable_parent_win(self):
        self.child_win_flag = False
        self.win.enabled = True

    def get_win_flag(self):
        return self.win_flag

    def get_child_win_flag(self):
        return self.child_win_flag

        
class upgrade_button:

    rect_color = (255,214,150)
    color_grey = (160,160,160)
    
    def __init__(self):
        
        self.win_flag = False
        self.child_win_flag = False
        
        # Functions for upgrading a facility
    def upgrade(self,button=None):
        ''' Initiated when the button for upgrading a facility is clicked
        '''
        gui_obj.disable_buttons()
        myfont = pygame.font.Font("font.ttf", resize_pt(20))

        # Custom Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont
        win_style['font-color'] = self.rect_color
        win_style['bg-color'] = (0,0,0)

        # Calculating position and size of window from the size of the desktop        
        position_win =resize_pos((200.0,50.0))
        size_win =resize_pos((800.0,600.0))

        # Creating window
        self.win = Window(position = position_win, size = size_win, parent = desktop, text = "Upgrade Facility " ,style = win_style,shadeable = False)
        self.win.surf.set_alpha(140) 
        self.win.onClose = lambda button: self.close_win_safe()
        self.win_flag = True

        # Pausing the update thread
        pause_update_thread()
        
        #  Creating Custom label style
        myfont2 = pygame.font.Font("font.ttf", resize_pt(16))
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 1
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont2
        labelStyleCopy['font-color'] = self.rect_color
        labelStyleCopy['border-color'] = self.color_grey
        text = 'Please select a Facility and press Upgrade button to upgrade.'
        self.message_label = Label(position = resize_pos((450,150),(800.0,600.0),self.win.size),size = resize_pos((200,100),(800.0,600.0),self.win.size), parent = self.win, text = text, style = labelStyleCopy)


        # creating custom style for option box
        op_style = gui.defaultOptionBoxStyle.copy()
        op_style['font'] = myfont
        op_style['font-color'] = self.rect_color
        op_style['autosize'] = True
        op_style['word wrap'] = False
        # Creating option boxes for all the facilities
        position_optionbox = resize_pos((200.0,150.0),(800.0,600.0),size_win)        
        self.housing_box = OptionBox(position = position_optionbox, parent = self.win, style = op_style, text = 'House')
        self.housing_box.onClick =  self.on_select_upgrade_option_box
        self.hospital_box = OptionBox(position = self.win.nextPosition(resize_pt_y(10)), parent = self.win, style = op_style, text = 'Hospital')
        self.hospital_box.onClick = self.on_select_upgrade_option_box
        self.workshop_box = OptionBox(position = self.win.nextPosition(resize_pt_y(10)), parent = self.win, style = op_style, text = 'Workshop')
        self.workshop_box.onClick = self.on_select_upgrade_option_box
        self.school_box = OptionBox(position = self.win.nextPosition(resize_pt_y(10)), parent = self.win, style = op_style, text = 'School')
        self.school_box.onClick = self.on_select_upgrade_option_box
        self.farm_box = OptionBox(position = self.win.nextPosition(resize_pt_y(10)), parent = self.win, style = op_style, text = 'Farm')
        self.farm_box.onClick = self.on_select_upgrade_option_box
        self.fountain_box = OptionBox(position = self.win.nextPosition(resize_pt_y(10)), parent = self.win, style = op_style, text = 'Well')
        self.fountain_box.onClick = self.on_select_upgrade_option_box
        myfont3 = pygame.font.Font("font.ttf", resize_pt(14))
        text ='Please select a Facility to see its next upgrade' 
        labelStyleCopy2 = gui.defaultLabelStyle.copy()
        labelStyleCopy2['border-width'] = 1
        labelStyleCopy2['wordwrap'] = True
        labelStyleCopy2['autosize'] = False
        labelStyleCopy2['font'] = myfont3
        labelStyleCopy2['font-color'] = self.rect_color
        labelStyleCopy2['border-color'] = self.color_grey

        self.message_label2 = Label(position = resize_pos((20,400),(800.0,600.0),self.win.size),size = resize_pos((570,120),(800.0,600.0),self.win.size), parent = self.win, text = text, style = labelStyleCopy2)

        # Creating buttons for Setting up the facility and closing the setup window
        button_style = gui.defaultButtonStyle.copy()
        button_style['font'] = myfont2
        
        self.win.surf.set_alpha(255)
        background = self.win.surf.subsurface(pygame.Rect(resize_rect((400,180,200,200))))
        self.background_pic = background.copy()
        self.win.surf.set_alpha(140)

        self.button_upgrade = Button(position = resize_pos((600.0,420.0),(800.0,600.0),size_win), size = resize_pos((120.0,50.0),(800.0,600.0),size_win), parent = self.win, text = "Upgrade",style = button_style)
        #self.button_close = Button(position = resize_pos((600.0,460.0),(800.0,600.0),size_win), size = resize_pos((120.0,50.0),(800.0,600.0),size_win), parent = self.win, text = "Close",style = button_style)
        #self.button_close.onClick  = self.close_win
        self.button_upgrade.onClick = self.upgrade_facility

    def on_select_upgrade_option_box(self,button):
        
        self.win.surf.set_alpha(255)
        self.win.surf.blit(self.background_pic,resize_pos((450,250)))
        self.win.surf.set_alpha(140)

        text = ''
        if button.text == 'House':
            image = House_tiles_list[2][2]
            text += get_upgrade_text(House)
        if button.text == 'Hospital':
            image = Hospital_tiles_list[2][2]
            text += get_upgrade_text(Hospital)
        if button.text == 'School':
            image = School_tiles_list[2][2]
            text += get_upgrade_text(School)
        if button.text == 'Workshop':
            image = Workshop_tiles_list[2][2]
            text += get_upgrade_text(Workshop)
        if button.text == 'Farm':
            image = Farm_tiles[0][1]
            text += get_upgrade_text(Farm)
        if button.text == 'Well':
            image = Fountain_tiles[0][3]
            text += get_upgrade_text(Fountain)
        display_image = pygame.transform.scale(image,resize_pos((140,140)))
        self.win.surf.blit(display_image,resize_pos((450,250)))
        self.message_label2.text = text
        self.message_label.text = 'Upgrades ' + button.text

    def upgrade_facility(self,button=None):
        ''' Upgrades the facility
        '''


        if self.housing_box.value:
            label_text =  upgrade_facility(House)
        elif self.hospital_box.value:
            label_text =  upgrade_facility(Hospital)
        elif self.workshop_box.value:
            label_text =  upgrade_facility(Workshop)
        elif self.fountain_box.value:
            label_text =  upgrade_facility(Fountain)
        elif self.school_box.value:
            label_text =  upgrade_facility(School)
        elif self.farm_box.value:
            label_text =  upgrade_facility(Farm)
        else:
            label_text = ' Please select a Facility for Upgrading'
        self.message_label.text = label_text
        if label_text== 'Facility has been upgraded':
            self.close_win()

    # Functions for upgrading a facility end here........
    def close_win(self,button=None):
        self.win.close()
        self.win_flag = False
        gui_obj.enable_buttons()

    def close_win_safe(self,button = None):
        self.win_flag = False
        gui_obj.enable_buttons()


    def get_win_flag(self):
        return self.win_flag

   
class buysell_button:

    rect_color = (255,214,150)
    color_grey = (160,160,160)
    
    def __init__(self):
        
        self.win_flag = False
        self.child_win_flag = False
        
   
    
    # Functions for Buy/Sell operation begin here
    def buysell(self,button=None):
        ''' Initiated when the button for buy/sell operation is pressed.
        '''

        
        gui_obj.disable_buttons()
        myfont = pygame.font.Font("font.ttf", resize_pt(20))

        # Custom Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont
        win_style['font-color'] = self.rect_color
        win_style['bg-color'] = (0,0,0)

        # Focus the animation window on the market
        transform_obj.focus_at((3200,2600)) # Replace this with the coordinates ofthe market in the base surface

        # Calculating position and size of window from the size of the desktop        
        position_win =resize_pos((200.0,50.0))
        size_win =resize_pos((800.0,600.0))

        # Creating window
        self.win = Window(position = position_win, size = size_win, parent = desktop, text = " Buy or Sell Resources " ,style = win_style,shadeable = False, moveable = False)
        self.win.surf.set_alpha(140) 
        self.win.onClose = lambda button: self.close_win_safe()
        self.win_flag = True

        # Pausing the update thread
        pause_update_thread()

        # Creating custom label style1
        myfont2 = pygame.font.Font("font.ttf",resize_pt(16))
        labelstyle1 = gui.defaultLabelStyle.copy()
        labelstyle1['border-width'] = 0
        labelstyle1['wordwrap'] = False
        labelstyle1['autosize'] = True
        labelstyle1['font'] = myfont2
        labelstyle1['font-color'] = self.rect_color

        heading_label1 = Label(position = resize_pos((10.0,70.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Resources', style = labelstyle1)
        heading_label2 = Label(position = resize_pos((180.0,70.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Village', style = labelstyle1)
        heading_label3 = Label(position = resize_pos((180.0,85.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Quantity', style = labelstyle1)
        heading_label4 = Label(position = resize_pos((370.0,70.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Price', style = labelstyle1)
        #heading_label5 = Label(position = resize_pos((520.0,70.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Resources', style = labelstyle1)
        heading_label6 = Label(position = resize_pos((270.0,70.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Market', style = labelstyle1)
        heading_label7 = Label(position = resize_pos((270.0,85.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Quantity', style = labelstyle1)

        # creating custom style for option box
        op_style = gui.defaultOptionBoxStyle.copy()
        op_style['font'] = myfont2
        op_style['font-color'] = self.rect_color
        op_style['autosize'] = True
        op_style['word wrap'] = False

        # Creating option boxes for all the resources
        position_optionbox = resize_pos((10.0,140.0),(800.0,600.0),self.win.size)        
        self.water_box = OptionBox(position = position_optionbox, parent = self.win, style = op_style, text = 'Water')
        self.buildmat_box = OptionBox(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, style = op_style, text = 'Building Materials')
        self.tools_box = OptionBox(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, style = op_style, text = 'Tools')
        self.books_box = OptionBox(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, style = op_style, text = 'Books')
        self.medicine_box = OptionBox(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, style = op_style, text = 'Medicines')
        self.rice_box = OptionBox(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, style = op_style, text = 'Rice')
        self.wheat_box = OptionBox(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, style = op_style, text = 'Fruit & Vegatables')
        self.beans_box = OptionBox(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, style = op_style, text = 'Beans')
        self.sugar_box = OptionBox(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, style = op_style, text = 'Sugar')
        self.salt_box = OptionBox(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, style = op_style, text = 'Salt')
        self.oil_box = OptionBox(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, style = op_style, text = 'Oil')
        
        #Creating CheckBox style
        ch_style = gui.defaultCheckBoxStyle.copy()
        ch_style['font'] = myfont2
        ch_style['font-color'] = self.rect_color
        ch_style['autosize'] = True
        #ch_style['word wrap'] = False
        
        self.barObject = marketBarChart()
        self.barObject.drawValueChart(self.win.surf)
        
        if test_sharing():
            
            #Creating Checkbox for share trade with peer villages
            self.shareCheckBox = CheckBox(position = resize_pos((440, 140), (800, 600), self.win.size),  parent = self.win,  style = ch_style,  text = 'Trade with Peer Villages' )
            self.shareCheckBox.value = False        
            self.shareCheckBox.onValueChanged = self.drawPriceChart()
        


        # Creating labels for village values of Resources 
        self.label_vwater = Label(position = resize_pos((190.0,140.0),(800.0,600.0),self.win.size), parent = self.win, text = str(int(Water.get_vquantity())), style = labelstyle1)
        self.label_vbuildmat = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Buildmat.get_vquantity())), style = labelstyle1)
        self.label_vtools = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Tools.get_vquantity())), style = labelstyle1)
        self.label_vbooks = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Book.get_vquantity())), style = labelstyle1)
        self.label_vmedicine = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Medicine.get_vquantity())), style = labelstyle1)
        self.label_vrice = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Rice.get_vquantity())), style = labelstyle1)
        self.label_vwheat = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Wheat.get_vquantity())), style = labelstyle1)
        self.label_vbeans = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Beans.get_vquantity())), style = labelstyle1)
        self.label_vsugar = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Sugar.get_vquantity())), style = labelstyle1)
        self.label_vsalt = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Salt.get_vquantity())), style = labelstyle1)
        self.label_voil = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Oil.get_vquantity())), style = labelstyle1)

        #Creating labels for value and price of resources
        self.label_res_price_flag = False
        self.label_res_value = Label(position = resize_pos((650.0,200.0),(800.0,600.0),self.win.size), parent = self.win, text = str(int(self.barObject.bar1Val)), style = labelstyle1)
        
        #Creating a label for value to be printed
        self.label_quantity = Label(position = resize_pos((440.0,170.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Quantity ', style = labelstyle1)
                    
        if test_sharing():
            if self.shareCheckBox.value:
                self.label_price = Label(position = resize_pos((400.0,250.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Price ', style = labelstyle1)
                self.label_res_price = Label(position = resize_pos((650.0,280.0),(800.0,600.0),self.win.size), parent = self.win, text = str(int(self.barObject.bar2Val)), style = labelstyle1)
        
        # Creating labels for prices of Resources 
        self.price_vwater = Label(position = resize_pos((370.0,140.0),(800.0,600.0),self.win.size), parent = self.win, text = str(int(Water.get_price())), style = labelstyle1)
        self.price_vbuildmat = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Buildmat.get_price())), style = labelstyle1)
        self.price_vtools = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Tools.get_price())), style = labelstyle1)
        self.price_vbooks = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Book.get_price())), style = labelstyle1)
        self.price_vmedicine = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Medicine.get_price())), style = labelstyle1)
        self.price_vrice = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Rice.get_price())), style = labelstyle1)
        self.price_vwheat = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Wheat.get_price())), style = labelstyle1)
        self.price_vbeans = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Beans.get_price())), style = labelstyle1)
        self.price_vsugar = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Sugar.get_price())), style = labelstyle1)
        self.price_vsalt = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Salt.get_price())), style = labelstyle1)
        self.price_voil = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Oil.get_price())), style = labelstyle1)

        '''
        # Creating a textbox to enter the quantity to buy or sell
        textbox_style = gui.defaultTextBoxStyle.copy()
        textbox_style['font'] = myfont2
        textbox_style['font-color'] = self.rect_color
        self.label_quantity = Label(position = resize_pos((360.0,150.0),(800.0,600.0),self.win.size), parent = self.win, text = ' Quantity ', style = labelstyle1)
        self.win.textbox = TextBox(position = resize_pos((350.0, 200.0),(800.0,600.0),self.win.size), size = resize_pos((100,20),(800.0,600.0),self.win.size), parent = self.win, style = textbox_style) 
        '''

        # Creating buttons for buying and selling and closing the window
        button_style = gui.defaultButtonStyle.copy()
        button_style['font'] = myfont2

        self.button_buy = Button(position = resize_pos((560.0,350.0),(800.0,600.0),size_win), size = resize_pos((70.0,50.0),(800.0,600.0),size_win), parent = self.win, text = " Buy ",style = button_style)
        self.button_sell = Button(position = resize_pos((460.0,350.0),(800.0,600.0),size_win), size = resize_pos((70.0,50.0),(800.0,600.0),size_win), parent = self.win, text = " Sell ",style = button_style)
        self.button_close = Button(position = resize_pos((650.0,500.0),(800.0,600.0),size_win), size = resize_pos((120.0,50.0),(800.0,600.0),size_win), parent = self.win, text = "Close",style = button_style)
        self.button_buy.onClick = self.buy_resources
        self.button_sell.onClick = self.sell_resources
        self.button_close.onClick  = self.close_win
        
        # Creating labels for market values of Resources 
        self.label_mwater = Label(position = resize_pos((270.0,140.0),(800.0,600.0),self.win.size), parent = self.win, text = str(int(Water.get_mquantity())), style = labelstyle1)
        self.label_mbuildmat = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Buildmat.get_mquantity())), style = labelstyle1)
        self.label_mtools = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Tools.get_mquantity())), style = labelstyle1)
        self.label_mbooks = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Book.get_mquantity())), style = labelstyle1)
        self.label_mmedicine = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Medicine.get_mquantity())), style = labelstyle1)
        self.label_mrice = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Rice.get_mquantity())), style = labelstyle1)
        self.label_mwheat = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Wheat.get_mquantity())), style = labelstyle1)
        self.label_mbeans = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Beans.get_mquantity())), style = labelstyle1)
        self.label_msugar = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Sugar.get_mquantity())), style = labelstyle1)
        self.label_msalt = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Salt.get_mquantity())), style = labelstyle1)
        self.label_moil = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, text = str(int(Oil.get_mquantity())), style = labelstyle1)



        # Creating label to display the status messages
        #  Creating Custom label style
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 1
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont2
        labelStyleCopy['font-color'] = self.rect_color
        labelStyleCopy['border-color'] = self.color_grey
        text = 'Welcome to the market of SHEYLAN, where you can trade resources. Select which item you would like to buy or sell on the left-hand column, enter the amount, and then choose buy or sell'
        self.message_label = Label(position = resize_pos((80,470),(800.0,600.0),self.win.size),size = resize_pos((500,100),(800.0,600.0),self.win.size), parent = self.win, text = text, style = labelStyleCopy)

    def updateMarketLabelValues(self,button = None):
        self.label_res_value.text = str(int(self.barObject.bar1Val))
        if test_sharing():
            if self.shareCheckBox.value:
                self.label_res_price.text = str(int(self.barObject.bar2Val))
                
    def drawPriceChart(self,button = None):
        
        # Creating custom label style1
        
        if test_sharing():
            if self.shareCheckBox.value:
                myfont2 = pygame.font.Font("font.ttf",resize_pt(16))
                labelstyle1 = gui.defaultLabelStyle.copy()
                labelstyle1['border-width'] = 0
                labelstyle1['wordwrap'] = False
                labelstyle1['autosize'] = True
                labelstyle1['font'] = myfont2
                labelstyle1['font-color'] = self.rect_color
                #print self.shareCheckBox.value
    
            
                self.barObject.drawPriceChart(self.win.surf)
                if not self.label_res_price_flag:            
                    self.label_price = Label(position = resize_pos((440.0,250.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Price ', style = labelstyle1)
                    self.label_res_price = Label(position = resize_pos((650.0,280.0),(800.0,600.0),self.win.size), parent = self.win, text = str(int(self.barObject.bar2Val)), style = labelstyle1)
                    self.label_res_price_flag = True
            
            else:
                self.barObject.deletePriceChart()
            
            
    def buy_resources(self,button):
        ''' Initiated for doing the transaction of buying the resources 
        '''
        # Checking whether the user has entered the value in text box properly
        quantity = self.barObject.bar1Val  
        price = self.barObject.bar2Val

        # Checking whether the user has selected the appropriate option box for the resource or not, and do the appropriate action
        if self.water_box.value:
            if not self.shareCheckBox.value:
                label_text =  buy_res(Water,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_vwater.text = str(int(Water.get_vquantity()))
                    self.label_mwater.text = str(int(Water.get_mquantity()))
            else:
                initiateTrade(True,Water,quantity,price)
        elif self.buildmat_box.value:
            if not self.shareCheckBox.value:
                label_text =  buy_res(Buildmat,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_vbuildmat.text = str(int(Buildmat.get_vquantity()))
                    self.label_mbuildmat.text = str(int(Buildmat.get_mquantity()))
            else:
                initiateTrade(True,Buildmat,quantity,price)
        elif self.tools_box.value:
            if not self.shareCheckBox.value:
                label_text =  buy_res(Tools,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_vtools.text = str(int(Tools.get_vquantity()))
                    self.label_mtools.text = str(int(Tools.get_mquantity()))
            else:
                initiateTrade(True,Tools,quantity,price)
        elif self.medicine_box.value:
            if not self.shareCheckBox.value:
                label_text =  buy_res(Medicine,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_vmedicine.text = str(int(Medicine.get_vquantity()))
                    self.label_mmedicine.text = str(int(Medicine.get_mquantity()))
            else:
                initiateTrade(True,Medicine,quantity,price)
        elif self.books_box.value:
            if not self.shareCheckBox.value:
                label_text =  buy_res(Book,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_vbooks.text = str(int(Book.get_vquantity()))
                    self.label_mbooks.text = str(int(Book.get_mquantity()))
            else:
                initiateTrade(True,Book,quantity,price)
        elif self.rice_box.value:
            if not self.shareCheckBox.value:
                label_text =  buy_res(Rice,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_vrice.text = str(int(Rice.get_vquantity()))
                    self.label_mrice.text = str(int(Rice.get_mquantity()))
            else:
                initiateTrade(True,Rice,quantity,price)
        elif self.wheat_box.value:
            if not self.shareCheckBox.value:
                label_text =  buy_res(Wheat,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_vwheat.text = str(int(Wheat.get_vquantity()))
                    self.label_mwheat.text = str(int(Wheat.get_mquantity()))
            else:
                initiateTrade(True,Wheat,quantity,price)
        elif self.beans_box.value:
            if not self.shareCheckBox.value:
                label_text =  buy_res(Beans,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_vbeans.text = str(int(Beans.get_vquantity()))
                    self.label_mbeans.text = str(int(Beans.get_mquantity()))
            else:
                initiateTrade(True,Beans,quantity,price)
        elif self.sugar_box.value:
            if not self.shareCheckBox.value:
                label_text =  buy_res(Sugar,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_vsugar.text = str(int(Sugar.get_vquantity()))
                    self.label_msugar.text = str(int(Sugar.get_mquantity()))
            else:
                initiateTrade(True,Sugar,quantity,price)
        elif self.salt_box.value:
            if not self.shareCheckBox.value:
                label_text =  buy_res(Salt,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_vsalt.text = str(int(Salt.get_vquantity()))
                    self.label_msalt.text = str(int(Salt.get_mquantity()))
            else:
                initiateTrade(True,Salt,quantity,price)
        elif self.oil_box.value:
            if not self.shareCheckBox.value:
                label_text =  buy_res(Oil,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_voil.text = str(int(Oil.get_vquantity()))
                    self.label_moil.text = str(int(Oil.get_mquantity()))
            else:
                initiateTrade(True,Oil,quantity,price)
        else:
            label_text = ' Please select a Resource for Trading'

        self.message_label.text = label_text
        



    def sell_resources(self,button):
        ''' Initiated for doing the transaction of buying the resources 
        '''
        # Checking whether the user has entered the value in text box properly
        quantity = self.barObject.bar1Val

        # Checking whether the user has selected the appropriate option box for the resource or not, and do the appropriate action
        if self.water_box.value:
            if not self.shareCheckBox.value:
                label_text =  sell_res(Water,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_vwater.text = str(int(Water.get_vquantity()))
                    self.label_mwater.text = str(int(Water.get_mquantity()))
            else:
                initiateTrade(False,Water,quantity,price)
        elif self.buildmat_box.value:
            if not self.shareCheckBox.value:
                label_text =  sell_res(Buildmat,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_vbuildmat.text = str(int(Buildmat.get_vquantity()))
                    self.label_mbuildmat.text = str(int(Buildmat.get_mquantity()))
            else:
                initiateTrade(False,Buildmat,quantity,price)
        elif self.tools_box.value:
            if not self.shareCheckBox.value:
                label_text =  sell_res(Tools,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_vtools.text = str(int(Tools.get_vquantity()))
                    self.label_mtools.text = str(int(Tools.get_mquantity()))
            else:
                initiateTrade(False,Tools,quantity,price)
        elif self.medicine_box.value:
            if not self.shareCheckBox.value:
                label_text =  sell_res(Medicine,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_vmedicine.text = str(int(Medicine.get_vquantity()))
                    self.label_mmedicine.text = str(int(Medicine.get_mquantity()))
            else:
                initiateTrade(False,Medicine,quantity,price)
        elif self.books_box.value:
            if not self.shareCheckBox.value:
                label_text =  sell_res(Book,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_vbooks.text = str(int(Book.get_vquantity()))
                    self.label_mbooks.text = str(int(Book.get_mquantity()))
            else:
                initiateTrade(False,Book,quantity,price)
        elif self.rice_box.value:
            if not self.shareCheckBox.value:
                label_text =  sell_res(Rice,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_vrice.text = str(int(Rice.get_vquantity()))
                    self.label_mrice.text = str(int(Rice.get_mquantity()))
            else:
                initiateTrade(False,Rice,quantity,price)
        elif self.wheat_box.value:
            if not self.shareCheckBox.value:
                label_text =  sell_res(Wheat,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_vwheat.text = str(int(Wheat.get_vquantity()))
                    self.label_mwheat.text = str(int(Wheat.get_mquantity()))
            else:
                initiateTrade(False,Wheat,quantity,price)
        elif self.beans_box.value:
            if not self.shareCheckBox.value:
                label_text =  sell_res(Beans,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_vbeans.text = str(int(Beans.get_vquantity()))
                    self.label_mbeans.text = str(int(Beans.get_mquantity()))
            else:
                initiateTrade(False,Beans,quantity,price)
        elif self.sugar_box.value:
            if not self.shareCheckBox.value:
                label_text =  sell_res(Sugar,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_vsugar.text = str(int(Sugar.get_vquantity()))
                    self.label_msugar.text = str(int(Sugar.get_mquantity()))
            else:
                initiateTrade(False,Sugar,quantity,price)
        elif self.salt_box.value:
            if not self.shareCheckBox.value:
                label_text =  sell_res(Salt,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_vsalt.text = str(int(Salt.get_vquantity()))
                    self.label_msalt.text = str(int(Salt.get_mquantity()))
            else:
                initiateTrade(False,Salt,quantity,price)
        elif self.oil_box.value:
            if not self.shareCheckBox.value:
                label_text =  sell_res(Oil,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_voil.text = str(int(Oil.get_vquantity()))
                    self.label_moil.text = str(int(Oil.get_mquantity()))
            else:
                initiateTrade(False,Oil,quantity,price)
        else:
            label_text = ' Please select a Resource for Trading'
        self.message_label.text = label_text
        
        
    def close_win(self,button=None):
        self.win.close()
        self.win_flag = False
        gui_obj.enable_buttons()

    def close_win_safe(self,button = None):
        self.win_flag = False
        gui_obj.enable_buttons()



    def get_win_flag(self):
        return self.win_flag

        

    

class gui_buttons:

    rect_color = (255,214,150)
    color_grey = (160,160,160)

    def initialize(self):
        ''' Initialises the buttons for setting up facility, upgrading it and for buy/sell operations
        '''
        myfont = pygame.font.Font("font.ttf", resize_pt(17))
        button_style = gui.defaultButtonStyle.copy()
        button_style['font'] = myfont
        self.setup_button = Button(position = resize_pos((50,865)), size = resize_pos((200,25)), parent = desktop, text = "Setup Facility",style = button_style)
        self.upgrade_button = Button(position = resize_pos((350,865)), size = resize_pos((200,25)), parent = desktop, text = "Upgrade Facility",style = button_style)
        self.buysell_button = Button(position = resize_pos((650,865)), size = resize_pos((200,25)), parent = desktop, text = "Buy/Sell Resources",style = button_style)
        self.setup_obj = setup_button()
        self.upgrade_obj = upgrade_button()
        self.buysell_obj = buysell_button()
        self.setup_button.onClick = self.setup_obj.setup
        self.upgrade_button.onClick = self.upgrade_obj.upgrade
        self.buysell_button.onClick = self.buysell_obj.buysell
        self.win_flag = False
        self.child_win_flag = False
        

    def get_win_flag(self):
        return (self.setup_obj.get_win_flag() or self.upgrade_obj.get_win_flag() or self.buysell_obj.get_win_flag())

    def get_child_win_flag(self):
        return self.setup_obj.get_child_win_flag()

    def close_child_win(self):
        self.setup_obj.child_win.close()
        self.setup_obj.enable_parent_win()

    def close_win(self):
        if self.setup_obj.get_win_flag():
            self.setup_obj.close_win()
        elif self.upgrade_obj.get_win_flag():
            self.upgrade_obj.close_win()
        elif self.buysell_obj.get_win_flag():
            self.buysell_obj.close_win()
            
    def press_enter(self):
        
        # responds to the enter keypress
        if  self.get_child_win_flag():
            self.setup_obj.setup_facility_farm()
        
        elif self.setup_obj.get_win_flag():
            self.setup_obj.setup_facility()
            
        elif self.upgrade_obj.get_win_flag():
            self.upgrade_obj.upgrade_facility()
            
        
    def disable_buttons(self):

        # stopping the motion of the background
        transform_obj.stop_mouse_move()
        total_update_flag = True

        self.setup_button.enabled = False
        self.upgrade_button.enabled = False
        self.buysell_button.enabled = False

    def enable_buttons(self):

        resume_update_thread()

        # resume mouse motion
        transform_obj.resume_mouse_move()

        self.win_flag = False

        self.setup_button.enabled = True
        self.upgrade_button.enabled = True
        self.buysell_button.enabled = True
        total_update_flag = True



    
  
gui_obj = gui_buttons()

def initialize_gui():
    
    ''' Function to initialize the GUI
    '''
    global gui_obj
    gui_obj.initialize()     
    

def initiateTrade(buysell,resource,quantity,price):
    ''' buysell is a flag if True : Buy , if False : Sell
        resource tells which resource is to be traded
        price : price at which the resource will be traded
    '''
    if buysell:
        cost  = quantity*price
        if cost > Money.get_money():
            gui_obj.buysell_obj.message_label.text = " Village doesn't have enough money to buy the resources"
            return
        broadcast_msg(['Trade',resource.get_name(),str(price),'sell'])
        setUnicastTradingFlag('sell')
    else:
        if quantity > resource.get_vquantity():
            gui_obj.buysell_obj.message_label.text = " There are not enough resources in the village to trade"
            return
        broadcast_msg(['Trade',resource.get_name(),str(quantity),str(price),'buy'])
        setUnicastTradingFlag('buy')
        
    

