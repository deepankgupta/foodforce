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
#from threades import *
import threades
import threading

import gui
#from gui import *
import pygame
import load_images
#from model import *
import game_events
import model
if model.FLAG_XO:
    import game_sharing

class marketBarChart:
    '''Class which displays the bar chart in the market window
    '''
    color1 = (255,214,150)
    color2 = (170,142,100)
    #color3 = (85,71,50)
    color_rect = (50,100,150)

    def drawValueChart(self,surface,initial_value = 10,maximum_value = 100.0):
        ''' Draws a barchart on the screen
        '''

        self.price_flag = False
        self.surf = surface
        self.bar1Val = initial_value
        self.bar1ValMax = maximum_value
        pygame.draw.rect(surface,self.color1,threades.resize_rect((440,200,200*self.bar1Val/self.bar1ValMax,30)))

        pygame.draw.rect(surface,self.color_rect,threades.resize_rect((440,200,200,30)),2)

    def drawPriceChart(self,surface,initial_price = 10, maximum_value = 25):
        ''' Draws a barchart on the screen
        '''
        if self.price_flag == False:
            self.price_flag = True
            self.bar2Val = initial_price
            self.bar2ValMax = maximum_value
            pygame.draw.rect(surface,self.color2,threades.resize_rect((440,280,200*self.bar2Val/self.bar2ValMax,30)))

            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((440,280,200,30)),2)


    def updateChart(self,(x,y)):
        ''' Updates the bar chart on the basis of the mouse click
        '''
        surface = self.surf
        if (x>threades.resize_pt_x(640)) and (x<threades.resize_pt_x(840)) and (y>threades.resize_pt_y(250)) and (y<threades.resize_pt_y(280)):
            pygame.draw.rect(surface,(0,0,0,180),threades.resize_rect((440,200,200,50)))

            self.bar1Val = (x-threades.resize_pt_x(640))*self.bar1ValMax/threades.resize_pt_x(200)

            if self.bar1Val > self.bar1ValMax:
                self.bar1Val = self.bar1ValMax
            if self.bar1Val < 0:
                self.bar1Val = 0

            pygame.draw.rect(surface,self.color1,threades.resize_rect((440,200,200*self.bar1Val/self.bar1ValMax,30)))

            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((440,200,200,30)),2)
            gui_obj.buysell_obj.updateMarketLabelValues()

        if self.price_flag:
            if (x>threades.resize_pt_x(640)) and (x<threades.resize_pt_x(840)) and (y>threades.resize_pt_y(330)) and (y<threades.resize_pt_y(360)):
                pygame.draw.rect(surface,(0,0,0,180),threades.resize_rect((440,280,200,30)))

                self.bar2Val = (x-threades.resize_pt_x(640))*self.bar2ValMax/threades.resize_pt_x(200)

                if self.bar2Val > self.bar2ValMax:
                    self.bar2Val = self.bar2ValMax
                if self.bar2Val < 0:
                    self.bar2Val = 0

                pygame.draw.rect(surface,self.color2,threades.resize_rect((440,280,200*self.bar2Val/self.bar2ValMax,30)))

                pygame.draw.rect(surface,self.color_rect,threades.resize_rect((440,280,200,30)),2)
                gui_obj.buysell_obj.updateMarketLabelValues()

        #gui_obj.buysell_obj.drawPriceChart()

    def deletePriceChart(self):

        if self.price_flag:
            pygame.draw.rect(self.surf,(0,0,0,180),threades.resize_rect((438,278,234,34)))
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


        pygame.draw.rect(surface,self.color1,threades.resize_rect((100,50.0+200*(100-self.bar1Val)/100,50,200*self.bar1Val/100.0)))
        pygame.draw.rect(surface,self.color2,threades.resize_rect((250,50.0+200*(100-self.bar2Val)/100,50,200*self.bar2Val/100.0)))
        pygame.draw.rect(surface,self.color3,threades.resize_rect((400,50.0+200*(100-self.bar3Val)/100,50,200*self.bar3Val/100.0)))

        pygame.draw.rect(surface,self.color_rect,threades.resize_rect((100,50,50,200)),2)
        pygame.draw.rect(surface,self.color_rect,threades.resize_rect((250,50,50,200)),2)
        pygame.draw.rect(surface,self.color_rect,threades.resize_rect((400,50,50,200)),2)

    def updateChart(self,(x,y)):
        ''' Updates the bar chart on the basis of the mouse click
        '''
        surface = self.surf
        if (x>threades.resize_pt_x(400)) and (x<threades.resize_pt_x(450)) and (y>threades.resize_pt_y(200)) and (y<threades.resize_pt_y(400)):
            pygame.draw.rect(surface,(0,0,0),threades.resize_rect((100,50,350,200)))
            change = self.bar1Val - (threades.resize_pt_y(400)-y)*100/threades.resize_pt_y(200.0)
            self.bar1Val = self.bar1Val - change
            ratio1 = self.bar2Val/(self.bar2Val +self.bar3Val+0.0)
            ratio2 = self.bar3Val/(self.bar2Val +self.bar3Val+0.0)
            self.bar2Val = self.bar2Val + ratio1*change
            self.bar3Val = self.bar3Val + ratio2*change


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

            pygame.draw.rect(surface,self.color1,threades.resize_rect((100,50.0+200*(100-self.bar1Val)/100,50,200*self.bar1Val/100.0)))
            pygame.draw.rect(surface,self.color2,threades.resize_rect((250,50.0+200*(100-self.bar2Val)/100,50,200*self.bar2Val/100.0)))
            pygame.draw.rect(surface,self.color3,threades.resize_rect((400,50.0+200*(100-self.bar3Val)/100,50,200*self.bar3Val/100.0)))

            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((100,50,50,200)),2)
            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((250,50,50,200)),2)
            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((400,50,50,200)),2)



        if (x>threades.resize_pt_x(550)) and (x<threades.resize_pt_x(600)) and (y>threades.resize_pt_y(200)) and (y<threades.resize_pt_y(400)):
            pygame.draw.rect(surface,(0,0,0),threades.resize_rect((100,50,350,200)))
            change = self.bar2Val - (threades.resize_pt_y(400)-y)*100/threades.resize_pt_y(200.0)
            self.bar2Val = self.bar2Val - change
            ratio1 = self.bar1Val/(self.bar1Val +self.bar3Val+0.0)
            ratio2 = self.bar3Val/(self.bar1Val +self.bar3Val+0.0)
            self.bar1Val = self.bar1Val + ratio1*change
            self.bar3Val = self.bar3Val + ratio2*change

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

            pygame.draw.rect(surface,self.color1,threades.resize_rect((100,50.0+200*(100-self.bar1Val)/100,50,200*self.bar1Val/100.0)))
            pygame.draw.rect(surface,self.color2,threades.resize_rect((250,50.0+200*(100-self.bar2Val)/100,50,200*self.bar2Val/100.0)))
            pygame.draw.rect(surface,self.color3,threades.resize_rect((400,50.0+200*(100-self.bar3Val)/100,50,200*self.bar3Val/100.0)))

            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((100,50,50,200)),2)
            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((250,50,50,200)),2)
            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((400,50,50,200)),2)



        if (x>threades.resize_pt_x(700)) and (x<threades.resize_pt_x(750)) and (y>threades.resize_pt_y(200)) and (y<threades.resize_pt_y(400)):
            pygame.draw.rect(surface,(0,0,0),threades.resize_rect((100,50,350,200)))
            change = self.bar3Val - (threades.resize_pt_y(400)-y)*100/threades.resize_pt_y(200.0)
            self.bar3Val = self.bar3Val - change
            ratio1 = self.bar2Val/(self.bar2Val +self.bar1Val+0.0)
            ratio2 = self.bar1Val/(self.bar2Val +self.bar1Val+0.0)
            self.bar2Val = self.bar2Val + ratio1*change
            self.bar1Val = self.bar1Val + ratio2*change

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

            pygame.draw.rect(surface,self.color1,threades.resize_rect((100,50.0+200*(100-self.bar1Val)/100,50,200*self.bar1Val/100.0)))
            pygame.draw.rect(surface,self.color2,threades.resize_rect((250,50.0+200*(100-self.bar2Val)/100,50,200*self.bar2Val/100.0)))
            pygame.draw.rect(surface,self.color3,threades.resize_rect((400,50.0+200*(100-self.bar3Val)/100,50,200*self.bar3Val/100.0)))

            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((100,50,50,200)),2)
            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((250,50,50,200)),2)
            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((400,50,50,200)),2)






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
        myfont = pygame.font.Font("font.ttf", threades.resize_pt(20))

        # Custom gui.Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont
        win_style['font-color'] = self.rect_color
        win_style['bg-color'] = (0,0,0, 180)

        # Calculating position and size of window from the size of the threades.desktop
        position_win =threades.resize_pos((200.0,50.0))
        size_win =threades.resize_pos((800.0,600.0))

        # Creating window
        self.win = gui.Window(position = position_win, size = size_win, parent = threades.desktop, text = "Set up a facility for your village " ,style = win_style,shadeable = False)

        self.win.surf.set_alpha(140)
        self.win.onClose = lambda button: self.close_win_safe()
        self.win_flag = True

        # Pausing the update thread
        #threades.pause_update_thread()

        #  Creating Custom label style
        myfont2 = pygame.font.Font("font.ttf", threades.resize_pt(16))
        myfont3 = pygame.font.Font("font.ttf", threades.resize_pt(14))
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 1
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont2
        labelStyleCopy['font-color'] = self.rect_color
        default_text = 'What would you like to set up? '
        self.message_label = gui.Label(position = threades.resize_pos((450,120),(800.0,600.0),self.win.size),size = threades.resize_pos((250,100),(800.0,600.0),self.win.size), parent = self.win, text = default_text, style = labelStyleCopy)
        text ='Please select a Facility to see its status and Requirements'
        labelStyleCopy2 = gui.defaultLabelStyle.copy()
        labelStyleCopy2['border-width'] = 1
        labelStyleCopy2['wordwrap'] = True
        labelStyleCopy2['autosize'] = False
        labelStyleCopy2['font'] = myfont3
        labelStyleCopy2['font-color'] = self.rect_color

        self.message_label2 = gui.Label(position = threades.resize_pos((30,450),(800.0,600.0),self.win.size),size = threades.resize_pos((570,120),(800.0,600.0),self.win.size), parent = self.win, text = text, style = labelStyleCopy2)

        #Creating new button style
        buttonsurf = pygame.image.load(os.path.join('art','button.png')).convert_alpha()
        buttonsurf = pygame.transform.scale(buttonsurf, (36, threades.resize_pt_y( 40)))
        bt_style = gui.createButtonStyle(myfont,(0,0,0), buttonsurf,4,1,4,4,1,4,4,1,4,4,1,4)



        # Creating option boxes for all the facilities
        position_bt = threades.resize_pos((50.0,90.0),(800.0,600.0),size_win)
        size_bt = threades.resize_pos((320.0,200.0),(800.0,600.0),size_win)
        self.housing_box = gui.Button(position = position_bt, size = size_bt,  parent = self.win, style = bt_style, text = 'Hut')
        self.housing_box.onMouseOver =  self.on_select_setup_option_box
        self.housing_box.onClick = self.setup_facility
        self.hospital_box = gui.Button(position = self.win.nextPosition(threades.resize_pt_y(10)), size = size_bt, parent = self.win, style = bt_style, text = 'Hospital')
        self.hospital_box.onMouseOver = self.on_select_setup_option_box
        self.hospital_box.onClick = self.setup_facility
        self.workshop_box = gui.Button(position = self.win.nextPosition(threades.resize_pt_y(10)), size = size_bt, parent = self.win, style = bt_style, text = 'Workshop')
        self.workshop_box.onMouseOver = self.on_select_setup_option_box
        self.workshop_box.onClick = self.setup_facility
        self.school_box = gui.Button(position = self.win.nextPosition(threades.resize_pt_y(10)), size = size_bt, parent = self.win, style = bt_style, text = 'School')
        self.school_box.onMouseOver = self.on_select_setup_option_box
        self.school_box.onClick = self.setup_facility
        self.farm_box = gui.Button(position = self.win.nextPosition(threades.resize_pt_y(10)), size = size_bt, parent = self.win, style = bt_style, text = 'Farm')
        self.farm_box.onMouseOver = self.on_select_setup_option_box
        self.farm_box.onClick = self.setup_facility
        self.fountain_box = gui.Button(position = self.win.nextPosition(threades.resize_pt_y(10)), size = size_bt, parent = self.win, style = bt_style, text = 'Well')
        self.fountain_box.onMouseOver = self.on_select_setup_option_box
        self.fountain_box.onClick = self.setup_facility



    def on_select_setup_option_box(self,button):

        #self.win.surf.set_alpha(255)
        #self.win.surf.blit(self.background_pic,threades.resize_pos((450,250)))
        #self.win.surf.set_alpha(140)

        if button.text == 'Hut':
            text = 'Hut: '
            #image = load_images. House_tiles_list[2][2]
            text += threades.get_setup_text(model.House)
        if button.text == 'Hospital':
            text = 'Hospital: '
            #image = load_images. Hospital_tiles_list[2][2]
            text += threades.get_setup_text(model.Hospital)
        if button.text == 'School':
            text = 'School: '
            #image = load_images.School_tiles_list[2][2]
            text += threades.get_setup_text(model.School)
        if button.text == 'Workshop':
            text = 'Workshop: '
            #image = load_images.Workshop_tiles_list[2][2]
            text += threades.get_setup_text(model.Workshop)
        if button.text == 'Farm':
            text = 'Farm: '
            #image = load_images.Farm_tiles[0][1]
            text += threades.get_setup_text(model.Farm)
        if button.text == 'Well':
            text = 'Well: '
            #image = load_images.Fountain_tiles[0][3]
            text += threades.get_setup_text(model.Fountain)
        #display_image = pygame.transform.scale(image,threades.resize_pos((140,140)))
        #self.win.surf.blit(display_image,threades.resize_pos((450,250)))
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


        if button.text == 'Hut':
            label_text =  threades.build_facility(model.House)
        elif button.text == 'Hospital':
            label_text =  threades.build_facility(model.Hospital)
        elif button.text == 'Workshop':
            label_text =  threades.build_facility(model.Workshop)
        elif button.text == 'Well':
            label_text =  threades.build_facility(model.Fountain)
        elif button.text == 'School':
            label_text =  threades.build_facility(model.School)
        elif button.text == 'Farm':
            label_text =  self.build_facility_farm()
        else:
            label_text = 'Please select a Facility for building'
        self.message_label.text = label_text
        if label_text== 'Facility has been build':
            self.close_win()

    def build_facility_farm(self):

        myfont = pygame.font.Font("font.ttf",threades.resize_pt(22))

        # Custom gui.Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont
        win_style['font-color'] = self.rect_color
        win_style['bg-color'] = (0,0,0)

        # Calculating position and size of window from the size of the threades.desktop
        position_win =threades.resize_pos((300.0,150.0))
        size_win =threades.resize_pos((600.0,400.0))

        # Creating window
        self.child_win = gui.Window(position = position_win, size = size_win, parent = threades.desktop, text = "Setup Farm " ,style = win_style,shadeable = False,moveable = False)
        #self.child_win.surf.set_alpha(190)
        self.win.enabled = False
        self.child_win_flag = True
        self.child_win.onClose = lambda button: self.enable_parent_win()

        self.bardisplay = barChart()
        self.bardisplay.drawChart(self.child_win.surf,33,33,34)

        # Creating custom label style1
        myfont2 = pygame.font.Font("font.ttf",threades.resize_pt(16))
        labelstyle1 = gui.defaultLabelStyle.copy()
        labelstyle1['border-width'] = 0
        labelstyle1['wordwrap'] = False
        labelstyle1['autosize'] = True
        labelstyle1['font'] = myfont2
        labelstyle1['font-color'] = self.rect_color

        label_rice = gui.Label(position = threades.resize_pos((100.0,260.0),(600.0,400.0),self.child_win.size), parent = self.child_win, text = 'Rice', style = labelstyle1)
        label_veg = gui.Label(position = threades.resize_pos((250.0,260.0),(600.0,400.0),self.child_win.size), parent = self.child_win, text = 'Fruit and \nVegetables', style = labelstyle1)
        label_beans = gui.Label(position = threades.resize_pos((400.0,260.0),(600.0,400.0),self.child_win.size), parent = self.child_win, text = 'Beans', style = labelstyle1)

        # Creating second custom label style
        labelStyleCopy2 = gui.defaultLabelStyle.copy()
        labelStyleCopy2['border-width'] = 0
        labelStyleCopy2['wordwrap'] = True
        labelStyleCopy2['autosize'] = False
        labelStyleCopy2['font'] = myfont2
        labelStyleCopy2['border-color'] = self.rect_color
        labelStyleCopy2['font-color'] = self.rect_color

        text = 'Balance the bar chart to select the percentages of different food items you want to grow in your farm'
        self.message_label2 = gui.Label(position = threades.resize_pos((20,320),(600.0,400.0),self.child_win.size),size = threades.resize_pos((470,70),(600.0,400.0),self.child_win.size), parent = self.child_win, text = text, style = labelStyleCopy2)

        '''
        # Creating custom text box style
        textbox_style = gui.defaultTextBoxStyle.copy()
        textbox_style['font'] = myfont2
        textbox_style['font-color'] = self.rect_color
        self.textbox_rice = TextBox(position = threades.resize_pos((300.0, 70.0),(600.0,400.0),self.child_win.size), size = threades.resize_pos((50,20),(600.0,400.0),self.child_win.size), parent = self.child_win, style = textbox_style)
        self.textbox_veg = TextBox(position = threades.resize_pos((300.0, 110.0),(600.0,400.0),self.child_win.size), size = threades.resize_pos((50,20),(600.0,400.0),self.child_win.size), parent = self.child_win, style = textbox_style)
        self.textbox_beans = TextBox(position = threades.resize_pos((300.0, 150.0),(600.0,400.0),self.child_win.size), size = threades.resize_pos((50,20),(600.0,400.0),self.child_win.size), parent = self.child_win, style = textbox_style)
        '''

        # Custom button style
        button_style = gui.defaultButtonStyle.copy()
        button_style['font'] = myfont2

        self.button_setup_farm = gui.Button(position = threades.resize_pos((500.0,320.0),(600.0,400.0),size_win), size = threades.resize_pos((80.0,50.0),(600.0,400.0),size_win), parent = self.child_win, text = "Set Up",style = button_style)
        self.button_setup_farm.onClick = self.setup_facility_farm

        self.return_text_farm = ' '
        return self.return_text_farm


    def setup_facility_farm(self,button=None):

        # Finally setting up the facility after the button is clicked
        quantity1 = self.bardisplay.bar1Val
        quantity2 = self.bardisplay.bar2Val
        quantity3 = self.bardisplay.bar3Val
        list_food = [quantity1,quantity2,quantity3]
        label_text = threades.build_facility(model.Farm,list_food)
        if label_text == 'Facility has been build':
            self.child_win.close()
            self.enable_parent_win()
            self.close_win()
        else:
            self.child_win.close()
            self.enable_parent_win()
            self.message_label.text = label_text
            #threades.message.push_message(label_text,'high')
        return

    def enable_parent_win(self):
        self.child_win_flag = False
        self.win.enabled = True
        self.close_win()
        self.setup()

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
        myfont = pygame.font.Font("font.ttf", threades.resize_pt(20))

        # Custom gui.Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont
        win_style['font-color'] = self.rect_color
        win_style['bg-color'] = (0,0,0, 180)

        # Calculating position and size of window from the size of the threades.desktop
        position_win =threades.resize_pos((200.0,50.0))
        size_win =threades.resize_pos((800.0,600.0))

        # Creating window
        self.win = gui.Window(position = position_win, size = size_win, parent = threades.desktop, text = "Upgrade Facility " ,style = win_style,shadeable = False)
        self.win.surf.set_alpha(140)
        self.win.onClose = lambda button: self.close_win_safe()
        self.win_flag = True

        # Pausing the update thread
        #threades.pause_update_thread()

        #  Creating Custom label style
        myfont2 = pygame.font.Font("font.ttf", threades.resize_pt(16))
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 1
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont2
        labelStyleCopy['font-color'] = self.rect_color
        labelStyleCopy['border-color'] = self.color_grey
        text = 'Please select a Facility to upgrade.'
        self.message_label = gui.Label(position = threades.resize_pos((450,150),(800.0,600.0),self.win.size),size = threades.resize_pos((200,100),(800.0,600.0),self.win.size), parent = self.win, text = text, style = labelStyleCopy)




        #Creating new button style
        buttonsurf = pygame.image.load(os.path.join('art','button.png')).convert_alpha()
        buttonsurf = pygame.transform.scale(buttonsurf, (36, threades.resize_pt_y( 40)))
        bt_style = gui.createButtonStyle(myfont,(0,0,0), buttonsurf,4,1,4,4,1,4,4,1,4,4,1,4)


        # Creating buttons for all the facilities
        position_bt = threades.resize_pos((50.0,90.0),(800.0,600.0),size_win)
        size_bt = threades.resize_pos((320.0,200.0),(800.0,600.0),size_win)
        self.housing_box = gui.Button(position = position_bt, size = size_bt,  parent = self.win, style = bt_style, text = 'Hut')
        self.housing_box.onMouseOver =  self.on_select_upgrade_option_box
        self.housing_box.onClick = self.upgrade_facility
        self.hospital_box = gui.Button(position = self.win.nextPosition(threades.resize_pt_y(10)), size = size_bt, parent = self.win, style = bt_style, text = 'Hospital')
        self.hospital_box.onMouseOver = self.on_select_upgrade_option_box
        self.hospital_box.onClick = self.upgrade_facility
        self.workshop_box = gui.Button(position = self.win.nextPosition(threades.resize_pt_y(10)), size = size_bt, parent = self.win, style = bt_style, text = 'Workshop')
        self.workshop_box.onMouseOver = self.on_select_upgrade_option_box
        self.workshop_box.onClick = self.upgrade_facility
        self.school_box = gui.Button(position = self.win.nextPosition(threades.resize_pt_y(10)), size = size_bt, parent = self.win, style = bt_style, text = 'School')
        self.school_box.onMouseOver = self.on_select_upgrade_option_box
        self.school_box.onClick = self.upgrade_facility
        self.farm_box = gui.Button(position = self.win.nextPosition(threades.resize_pt_y(10)), size = size_bt, parent = self.win, style = bt_style, text = 'Farm')
        self.farm_box.onMouseOver = self.on_select_upgrade_option_box
        self.farm_box.onClick = self.upgrade_facility
        self.fountain_box = gui.Button(position = self.win.nextPosition(threades.resize_pt_y(10)), size = size_bt, parent = self.win, style = bt_style, text = 'Well')
        self.fountain_box.onMouseOver = self.on_select_upgrade_option_box
        self.fountain_box.onClick = self.upgrade_facility


        text ='Please select a Facility to see its next upgrade'
        labelStyleCopy2 = gui.defaultLabelStyle.copy()
        labelStyleCopy2['border-width'] = 1
        labelStyleCopy2['wordwrap'] = True
        labelStyleCopy2['autosize'] = False
        labelStyleCopy2['font'] = myfont2
        labelStyleCopy2['font-color'] = self.rect_color

        self.message_label2 = gui.Label(position = threades.resize_pos((20,450),(800.0,600.0),self.win.size),size = threades.resize_pos((570,120),(800.0,600.0),self.win.size), parent = self.win, text = text, style = labelStyleCopy2)



    def on_select_upgrade_option_box(self,button):

        #self.win.surf.set_alpha(255)
        #self.win.surf.blit(self.background_pic,threades.resize_pos((450,250)))
        #self.win.surf.set_alpha(140)

        text = ''
        if button.text == 'Hut':
            #image = load_images. House_tiles_list[2][2]
            text += threades.get_upgrade_text(model.House)
        if button.text == 'Hospital':
            #image = load_images. Hospital_tiles_list[2][2]
            text += threades.get_upgrade_text(model.Hospital)
        if button.text == 'School':
            #image = load_images.School_tiles_list[2][2]
            text += threades.get_upgrade_text(model.School)
        if button.text == 'Workshop':
            #image = load_images.Workshop_tiles_list[2][2]
            text += threades.get_upgrade_text(model.Workshop)
        if button.text == 'Farm':
            #image = load_images.Farm_tiles[0][1]
            text += threades.get_upgrade_text(model.Farm)
        if button.text == 'Well':
            #image = load_images.Fountain_tiles[0][3]
            text += threades.get_upgrade_text(model.Fountain)
        #display_image = pygame.transform.scale(image,threades.resize_pos((140,140)))
        #self.win.surf.blit(display_image,threades.resize_pos((450,250)))
        self.message_label2.text = text
        self.message_label.text = 'Upgrades ' + button.text

    def upgrade_facility(self,button=None):
        ''' Upgrades the facility
        '''


        if button.text == 'Hut':
            label_text =  threades.upgrade_facility(model.House)
        elif button.text == 'Hospital':
            label_text =  threades.upgrade_facility(model.Hospital)
        elif button.text == 'Workshop':
            label_text =  threades.upgrade_facility(model.Workshop)
        elif button.text == 'Well':
            label_text =  threades.upgrade_facility(model.Fountain)
        elif button.text == 'School':
            label_text =  threades.upgrade_facility(model.School)
        elif button.text == 'Farm':
            label_text =  threades.upgrade_facility(model.Farm)
        else:
            label_text = 'Please select a Facility for Upgrading'
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

        global ActivitySharedFlag
        gui_obj.disable_buttons()
        myfont = pygame.font.Font("font.ttf", threades.resize_pt(20))

        # Custom gui.Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont
        win_style['font-color'] = self.rect_color
        win_style['bg-color'] = (0,0,0, 180)

        # Focus the animation window on the market
        threades.transform_obj.focus_at((3200,2600)) # Replace this with the coordinates ofthe market in the base surface

        # Calculating position and size of window from the size of the threades.desktop
        position_win =threades.resize_pos((200.0,50.0))
        size_win =threades.resize_pos((800.0,600.0))

        # Creating window
        self.win = gui.Window(position = position_win, size = size_win, parent = threades.desktop, text = " Buy or Sell Resources " ,style = win_style,shadeable = False, moveable = False)
        self.win.surf.set_alpha(140)
        self.win.onClose = lambda button: self.close_win_safe()
        self.win_flag = True

        # Pausing the update thread
        threades.pause_update_thread()

        # Creating custom label style1
        myfont2 = pygame.font.Font("font.ttf",threades.resize_pt(16))
        labelstyle1 = gui.defaultLabelStyle.copy()
        labelstyle1['border-width'] = 0
        labelstyle1['wordwrap'] = False
        labelstyle1['autosize'] = True
        labelstyle1['font'] = myfont2
        labelstyle1['font-color'] = self.rect_color

        heading_label1 = gui.Label(position = threades.resize_pos((10.0,70.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Resources', style = labelstyle1)
        heading_label2 = gui.Label(position = threades.resize_pos((180.0,70.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Village', style = labelstyle1)
        heading_label3 = gui.Label(position = threades.resize_pos((180.0,85.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Quantity', style = labelstyle1)
        heading_label4 = gui.Label(position = threades.resize_pos((370.0,70.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Price', style = labelstyle1)
        #heading_label5 = gui.Label(position = threades.resize_pos((520.0,70.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Resources', style = labelstyle1)
        heading_label6 = gui.Label(position = threades.resize_pos((270.0,70.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Market', style = labelstyle1)
        heading_label7 = gui.Label(position = threades.resize_pos((270.0,85.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Quantity', style = labelstyle1)

        # creating custom style for option box
        op_style = gui.defaultOptionBoxStyle.copy()
        op_style['font'] = myfont2
        op_style['font-color'] = self.rect_color
        op_style['autosize'] = True
        op_style['word wrap'] = False
        op_style['normal'] = True
        self.op_style = op_style

        # Creating option boxes for all the resources
        position_optionbox = threades.resize_pos((10.0,140.0),(800.0,600.0),self.win.size)
        self.water_box = gui.OptionBox(position = position_optionbox, parent = self.win, style = op_style, text = 'Water')
        self.water_box.onValueChanged = self.onOptionSelect
        self.buildmat_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, style = op_style, text = 'Bricks')
        self.buildmat_box.onValueChanged = self.onOptionSelect
        self.tools_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, style = op_style, text = 'Tools')
        self.tools_box.onValueChanged = self.onOptionSelect
        self.books_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, style = op_style, text = 'Books')
        self.books_box.onValueChanged = self.onOptionSelect
        self.medicine_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, style = op_style, text = 'Medicines')
        self.medicine_box.onValueChanged = self.onOptionSelect
        self.rice_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, style = op_style, text = 'Rice')
        self.rice_box.onValueChanged = self.onOptionSelect
        self.wheat_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, style = op_style, text = 'Fruit & Vegetables')
        self.wheat_box.onValueChanged = self.onOptionSelect
        self.beans_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, style = op_style, text = 'Beans')
        self.beans_box.onValueChanged = self.onOptionSelect
        self.sugar_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, style = op_style, text = 'Sugar')
        self.sugar_box.onValueChanged = self.onOptionSelect
        self.salt_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, style = op_style, text = 'Salt')
        self.salt_box.onValueChanged = self.onOptionSelect
        self.oil_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, style = op_style, text = 'Oil')
        self.oil_box.onValueChanged = self.onOptionSelect
        
        #Creating CheckBox style
        ch_style = gui.defaultCheckBoxStyle.copy()
        ch_style['font'] = myfont2
        ch_style['font-color'] = self.rect_color
        ch_style['autosize'] = True
        #ch_style['word wrap'] = False

        self.barObject = marketBarChart()
        self.barObject.drawValueChart(self.win.surf)

        if model.FLAG_XO:

            if game_sharing.test_connected():

                #Creating Checkbox for share trade with peer villages
                self.shareCheckBox = gui.CheckBox(position = threades.resize_pos((440, 140), (800, 600), self.win.size),  parent = self.win,  style = ch_style,  text = 'Trade with Peer Villages' )
                self.shareCheckBox.value = False
                self.shareCheckBox.onValueChanged = self.drawPriceChart()



        # Creating labels for village values of Resources
        self.label_vwater = gui.Label(position = threades.resize_pos((190.0,140.0),(800.0,600.0),self.win.size), parent = self.win, text = str(int(model.Water.get_vquantity())), style = labelstyle1)
        self.label_vbuildmat = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Buildmat.get_vquantity())), style = labelstyle1)
        self.label_vtools = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Tools.get_vquantity())), style = labelstyle1)
        self.label_vbooks = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Book.get_vquantity())), style = labelstyle1)
        self.label_vmedicine = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Medicine.get_vquantity())), style = labelstyle1)
        self.label_vrice = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Rice.get_vquantity())), style = labelstyle1)
        self.label_vwheat = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Wheat.get_vquantity())), style = labelstyle1)
        self.label_vbeans = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Beans.get_vquantity())), style = labelstyle1)
        self.label_vsugar = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Sugar.get_vquantity())), style = labelstyle1)
        self.label_vsalt = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Salt.get_vquantity())), style = labelstyle1)
        self.label_voil = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Oil.get_vquantity())), style = labelstyle1)

        #Creating labels for value and price of resources
        self.label_res_price_flag = False
        self.label_res_value = gui.Label(position = threades.resize_pos((650.0,200.0),(800.0,600.0),self.win.size), parent = self.win, text = str(int(self.barObject.bar1Val)), style = labelstyle1)

        #Creating a label for value to be printed
        self.label_quantity = gui.Label(position = threades.resize_pos((440.0,170.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Quantity ', style = labelstyle1)

        if model.FLAG_XO:
            if game_sharing.test_connected():
                if self.shareCheckBox.value:
                    self.label_price = gui.Label(position = threades.resize_pos((400.0,250.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Price ', style = labelstyle1)
                    self.label_res_price = gui.Label(position = threades.resize_pos((650.0,280.0),(800.0,600.0),self.win.size), parent = self.win, text = str(int(self.barObject.bar2Val)), style = labelstyle1)

        # Creating labels for prices of Resources
        self.price_vwater = gui.Label(position = threades.resize_pos((370.0,140.0),(800.0,600.0),self.win.size), parent = self.win, text = str(int(model.Water.get_price())), style = labelstyle1)
        self.price_vbuildmat = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Buildmat.get_price())), style = labelstyle1)
        self.price_vtools = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Tools.get_price())), style = labelstyle1)
        self.price_vbooks = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Book.get_price())), style = labelstyle1)
        self.price_vmedicine = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Medicine.get_price())), style = labelstyle1)
        self.price_vrice = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Rice.get_price())), style = labelstyle1)
        self.price_vwheat = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Wheat.get_price())), style = labelstyle1)
        self.price_vbeans = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Beans.get_price())), style = labelstyle1)
        self.price_vsugar = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Sugar.get_price())), style = labelstyle1)
        self.price_vsalt = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Salt.get_price())), style = labelstyle1)
        self.price_voil = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Oil.get_price())), style = labelstyle1)

        '''
        # Creating a textbox to enter the quantity to buy or sell
        textbox_style = gui.defaultTextBoxStyle.copy()
        textbox_style['font'] = myfont2
        textbox_style['font-color'] = self.rect_color
        self.label_quantity = gui.Label(position = threades.resize_pos((360.0,150.0),(800.0,600.0),self.win.size), parent = self.win, text = ' Quantity ', style = labelstyle1)
        self.win.textbox = TextBox(position = threades.resize_pos((350.0, 200.0),(800.0,600.0),self.win.size), size = threades.resize_pos((100,20),(800.0,600.0),self.win.size), parent = self.win, style = textbox_style)
        '''

        #Creating new button style
        buttonsurf = pygame.image.load(os.path.join('art','button.png')).convert_alpha()
        buttonsurf = pygame.transform.scale(buttonsurf, (36, threades.resize_pt_y( 40)))
        button_style = gui.createButtonStyle(myfont,(0,0,0), buttonsurf,4,1,4,4,1,4,4,1,4,4,1,4)

        self.button_buy = gui.Button(position = threades.resize_pos((560.0,350.0),(800.0,600.0),size_win), size = threades.resize_pos((100.0,50.0),(800.0,600.0),size_win), parent = self.win, text = " Buy ",style = button_style)
        self.button_sell = gui.Button(position = threades.resize_pos((460.0,350.0),(800.0,600.0),size_win), size = threades.resize_pos((100.0,50.0),(800.0,600.0),size_win), parent = self.win, text = " Sell ",style = button_style)
        self.button_close = gui.Button(position = threades.resize_pos((650.0,500.0),(800.0,600.0),size_win), size = threades.resize_pos((120.0,50.0),(800.0,600.0),size_win), parent = self.win, text = "Close",style = button_style)
        self.button_buy.onClick = self.buy_resources
        self.button_sell.onClick = self.sell_resources
        self.button_close.onClick  = self.close_win

        # Creating labels for market values of Resources
        self.label_mwater = gui.Label(position = threades.resize_pos((270.0,140.0),(800.0,600.0),self.win.size), parent = self.win, text = str(int(model.Water.get_mquantity())), style = labelstyle1)
        self.label_mbuildmat = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Buildmat.get_mquantity())), style = labelstyle1)
        self.label_mtools = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Tools.get_mquantity())), style = labelstyle1)
        self.label_mbooks = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Book.get_mquantity())), style = labelstyle1)
        self.label_mmedicine = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Medicine.get_mquantity())), style = labelstyle1)
        self.label_mrice = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Rice.get_mquantity())), style = labelstyle1)
        self.label_mwheat = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Wheat.get_mquantity())), style = labelstyle1)
        self.label_mbeans = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Beans.get_mquantity())), style = labelstyle1)
        self.label_msugar = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Sugar.get_mquantity())), style = labelstyle1)
        self.label_msalt = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Salt.get_mquantity())), style = labelstyle1)
        self.label_moil = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Oil.get_mquantity())), style = labelstyle1)



        # Creating label to display the status messages
        #  Creating Custom label style
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 1
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont2
        labelStyleCopy['font-color'] = self.rect_color

        text = 'Welcome to the market of SHEYLAN, where you can trade resources. Select which item you would like to buy or sell on the left-hand column, enter the amount, and then choose buy or sell'
        self.message_label = gui.Label(position = threades.resize_pos((80,470),(800.0,600.0),self.win.size),size = threades.resize_pos((500,100),(800.0,600.0),self.win.size), parent = self.win, text = text, style = labelStyleCopy)

    def updateMarketLabelValues(self,button = None):
        self.label_res_value.text = str(int(self.barObject.bar1Val))
        if model.FLAG_XO:

            if game_sharing.test_connected():
                if self.shareCheckBox.value:
                    self.label_res_price.text = str(int(self.barObject.bar2Val))

    def onOptionSelect(self,button= None):
        
        font_color = (50,200,23)
        myfont2 = pygame.font.Font("font.ttf",threades.resize_pt(16))
        # creating custom style for option box
        op_style = gui.defaultOptionBoxStyle.copy()
        op_style['font'] = myfont2
        op_style['font-color'] = font_color
        op_style['autosize'] = True
        op_style['word wrap'] = False
        op_style['normal'] = False
        
        if not self.water_box.style['normal']:
            self.water_box.style = self.op_style
        if not self.buildmat_box.style['normal']:
            self.buildmat_box.style = self.op_style
        if not self.tools_box.style['normal']:
            self.tools_box.style = self.op_style
        if not self.books_box.style['normal']:
            self.books_box.style = self.op_style
        if not self.medicine_box.style['normal']:
            self.medicine_box.style = self.op_style
        if not self.rice_box.style['normal']:
            self.rice_box.style = self.op_style
        if not self.wheat_box.style['normal']:
            self.wheat_box.style = self.op_style
        if not self.beans_box.style['normal']:
            self.beans_box.style = self.op_style
        if not self.sugar_box.style['normal']:
            self.sugar_box.style = self.op_style
        if not self.salt_box.style['normal']:
            self.salt_box.style = self.op_style
        if not self.oil_box.style['normal']:
            self.oil_box.style = self.op_style
        
        button.style = op_style
            
    def drawPriceChart(self,button = None):

        # Creating custom label style1
        if model.FLAG_XO:

            if game_sharing.test_connected():
                if self.shareCheckBox.value:
                    myfont2 = pygame.font.Font("font.ttf",threades.resize_pt(16))
                    labelstyle1 = gui.defaultLabelStyle.copy()
                    labelstyle1['border-width'] = 0
                    labelstyle1['wordwrap'] = False
                    labelstyle1['autosize'] = True
                    labelstyle1['font'] = myfont2
                    labelstyle1['font-color'] = self.rect_color
                    #print self.shareCheckBox.value


                    self.barObject.drawPriceChart(self.win.surf)
                    if not self.label_res_price_flag:
                        self.label_price = gui.Label(position = threades.resize_pos((440.0,250.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Price ', style = labelstyle1)
                        self.label_res_price = gui.Label(position = threades.resize_pos((650.0,280.0),(800.0,600.0),self.win.size), parent = self.win, text = str(int(self.barObject.bar2Val)), style = labelstyle1)
                        self.label_res_price_flag = True

                else:
                    self.barObject.deletePriceChart()


    def buy_resources(self,button):
        ''' Initiated for doing the transaction of buying the resources
        '''
        # Checking whether the user has entered the value in text box properly
        quantity = self.barObject.bar1Val
        if int(quantity) == 0:
            self.message_label.text = "The quantity needs to be more than zero."
            return
        price = 0
        if model.FLAG_XO:
            if game_sharing.test_connected() and self.shareCheckBox.value:
                price = int(self.barObject.bar2Val)

        label_text = self.message_label.text
        # Checking whether the user has selected the appropriate option box for the resource or not, and do the appropriate action
        if self.water_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Water,quantity,price)
            else:
                label_text =  threades.buy_res(model.Water,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_vwater.text = str(int(model.Water.get_vquantity()))
                    self.label_mwater.text = str(int(model.Water.get_mquantity()))
        elif self.buildmat_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Buildmat,quantity,price)
            else:
                label_text =  threades.buy_res(model.Buildmat,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_vbuildmat.text = str(int(model.Buildmat.get_vquantity()))
                    self.label_mbuildmat.text = str(int(model.Buildmat.get_mquantity()))
        elif self.tools_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Tools,quantity,price)
            else:
                label_text =  threades.buy_res(model.Tools,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_vtools.text = str(int(model.Tools.get_vquantity()))
                    self.label_mtools.text = str(int(model.Tools.get_mquantity()))
        elif self.medicine_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Medicine,quantity,price)
            else:
                label_text =  threades.buy_res(model.Medicine,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_vmedicine.text = str(int(model.Medicine.get_vquantity()))
                    self.label_mmedicine.text = str(int(model.Medicine.get_mquantity()))
        elif self.books_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Books,quantity,price)
            else:
                label_text =  threades.buy_res(model.Book,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_vbooks.text = str(int(model.Book.get_vquantity()))
                    self.label_mbooks.text = str(int(model.Book.get_mquantity()))
        elif self.rice_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Rice,quantity,price)
            else:
                label_text =  threades.buy_res(model.Rice,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_vrice.text = str(int(model.Rice.get_vquantity()))
                    self.label_mrice.text = str(int(model.Rice.get_mquantity()))
        elif self.wheat_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Wheat,quantity,price)
            else:
                label_text =  threades.buy_res(model.Wheat,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_vwheat.text = str(int(model.Wheat.get_vquantity()))
                    self.label_mwheat.text = str(int(model.Wheat.get_mquantity()))
        elif self.beans_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Beans,quantity,price)
            else:
                label_text =  threades.buy_res(model.Beans,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_vbeans.text = str(int(model.Beans.get_vquantity()))
                    self.label_mbeans.text = str(int(model.Beans.get_mquantity()))
        elif self.sugar_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Sugar,quantity,price)
            else:
                label_text =  threades.buy_res(model.Sugar,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_vsugar.text = str(int(model.Sugar.get_vquantity()))
                    self.label_msugar.text = str(int(model.Sugar.get_mquantity()))
        elif self.salt_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Salt,quantity,price)
            else:
                label_text =  threades.buy_res(model.Salt,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_vsalt.text = str(int(model.Salt.get_vquantity()))
                    self.label_msalt.text = str(int(model.Salt.get_mquantity()))
        elif self.oil_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Oil,quantity,price)
            else:
                label_text =  threades.buy_res(model.Oil,quantity)
                if label_text == 'The Village has bought the resource you demanded':
                    self.label_voil.text = str(int(model.Oil.get_vquantity()))
                    self.label_moil.text = str(int(model.Oil.get_mquantity()))
        else:
            label_text = ' Please select a Resource for Trading'

        self.message_label.text = label_text




    def sell_resources(self,button):
        ''' Initiated for doing the transaction of buying the resources
        '''
        # Checking whether the user has entered the value in text box properly
        quantity = self.barObject.bar1Val
        if int(quantity) == 0:
            self.message_label.text = "The quantity needs to be more than zero."
            return
        price = 0
        if model.FLAG_XO:
            if game_sharing.test_connected() and self.shareCheckBox.value:
                price = int(self.barObject.bar2Val)

        label_text = self.message_label.text
        # Checking whether the user has selected the appropriate option box for the resource or not, and do the appropriate action
        if self.water_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Water,quantity,price)
            else:
                label_text =  threades.sell_res(model.Water,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_vwater.text = str(int(model.Water.get_vquantity()))
                    self.label_mwater.text = str(int(model.Water.get_mquantity()))
        elif self.buildmat_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Buildmat,quantity,price)
            else:
                label_text =  threades.sell_res(model.Buildmat,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_vbuildmat.text = str(int(model.Buildmat.get_vquantity()))
                    self.label_mbuildmat.text = str(int(model.Buildmat.get_mquantity()))
        elif self.tools_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Tools,quantity,price)
            else:
                label_text =  threades.sell_res(model.Tools,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_vtools.text = str(int(model.Tools.get_vquantity()))
                    self.label_mtools.text = str(int(model.Tools.get_mquantity()))
        elif self.medicine_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Medicine,quantity,price)
            else:
                label_text =  threades.sell_res(model.Medicine,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_vmedicine.text = str(int(model.Medicine.get_vquantity()))
                    self.label_mmedicine.text = str(int(model.Medicine.get_mquantity()))
        elif self.books_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Books,quantity,price)
            else:
                label_text =  threades.sell_res(model.Book,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_vbooks.text = str(int(model.Book.get_vquantity()))
                    self.label_mbooks.text = str(int(model.Book.get_mquantity()))
        elif self.rice_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Rice,quantity,price)
            else:
                label_text =  threades.sell_res(model.Rice,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_vrice.text = str(int(model.Rice.get_vquantity()))
                    self.label_mrice.text = str(int(model.Rice.get_mquantity()))
        elif self.wheat_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Wheat,quantity,price)
            else:
                label_text =  threades.sell_res(model.Wheat,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_vwheat.text = str(int(model.Wheat.get_vquantity()))
                    self.label_mwheat.text = str(int(model.Wheat.get_mquantity()))
        elif self.beans_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Beans,quantity,price)
            else:
                label_text =  threades.sell_res(model.Beans,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_vbeans.text = str(int(model.Beans.get_vquantity()))
                    self.label_mbeans.text = str(int(model.Beans.get_mquantity()))
        elif self.sugar_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Sugar,quantity,price)
            else:
                label_text =  threades.sell_res(model.Sugar,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_vsugar.text = str(int(model.Sugar.get_vquantity()))
                    self.label_msugar.text = str(int(model.Sugar.get_mquantity()))
        elif self.salt_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Salt,quantity,price)
            else:
                label_text =  threades.sell_res(model.Salt,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_vsalt.text = str(int(model.Salt.get_vquantity()))
                    self.label_msalt.text = str(int(model.Salt.get_mquantity()))
        elif self.oil_box.value:
            if model.FLAG_XO and game_sharing.test_connected() and self.shareCheckBox.value:
                initiateTrade(True,model.Oil,quantity,price)
            else:
                label_text =  threades.sell_res(model.Oil,quantity)
                if label_text == 'The Village has sold the resource you demanded':
                    self.label_voil.text = str(int(model.Oil.get_vquantity()))
                    self.label_moil.text = str(int(model.Oil.get_mquantity()))
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


class showInstructions:
    
    def __init__(self):
    
        self.text = ""
        self.winFlag = False
    
    def addMessage(self,text= None, flag = False):
        
        if text:
            self.text = text
         
        if self.winFlag:
            sleep(2)
            self.winFlag = False
            
        self.showMessage(flag)
            
    def showMessage(self,flag = False):
        
        #print "flag is ",flag," text is ",self.text
        
        self.winFlag = True
        font_color = (100,200,200)
        myfont = pygame.font.Font("font.ttf", threades.resize_pt(17))
        # Custom gui.Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont
        win_style['bg-color'] = (0,0,0)
        win_style['font-color'] = font_color
        
        # Calculating position and size of window from the size of the threades.desktop
        position_win =threades.resize_pos((20.0,42.0))
        size_win =threades.resize_pos((700.0,200.0))
    
        # Creating custom label style for the text to be displayed as a threades.message
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont
        labelStyleCopy['font-color'] = font_color
    
        # Creating window
        win = gui.Window(position = position_win, size = size_win, parent = threades.desktop, text = "Current Objective" ,style = win_style ,closeable = False ,shadeable = False,moveable = False)
        pygame.draw.rect(win.surf,font_color,threades.resize_rect((3,3,695,195)),1)            
        
        # Creating label
        message_label = gui.Label(position = threades.resize_pos((5,50),(690.0,190.0),win.size),size = threades.resize_pos((500,50),(500.0,10.0),win.size), parent = win, text = self.text, style = labelStyleCopy)
        length = len(self.text)
        length = length/50 + 4
        sleep(length)
        win.close()
        if flag:
            event = game_events.Event(type = game_events.ACTIONCOMPLETEEVENT, facility_name = '', res_name = '' , res_quantity = 0)
            game_events.EventQueue.add(event)
        
showMessages = showInstructions()

class gui_buttons:

    rect_color = (255,214,150)
    color_grey = (160,160,160)

    def initialize(self):
        ''' Initialises the buttons for setting up facility, upgrading it and for buy/sell operations
        '''
        myfont = pygame.font.Font("font.ttf", threades.resize_pt(17))

        self.instruction_text = ""
        #Creating new button style
        buttonsurf = pygame.image.load(os.path.join('art','button.png')).convert_alpha()
        buttonsurf = pygame.transform.scale(buttonsurf, (36, threades.resize_pt_y( 40)))
        button_style = gui.createButtonStyle(myfont,(0,0,0), buttonsurf,4,1,4,4,1,4,4,1,4,4,1,4)
        button_style['font'] = myfont

        self.setup_button = gui.Button(position = threades.resize_pos((7,859)), size = threades.resize_pos((290,25)), parent = threades.desktop, text = "Build",style = button_style)
        self.upgrade_button = gui.Button(position = threades.resize_pos((307,859)), size = threades.resize_pos((290,25)), parent = threades.desktop, text = "Upgrade",style = button_style)
        self.buysell_button = gui.Button(position = threades.resize_pos((607,859)), size = threades.resize_pos((290,25)), parent = threades.desktop, text = "Market",style = button_style)

        #Creating new button style
        buttonsurf = pygame.image.load(os.path.join('art','button.png')).convert_alpha()
        buttonsurf = pygame.transform.scale(buttonsurf, (36, threades.resize_pt_y(30)))
        button_style = gui.createButtonStyle(myfont,(0,0,0), buttonsurf,4,1,4,4,1,4,4,1,4,4,1,4)
        button_style['font'] = myfont
        self.instructions_button = gui.Button(position = threades.resize_pos((1000,10)), size = threades.resize_pos((190,25)), parent = threades.desktop, text = "Current Objective",style = button_style)

        self.setup_obj = setup_button()
        self.upgrade_obj = upgrade_button()
        self.buysell_obj = buysell_button()
        self.setup_button.onClick = self.setup_obj.setup
        self.upgrade_button.onClick = self.upgrade_obj.upgrade
        self.buysell_button.onClick = self.buysell_obj.buysell
        self.instructions_button.onClick = self.showInstruction
        self.win_flag = False
        self.child_win_flag = False

    
    def showInstruction(self, button = None):
    
        thread_instruction = threading.Thread(target = showMessages.addMessage, args=[]).start()
        
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
        threades.transform_obj.stop_mouse_move()
        threades.total_update_flag = True

        self.setup_button.enabled = False
        self.upgrade_button.enabled = False
        self.buysell_button.enabled = False

    def enable_buttons(self):

        threades.resume_update_thread()

        # resume mouse motion
        threades.transform_obj.resume_mouse_move()

        self.win_flag = False

        self.setup_button.enabled = True
        self.upgrade_button.enabled = True
        self.buysell_button.enabled = True
        threades.total_update_flag = True





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
    if not buysell:
        cost  = quantity*price
        if cost > model.money.get_money():
            gui_obj.buysell_obj.message_label.text = " Village doesn't have enough money to buy the resources"
            return
        game_sharing.broadcast_msg(['Trade',resource.get_name(),str(quantity),str(price),'sell'])
        game_sharing.setUnicastTradingFlag('sell')
    else:
        if quantity > resource.get_vquantity():
            gui_obj.buysell_obj.message_label.text = " There are not enough resources in the village to trade"
            return
        game_sharing.broadcast_msg(['Trade',resource.get_name(),str(quantity),str(price),'buy'])
        game_sharing.setUnicastTradingFlag('buy')

    if gui_obj.buysell_obj.get_win_flag():
        gui_obj.buysell_obj.close_win()



