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

import pygame
from pygame.locals import *
from sys import exit
import os
from time import *
from threades import *
import threades
import threading
import gui
from gui import *
import defaultStyle
from load_images import *
from display_panel import *
from gui_buttons import *



    


desktop2 = Desktop()
def message_window():
    ''' Thread to display the messages'''

    font_color = (255,214,150)
    myfont = pygame.font.Font("font.ttf", resize_pt(17))
    # Custom Window Style
    win_style = gui.defaultWindowStyle.copy()
    win_style['font'] = myfont
    win_style['bg-color'] = (0,0,0)
    
    # Calculating position and size of window from the size of the desktop
    position_win =resize_pos((745.0,42.0))
    size_win =resize_pos((450.0,150.0))

    # Creating custom label style for the text to be displayed as a message
    labelStyleCopy = gui.defaultLabelStyle.copy()
    labelStyleCopy['wordwrap'] = True
    labelStyleCopy['autosize'] = False
    labelStyleCopy['font'] = myfont
    #labelStyleCopy['font-color'] = font_color

    while True:
        (text,color) = message.pop_message()
        if text:

            # Creating window
            win_style['font-color'] = color
            labelStyleCopy['font-color'] = color

            win = Window(position = position_win, size = size_win, parent = desktop, text = "Message " ,style = win_style ,closeable = False ,shadeable = False,moveable = False)
            pygame.draw.rect(win.surf,color,resize_rect((3,3,444,144)),1)            
            #win.surf.set_alpha(160)
            # Creating label
            message_label = Label(position = resize_pos((5,50),(450.0,150.0),win.size),size = resize_pos((440,140),(450.0,150.0),win.size), parent = win, text = text, style = labelStyleCopy)
            sleep(6)
            win.close()
        sleep(2)









class Earthquake(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        mask= pygame.surface.Surface((1200,560),SRCALPHA)
        mask.fill((0,0,0))
        mask.set_alpha(0)
        self.alpha = 0
        self.image = mask
        self.rect = self.image.get_rect()
        self.rect.move((0,0))
        self.counter = 0
        self.prev_disp = (0,0)
        self.move_dir = [(-20,-20),(-20,-10),(-20,0),(-20,10),(-20,20),(-10,-20),(-10,-20),(-10,0),(-10,10),(-10,20),(0,-20),(0,-10),(0,0),(0,10),(0,20),(10,-20),(10,-20),(10,0),(10,10),(10,20),(20,-20),(20,-10),(20,0),(20,10),(20,20)]
        # To close all open windows
        if gui_obj.get_child_win_flag():
            escape()
            escape()
        elif gui_obj.get_win_flag():
            escape()

    def update(self):

        global Hospital
        global House
        global School
        global Workshop
        global ppl


        self.counter +=1
        if self.counter <50:
            transform_obj.move_free((-self.prev_disp[0],-self.prev_disp[1]))
            self.prev_disp = self.move_dir[int(random.random()*25)]
            transform_obj.move_free(self.prev_disp)
        if self.counter >20 and self.counter <50:
            self.alpha +=8
            self.image.set_alpha(self.alpha)
        if self.counter==40:
            display_text = ' Your Village Sheylan has ben hit by an Earthquake'
            message.push_message(display_text,'high')
        if self.counter == 80:
            display_earthquake_images()
            demolish_facility('Hospital')
            demolish_facility('House')
            demolish_facility('House')
            demolish_facility('House')
            demolish_facility('School')
            demolish_facility('Workshop')
            ppl.change_total_population(-10)
        if self.counter > 81:
            if self.alpha >2:
                self.alpha -=2
            self.image.set_alpha(self.alpha)
        if self.counter >180:
            natural_calamities.remove(earthquake)

def display_earthquake_images():

    image1 = pygame.image.load(os.path.join('data', 'earthquake1.png')).convert()
    screen.blit(pygame.transform.scale(image1,new_screen_size),(0,0))
    pygame.display.flip()
    sleep(3)

    image2 = pygame.image.load(os.path.join('data', 'earthquake2.png')).convert()
    screen.blit(pygame.transform.scale(image2,new_screen_size),(0,0))
    pygame.display.flip()
    sleep(3)

    image3 = pygame.image.load(os.path.join('data', 'earthquake3.png')).convert()
    screen.blit(pygame.transform.scale(image3,new_screen_size),(0,0))
    pygame.display.flip()
    sleep(3)

earthquake = None
def earthquake():
    ''' This method needs to be called when there is an earthquake in the
    village, it decreases the number of installations of some facilities and
    also reduce the population
    '''
    global earthquake

    earthquake  = Earthquake()
    natural_calamities.add(earthquake)


def load_sound(name):

    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join(name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:

        raise SystemExit, message
    return sound

def escape():

    win_flag = gui_obj.get_win_flag()
    child_win_flag = gui_obj.get_child_win_flag()
    if child_win_flag:
        gui_obj.close_child_win()
    elif win_flag:
        gui_obj.close_win()
    else:
        pause_screen(False)

def safe_exit(button = None):

    soundtrack.stop()
    pygame.mixer.quit()
    pygame.quit()
    exit()



clock = pygame.time.Clock()


def event_handling(e):
    if e.type == pygame.QUIT:
        safe_exit()
    if e.type == QUIT:
        safe_exit()
    if e.type == KEYDOWN:
        if e.key == 27:  # For escape key
            escape()
        if e.key == K_UP:
            transform_obj.start_move('up')
        if e.key == K_DOWN:
            transform_obj.start_move('down')
        if e.key == K_LEFT:
            transform_obj.start_move('left')
        if e.key == K_RIGHT:
            transform_obj.start_move('right')
        if e.key == K_f or e.key == 61:
            transform_obj.focus()
        if e.key == K_d or e.key == 45:
            transform_obj.defocus()
        if e.key == K_RETURN:
            gui_obj.press_enter()

        win_flag = gui_obj.get_win_flag()
        if not win_flag:
            if e.key == K_s:
                gui_obj.setup_obj.setup()
            if e.key == K_u:
                gui_obj.upgrade_obj.upgrade()
            if e.key == K_b:
                gui_obj.buysell_obj.buysell()
            if e.key == K_e:
                earthquake()

    if e.type == KEYUP:
        if e.key == K_UP:
            transform_obj.stop_move('up')
        if e.key == K_DOWN:
            transform_obj.stop_move('down')
        if e.key == K_LEFT:
            transform_obj.stop_move('left')
        if e.key == K_RIGHT:
            transform_obj.stop_move('right')

    x,y = pygame.mouse.get_pos()
    r = pygame.Rect(resize_rect((0,40,930,560)))
    if gui_obj.buysell_obj.get_win_flag():
        gui_obj.buysell_obj.drawPriceChart()
    if r.collidepoint(x,y):
        
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1 and gui_obj.get_child_win_flag():
                gui_obj.setup_obj.bardisplay.updateChart((x,y))
            if e.button == 1 and gui_obj.buysell_obj.get_win_flag():
                gui_obj.buysell_obj.barObject.updateChart((x,y))
            if e.button == 4:
                transform_obj.focus()
            if e.button == 5:
                transform_obj.defocus()

soundtrack = load_sound(os.path.join('data', 'soundtrack.ogg'))

def get_update_region():
    # Function which returns the regions to be updated
    
    list_rects = []
    if total_update_flag:
        screen.blit(surface_top,(0,0))
        pygame.draw.rect(screen,(0,0,0),resize_rect((0,600,1200,300)))
        list_rects.append(pygame.Rect(resize_pos((0,0)),resize_pos((1200,900))))
        return list_rects
    
    list_rects.append(pygame.Rect(resize_pos((0,40)),resize_pos((930,560))))
                      
    if (panel.ind.update_flag or panel.man.update_flag or panel.res.update_flag or panel_update_flag):
        pygame.draw.rect(screen,(0,0,0),resize_rect((0,600,1200,300)))
        list_rects.append(pygame.Rect(resize_pos((0,600)),resize_pos((1200,300))))
    
    if panel.map.update_flag or map_update_flag:
        list_rects.append(pygame.Rect(resize_pos((930,390)),resize_pos((270,210))))
        
    if panel.res.money_flag or top_update_flag:
        screen.blit(surface_top,(0,0))
        list_rects.append(pygame.Rect((0,0),resize_pos((1200,40))))
        
    if panel.fac.update_flag or facilities_update_flag:
        list_rects.append(pygame.Rect(resize_pos((930,40)),resize_pos((270,350))))
        
    return list_rects

    

class starting_intro:
    ''' Display the starting intro_text and menu
    '''

    def main_menu(self,pause_flag = True):
        ''' Display the starting menu
        '''

        logo = pygame.image.load(os.path.join('data', 'logo.png')).convert()
        self.ff_logo = pygame.transform.scale(logo,resize_pos((1111,250)))
        screen.fill((0,0,0))
        screen.blit(self.ff_logo,resize_pos((40,50)))

        # Font type
        myfont = pygame.font.Font("font.ttf", resize_pt(17))

        # Creating new button style
        buttonsurf = pygame.image.load(os.path.join('art','button_green.png')).convert_alpha()
        self.button_style = gui.createButtonStyle(myfont,(0,0,0), buttonsurf,4,1,4,4,1,4,4,1,4,4,1,4)

        self.pause_flag = pause_flag
        if self.pause_flag:
            self.start_button = Button(position = resize_pos((500,500)), size = resize_pos((200,30)), parent = desktop2, text = "Start New Game",style = self.button_style)
            self.start_button.onClick = self.startup_text
        else:
            self.resume_button = Button(position = resize_pos((500,500)), size = resize_pos((200,30)), parent = desktop2, text = "Resume Game",style = self.button_style)
            self.resume_button.onClick = self.resume

    #self.resume_button = Button(position = resize_pos((500,550)), size = resize_pos((200,30)), parent = desktop, text = "Resume Game",style = self.button_style)
        self.controls_button = Button(position = resize_pos((500,550)), size = resize_pos((200,30)), parent = desktop2, text = "Controls",style = self.button_style)
        self.exit_button = Button(position = resize_pos((500,600)), size = resize_pos((200,30)), parent = desktop2, text = "Exit",style = self.button_style)
        self.instructions_button = Button(position = resize_pos((800,20)), size = resize_pos((150,30)), parent = desktop2, text = "Guide",style = self.button_style)
        self.about_us_button = Button(position = resize_pos((1000,20)), size = resize_pos((150,30)), parent = desktop2, text = "About Us",style = self.button_style)
        
                                      
        #self.resume_button.onClick = self.resume
        self.controls_button.onClick = self.controls
        self.exit_button.onClick = safe_exit
        
        self.instructions_button.onClick = self.instructionsWindow
        self.about_us_button.onClick = self.aboutUsWindow

        self.run = True

    def instructionsWindow(self,button = None):
        ''' Opens a window for Instructions
        '''
        
        self.remove_buttons()
        self.lightgreen_color = (0,100,0)
        self.green_color = (0,150,0)
        self.black_color = (0,0,0)
        myfont1 = pygame.font.Font("font.ttf", resize_pt(40))

        # Custom Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont1
        win_style['font-color'] = self.green_color
        win_style['bg-color'] = (0,0,0)
        win_style['border-color'] = (0,150,0)
        # Calculating position and size of window from the size of the desktop
        position_win =resize_pos((150.0,270.0))
        size_win =resize_pos((900.0,600.0))

        # Creating window
        self.win = Window(position = position_win, size = size_win, parent = desktop2, text = "     Guide" , style = win_style, shadeable = False, closeable = False,moveable = False)
        self.win.onClose = lambda button: self.main_menu(self.pause_flag)
        #self.win.surf.set_alpha(140) This seems to be redundant as translucency doesnt seems to work properly

        myfont2 = pygame.font.Font("font.ttf", resize_pt(20))
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 1
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont2
        labelStyleCopy['font-color'] = (0,200,0)
        labelStyleCopy['border-color'] = self.black_color
        
        self.skip_button = Button(position = resize_pos((500,550),(900.0,600.0),self.win.size), size = resize_pos((80,30),(900.0,600.0),self.win.size), parent = self.win, text = "  Skip  ",style = self.button_style)
        self.next_button = Button(position = resize_pos((380,550),(900.0,600.0),self.win.size), size = resize_pos((80,30),(900.0,600.0),self.win.size), parent = self.win, text = "  Next > ",style = self.button_style)
        self.prev_button = Button(position = resize_pos((260,550),(900.0,600.0),self.win.size), size = resize_pos((80,30),(900.0,600.0),self.win.size), parent = self.win, text = "  < Prev  ",style = self.button_style)

        self.next_button.onClick = self.increaseInstructionsCounter
        self.prev_button.onClick = self.decreaseInstructionsCounter
        self.skip_button.onClick = self.close_win
        self.instructions_run = True
        logo =  pygame.image.load(os.path.join('data', 'logo.png')).convert()
        ff_logo = pygame.transform.scale(logo,resize_pos((1111,250)))
        
        self.instructions_counter = 0
        label = Label(position = resize_pos((10.0,100.0),(900.0,600.0),self.win.size),size = resize_pos((880.0,440.0),(900.0,600.0),self.win.size), parent = self.win, text = '', style = labelStyleCopy)

        while self.instructions_run:
            pygame.display.set_caption('FoodForce2')
            screen.fill((0,0,0))
            screen.blit(ff_logo,resize_pos((40,50)))

            label.text = instruction_text[self.instructions_counter]
            for e in gui.setEvents(pygame.event.get()):
                if e.type == KEYDOWN:
                    if e.key == 27:  # For escape key
                        self.instructions_run = False
                        self.win.close()
                    if e.key == K_RIGHT:
                        if self.instructions_counter < len(instruction_text)-1:
                            self.instructions_counter += 1
                    if e.key == K_LEFT:
                        if self.instructions_counter > 0 :
                            self.instructions_counter -= 1

            desktop2.update()
            desktop2.draw()
            pygame.display.update()
            
    def increaseInstructionsCounter(self,button = None):
        if self.instructions_counter < len(instruction_text)-1:
            self.instructions_counter +=1
    
    def decreaseInstructionsCounter(self,button = None):
        if self.instructions_counter > 0 :
            self.instructions_counter -=1
        

            

    def aboutUsWindow(self,button = None):
        ''' Displays the credits
        '''
        
        self.remove_buttons()
        self.lightgreen_color = (0,100,0)
        self.green_color = (0,150,0)
        self.black_color = (0,0,0)
        myfont1 = pygame.font.Font("font.ttf", resize_pt(40))

        # Custom Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont1
        win_style['font-color'] = self.green_color
        win_style['bg-color'] = (0,0,0)
        win_style['border-color'] = (0,150,0)
        # Calculating position and size of window from the size of the desktop
        position_win =resize_pos((150.0,270.0))
        size_win =resize_pos((900.0,600.0))

        # Creating window
        self.win = Window(position = position_win, size = size_win, parent = desktop2, text = "     About Us " , style = win_style, shadeable = False, closeable = False,moveable = False)
        self.win.onClose = lambda button: self.main_menu(self.pause_flag)
        #self.win.surf.set_alpha(140) This seems to be redundant as translucency doesnt seems to work properly

        self.next_button = Button(position = resize_pos((500,650)), size = resize_pos((200,30)), parent = self.win, text = "Next ",style = self.button_style)
        
        myfont2 = pygame.font.Font("font.ttf", resize_pt(20))
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 1
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont2
        labelStyleCopy['font-color'] = (0,200,0)
        labelStyleCopy['border-color'] = self.black_color
        
        self.close_button = Button(position = resize_pos((500,550),(900.0,600.0),self.win.size), size = resize_pos((80,30),(900.0,600.0),self.win.size), parent = self.win, text = "  Close  ",style = self.button_style)
        
        self.close_button.onClick = self.close_win
        self.about_us_run = True
        logo =  pygame.image.load(os.path.join('data', 'logo.png')).convert()
        ff_logo = pygame.transform.scale(logo,resize_pos((1111,250)))
        
        #self.instructions_counter = 0
        label = Label(position = resize_pos((10.0,100.0),(900.0,600.0),self.win.size),size = resize_pos((880.0,440.0),(900.0,600.0),self.win.size), parent = self.win, text = '', style = labelStyleCopy)

        while self.about_us_run:
            pygame.display.set_caption('FoodForce2')
            screen.fill((0,0,0))
            screen.blit(ff_logo,resize_pos((40,50)))

            label.text = about_us_text
            for e in gui.setEvents(pygame.event.get()):
                if e.type == KEYDOWN:
                    if e.key == 27:  # For escape key
                        self.about_us_run = False
                        self.win.close()
         
            desktop2.update()
            desktop2.draw()
            pygame.display.update()
    
    def startup_text(self,button = None):
        ''' Displays the startup text
        '''

        self.remove_buttons()
        screen.fill((255,255,255))
        hunger_map = pygame.image.load(os.path.join('data', 'Wfpwork.png')).convert()
        hunger_map =  pygame.transform.scale(hunger_map,new_screen_size)
        screen.blit(hunger_map,resize_pos((0,0)))

        color_brown = (255,214,150)
        # Window custom style
        myfont = pygame.font.Font("font.ttf", resize_pt(28))
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont
        win_style['font-color'] = color_brown
        win_style['bg-color'] = (0,0,0)
        win_style['border-color'] = color_brown
        position_win =resize_pos((200.0,50.0))
        size_win =resize_pos((800.0,600.0))
        win = Window(position = position_win, size = size_win, parent = desktop2, text = " FOODFORCE II : ESCAPING POVERTY  " ,style = win_style,shadeable = False, closeable = False,moveable = False)
        self.startup_text_run = True
        win.surf.set_alpha(100)
        myfont2 = pygame.font.Font("font.ttf",resize_pt(19))
        labelstyle1 = gui.defaultLabelStyle.copy()
        labelstyle1['border-width'] = 0
        labelstyle1['wordwrap'] = True
        labelstyle1['autosize'] = False
        labelstyle1['font'] = myfont2
        labelstyle1['font-color'] = color_brown

        counter = 0
        label = Label(position = resize_pos((10.0,130.0),(800.0,600.0),win.size),size = resize_pos((780.0,460.0),(800.0,600.0),win.size), parent = win, text = '', style = labelstyle1)
        
        button_style = gui.defaultButtonStyle.copy()
        button_style['font'] = myfont2

        self.skip_button = Button(position = resize_pos((600,550),(800.0,600.0),win.size), size = resize_pos((150,30),(800.0,600.0),win.size), parent = win, text = "  Skip  ",style = button_style)
        self.skip_button.onClick = self.turnoff_startup_run
        threades.global_time = 0
        
        #One time show of the background image
        screen.fill((255,255,255))
        screen.blit(hunger_map,resize_pos((0,0)))
        pygame.display.flip()
        #sleep(5)
        first_display = True
        threades.global_time = 0
        while self.startup_text_run:

            label.text =  trailer_text[counter]
            for e in gui.setEvents(pygame.event.get()):
                if e.type == pygame.QUIT:
                    safe_exit()
                if e.type == KEYDOWN:
                    if e.key == 27:  # For escape key
                        self.startup_text_run = False
                    if e.key == K_RETURN:
                        counter += 1
            
            if threades.global_time >= 5000:
                first_display = False                
                threades.global_time = 0
                counter += 1
            if not first_display:
                
                screen.fill((255,255,255))
                screen.blit(hunger_map,resize_pos((0,0)))
                desktop2.update()
                desktop2.draw()
                pygame.display.flip()
                
            if counter == len(trailer_text):
                self.startup_text_run = False
            
            
            
        
            threades.iteration_time = clock.tick()
            threades.global_time += threades.iteration_time
        win.close()

        
        self.run = False

    def turnoff_startup_run(self,button = None):
        
        self.startup_text_run = False
        
    def resume(self,button = None):
        ''' Resumes Game
        '''
        self.remove_buttons()
        self.run = False

    def controls(self,button = None):
        """"show controllers
        """
        self.remove_buttons()
        self.lightgreen_color = (0,100,0)
        self.green_color = (0,150,0)
        self.black_color = (0,0,0)
        myfont1 = pygame.font.Font("font.ttf", resize_pt(40))

        # Custom Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont1
        win_style['font-color'] = self.green_color
        win_style['bg-color'] = (0,0,0)
        win_style['border-color'] = (0,150,0)
        # Calculating position and size of window from the size of the desktop
        position_win =resize_pos((150.0,270.0))
        size_win =resize_pos((900.0,600.0))

        # Creating window
        self.win = Window(position = position_win, size = size_win, parent = desktop2, text = "     Controls " , style = win_style, shadeable = False, closeable = False)
        self.win.onClose = lambda button: self.main_menu(self.pause_flag)
        self.win.surf.set_alpha(140)

        control_text = """\n\n  Setup Facility           :       s \n\n  Upgrade Facility       :       u \n\n  Buy/Sell                    :       b \n\n  Scroll screen up       :       up arrow \n\n  Scroll screen down   :       down arrow \n\n  Scroll screen left      :       left arrow \n\n  Scroll screen right    :       right arrow """
        myfont2 = pygame.font.Font("font.ttf", resize_pt(25))
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 1
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont2
        labelStyleCopy['font-color'] = self.lightgreen_color
        labelStyleCopy['border-color'] = self.black_color
        self.message_label = Label(position = resize_pos((80,80),(600.0,600.0),self.win.size),size = resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "Setup Facility ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((80,130),(600.0,600.0),self.win.size),size = resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "Upgrade Facility ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((80,180),(600.0,600.0),self.win.size),size = resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "Buy/Sell ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((80,230),(600.0,600.0),self.win.size),size = resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "Scroll Screen up ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((80,280),(600.0,600.0),self.win.size),size = resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "Scroll Screen down", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((80,330),(600.0,600.0),self.win.size),size = resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "Scroll Screen left ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((80,380),(600.0,600.0),self.win.size),size = resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "Scroll Screen right ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((80,430),(600.0,600.0),self.win.size),size = resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "Focus ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((80,480),(600.0,600.0),self.win.size),size = resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "De Focus ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((330,80),(600.0,600.0),self.win.size),size = resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = ": ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((330,130),(600.0,600.0),self.win.size),size = resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = ": ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((330,180),(600.0,600.0),self.win.size),size = resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = ": ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((330,230),(600.0,600.0),self.win.size),size = resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = ": ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((330,280),(600.0,600.0),self.win.size),size = resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = ": ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((330,330),(600.0,600.0),self.win.size),size = resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = ": ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((330,380),(600.0,600.0),self.win.size),size = resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = ": ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((330,430),(600.0,600.0),self.win.size),size = resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = ": ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((330,480),(600.0,600.0),self.win.size),size = resize_pos((10,70),(600.0,600.0),self.win.size), parent = self.win, text = ": ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((350,80),(600.0,600.0),self.win.size),size = resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "s ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((350,130),(600.0,600.0),self.win.size),size = resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "u ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((350,180),(600.0,600.0),self.win.size),size = resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "b ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((350,230),(600.0,600.0),self.win.size),size = resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "up arrow ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((350,280),(600.0,600.0),self.win.size),size = resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "down arrow ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((350,330),(600.0,600.0),self.win.size),size = resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "left arrrow ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((350,380),(600.0,600.0),self.win.size),size = resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "right arrow ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((350,430),(600.0,600.0),self.win.size),size = resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "f ", style = labelStyleCopy)
        self.message_label = Label(position = resize_pos((350,480),(600.0,600.0),self.win.size),size = resize_pos((240,70),(600.0,600.0),self.win.size), parent = self.win, text = "d ", style = labelStyleCopy)

        self.win.surf.set_alpha(255)
        self.ok_button = Button(position = resize_pos((480,550),(600.0,600.0),self.win.size), size = resize_pos((80,30),(600.0,600.0),self.win.size), parent = self.win, text = "  OK  ",style = self.button_style)

        self.ok_button.onClick = self.close_win
        self.controls_run = True
        logo =  pygame.image.load(os.path.join('data', 'logo.png')).convert()
        ff_logo = pygame.transform.scale(logo,resize_pos((1111,250)))
        while self.controls_run:
            pygame.display.set_caption('FoodForce2')
            screen.fill((0,0,0))
            screen.blit(ff_logo,resize_pos((40,50)))

            for e in gui.setEvents(pygame.event.get()):
                if e.type == KEYDOWN:
                    if e.key == 27:  # For escape key
                        self.controls_run = False
                        self.win.close()

            desktop2.update()
            desktop2.draw()
            pygame.display.update()


    def close_win(self,button = None):
        self.win.close()
        self.controls_run = False
        self.instructions_run = False
        self.about_us_run = False

    def remove_buttons(self):
        ''' Removes the buttons from the Desktop
        '''

        win = Window(position = (0,0), size = (100,100), parent = desktop2)
        if self.pause_flag:
            self.start_button._set_parent(win)
        else:
            self.resume_button._set_parent(win)

        self.controls_button._set_parent(win)
        self.exit_button._set_parent(win)
        self.about_us_button._set_parent(win)
        self.instructions_button._set_parent(win)
        win.close()





def pause_screen(pause_flag = True):

    start = starting_intro()

    start.main_menu(pause_flag)
    logo =  pygame.image.load(os.path.join('data', 'logo.png')).convert()
    ff_logo = pygame.transform.scale(logo,resize_pos((1111,250)))
    while start.run:
        pygame.display.set_caption('FoodForce2')
        screen.fill((0,0,0))
        screen.blit(ff_logo,resize_pos((40,50)))
        
        for e in gui.setEvents(pygame.event.get()):
            if e.type == pygame.QUIT:
                safe_exit()
            if e.type == QUIT:
                safe_exit()

        desktop2.update()
        desktop2.draw()
        pygame.display.update()
    total_update_flag = True

wfp_logo = pygame.image.load(os.path.join('data', 'top.png')).convert()
surface_top = pygame.transform.scale(wfp_logo,resize_pos((1200,40)))
   
def main():

    global panel
    
    # Displaying the WFP logo
    intro_thread = threading.Thread(target = load_images, args=[])
    intro_thread.start()
    # Loading and starting the sound play
    soundtrack.play(-1)

    pause_screen()



    intro_thread.join()
    initialize_facilities()

    #surface_middle = pygame.transform.scale(surface3,resize_pos((1200,560)))
    

    initialize_gui()

    screen.fill((0,0,0))
    panel = display_panel()
    animation_obj = Animation()
    animation_obj.update()
    # Starting of the threads
    update_thread = threading.Thread(target = threades.update_turn, args=[]).start()
    message_thread = threading.Thread(target = message_window, args=[]).start()
    mouse_flag = False
        
    # The main infinite loop
    while True:
        #clock.tick()

        mouse_flag = False
            
        (x,y) = (0,0)
        x,y = pygame.mouse.get_pos()
        
        if ((x < new_screen_size[0]) and (x > (new_screen_size[0]-60))):
            transform_obj.move_free((0,0))
            
        if (x < 60 and x > 0):
            transform_obj.move_free((0,0))
            
        if (y < resize_pt_y(900)) and (y > resize_pt_y(840)):
            transform_obj.move_free((0,0))
            
        if ((y < resize_pt_y(60)) and (y > resize_pt_y(0))):
            transform_obj.move_free((0,0))
            
        if (x > resize_pt_x(0)) and (x < resize_pt_x(600)) and (y > resize_pt_y(845)) and (y < resize_pt_y(900)):
            mouse_flag = True
            
        pygame.display.set_caption('FoodForce2')

        for e in gui.setEvents(pygame.event.get()):
            event_handling(e)

        #pygame.draw.rect(screen,(209,169,106),resize_rect((0,40,1200,560)))
        animation_obj.update()


        
        #For middle surface
        #surface_middle = pygame.transform.scale(surface3,resize_pos((1200,560)))
        #screen.blit(surface_middle,resize_pos((0,40)))

        

        
        rects_list = get_update_region()
        panel.update()
        
        if (total_update_flag or map_update_flag or facilities_update_flag or panel_update_flag or panel.res.money_flag):
            desktop.update()
            desktop.draw()
        
        pygame.display.update(rects_list)

        threades.iteration_time = clock.tick()
        threades.global_time += threades.iteration_time


if __name__ == '__main__':
    main()



