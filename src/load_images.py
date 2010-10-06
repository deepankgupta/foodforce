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
import os
from pygame.locals import *
import pickle



class Spritesheet:
    """ Base class for creating sprites for each facility, natural calamities, people, map.
    """
    def __init__(self, filename):
        """ initialize the sprite
        @ivar filename name of the file where image is store
        @type filename integer
        """
        self.sheet = pygame.image.load(os.path.join('data', filename)).convert_alpha()
        
    def imgat(self, rect, colorkey = None):
        """ blit the image according to position in rect and color in colorkey
        @ivar rect coordinates for image to be displayed
        @type rect tuple of integers
        @ivar colorkey color to be used
        @type colorkey integer
        """
        rect = Rect(rect)
        #print rect
        image = self.sheet.subsurface(rect)
        #image.blit(self.sheet, (0, 0), rect)
        '''
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
                
            image.set_colorkey(colorkey, RLEACCEL)
        '''
        return image
            
    def imgsat(self, rects, colorkey = None):
        """ creates a list of all sprites 
        @ivar rects list of coordinates of buildings of each facility
        @type rects list of coordinates
        @ivar colorkey color to be used
        @type colorkey integer
        """
        imgs = []
        for rect in rects:
            imgs.append(self.imgat(rect, colorkey))
        return imgs
    
def graphics_layout(file_name):
    """ used to initialize the constants
    @ivar file_name data file containing the position of graphical data
    @type file_name string
    """
    data_file = open(file_name,'rb')

    
    # Saving the positions of all the facilities
    global workshop_posn_list, house_posn_list, hospital_posn_list, school_posn_list, farm_posn_list, fountain_posn_list
    workshop_posn_list = pickle.load(data_file)
    house_posn_list = pickle.load(data_file)
    hospital_posn_list = pickle.load(data_file)
    school_posn_list = pickle.load(data_file)
    farm_posn_list = pickle.load(data_file)
    fountain_posn_list = pickle.load(data_file)
    global facilities_posn_list
    facilities_posn_list = pickle.load(data_file)
    # Saving the attributes for the villagers with each facility
    global workshop_villagers, house_villagers, hospital_villagers, school_villagers, farm_villagers, fountain_villagers, facility_villagers,back_image_level1 
    workshop_villagers = pickle.load(data_file)
    house_villagers = pickle.load(data_file)
    hospital_villagers = pickle.load(data_file)
    school_villagers = pickle.load(data_file)
    farm_villagers = pickle.load(data_file)
    fountain_villagers = pickle.load(data_file)
    facility_villagers = pickle.load(data_file)
    back_image_level1=pickle.load(data_file)
    data_file.close()

graphics_layout('graphics_layout.pkl')

def load_images():
    """ load the images for each facility
    """
    
    global House_tiles_list
    global Hospital_tiles_list
    global Farm_tiles
    global Workshop_tiles_list
    global School_tiles_list
    global Fountain_tiles
    global Man_tiles 
    global Woman_tiles 
    global Boy_tiles 
    global Girl_tiles 
    global Map_images
    
    
    House_tiles_list = [[],[],[],[]]
    Hospital_tiles_list = [[],[],[],[]]
    Farm_tiles = [[]]
    Workshop_tiles_list = [[],[],[],[]]
    School_tiles_list = [[],[],[],[]]
    Fountain_tiles = [[]]
    Man_tiles = []
    Woman_tiles = []
    Boy_tiles = []
    Girl_tiles = []
    Map_images = []
    
    
    
    
    # Loading images of People
    ss = Spritesheet('People.png')
    Man_tiles.append(ss.imgsat([(0,0,60,115),(60,1,60,115),(120,0,60,115),(60,1,60,115),    (0,117,60,113),(62,117,60,113),(120,117,60,112),(62,117,60,113),  (172,116,60,114),(172,116,60,114),(172,116,60,114),(172,116,60,114),  (170,0,60,115),(170,0,60,115),(170,0,60,115),(170,0,60,115)],-1))
    
    Woman_tiles.append(ss.imgsat([(225,0,60,115),(287,0,60,115),(346,0,60,115),(287,0,60,115),  (230,117,60,113),(288,117,60,113),(343,117,60,113),(288,117,60,113),  (398,115,60,115),(398,115,60,115),(398,115,60,115),(398,115,60,115),  (397,0,60,115),(397,0,60,115),(397,0,60,115),(397,0,60,115)],-1))
    
    Boy_tiles.append(ss.imgsat([(455,26,45,74),(517,26,45,74),(575,26,45,74),(517,26,45,74),  (455,130,45,74),(517,130,45,74),(575,130,45,74),(517,130,45,74),  (621,133,45,74),(621,133,45,74),(621,133,45,74),(621,133,45,74),  (621,26,45,74),(621,26,45,74),(621,26,45,74),(621,26,45,74)],-1))
    
    Girl_tiles.append(ss.imgsat([(670,18,45,90),(730,18,45,90),(786,19,45,90),(730,18,45,90),  (670,127,45,90),(730,127,45,90),(791,127,45,90),(730,127,45,90),  (842,119,45,90),(842,119,45,90),(842,119,45,90),(842,119,45,90),  (844,14,45,90),(844,14,45,90),(844,14,45,90),(844,14,45,90)],-1))
    
    # Loading images for the mini map
    ss = Spritesheet('dot_house.png')
    tiles = ss.imgat(( 0, 0, 15, 15), -1)
    Map_images.append(tiles)
    
    ss = Spritesheet('dot_school.png')
    tiles = ss.imgat(( 0, 0, 15, 15), -1)
    Map_images.append(tiles)
    
    ss = Spritesheet('dot_hospital.png')
    tiles = ss.imgat(( 0, 0, 15, 15), -1)
    Map_images.append(tiles)
    
    ss = Spritesheet('dot_workshop.png')
    tiles = ss.imgat(( 0, 0, 15, 15), -1)
    Map_images.append(tiles)
    
    ss = Spritesheet('dot_farm.png')
    tiles = ss.imgat(( 0, 0, 15, 15), -1)
    Map_images.append(tiles)
    
    ss = Spritesheet('dot_fountain.png')
    tiles = ss.imgat(( 0, 0, 15, 15), -1)
    Map_images.append(tiles)
    
    ss = Spritesheet('dot_market.png')
    tiles = ss.imgat(( 0, 0, 15, 15), -1)
    Map_images.append(tiles)
    
def load_images_facility(facility_name = '',level = 0):
    ''' Loads the images of a facility of any level
    '''
    
    global House_tiles_list
    global Hospital_tiles_list
    global Farm_tiles
    global Workshop_tiles_list
    global School_tiles_list
    global Fountain_tiles
    
    
    if facility_name == 'HOUSE':
        
        House_tiles_list = [[],[],[],[]]
        if level == 0:
            ss = Spritesheet('house_upgrade0.png')
            tiles = ss.imgsat([(   0, 0, 250, 300),( 250, 0, 280, 300),( 530, 0, 280, 300),( 810, 0, 280, 300)], -1)
            House_tiles_list[0] = tiles        
            
        if level == 1:
            ss = Spritesheet('house_upgrade1.png')
            tiles = ss.imgsat([(   0, 0, 260, 300),( 260, 0, 260, 300),( 520, 0, 260, 300)], -1)
            House_tiles_list[1]= tiles
            
        if level == 2:
            ss = Spritesheet('house_upgrade2.png')
            tiles = ss.imgsat([(   0, 0, 260, 300),( 260, 0, 260, 300),( 520, 0, 360, 300)], -1)
            House_tiles_list[2] = tiles
            
        if level == 3:
            ss = Spritesheet('house_upgrade3.png')
            tiles = ss.imgsat([(   0, 0, 260, 300),( 260, 0, 260, 300),( 520, 0, 360, 300)], -1)
            House_tiles_list[3] = tiles
                
    if facility_name == 'WORKSHOP':
        Workshop_tiles_list = [[],[],[],[]]
        if level == 0:
            ss = Spritesheet('workshop_upgrade0.png')
            tiles = ss.imgsat([(   0, 0, 480, 500),( 480, 0,520, 500),( 1000, 0, 520, 500)], -1)
            Workshop_tiles_list[0] = tiles
        
        if level == 1:
            ss = Spritesheet('workshop_upgrade1.png')
            tiles = ss.imgsat([( 0, 0, 520, 500),( 520, 0, 520, 500),( 1040, 0, 520, 500)], -1)
            Workshop_tiles_list[1] = tiles
        
        if level == 2:
            ss = Spritesheet('workshop_upgrade2.png')
            tiles = ss.imgsat([(   0, 0, 515, 500),( 515, 0, 515, 500),( 1030, 0, 515, 500)], -1)
            Workshop_tiles_list[2] = tiles
        
        if level == 3:
            ss = Spritesheet('workshop_upgrade3.png')
            tiles = ss.imgsat([(   0, 0, 520, 520),( 520, 0, 520, 520),( 1040, 0, 760, 520)], -1)
            Workshop_tiles_list[3] = tiles
            
    if facility_name == 'SCHOOL':
        School_tiles_list = [[],[],[],[]]
        if level == 0:
            ss = Spritesheet('school_upgrade0.png')
            tiles = ss.imgsat([( 0, 0, 410, 450),( 410, 0, 440, 450),( 850, 0, 440, 450),( 1290, 0, 440, 450)], -1)
            School_tiles_list[0] = tiles
            
        if level == 1:
            ss = Spritesheet('school_upgrade1.png')
            tiles = ss.imgsat([( 0, 0, 420, 450),( 420, 0, 420, 450),( 840, 0, 420, 450)], -1)
            School_tiles_list[1] = tiles
        
        if level == 2:
            ss = Spritesheet('school_upgrade2.png')
            tiles = ss.imgsat([( 0, 0, 420, 450),( 420, 0, 420, 450),( 840, 0, 420, 450)], -1)
            School_tiles_list[2] = tiles
          
        if level == 3:
            ss = Spritesheet('school_upgrade3.png')
            tiles = ss.imgsat([( 0, 0, 420, 450),( 420, 0, 420, 450),( 840, 0, 420, 450)], -1)
            School_tiles_list[3] = tiles
    
    if facility_name == 'HOSPITAL':
        Hospital_tiles_list = [[],[],[],[]]
        if level == 0:
            ss = Spritesheet('hospital_upgrade0.png')
            tiles = ss.imgsat([(   0, 0, 340, 500),( 340, 0, 370, 500),( 710, 0, 370, 500),( 1080, 0, 363, 500)], -1)
            Hospital_tiles_list[0] = tiles
            
        if level == 1:
            ss = Spritesheet('hospital_upgrade1.png')
            tiles = ss.imgsat([(   0, 0, 370, 500),( 370, 0, 370, 500),( 740, 0, 370, 500)], -1)
            Hospital_tiles_list[1] = tiles
            
        if level == 2:
            ss = Spritesheet('hospital_upgrade2.png')
            tiles = ss.imgsat([(   0, 0, 370, 500),( 370, 0, 370, 500),( 740, 0, 370, 500)], -1)
            Hospital_tiles_list[2] = tiles
            
        if level == 3:
            ss = Spritesheet('hospital_upgrade3.png')
            tiles = ss.imgsat([(   0, 0, 370, 500),( 370, 0, 370, 500),( 740, 0, 370, 500)], -1)
            Hospital_tiles_list[3] = tiles
                    
    if facility_name == 'FARM':
        Farm_tiles = [[]]
        ss = Spritesheet('farm.png')
        tiles = ss.imgsat([(   0, 0, 500, 500),( 516, 0, 480, 500),( 1000, 0, 516, 500)], -1)
        Farm_tiles[0] = tiles
        
    if facility_name == 'FOUNTAIN':
        Fountain_tiles = [[]]
        ss = Spritesheet('fountain.png')
        tiles = ss.imgsat([( 0, 0, 140, 192),( 150, 0, 115, 192),( 285, 0, 130, 192),( 435, 0, 197, 192)], -1)
        Fountain_tiles[0] = tiles

    
    
def load_images_ppl():
    
    global Man_tiles 
    global Woman_tiles 
    global Boy_tiles 
    global Girl_tiles 
    
    Man_tiles = []
    Woman_tiles = []
    Boy_tiles = []
    Girl_tiles = []
    
    # Loading images of People
    ss = Spritesheet('People.png')
    Man_tiles.append(ss.imgsat([(0,0,60,115),(60,1,60,115),(120,0,60,115),(60,1,60,115),    (0,117,60,113),(62,117,60,113),(120,117,60,112),(62,117,60,113),  (172,116,60,114),(172,116,60,114),(172,116,60,114),(172,116,60,114),  (170,0,60,115),(170,0,60,115),(170,0,60,115),(170,0,60,115)],-1))
    
    Woman_tiles.append(ss.imgsat([(225,0,60,115),(287,0,60,115),(346,0,60,115),(287,0,60,115),  (230,117,60,113),(288,117,60,113),(343,117,60,113),(288,117,60,113),  (398,115,60,115),(398,115,60,115),(398,115,60,115),(398,115,60,115),  (397,0,60,115),(397,0,60,115),(397,0,60,115),(397,0,60,115)],-1))
    
    Boy_tiles.append(ss.imgsat([(455,26,45,74),(517,26,45,74),(575,26,45,74),(517,26,45,74),  (455,130,45,74),(517,130,45,74),(575,130,45,74),(517,130,45,74),  (621,133,45,74),(621,133,45,74),(621,133,45,74),(621,133,45,74),  (621,26,45,74),(621,26,45,74),(621,26,45,74),(621,26,45,74)],-1))
    
    Girl_tiles.append(ss.imgsat([(670,18,45,90),(730,18,45,90),(786,19,45,90),(730,18,45,90),  (670,127,45,90),(730,127,45,90),(791,127,45,90),(730,127,45,90),  (842,119,45,90),(842,119,45,90),(842,119,45,90),(842,119,45,90),  (844,14,45,90),(844,14,45,90),(844,14,45,90),(844,14,45,90)],-1))
    
    
    