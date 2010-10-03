#! /usr/bin/env python
#
#   Author : Mohit Taneja (mohitgenii@gmail.com)
#   Date : 9/12/2008 
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
import threades
import threading
import game_events
import texts_eng
import texts_spa
import model
import gui_buttons
import random



class Earthquake(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        mask= pygame.surface.Surface(threades.resize_pos((930,600)),SRCALPHA)
        mask.fill((0,0,0,0))
        self.clock = pygame.time.Clock()
        self.time = 0
        #mask.set_alpha(0)
        self.alpha = 0
        self.image = mask
        self.rect = self.image.get_rect()
        self.rect.move(threades.resize_pos((0,0)))
        self.counter = 0
        self.prev_disp = (0,0)
        self.move_dir = [(-20,-20),(-20,-10),(-20,0),(-20,10),(-20,20),(-10,-20),(-10,-20),(-10,0),(-10,10),(-10,20),(0,-20),(0,-10),(0,0),(0,10),(0,20),(10,-20),(10,-20),(10,0),(10,10),(10,20),(20,-20),(20,-10),(20,0),(20,10),(20,20)]
        # To close all open windows
        if gui_buttons.gui_obj.get_child_win_flag():
            gui_buttons.gui_obj.close_child_win()
            gui_buttons.gui_obj.close_win()
        elif gui_buttons.gui_obj.get_win_flag():
            gui_buttons.gui_obj.close_win()

    def update(self):

        global Hospital
        global House
        global School
        global Workshop
        global ppl


        self.time += self.clock.tick()
        if self.time >= 100:
            self.counter +=1
            self.time = 0
            if self.counter <50:
                threades.transform_obj.move_free((-self.prev_disp[0],-self.prev_disp[1]))
                self.prev_disp = self.move_dir[int(random.random()*25)]
                threades.transform_obj.move_free(self.prev_disp)
            if self.counter >20 and self.counter <60:
                self.alpha +=6
                self.image.fill((0,0,0,int(self.alpha)))
                #threades.screen.blit(self.image,(0,40))
            if self.counter==40:
                display_text = ' Your Village has been hit by an Earthquake'
                threades.message.push_message(display_text,'high')
            if self.counter == 80:
                threades.audio.play_music(True,'soundtrack')
                display_earthquake_images()
                threades.demolish_facility('Hospital')
                threades.demolish_facility('House')
                threades.demolish_facility('House')
                threades.demolish_facility('House')
                threades.demolish_facility('School')
                threades.demolish_facility('Workshop')
                model.ppl.change_total_population(-10)
            if self.counter > 81:
                if self.alpha >=2:
                    self.alpha -=2
                self.image.fill((0,0,0,int(self.alpha)))
                #threades.screen.blit(self.image,(0,40))
            if self.counter >220:
                event = game_events.Event(type = game_events.ACTIONCOMPLETEEVENT, facility_name = '', res_name = '' , res_quantity = 0)
                game_events.EventQueue.add(event)
                threades.natural_calamities.remove(earth_quake)

def display_earthquake_images():

    image1 = pygame.image.load(os.path.join('data', 'earthquake1.png')).convert()
    threades.screen.blit(pygame.transform.scale(image1,threades.new_screen_size),(0,0))
    pygame.display.flip()
    sleep(3)

    image2 = pygame.image.load(os.path.join('data', 'earthquake2.png')).convert()
    threades.screen.blit(pygame.transform.scale(image2,threades.new_screen_size),(0,0))
    pygame.display.flip()
    sleep(3)
    
    image3 = pygame.image.load(os.path.join('data', 'earthquake3.png')).convert()
    threades.screen.blit(pygame.transform.scale(image3,threades.new_screen_size),(0,0))
    pygame.display.flip()
    sleep(3)

    
    
earth_quake = None

def earthquake():
    ''' This method needs to be called when there is an earthquake in the
    village, it decreases the number of installations of some facilities and
    also reduce the population
    '''
    global earthquake

    earth_quake  = Earthquake()
    threades.natural_calamities.add(earth_quake)
    threades.audio.play_music(True,'earthquake')
