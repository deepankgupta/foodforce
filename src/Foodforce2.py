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

    font_color = (160,160,160)
    myfont = pygame.font.Font("font.ttf", resize_pt(20))
    # Custom Window Style
    win_style = gui.defaultWindowStyle.copy()
    win_style['font'] = myfont
    win_style['font-color'] = font_color
    win_style['bg-color'] = (0,0,25)
    # Calculating position and size of window from the size of the desktop
    position_win =resize_pos((745.0,42.0))
    size_win =resize_pos((450.0,150.0))

    # Creating custom label style for the text to be displayed as a message
    labelStyleCopy = gui.defaultLabelStyle.copy()
    labelStyleCopy['wordwrap'] = True
    labelStyleCopy['autosize'] = False
    labelStyleCopy['font'] = myfont
    labelStyleCopy['font-color'] = font_color

    while True:
        (text,color) = message.pop_message()
        if text:

            # Creating window
            win = Window(position = position_win, size = size_win, parent = desktop, text = "Message " ,style = win_style)
            win.surf.set_alpha(160)
            # Creating label
            message_label = Label(position = resize_pos((5,50),(450.0,150.0),win.size),size = resize_pos((445,140),(450.0,150.0),win.size), parent = win, text = text, style = labelStyleCopy)
            sleep(6)
            win.close()
        sleep(1)









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
    r = pygame.Rect(resize_rect((0,40,1200,560)))
    if r.collidepoint(x,y):
        if e.type == MOUSEMOTION:
            if e.buttons == (1,0,0):
                transform_obj.move_mouse(e.rel)

        if e.type == MOUSEBUTTONDOWN:
            if e.button == 4:
                transform_obj.focus()
            if e.button == 5:
                transform_obj.defocus()

soundtrack = load_sound(os.path.join('data', 'soundtrack.ogg'))


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

        #self.resume_button.onClick = self.resume
        self.controls_button.onClick = self.controls
        self.exit_button.onClick = safe_exit

        self.run = True

    def startup_text(self,button = None):
        ''' Displays the startup text
        '''

        self.remove_buttons()
        screen.fill((255,255,255))
        hunger_map = pygame.image.load(os.path.join('data', 'hunger_map.png')).convert()
        hunger_map =  pygame.transform.scale(hunger_map,new_screen_size)
        screen.blit(hunger_map,resize_pos((0,0)))

        # Window custom style
        myfont = pygame.font.Font("font.ttf", resize_pt(28))
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont
        win_style['font-color'] = (255,255,255)
        win_style['bg-color'] = (0,0,0)
        position_win =resize_pos((200.0,50.0))
        size_win =resize_pos((800.0,600.0))
        win = Window(position = position_win, size = size_win, parent = desktop2, text = " FOODFORCE: ESCAPING POVERTY  " ,style = win_style,shadeable = False, closeable = False)
        run = True
        win.surf.set_alpha(100)
        myfont2 = pygame.font.Font("font.ttf",resize_pt(23))
        labelstyle1 = gui.defaultLabelStyle.copy()
        labelstyle1['border-width'] = 0
        labelstyle1['wordwrap'] = False
        labelstyle1['autosize'] = True
        labelstyle1['font'] = myfont2
        labelstyle1['font-color'] = (255,255,255)

        counter = 0
        label = Label(position = resize_pos((10.0,130.0),(800.0,600.0),win.size), parent = win, text = '', style = labelstyle1)

        threades.global_time = 0
        while run:

            for e in gui.setEvents(pygame.event.get()):
                if e.type == pygame.QUIT:
                    safe_exit()
                if e.type == KEYDOWN:
                    if e.key == 27:  # For escape key
                        run = False
            label.text =  trailer_text[counter]
            if threades.global_time >= 5000:
                threades.global_time = 0
                counter += 1
            screen.fill((255,255,255))
            screen.blit(hunger_map,resize_pos((0,0)))
            desktop2.update()
            desktop2.draw()
            pygame.display.flip()
            if counter == 8:
                run = False
            threades.iteration_time = clock.tick()
            threades.global_time += threades.iteration_time
        win.close()


        screen.fill((255,255,255))
        hunger_map = pygame.image.load(os.path.join('data', 'wfp_work.png')).convert()
        hunger_map =  pygame.transform.scale(hunger_map,new_screen_size)
        screen.blit(hunger_map,resize_pos((0,0)))

        win = Window(position = position_win, size = size_win, parent = desktop2, text = " FOODFORCE: INSTRUCTIONS  " ,style = win_style,shadeable = False, closeable = False)
        run = True
        win.surf.set_alpha(160)

        counter = 0
        label = Label(position = resize_pos((10.0,130.0),(800.0,600.0),win.size), parent = win, text = '', style = labelstyle1)

        threades.global_time = 0
        while run:

            for e in gui.setEvents(pygame.event.get()):
                if e.type == pygame.QUIT:
                    safe_exit()
                if e.type == KEYDOWN:
                    if e.key == 27:  # For escape key
                        run = False
            label.text =  instruction_text[counter]
            if threades.global_time >= 17000:
                threades.global_time = 0
                counter += 1
            screen.fill((255,255,255))
            screen.blit(hunger_map,resize_pos((0,0)))
            desktop2.update()
            desktop2.draw()
            pygame.display.flip()
            if counter == 8:
                run = False
            threades.iteration_time = clock.tick()
            threades.global_time += threades.iteration_time
        win.close()
        self.run = False

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
            pygame.display.set_caption(str(int(clock.get_fps())))
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
    	win.close()




def pause_screen(pause_flag = True):

    start = starting_intro()

    start.main_menu(pause_flag)
    logo =  pygame.image.load(os.path.join('data', 'logo.png')).convert()
    ff_logo = pygame.transform.scale(logo,resize_pos((1111,250)))
    while start.run:
        pygame.display.set_caption(str(int(clock.get_fps())))
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


def main():


    # Displaying the WFP logo
    intro_thread = threading.Thread(target = load_images, args=[])
    intro_thread.start()
    # Loading and starting the sound play
    soundtrack.play(-1)

    pause_screen()



    wfp_logo = pygame.image.load(os.path.join('data', 'top.png')).convert()
    intro_thread.join()
    initialize_facilities()

    #surface_middle = pygame.transform.scale(surface3,resize_pos((1200,560)))
    surface_top = pygame.transform.scale(wfp_logo,resize_pos((1200,40)))


    initialize_gui()

    screen.fill((0,0,0))
    panel = display_panel()
    animation_obj = Animation()
    animation_obj.update()
    # Starting of the threads
    update_thread = threading.Thread(target = threades.update_turn, args=[]).start()
    message_thread = threading.Thread(target = message_window, args=[]).start()

    # The main infinite loop
    while True:
        #clock.tick()


        pygame.display.set_caption(str(int(clock.get_fps())))

        for e in gui.setEvents(pygame.event.get()):
	    event_handling(e)

        #pygame.draw.rect(screen,(209,169,106),resize_rect((0,40,1200,560)))
        animation_obj.update()


        # For top surface
        screen.blit(surface_top,(0,0))

        # For middle surface
        #surface_middle = pygame.transform.scale(surface3,resize_pos((1200,560)))
        #screen.blit(surface_middle,resize_pos((0,40)))

        # For bottom surface
        pygame.draw.rect(screen,(0,0,0),resize_rect((0,600,1200,300)))


        panel.update()

        desktop.update()

        desktop.draw()

        pygame.display.update()

        threades.iteration_time = clock.tick()
        threades.global_time += threades.iteration_time


if __name__ == '__main__':
    main()



