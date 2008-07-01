#! /usr/bin/env python
#
#   Copyright (C) 2006, 2007, One Laptop Per Child
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

import os
import random
import time
import threading
import IsoCollision
import pygame
import pygame.mixer
from pygame.locals import *
from sys import exit
from time import sleep,time,ctime
from pgu import text, gui as pgui
from threades import *

SCREENRECT = Rect(0, 0, 1200, 830)
ANIMRECT = Rect(0, 30, 1200, 550)

class Spritesheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(os.path.join('data', filename)).convert()
        
    def imgat(self, rect, colorkey = None):
        rect = Rect(rect)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image
            
    def imgsat(self, rects, colorkey = None):
        imgs = []
        for rect in rects:
            imgs.append(self.imgat(rect, colorkey))
        return imgs
        
        
class Build(pygame.sprite.Sprite):
    
    def __init__(self, filename, colorkey, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('data', filename)).convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = self.image.get_at((0, 0))
            self.image.set_colorkey(colorkey, RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)
        

class Environment(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        spritesheet = Spritesheet('tileset.png')
        matrix = []
        for i in range(9):
            for j in range(12):
                matrix.append((2+(j*50), 2+(i*50), 48, 48))
        self.tiles = spritesheet.imgsat(matrix)
        self.wfp_logo = pygame.image.load(os.path.join('data', 'top.png')).convert()
         
    def get_background(self):
        background = pygame.Surface(SCREENRECT.size).convert()
        background.fill((75, 75, 75))
        background.blit(self.wfp_logo,(0,0))
        background.fill((128, 128, 128),(0, 42,1200, 3))
        ground = [
        #          01--02--03--04--05--06--07--08--09--10--11--12--13--14--15--16--17--18--19--20--21--22--23--24--25
                 [ 32, 7, 34, 35, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 33, 34, 8, 32], 
                 [  7, 35, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 33, 8], 
                 [ 35, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 33], 
                 [  6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6], 
                 [  6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6], 
                 [  6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6], 
                 [  6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 40, 41, 42, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6], 
                 [  6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 40, 74, 101, 75, 42, 6, 6, 6, 6, 9, 11, 9, 11, 9, 11], 
                 [  6, 6, 6, 6, 6, 6, 6, 6, 6, 40, 74, 102, 29, 100, 75, 42, 6, 6, 6, 21, 23, 21, 23, 21, 23], 
                 [  6, 6, 6, 6, 6, 6, 6, 6, 6, 52, 90, 29, 29, 29, 88, 54, 6, 6, 6, 21, 23, 21, 23, 21, 23], 
                 [  6,  6,  6,  6,  6,  6,  6,  6,  6, 52, 90, 29, 29, 29, 88, 54,  6,  6,  6, 21, 23, 21, 23, 21, 23], 
                 ]
        # Draw village ground
        for x in range(25):
            for y in range(11):
                background.blit(self.tiles[ground[y][x]], (x*48, 45+(y*48)))     
        
        # Draw message bar
        background.fill((128, 128, 128),(0, 545,1200, 3))
        background.fill((0, 0, 0),(0, 548,1200, 25))
        background.fill((128, 128, 128),(0, 573,1200, 3))
        
        # Draw GUI background
        background.fill((128, 128, 128),(760, 573,3, 500))

        return background
        
class MessageDisplay(pygame.sprite.Sprite):
    def __init__(self, x, y, msgs=[]):
        pygame.sprite.Sprite.__init__(self)
        self.msgs = msgs
        spritesheet = Spritesheet('display.png')
        self.tiles = spritesheet.imgsat([(0, 0, 7, 36), (7, 0, 22, 36), (30, 0, 7, 36)])
        self.rect = pygame.Rect([ x, y] , [ 1200, 36] )
        self.image = pygame.Surface([1200,36]).convert()
        self.image.blit(self.tiles[1],(0,0))
        for i in range(54):
            self.image.blit(self.tiles[1],((22*i),0))
        self.image.blit(self.tiles[1],(1194,0))

        colorkey = self.image.get_at((0, 0))
        #self.image.set_colorkey(colorkey, RLEACCEL)
        
    def add_message(self, msg, weigth=1):
        if msg not in self.msgs:
            self.msgs.append(msg)
        
    def rem_message(self, msg):
        if msg in self.msgs:
            self.msgs.remove(msg)

class House(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.d = 5
        self.speed = [5, 0]
        
        ss = Spritesheet('tiles_house.png')
                                    
        self.tiles = ss.imgsat([(  0, 0, 89, 76), ( 89, 0, 89, 76),
                                (178, 0, 89, 76), (267, 0, 89, 76),
                                (355, 0, 89, 76), (445, 0, 89, 76)
                               ], -1)                            
                                
        self.frame = int(random.random()*1)
        self.image = self.tiles[self.frame]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move((x, y))
        self.counter = 0

    def update(self):
        if self.counter < 20:
            self.counter += 1
        else:
            self.counter = 0
            
            if self.frame >=4:
                light = int(random.random()*10)
                if light <1:
                    self.frame = 5
                else:
                    self.frame = 4
            else:
                self.frame  += 1
            self.image = self.tiles[self.frame]

    def set_frame(self, frame):
        self.frame = frame
        self.image = self.tiles[self.frame]        
            

class Hospital(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.d = 5
        self.speed = [5, 0]
        
        ss = Spritesheet('tiles_hospital.png')
                                    
        self.tiles = ss.imgsat([(   1, 0, 201, 165),( 202, 0, 201, 165),
                                ( 403, 0, 201, 165),( 604, 0, 201, 165),
                                ( 805, 0, 201, 165),(1006, 0, 201, 165),
                                (1207, 0, 201, 165),(1408, 0, 201, 165),
                                (1609, 0, 201, 165),(1810, 0, 201, 165),
                                (2011, 0, 201, 165),
                               ], -1)                            
                                
        self.frame = 0
        self.image = self.tiles[self.frame]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move((x, y))
        self.counter = 0

    def update(self):
        if self.counter < 40:
            self.counter += 1
        else:
            self.counter = 0
            
            if self.frame >= 7:
                light = int(random.random()*10)
                if light <= 3:
                    self.frame = 7 + light
                else:
                    self.frame = 7
            else:
                self.frame += 1
            
            self.image = self.tiles[self.frame]

    def set_frame(self, frame):
        self.frame = frame
        self.image = self.tiles[self.frame]        

class School(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        ss = Spritesheet('tiles_school.png')
                                    
        self.tiles = ss.imgsat([(   1, 0, 201, 165),( 202, 0, 201, 165),
                                ( 403, 0, 201, 165),( 604, 0, 201, 165),
                                ( 805, 0, 201, 165),(1006, 0, 201, 165),
                                (1207, 0, 201, 165),(1408, 0, 201, 165),
                                (1609, 0, 201, 165),(1810, 0, 201, 165),
                                (2011, 0, 201, 165),
                               ], -1)                            
                                
        self.frame = 0
        self.image = self.tiles[self.frame]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move((x, y))
        self.counter = 0

    def update(self):
        if self.counter < 4:
            self.counter += 1
        else:
            self.counter = 0
            
            if self.frame >= 7:
                light = int(random.random()*10)
                if light <= 3:
                    self.frame = 7 + light
                else:
                    self.frame = 7
            else:
                self.frame += 1
            
            self.image = self.tiles[self.frame]

    def set_frame(self, frame):
        self.frame = frame
        self.image = self.tiles[self.frame]        

class Training(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        ss = Spritesheet('tiles_work.png')
                                    
        self.tiles = ss.imgsat([(   1, 0, 201, 165),( 202, 0, 201, 165),
                                ( 403, 0, 201, 165),( 604, 0, 201, 165),
                                ( 805, 0, 201, 165),(1006, 0, 201, 165),
                                (1207, 0, 201, 165),(1408, 0, 201, 165),
                                (1609, 0, 201, 165),(1810, 0, 201, 165),
                                (2011, 0, 201, 165),
                               ], -1)                            
                                
        self.frame = 0
        self.image = self.tiles[self.frame]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move((x, y))
        self.counter = 0

    def update(self):
        if self.counter < 4:
            self.counter += 1
        else:
            self.counter = 0
            
            if self.frame >= 7:
                light = int(random.random()*10)
                if light <= 3:
                    self.frame = 7 + light
                else:
                    self.frame = 7
            else:
                self.frame += 1
            
            self.image = self.tiles[self.frame]

    def set_frame(self, frame):
        self.frame = frame
        self.image = self.tiles[self.frame]        


class Villager(pygame.sprite.Sprite):
    
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.dx = 2
        self.dy = 1
        self.speed = [2, 1]
        
        ss = Spritesheet(image)
                                    
        self.tiles = ss.imgsat([(0, 0, 15, 30), (16, 0, 15, 30), (32, 0, 15, 30), (48, 0, 15, 30),
                                (0, 31, 15, 30), (16, 31, 15, 30), (32, 31, 15, 30), (48, 31, 15, 30),
                                (0, 62, 15, 30), (16, 62, 15, 30), (32, 62, 15, 30), (48, 62, 15, 30),
                                (0, 93, 15, 30), (16, 93, 15, 30), (32, 93, 15, 30), (48, 93, 15, 30),
                               ], -1)                            

        self.frame = 0
        self.set_direction()
        self.image = self.tiles[self.frame]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move((300+int(random.random()*600), 240+int(random.random()*100)))
    
    def set_direction(self):
        sp = self.speed
        if sp[0] < 0  and sp[1] < 0:
            self.dtiles = self.tiles[0:4]
        elif sp[0] > 0  and sp[1] > 0:
            self.dtiles = self.tiles[4:8]
        elif sp[0] > 0  and sp[1] < 0:
            self.dtiles = self.tiles[8:12]
        elif sp[0] < 0  and sp[1] > 0:
            self.dtiles = self.tiles[12:16]
            
    def collide_build(self):
        #self.rect = self.rect.move([-2*self.speed[0], -2*self.speed[1]])
        self.set_speed(map(lambda x: -x, self.speed))

    def collide_villager(self):
        sp = self.speed
        dx = self.dx
        dy = self.dy
        if sp[0] < 0  and sp[1] < 0:
            self.speed = [dx, dy]
        elif sp[0] > 0  and sp[1] > 0:
            self.speed = [-dx, -dy]
        elif sp[0] > 0  and sp[1] < 0:
            self.speed = [-dx, dy]
        elif sp[0] < 0  and sp[1] > 0:
            self.speed = [dx, -dy]  
            
        self.set_direction()
    
    def set_speed(self, speed):
        self.speed = speed
        self.set_direction()
    
    def update(self):
        if self.frame == 3:
            self.frame = 0
        else:
            self.frame  += 1
            
        self.image = self.dtiles[self.frame]
        self.rect = self.rect.move([self.speed[0], self.speed[1]])
        if self.rect.left <= 0 or self.rect.right >= ANIMRECT.width:
            self.speed[0] = -self.speed[0]
            self.set_direction()
            self.rect = self.rect.move(self.speed)
            #self.rect = self.rect.move(self.speed)
        elif self.rect.top <= 45 or self.rect.bottom >= ANIMRECT.height:
            self.speed[1] = -self.speed[1]
            self.set_direction()
            self.rect = self.rect.move(self.speed)
            #self.rect = self.rect.move(self.speed)
        self.rect.clamp_ip(ANIMRECT)
        
class MainUI(pgui.Container):
    def __init__(self, x_base, y_base):
        pgui.Container.__init__(self)
        self.x = x_base
        self.y = y_base
        
        self.indicators = {}
        
        self.add(pgui.Label("Escaping Poverty"), 260, 0)
        self.add(pgui.Label("Money: $"+ str(int(money.get_money())) ), 630, 0)
        self.add(pgui.Label("January, Year 1"), 1050, 0)

        self.add(pgui.Label("Village Resources"), self.x + 20, self.y + 10)
        village_list = pgui.List(width=285, height=200)
        list1 = ('WATER', 'MEDICINE', 'BOOKS', 'TOOLS', 'BUILDING MATERIAL', 'RICE' , 'WHEAT' , 'BEANS' , 'SUGAR' , 'SALT' , 'OILS')
        for resource in list1:
            value = 0
            for res in resources:
                if res.get_name() == resource:
                    value = res.get_vquantity()
            table = pgui.Table()
            table.tr()
            table.td(pgui.Label(resource, align=-1),colspan=4, width=215, align=-1)
            table.td(pgui.Label(str(int(value)), align=2), align=2)
            village_list.add(table)
        
        self.add(village_list, self.x + 15, self.y + 30)

        self.add(pgui.Button('<- Buy', width=120, height=30), self.x + 315, self.y + 30)
        self.add(pgui.Button('Sell ->', width=120, height=30), self.x + 315, self.y + 75)
        self.add(pgui.Button('Next Month', width=120, height=30), self.x + 315, self.y + 195)
        
        self.add(pgui.Label("Trader"), self.x + 455, self.y + 10)
        trader_list = pgui.List(width=285, height=200)
        
        list2 = ('WATER', 'MEDICINE', 'BOOKS', 'TOOLS', 'BUILDING MATERIAL', 'RICE' , 'WHEAT' , 'BEANS' , 'SUGAR' , 'SALT' , 'OILS')
        list3 = ('1', '38', '286', '1547', '85000', '770000')
        list4 = ('1', '38', '286', '1547', '85000', '770000')
        for resource in list2:
            value = 0
            for res in resources:
                if res.get_name() == resource:
                    value = res.get_mquantity()
            table = pgui.Table()
            table.tr()
            table.td(pgui.Label(resource, align=-1), width=215, align=-1)
            table.td(pgui.Label(str(int(value)), align=2), align=2)
            trader_list.add(table)
        self.add(trader_list, self.x + 450, self.y + 30)
        
        self.add(pgui.Label("Indicators"), self.x + 780, self.y + 10)
        
        self.add_indicator('Housing', 0, self.x + 780, self.y + 30)
        self.add_indicator('Health', 20, self.x + 780, self.y + 65)
        self.add_indicator('Nutrition', 40, self.x + 780, self.y + 100)
        self.add_indicator('Education', 60, self.x + 780, self.y + 135)
        self.add_indicator('Food', 80, self.x + 780, self.y + 170)
        self.add_indicator('Training', 100, self.x + 780, self.y + 205)
                
    def add_indicator(self, name, value, x, y):
        self.indicators[name] = IndicatorUI(self, name, value, x, y)
        
    def update_village_resources(self, **resources):
        for resource, quantity in resources:
            pass

    def update_trader_resources(self, **resources):
        for resource, quantity in resources:
            pass
            
    
class IndicatorUI():
    def __init__(self, container, name, value, x, y):
        self.c = container
        self.x = x
        self.y = y
        self._label = pgui.Label(name, align=-1, width=75, height=20)
        self._bar = pgui.ProgressBar(value=value, min=0, max=100, size=20, height=15, width=270)
        self._label_value = pgui.Label(str(value)+'%', width=200, height=20)
        
        self.c.add(self._label,self.x, self.y)
        self.c.add(self._bar,self.x+95, self.y)
        self.c.add(self._label_value,self.x+370, self.y)
        
    def set_name(self, name):
        self._label.value = name
    
    def get_name(self):
        return self._label.value
    
    def set_value(self, value):
        self._bar.value = value
        self._label_value.set_value(str(value)+'%')

    def get_value(self):
        return self._bar.value

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join(name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', name
        raise SystemExit, message
    return sound

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1200,830))
    pygame.display.set_caption('Food Force: Scaping Poverty')
    update_thread = threading.Thread(target = update_turn, args=[]).start()
    
    # make background
    env = Environment()
    background = env.get_background()    
    screen.blit(background, (0, 0))
    pygame.display.update()
            
    # keep track of sprites
    all = pygame.sprite.RenderUpdates() 
    villagers = pygame.sprite.Group()
    builds = pygame.sprite.Group()
    
    speeds = [[2,1],[-2,-1],[-2,1],[2,-1]]
    for i in range(30):
        dir = int(random.random()*4)
        villager = Villager('villager1.png')
        villager.set_speed(speeds[dir])
        villager.add(all, villagers)     
        
    hospital = Hospital(0, 380)
    hospital.add(all, builds)
    
    school = School(450, 20)
    school.add(all, builds)
    
    work = Training(800, 20)
    work.add(all, builds)
    
    tenda1 = House(0, 90)
    tenda2 = House(78, 45)
    
    tenda3 = House(0, 180)
    tenda4 = House(78, 135)
    tenda5 = House(156, 90)
    tenda6 = House(234, 45)
    
    tenda7 = House(0, 270)
    tenda8 = House(78, 225)    
    tenda9 = House(156, 180)
    tenda10 = House(234, 135)
    #tenda9 = House(312, 90)
    #tenda10 = House(390, 45)
    
    tenda10.add(all, builds)
    tenda9.add(all, builds)
    tenda8.add(all, builds)
    tenda7.add(all, builds)
    tenda6.add(all, builds)
    tenda5.add(all, builds)
    tenda4.add(all, builds)
    tenda3.add(all, builds)
    tenda2.add(all, builds)
    tenda1.add(all, builds)
        
    fountain = Build('fontain.png', -1, 540, 430)
    fountain.add(all)
    
    
    font = pygame.font.SysFont("DejaVuSans", 24)
    
    #msg_display = MessageDisplay(0,545)
    #msg_display.add(all)
    
    # gui elements
    app = pgui.App()
    c = MainUI(0, 560)
    app.init(c)
    
    # Sprite elements

    
    soundtrack_loaded = False
    soundtrack_playing = False
    
    # keep track of time
    clock = pygame.time.Clock()
    
    iso = IsoCollision.IsoCollision()
    
    # game loop
    while 1:
        #time.sleep(.05)
        # get input
        c.indicators['Housing'].set_value(Housing.get_value()/10)
        c.indicators['Nutrition'].set_value(Nutrition.get_value()/10)
        c.indicators['Health'].set_value(Health.get_value()/10)
        c.indicators['Education'].set_value(Education.get_value()/10)
        #c.indicators['Training'].set_value(Training.get_value())
        for event in pygame.event.get():
            if event.type == QUIT: 
                return 
            elif event.type == KEYDOWN:
                
                if event.key == K_m:
                    srf = pygame.Surface((400,400))
                    srf.fill((0,0,0))
                    srf.set_alpha(100)
                    screen.blit(srf,(100,100))
                    srf.set_alpha(0)
                    screen.blit(srf,(100,100))
                    pygame.display.update()
                if event.key == K_f:
                    pygame.display.flip()
                if event.key == K_1:
                    value = c.indicators['Housing'].get_value()
                    c.indicators['Housing'].set_value(value -5)
                if event.key == K_2:
                    value = c.indicators['Housing'].get_value()
                    c.indicators['Housing'].set_value(value +5)
                if event.key == K_UP:
                    map(lambda x: x.set_speed([-2, -2]), villagers.sprites())
                if event.key == K_DOWN:
                    map(lambda x: x.set_speed([2, 2]), villagers.sprites())
                if event.key == K_LEFT:
                    map(lambda x: x.set_speed([-2, 2]), villagers.sprites())
                if event.key == K_RIGHT:
                    map(lambda x: x.set_speed([2, -2]), villagers.sprites())
                if event.key == K_s:
                    if soundtrack_playing:
                        soundtrack_playing = False
                        soundtrack.fadeout(500)
                    else:
                        if not soundtrack_loaded:
                            soundtrack_loaded = True
                            soundtrack = load_sound(os.path.join(os.path.dirname(__file__), 'data', 'soundtrack.ogg'))
                        soundtrack_playing = True
                        soundtrack.play()
                if event.key == K_r:
                    for build in builds:
                        build.set_frame(0)
            app.event(event)
        
        collide = pygame.sprite.groupcollide(villagers, builds, False, False)
        for villager in collide.keys():
            villager.collide_build()
        #for build in builds:
        #    for villager in villagers:
        #        if iso.collision(villager, build):
        #            villager.collide_build()

        collide = pygame.sprite.groupcollide(villagers, villagers, False, False)
        #for villager, group in collide.iteritems():
        #    for item in group:
        #        #if item <> villager:
        #        villager.collide_villager()
        #        item.collide_villager()
        
        # clear sprites
        all.clear(screen, background)
        
        #update sprites
        all.update()
        
        
        # redraw sprites
        dirty_sprites = all.draw(screen)
        pygame.display.update(dirty_sprites)

        # redraw gui elements
        dirty_gui = app.update(screen)
        pygame.display.update(dirty_gui)        
        
        # maintain frame rate
        clock.tick(10)
        
if __name__ == '__main__': main()
