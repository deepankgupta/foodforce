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
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, RLEACCEL)
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
    
    
House_tiles_list = []
Hospital_tiles_list = []
Farm_tiles = [] 
Workshop_tiles_list = []
School_tiles_list = [] 
Fountain_tiles = []
Earthquake_tiles = []
Man_tiles = []
Woman_tiles = []
Boy_tiles = []
Girl_tiles = []
Map_images = []

# Saving the positions of all the facilities
workshop_posn_list = [(200,2550),(2000,5000),  (6500,400),  (6000,5300)]
house_posn_list = [(800,2000),(1000,2600),(1400,3300),(2000,2000),(2000,2600),  (2800,3800),(3800,3800),(3200,4500),  (5200,500),(4600,1100),(5500,1100),(6200,1600),(5000,1800),(5800,2200),(5200,2500),  (5000,3600),(5800,3500),(6500,3300),(6000,4100),(6750,3800),(6900,4500)]
hospital_posn_list = [(1400,3900), (7700,2200), (4500,4200)]
school_posn_list = [(2700,2000), (6100,2500), (7200,3000)]
farm_posn_list = [(300,500),(3000,500), (7400,800), (7500,3600)]
fountain_posn_list = [(2100,1200),(2200,3000),(3600,3500), (4500,1800),(6900,2000), (5900,3000),(6000,4800)]      

facilities_posn_list = [house_posn_list,school_posn_list,hospital_posn_list,workshop_posn_list,farm_posn_list,fountain_posn_list]
# Saving the attributes for the villagers with each facility
workshop_villagers = [ [ ('Man',(0,2400,1200,1500)), ('Man',(0,2400,1200,1500)) ], [ ('Man',(1500,4500,1200,1500)), ('Man',(1500,4500,1200,1500)) ], [ ('Man',(6200,0,1200,1500)), ('Man',(6200,0,1200,1500)) ], [ ('Man',(5500,4500,1200,1500)), ('Man',(5500,4500,1200,1500)) ] ]
house_villagers = [ [ ('Woman',(600,1800,2400,2000)), ('Woman',(600,1800,2400,2000)), ('Woman',(600,1800,2400,2000)), ('Boy',(600,1800,2400,2000)), ('Boy',(600,1800,2400,2000)), ('Girl',(600,1800,2400,2000)), ('Girl',(600,1800,2400,2000)) ],[],[],[],[], [ ('Woman',(2500,3500,2000,2000)), ('Woman',(2500,3500,2000,2000)), ('Boy',(2500,3500,2000,2000)), ('Girl',(2500,3500,2000,2000))],[],[], [ ('Man',(4500,0,2500,3000)), ('Woman',(4500,0,2500,3000)), ('Girl',(4500,0,2500,3000)), ('Girl',(4500,0,2500,3000)), ('Boy',(4500,0,2500,3000)), ('Boy',(4500,0,2500,3000)) ],[],[],[],[],[],[], [ ('Man',(4500,3000,3500,1800)), ('Woman',(4500,3000,3500,1800)), ('Woman',(4500,3000,3500,1800)), ('Boy',(4500,3000,3500,1800)), ('Girl',(4500,3000,3500,1800)) ],[],[],[],[],[] ]  
hospital_villagers = [ [ ('Man',(1000,3500,1200,1200)), ('Woman',(1000,3500,1200,1200)), ('Boy',(1000,3500,1200,1200)), ('Girl',(1000,3500,1200,1200)) ], [ ('Man',(7400,1800,1200,1200)), ('Woman',(7400,1800,1200,1200)), ('Boy',(7400,1800,1200,1200)), ('Girl',(7400,1800,1200,1200)) ], [ ('Man',(4500,4000,1200,1200)), ('Woman',(4500,4000,1200,1200)), ('Boy',(4500,4000,1200,1200)), ('Girl',(4500,4000,1200,1200)) ] ]
school_villagers = [ [ ('Boy',(2500,1800,1500,1500)), ('Boy',(2500,1800,1500,1500)), ('Girl',(2500,1800,1500,1500)) ], [ ('Boy',(1800,5800,1500,1500)), ('Girl',(1800,5800,1500,1500)), ('Girl',(1800,5800,1500,1500)) ], [ ('Boy',(7000,2800,1500,1500)), ('Boy',(7000,2800,1500,1500)), ('Girl',(7000,2800,1500,1500)) ] ]  
farm_villagers = [ [ ('Woman',(0,0,1000,1000)), ('Man',(0,0,1000,1000)) ], [ ('Woman',(2500,0,1000,1000)), ('Man',(2500,0,1000,1000)) ], [ ('Woman',(7000,600,1000,1000)), ('Man',(7000,600,1000,1000)) ], [ ('Woman',(7000,3500,1000,1000)), ('Man',(7000,3500,1000,1000)) ] ]
fountain_villagers = [ [],[],[],[],[],[],[] ]
facility_villagers = { 'WORKSHOP':workshop_villagers , 'HOUSE':house_villagers , 'HOSPITAL':hospital_villagers , 'SCHOOL':school_villagers , 'FARM':farm_villagers,'FOUNTAIN':fountain_villagers }
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
    
    # Loading images of School
    ss = Spritesheet('school_upgrade0.png')
    tiles = ss.imgsat([( 0, 0, 410, 450),( 410, 0, 440, 450),( 850, 0, 440, 450),( 1290, 0, 440, 450)], -1)
    School_tiles_list.append(tiles)        
    
    ss = Spritesheet('school_upgrade1.png')
    tiles = ss.imgsat([( 0, 0, 420, 450),( 420, 0, 420, 450),( 840, 0, 420, 450)], -1)
    School_tiles_list.append(tiles)
  
    ss = Spritesheet('school_upgrade2.png')
    tiles = ss.imgsat([( 0, 0, 420, 450),( 420, 0, 420, 450),( 840, 0, 420, 450)], -1)
    School_tiles_list.append(tiles)
  
    ss = Spritesheet('school_upgrade3.png')
    tiles = ss.imgsat([( 0, 0, 420, 450),( 420, 0, 420, 450),( 840, 0, 420, 450)], -1)
    School_tiles_list.append(tiles)
    
    
    
    # Loading images of Workshop
    ss = Spritesheet('workshop_upgrade0.png')
    tiles = ss.imgsat([(   0, 0, 480, 500),( 480, 0,520, 500),( 1000, 0, 520, 500)], -1)
    Workshop_tiles_list.append(tiles)        
    
    ss = Spritesheet('workshop_upgrade1.png')
    tiles = ss.imgsat([( 0, 0, 520, 500),( 520, 0, 520, 500),( 1040, 0, 520, 500)], -1)
    Workshop_tiles_list.append(tiles)
 
    ss = Spritesheet('workshop_upgrade2.png')
    tiles = ss.imgsat([(   0, 0, 515, 500),( 515, 0, 515, 500),( 1030, 0, 515, 500)], -1)
    Workshop_tiles_list.append(tiles)
    
    ss = Spritesheet('workshop_upgrade3.png')
    tiles = ss.imgsat([(   0, 0, 520, 520),( 520, 0, 520, 520),( 1040, 0, 760, 520)], -1)
    Workshop_tiles_list.append(tiles)
    
    
    # Loading images of House
    ss = Spritesheet('house_upgrade0.png')
    tiles = ss.imgsat([(   0, 0, 250, 300),( 250, 0, 280, 300),( 530, 0, 280, 300),( 810, 0, 280, 300)], -1)
    House_tiles_list.append(tiles)        
    
    ss = Spritesheet('house_upgrade1.png')
    tiles = ss.imgsat([(   0, 0, 260, 300),( 260, 0, 260, 300),( 520, 0, 260, 300)], -1)
    House_tiles_list.append(tiles)
 
    ss = Spritesheet('house_upgrade2.png')
    tiles = ss.imgsat([(   0, 0, 260, 300),( 260, 0, 260, 300),( 520, 0, 360, 300)], -1)
    House_tiles_list.append(tiles)
    
    ss = Spritesheet('house_upgrade3.png')
    tiles = ss.imgsat([(   0, 0, 260, 300),( 260, 0, 260, 300),( 520, 0, 360, 300)], -1)
    House_tiles_list.append(tiles)
    
    
    # Loading images of Hospital
    
    ss = Spritesheet('hospital_upgrade0.png')
    tiles = ss.imgsat([(   0, 0, 340, 500),( 340, 0, 370, 500),( 710, 0, 370, 500),( 1080, 0, 363, 500)], -1)
    Hospital_tiles_list.append(tiles)        
    
    ss = Spritesheet('hospital_upgrade1.png')
    tiles = ss.imgsat([(   0, 0, 370, 500),( 370, 0, 370, 500),( 740, 0, 370, 500)], -1)
    Hospital_tiles_list.append(tiles)
    
    ss = Spritesheet('hospital_upgrade2.png')
    tiles = ss.imgsat([(   0, 0, 370, 500),( 370, 0, 370, 500),( 740, 0, 370, 500)], -1)
    Hospital_tiles_list.append(tiles)
    
    ss = Spritesheet('hospital_upgrade3.png')
    tiles = ss.imgsat([(   0, 0, 370, 500),( 370, 0, 370, 500),( 740, 0, 370, 500)], -1)
    Hospital_tiles_list.append(tiles)
    
    # Loading of images of Farm
    
    ss = Spritesheet('farm.png')
    tiles = ss.imgsat([(   0, 0, 500, 500),( 516, 0, 480, 500),( 1000, 0, 516, 500)], -1)
    Farm_tiles.append(tiles)
    
    # Loading images of Fountain
    
    ss = Spritesheet('fountain.png')
    tiles = ss.imgsat([( 0, 0, 140, 192),( 150, 0, 115, 192),( 285, 0, 130, 192),( 435, 0, 197, 192)], -1)
    Fountain_tiles.append(tiles)

    # Loading images of People
    ss = Spritesheet('People.png')
    Man_tiles.append(ss.imgsat([(0,0,60,115),(60,1,60,115),(120,0,60,115),(60,1,60,115),    (0,117,60,113),(62,117,60,115),(120,117,60,112),(62,117,60,113),  (172,116,60,115),(172,116,60,115),(172,116,60,115),(172,116,60,115),  (170,0,60,115),(170,0,60,115),(170,0,60,115),(170,0,60,115)],-1))
    
    Woman_tiles.append(ss.imgsat([(225,0,60,115),(287,0,60,115),(346,0,60,115),(287,0,60,115),  (230,117,60,115),(288,117,60,115),(343,117,60,115),(288,117,60,115),  (398,115,60,115),(398,115,60,115),(398,115,60,115),(398,115,60,115),  (397,0,60,115),(397,0,60,115),(397,0,60,115),(397,0,60,115)],-1))
    
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