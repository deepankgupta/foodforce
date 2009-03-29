from sys import exit
import os
from time import *
from threades import *
import threades
import threading

import gui
from gui import *
from gui_buttons import *



class bar:

    color_bar = (47,47,255)

    def __init__(self, (x_value, y_value)):
        ''' Draws a bar on the surface at posn x,y
        '''
        self.x = x_value
        self.y = y_value

        pygame.draw.rect(screen,self.color_bar,resize_rect((self.x,self.y,250,18)),2)

        pygame.draw.rect(screen,(255,255,255),resize_rect((self.x+2,self.y+2,246,14)))



    def update_value(self,value):
        '''Updates the value of the bar
        '''

        max_value = 100.0
        max_pixel = 246.0
        colour = (177,135,73)           
        pygame.draw.rect(screen,self.color_bar,resize_rect((self.x,self.y,250,18)),2)        
        pygame.draw.rect(screen,colour,resize_rect((self.x+2,self.y+2,value/max_value*max_pixel,14)))
        pygame.draw.rect(screen,(255,255,255),resize_rect((self.x+2+value/max_value*max_pixel,self.y+2,max_pixel-value/max_value*max_pixel,14)))







class indicator_panel:

    global desktop
    font_bg_color = (0,0,0)       # This should be same as  the background colour for the label
    font_color = (255,214,150)    # This should be same as that for the font to be written on the label
    color_grey = (160,160,160)
    def __init__(self):
        ''' Draws the indicator panel on the surface
        '''
        
        self.update_flag = True

        myfont1 = pygame.font.Font("font.ttf", resize_pt(30))   # For main heading

        myfont2 = pygame.font.Font("font.ttf", resize_pt(20))   # For indicators name
        myfont3 = pygame.font.Font("font.ttf", resize_pt(16))
        # Creating a custom label style
        self.labelstyle1 = gui.defaultLabelStyle.copy()
        self.labelstyle1['border-width'] = 1
        self.labelstyle1['wordwrap'] = True
        self.labelstyle1['autosize'] = False
        self.labelstyle1['font'] = myfont1
        self.labelstyle1['font-color'] = self.font_color
        self.labelstyle1['border-color'] = self.color_grey
        # Drawing main Indicator label
        label = Label(position = resize_pos((900,600)),size = resize_pos((300,45)), parent = desktop, text = "      Indicators", style = self.labelstyle1)

        print " deawing indicator panel"
        
        # Creating second custom label
        self.labelstyle2 = gui.defaultLabelStyle.copy()
        self.labelstyle2['border-width'] = 0
        self.labelstyle2['wordwrap'] = True
        self.labelstyle2['autosize'] = False
        self.labelstyle2['font'] = myfont2
        self.labelstyle2['font-color'] = self.font_color
        self.labelstyle2['border-color'] = self.color_grey
        # Drawing all the indicators
        ind_namelist = (' Housing',' Nutrition',' Health',' Education',' Training')

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
        name_label_size = resize_pos((300,25))
        self.value_labels = []
        for i in range(5):
            label = Label(position = resize_pos((900,650+50*i)),size = name_label_size, parent = desktop, text = ind_namelist[i], style = self.labelstyle2)
            self.bar_dict.append(bar((902,677+50*i)))
            label = Label(position = resize_pos((1160,677+50*i)), parent = desktop, text = str(0), style = self.labelstyle3)
            self.value_labels.append(label)
    




    def update_value(self):
        ''' Updates the values of all the indicators
        '''
        
        for i in range(5):

            self.bar_dict[i].update_value(indicators_list[i].get_value())
            if not (self.value_labels[i].text == str(int(indicators_list[i].get_value()))+'%'):
                self.update_flag = True
        
        if self.update_flag or panel_update_flag or total_update_flag:
            pygame.draw.line(screen,self.color_grey,resize_pos((900,645)),resize_pos((900,900)),1)
        
            for i in range(5):
    
                self.bar_dict[i].update_value(indicators_list[i].get_value())
                if not (self.value_labels[i].text == str(int(indicators_list[i].get_value()))+'%'):
                    self.value_labels[i].text = str(int(indicators_list[i].get_value()))+'%'

        self.update_flag = False
        




class resources_panel:


    global desktop
    font_bg_color = (0,0,0)             # This should be same as  the background colour for the label
    font_color = (255,214,150)      # This should be same as that for the font to be written on the label
    color_grey = (160,160,160)
    def __init__(self):
        ''' Draws the resources panel on the surface
        '''
        
        self.update_flag = True
        self.money_flag = True
        myfont1 = pygame.font.Font("font.ttf", resize_pt(30))   # For main heading
        myfont2 = pygame.font.Font("font.ttf", resize_pt(20))   # For resources name and their value
        myfont3 = pygame.font.Font("font.ttf", resize_pt(16))
        myfont4 = pygame.font.Font("font.ttf", resize_pt(18))   # For the display of money
        
        # Creating a custom label style
        self.labelstyle1 = gui.defaultLabelStyle.copy()
        self.labelstyle1['border-width'] = 1
        self.labelstyle1['wordwrap'] = True
        self.labelstyle1['autosize'] = False
        self.labelstyle1['font'] = myfont1
        self.labelstyle1['font-color'] = self.font_color
        self.labelstyle1['border-color'] = self.color_grey
        

        # Drawing main Resources rectangle
        label = Label(position = resize_pos((400,600)),size = resize_pos((500,45)), parent = desktop, text = "                    Resources", style = self.labelstyle1)

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
        self.money_label = Label(position = resize_pos((850,10)), parent = desktop, text = 'Money -:   '+str(int(money.get_money()))+'      ', style = self.labelstyle4)
        
        self.value_labels = []
        # Drawing general resources list
        list_gen_res = (' Water',' Building Materials',' Tools',' Medicines',' Books')
        for i in range(5):
            label = Label(position = resize_pos((400,645+35*i)),size = resize_pos((200,35)), parent = desktop, text = list_gen_res[i], style = self.labelstyle2)
            label = Label(position = resize_pos((605,649+35*i)), parent = desktop, text = str(int(resources[i].get_vquantity())), style = self.labelstyle3)
            self.value_labels.append(label)
            
        # Drawing food resources list
        list_food_res = (' Rice',' Fruit & Vegatables',' Beans',' Sugar',' Salt',' Oil')
        for i in range(6):
            label = Label(position = resize_pos((650,645+35*i)),size = resize_pos((200,35)), parent = desktop, text = list_food_res[i], style = self.labelstyle2)
            label = Label(position = resize_pos((855,649+35*i)), parent = desktop, text = str(int(resources[i+5].get_vquantity())), style = self.labelstyle3)
            self.value_labels.append(label)
    

    def update_value(self):
        ''' Updates the resources panel
        '''

        self.money_flag = False
        for i in range(11):
            if not (self.value_labels[i].text == str(int(resources[i].get_vquantity()))):
                self.update_flag = True
        
        if self.update_flag or panel_update_flag or total_update_flag:
           
            
            pygame.draw.line(screen,self.color_grey,resize_pos((400,645)),resize_pos((400,855)),1)
            pygame.draw.line(screen,self.color_grey,resize_pos((650,645)),resize_pos((650,855)),1)
    
            for i in range(11):
                if not (self.value_labels[i].text == str(int(resources[i].get_vquantity()))):
                    self.value_labels[i].text = str(int(resources[i].get_vquantity()))
        
        if not (self.money_label.text == 'Money -:   '+str(int(money.get_money()))+'      '):
            self.money_flag = True
            self.money_label.text = 'Money -:   '+str(int(money.get_money()))+'      '

        self.update_flag = False
        
    
    
    


class manpower_panel:

    global desktop
    font_bg_color = (0,0,0)       # This should be same as  the background colour for the label
    font_color = (255,214,150)    # This should be same as that for the font to be written on the label
    color_grey = (160,160,160)
    def __init__(self):
        ''' Draws the manpower panel
        '''
        
        self.update_flag = True
        myfont1 = pygame.font.Font("font.ttf", resize_pt(30))   # For main heading
        myfont2 = pygame.font.Font("font.ttf", resize_pt(20))   # For resources name and their value
        myfont3 = pygame.font.Font("font.ttf", resize_pt(16))   # For resources name and their value

        # Creating a custom label style
        self.labelstyle1 = gui.defaultLabelStyle.copy()
        self.labelstyle1['border-width'] = 1
        self.labelstyle1['wordwrap'] = True
        self.labelstyle1['autosize'] = False
        self.labelstyle1['font'] = myfont1
        self.labelstyle1['font-color'] = self.font_color
        self.labelstyle1['border-color'] = self.color_grey

        # Drawing main Manpower Resources rectangle
        label = Label(position = resize_pos((0,600)),size = resize_pos((400,45)), parent = desktop, text = "  Manpower Distribution", style = self.labelstyle1)

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

        # Drawing Manpower resources list
        list_names = (' Total Population',' Sheltered People',' Educated People',' Healthy People',' People Fed',' People Employed')
        list_values = (ppl.get_total_population(),ppl.get_no_of_ppl_sheltered(),ppl.get_no_of_ppl_educated(),ppl.get_no_of_ppl_healthy(),ppl.get_no_of_ppl_fed(),ppl.get_total_no_of_ppl_emp())
        
        self.value_labels = []
        for i in range(6):
            label = Label(position = resize_pos((0,645+35*i)),size = resize_pos((350,35)), parent = desktop, text = list_names[i], style = self.labelstyle2)
            label = Label(position = resize_pos((355,649+35*i)), parent = desktop, text = str(int(list_values[i])), style = self.labelstyle3)
            self.value_labels.append(label)


    def update_value(self):
        ''' Updates the Manpower panel
        '''
        list_values = (ppl.get_total_population(),ppl.get_no_of_ppl_sheltered(),ppl.get_no_of_ppl_educated(),ppl.get_no_of_ppl_healthy(),ppl.get_no_of_ppl_fed(),ppl.get_total_no_of_ppl_emp())
        for i in range(6):

            if not (self.value_labels[i].text == str(int(list_values[i]))):
                self.update_flag = True
        
        if self.update_flag or panel_update_flag or total_update_flag:

            pygame.draw.line(screen,self.color_grey,resize_pos((900,645)),resize_pos((900,855)),1)
            pygame.draw.rect(screen,self.color_grey,resize_rect((0,855,300,45)),2)        
            pygame.draw.rect(screen,self.color_grey,resize_rect((300,855,300,45)),2)        
            pygame.draw.rect(screen,self.color_grey,resize_rect((600,855,300,45)),2)        
    
            for i in range(6):
    
                if not (self.value_labels[i].text == str(int(list_values[i]))):
                    self.value_labels[i].text = str(int(list_values[i]))
        
        self.update_flag = False
        
    
class facilities_panel:

    global desktop
    font_bg_color = (255,255,255)       # This should be same as  the background colour for the label
    font_color = (255,214,150)    # This should be same as that for the font to be written on the label
    color_grey = (160,160,160)
    def __init__(self):
        ''' Draws the Facilities panel
        '''
        self.update_flag = True
        myfont1 = pygame.font.Font("font.ttf", resize_pt(20))   # For resources name and their value
        
        self.labelstyle1 = gui.defaultLabelStyle.copy()
        self.labelstyle1['border-width'] = 0
        self.labelstyle1['wordwrap'] = False
        self.labelstyle1['autosize'] = False
        self.labelstyle1['font'] = myfont1
        self.labelstyle1['font-color'] = self.font_color
        #self.labelstyle1['bg-color'] = self.font_bg_color
        
        self.list_titles = ('Houses ','Schools ','Hospitals ','Workshops ','Farms ','Wells ')
        self.list_names = ('Number: ','Number: ','Number: ','Number: ','Number: ','Number: ')
        self.list_values1 = (House.get_number(),School.get_number(),Hospital.get_number(),Workshop.get_number(),Farm.get_number(),Fountain.get_number())
        self.list_values2 = (House.get_level(),School.get_level(),Hospital.get_level(),Workshop.get_level(),Farm.get_level(),Fountain.get_level())
        self.value_labels = []
        for i in range(6):
            label = Label(position = resize_pos((950,50+55*i)),size = resize_pos((300,30)), parent = desktop, text = self.list_titles[i], style = self.labelstyle1)
            label = Label(position = resize_pos((950,75+55*i)),size = resize_pos((300,30)), parent = desktop, text = self.list_names[i]+str(int(self.list_values1[i]))+' Level: '+str(int(self.list_values2[i])), style = self.labelstyle1)
            label.surf.set_alpha(200)
            self.value_labels.append(label)


    def update_value(self):
        ''' Updates the Facilities panel
        '''
        for i in range(6):

            if not (self.value_labels[i].text == self.list_names[i]+str(int(self.list_values1[i]))+' Level: '+str(int(self.list_values2[i]))):
                self.update_flag = False
        
        if self.update_flag or facilities_update_flag or total_update_flag:
            
            self.list_values1 = (House.get_original_number(),School.get_original_number(),Hospital.get_original_number(),Workshop.get_original_number(),Farm.get_original_number(),Fountain.get_original_number())
            self.list_values2 = (House.get_level(),School.get_level(),Hospital.get_level(),Workshop.get_level(),Farm.get_level(),Fountain.get_level())
            pygame.draw.rect(screen,(0,0,0),resize_rect((930,40,270,350))) 
            for i in range(6):
    
                if not (self.value_labels[i].text == self.list_names[i]+str(int(self.list_values1[i]))+' Level: '+str(int(self.list_values2[i]))):
                    self.value_labels[i].text = self.list_names[i]+str(int(self.list_values1[i]))+' Level: '+str(int(self.list_values2[i]))
        
        self.update_flag = False
        


class mini_map:

    def __init__(self):
        
        self.update_flag = True
        for i in range(6):
            Map_images[i] = pygame.transform.scale(Map_images[i],resize_pos((15,15)))
        self.map = pygame.image.load(os.path.join('data', 'map.png')).convert()
        self.map = pygame.transform.scale(self.map,resize_pos((270,210)))
        self.list_num_fac = []
        for i in range(len(facilities_list)):
            self.list_num_fac.append(facilities_list[i].get_original_number())
    
    def update(self):
        
        for i in range(len(facilities_list)):
            if not (self.list_num_fac[i] == facilities_list[i].get_original_number()):
                self.update_flag = True
    
        if self.update_flag or map_update_flag or total_update_flag:
            screen.blit(self.map,resize_pos((930,390)))
            posn = resize_pos((930+int(3200/33.3),390+int(2600/28.57)))
            screen.blit(Map_images[6],posn)
            for i in range(len(facilities_list)):
                for j in range(facilities_list[i].get_original_number()):
                    posn = resize_pos((930+int(facilities_posn_list[i][j][0]/33.3),390+int(facilities_posn_list[i][j][1]/28.57)))
                    screen.blit(Map_images[i],posn)
        
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
