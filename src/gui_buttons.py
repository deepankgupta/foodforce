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
        self.win.onClose = lambda button: gui_obj.enable_buttons()
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



    def setup_facility(self,button):
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
        self.child_win = Window(position = position_win, size = size_win, parent = desktop, text = "Setup Farm " ,style = win_style,shadeable = False)
        self.child_win.surf.set_alpha(190) 
        self.win.enabled = False
        self.child_win_flag = True
        self.child_win.onClose = lambda button: self.enable_parent_win()

        # Creating custom label style1
        myfont2 = pygame.font.Font("font.ttf",resize_pt(16))
        labelstyle1 = gui.defaultLabelStyle.copy()
        labelstyle1['border-width'] = 0
        labelstyle1['wordwrap'] = False
        labelstyle1['autosize'] = True
        labelstyle1['font'] = myfont2
        labelstyle1['font-color'] = self.rect_color

        label_rice = Label(position = resize_pos((10.0,70.0),(600.0,400.0),self.child_win.size), parent = self.child_win, text = 'Rice', style = labelstyle1)
        label_veg = Label(position = self.child_win.nextPosition(resize_pt_y(20)), parent = self.child_win, text = 'Fruit and Vegetables', style = labelstyle1)
        label_beans = Label(position = self.child_win.nextPosition(resize_pt_y(20)), parent = self.child_win, text = 'Beans', style = labelstyle1)

        # Creating second custom label style
        labelStyleCopy2 = gui.defaultLabelStyle.copy()
        labelStyleCopy2['border-width'] = 1
        labelStyleCopy2['wordwrap'] = True
        labelStyleCopy2['autosize'] = False
        labelStyleCopy2['font'] = myfont2
        labelStyleCopy2['font-color'] = self.rect_color
        labelStyleCopy2['border-color'] = self.color_grey
        text = ' Please enter the percentages of different food items you want to grow in your farm'
        self.message_label2 = Label(position = resize_pos((20,200),(600.0,400.0),self.child_win.size),size = resize_pos((470,120),(600.0,400.0),self.child_win.size), parent = self.child_win, text = text, style = labelStyleCopy2)

        # Creating custom text box style
        textbox_style = gui.defaultTextBoxStyle.copy()
        textbox_style['font'] = myfont2
        textbox_style['font-color'] = self.rect_color
        self.textbox_rice = TextBox(position = resize_pos((300.0, 70.0),(600.0,400.0),self.child_win.size), size = resize_pos((50,20),(600.0,400.0),self.child_win.size), parent = self.child_win, style = textbox_style) 
        self.textbox_veg = TextBox(position = resize_pos((300.0, 110.0),(600.0,400.0),self.child_win.size), size = resize_pos((50,20),(600.0,400.0),self.child_win.size), parent = self.child_win, style = textbox_style) 
        self.textbox_beans = TextBox(position = resize_pos((300.0, 150.0),(600.0,400.0),self.child_win.size), size = resize_pos((50,20),(600.0,400.0),self.child_win.size), parent = self.child_win, style = textbox_style) 

        # Custom button style        
        button_style = gui.defaultButtonStyle.copy()
        button_style['font'] = myfont2

        self.button_setup_farm = Button(position = resize_pos((500.0,300.0),(600.0,400.0),size_win), size = resize_pos((80.0,50.0),(600.0,400.0),size_win), parent = self.child_win, text = "Set Up",style = button_style)
        self.button_setup_farm.onClick = self.setup_facility_farm

        self.return_text_farm = ' '
        return self.return_text_farm


    def setup_facility_farm(self,button):

        # Checking whether the user has entered the value in text box properly
        text1 = self.textbox_rice.text

        try:
            if text1 == '':
                quantity1 = 0
            else:
                quantity1 = float(text1)

                if quantity1 < 0.0:
                    self.message_label2.text = 'Please enter a positive value as the percentage of rice'
                    return

        except:
            self.message_label2.text = 'Please enter a number as the percentage of rice you want to grow'
            return    

        text2 = self.textbox_veg.text

        try:
            if text2 == '':
                quantity2 = 0
            else:
                quantity2 = float(text2)

                if quantity2 < 0.0:
                    self.message_label2.text = 'Please enter a positive value as the percentage of vegetables'
                    return

        except:
            self.message_label2.text = 'Please enter a number as the percentage of vegetables you want to grow'
            return    

        text3 = self.textbox_beans.text
        print text3
        try:
            if text3 == '':
                quantity3 = 0
            else:

                quantity3 = float(text3)
                if quantity3 < 0.0:

                    self.message_label2.text = 'Please enter a positive value as the percentage of beans'
                    return

        except:
            self.message_label2.text = 'Please enter a number as the percentage of beans you want to grow'
            return    

        if ((quantity1 + quantity2 + quantity3)< 99.5) or ((quantity1 + quantity2 + quantity3)> 100.5):

            self.message_label2.text = 'The sum of all the percentages should be equal to 100'
            return

        list_food = [quantity1,quantity2,quantity3]
        label_text = build_facility(Farm,list_food)
        self.message_label2.text = label_text
        if label_text == 'Facility has been build':    
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
        self.win.onClose = lambda button: gui_obj.enable_buttons()
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

    def upgrade_facility(self,button):
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
        transform_obj.focus_at((2800,2500)) # Replace this with the coordinates ofthe market in the base surface

        # Calculating position and size of window from the size of the desktop        
        position_win =resize_pos((200.0,50.0))
        size_win =resize_pos((800.0,600.0))

        # Creating window
        self.win = Window(position = position_win, size = size_win, parent = desktop, text = " Buy or Sell Resources " ,style = win_style,shadeable = False)
        self.win.surf.set_alpha(140) 
        self.win.onClose = lambda button: gui_obj.enable_buttons()
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
        heading_label4 = Label(position = resize_pos((280.0,70.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Price', style = labelstyle1)
        heading_label5 = Label(position = resize_pos((520.0,70.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Resources', style = labelstyle1)
        heading_label6 = Label(position = resize_pos((700.0,70.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Market', style = labelstyle1)
        heading_label7 = Label(position = resize_pos((700.0,85.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Quantity', style = labelstyle1)

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


        # Creating labels for prices of Resources 
        self.price_vwater = Label(position = resize_pos((280.0,140.0),(800.0,600.0),self.win.size), parent = self.win, text = str(int(Water.get_price())), style = labelstyle1)
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


        # Creating labels for name of Resources for the market
        self.water_label = Label(position = resize_pos((520.0,140.0),(800.0,600.0),self.win.size), parent = self.win, style = labelstyle1, text = 'Water')
        self.buildmat_label = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, style = labelstyle1, text = 'Building Materials')
        self.tools_label = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, style = labelstyle1, text = 'Tools')
        self.books_label = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, style = labelstyle1, text = 'Books')
        self.medicine_label = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, style = labelstyle1, text = 'Medicines')
        self.rice_label = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, style = labelstyle1, text = 'Rice')
        self.wheat_label = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, style = labelstyle1, text = 'Fruit & Vegatables')
        self.beans_label = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, style = labelstyle1, text = 'Beans')
        self.sugar_label = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, style = labelstyle1, text = 'Sugar')
        self.salt_label = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, style = labelstyle1, text = 'Salt')
        self.oil_label = Label(position = self.win.nextPosition(resize_pt_y(7)), parent = self.win, style = labelstyle1, text = 'Oil')

        # Creating labels for market values of Resources 
        self.label_mwater = Label(position = resize_pos((700.0,140.0),(800.0,600.0),self.win.size), parent = self.win, text = str(int(Water.get_mquantity())), style = labelstyle1)
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

        # Creating a textbox to enter the quantity to buy or sell
        textbox_style = gui.defaultTextBoxStyle.copy()
        textbox_style['font'] = myfont2
        textbox_style['font-color'] = self.rect_color
        self.label_quantity = Label(position = resize_pos((360.0,150.0),(800.0,600.0),self.win.size), parent = self.win, text = ' Quantity ', style = labelstyle1)
        self.win.textbox = TextBox(position = resize_pos((350.0, 200.0),(800.0,600.0),self.win.size), size = resize_pos((100,20),(800.0,600.0),self.win.size), parent = self.win, style = textbox_style) 


       # Creating buttons for buying and selling and closing the window
        button_style = gui.defaultButtonStyle.copy()
        button_style['font'] = myfont2

        self.button_buy = Button(position = resize_pos((370.0,280.0),(800.0,600.0),size_win), size = resize_pos((70.0,50.0),(800.0,600.0),size_win), parent = self.win, text = " Buy ",style = button_style)
        self.button_sell = Button(position = resize_pos((370.0,330.0),(800.0,600.0),size_win), size = resize_pos((70.0,50.0),(800.0,600.0),size_win), parent = self.win, text = " Sell ",style = button_style)
        self.button_close = Button(position = resize_pos((650.0,500.0),(800.0,600.0),size_win), size = resize_pos((120.0,50.0),(800.0,600.0),size_win), parent = self.win, text = "Close",style = button_style)
        self.button_buy.onClick = self.buy_resources
        self.button_sell.onClick = self.sell_resources
        self.button_close.onClick  = self.close_win


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

    def buy_resources(self,button):
        ''' Initiated for doing the transaction of buying the resources 
        '''
        # Checking whether the user has entered the value in text box properly
        text = self.win.textbox.text
        try:
            quantity = int(float(text))
            if quantity == 0:
                self.message_label.text = 'Please Enter the quantity for buying or selling'
                return

        except:
            self.message_label.text = 'Please Enter a number as the quantity for buying or selling'
            return    

        # Checking whether the user has selected the appropriate option box for the resource or not, and do the appropriate action
        if self.water_box.value:
            label_text =  buy_res(Water,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_vwater.text = str(int(Water.get_vquantity()))
                self.label_mwater.text = str(int(Water.get_mquantity()))
        elif self.buildmat_box.value:
            label_text =  buy_res(Buildmat,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_vbuildmat.text = str(int(Buildmat.get_vquantity()))
                self.label_mbuildmat.text = str(int(Buildmat.get_mquantity()))
        elif self.tools_box.value:
            label_text =  buy_res(Tools,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_vtools.text = str(int(Tools.get_vquantity()))
                self.label_mtools.text = str(int(Tools.get_mquantity()))
        elif self.medicine_box.value:
            label_text =  buy_res(Medicine,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_vmedicine.text = str(int(Medicine.get_vquantity()))
                self.label_mmedicine.text = str(int(Medicine.get_mquantity()))
        elif self.books_box.value:
            label_text =  buy_res(Book,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_vbooks.text = str(int(Book.get_vquantity()))
                self.label_mbooks.text = str(int(Book.get_mquantity()))
        elif self.rice_box.value:
            label_text =  buy_res(Rice,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_vrice.text = str(int(Rice.get_vquantity()))
                self.label_mrice.text = str(int(Rice.get_mquantity()))
        elif self.wheat_box.value:
            label_text =  buy_res(Wheat,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_vwheat.text = str(int(Wheat.get_vquantity()))
                self.label_mwheat.text = str(int(Wheat.get_mquantity()))
        elif self.beans_box.value:
            label_text =  buy_res(Beans,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_vbeans.text = str(int(Beans.get_vquantity()))
                self.label_mbeans.text = str(int(Beans.get_mquantity()))
        elif self.sugar_box.value:
            label_text =  buy_res(Sugar,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_vsugar.text = str(int(Sugar.get_vquantity()))
                self.label_msugar.text = str(int(Sugar.get_mquantity()))
        elif self.salt_box.value:
            label_text =  buy_res(Salt,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_vsalt.text = str(int(Salt.get_vquantity()))
                self.label_msalt.text = str(int(Salt.get_mquantity()))
        elif self.oil_box.value:
            label_text =  buy_res(Oil,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_voil.text = str(int(Oil.get_vquantity()))
                self.label_moil.text = str(int(Oil.get_mquantity()))
        else:
            label_text = ' Please select a Resource for Trading'

        self.message_label.text = label_text
        self.win.textbox.text = ''



    def sell_resources(self,button):
        ''' Initiated for doing the transaction of buying the resources 
        '''
        # Checking whether the user has entered the value in text box properly
        text = self.win.textbox.text
        try:
            quantity = int(float(text))
            if quantity == 0:
                self.message_label.text = 'Please Enter the quantity for buying or selling'
                return

        except:
            self.message_label.text = 'Please Enter a number as the quantity for buying or selling'
            return    

        # Checking whether the user has selected the appropriate option box for the resource or not, and do the appropriate action
        if self.water_box.value:
            label_text =  sell_res(Water,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_vwater.text = str(int(Water.get_vquantity()))
                self.label_mwater.text = str(int(Water.get_mquantity()))
        elif self.buildmat_box.value:
            label_text =  sell_res(Buildmat,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_vbuildmat.text = str(int(Buildmat.get_vquantity()))
                self.label_mbuildmat.text = str(int(Buildmat.get_mquantity()))
        elif self.tools_box.value:
            label_text =  sell_res(Tools,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_vtools.text = str(int(Tools.get_vquantity()))
                self.label_mtools.text = str(int(Tools.get_mquantity()))
        elif self.medicine_box.value:
            label_text =  sell_res(Medicine,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_vmedicine.text = str(int(Medicine.get_vquantity()))
                self.label_mmedicine.text = str(int(Medicine.get_mquantity()))
        elif self.books_box.value:
            label_text =  sell_res(Book,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_vbooks.text = str(int(Book.get_vquantity()))
                self.label_mbooks.text = str(int(Book.get_mquantity()))
        elif self.rice_box.value:
            label_text =  sell_res(Rice,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_vrice.text = str(int(Rice.get_vquantity()))
                self.label_mrice.text = str(int(Rice.get_mquantity()))
        elif self.wheat_box.value:
            label_text =  sell_res(Wheat,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_vwheat.text = str(int(Wheat.get_vquantity()))
                self.label_mwheat.text = str(int(Wheat.get_mquantity()))
        elif self.beans_box.value:
            label_text =  sell_res(Beans,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_vbeans.text = str(int(Beans.get_vquantity()))
                self.label_mbeans.text = str(int(Beans.get_mquantity()))
        elif self.sugar_box.value:
            label_text =  sell_res(Sugar,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_vsugar.text = str(int(Sugar.get_vquantity()))
                self.label_msugar.text = str(int(Sugar.get_mquantity()))
        elif self.salt_box.value:
            label_text =  sell_res(Salt,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_vsalt.text = str(int(Salt.get_vquantity()))
                self.label_msalt.text = str(int(Salt.get_mquantity()))
        elif self.oil_box.value:
            label_text =  sell_res(Oil,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_voil.text = str(int(Oil.get_vquantity()))
                self.label_moil.text = str(int(Oil.get_mquantity()))
        else:
            label_text = ' Please select a Resource for Trading'
        self.message_label.text = label_text
        self.win.textbox.text = ''
        
        
    def close_win(self,button=None):
        self.win.close()
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
            
    def disable_buttons(self):

        # stopping the motion of the background
        transform_obj.stop_mouse_move()

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



    
  
gui_obj = gui_buttons()

def initialize_gui():
    
    ''' Function to initialize the GUI
    '''
    global gui_obj
    gui_obj.initialize()





  
    
    
    
    
    
    
        