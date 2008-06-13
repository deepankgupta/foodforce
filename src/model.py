#! /usr/bin/env python
#
#   Author : Deepank Gupta (deepankgupta@gmail.com)
#   Date : 25/02/2008 
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
#
#   CHANGE LOG:
#   LAST UPDATED 3/06/08
#    BY - Mohit Taneja (mohitgenii@gmail.com)
#
#   


import indicators
import facilities
import initial
import Exceptions




class Indicator:
    ''' A base class for one of the game indicators such as health, nutrition,
    and so on. Each indicator has a value e.g if health is 25% its value is 250
    and a dictionary of parameters->weight, which are
    responsible for indicator value. By parameter we mean the facilities and
    resources which affect the value of the indicator.
    '''

                                                        
    maximum_value =initial.MAX_INDICATOR 
    def __init__(self, name, value, pdict):
        ''' Constructor which takes the name, initial value of the indicator in variable value
        and pdict as a dictionary of parameters affecting the indicator
        it is assumed that the weights are the ratios i.e they are b/w 0and 1
        '''                                                                         # ASSUMPTION

        self.name = name
        self.set_value(value)
        self.set_parameters(pdict)
       
 

    def set_max(self, max_value =initial.MAX_INDICATOR):  
        ''' methods to assign maximum value that can be assigned to a indicator
        '''
     
        self.maximum_value = max_value


    # value methods

    def get_name(self):
        ''' Returns the name of the indicator
        '''

        return self.name

    def get_value(self):
        ''' Returns the value of the indicator
        '''

        return self._value

    def set_value(self, value):
        ''' Sets the value of the indicator if its greater than the maximum value
        it makes it equal to the maximum value and if it is less than 0 than makes it 0
        '''
    
        if(value <=self.maximum_value and value >= 0):
            self._value = value
        
        elif(value<0):
            self._value=0
        
        elif(value>self.maximum_value):
            self._value=self.maximum_value

    # parameter  methods

    def set_parameters(self, pdict):
        ''' Initializes the parameters dictionary that affects the value of an indicator
        '''
    
        self._parameters = pdict

    def get_parameters(self):
        '''get parameters'''
        return self._parameters

                           
    def add_parameter(self, parameter, weight):                                
        '''adds a new parameter to the dictionary, if a parameter and its value is passed
        to the function
        '''
    
        self._parameters[parameter] = weight
  

    def rem_parameter(self, parameter):
        '''to remove a parameter from the dictionary
        '''
    
        del self._parameters[parameter]


    def change_weight(self, parameter, weight):
        '''This function is called to change the weight of a particular parameter.
        '''
     
        self._parameters[parameter] = weight
        
 
    def turn(self, parameter_values):
        '''This function is called to update the value after a turn.
        parameter_values is a dictionary of parameters and there values.
        The value of an indicator depends only on the instantaneous value of the parameters.
        The values that are passed in this dictionary should be the
        (value of the parameter)/(maximum value of parameter)
        '''            
                                                             # ASSUMPTION
        self._value = 0
        for key in parameter_values.keys():

            if(self._parameters.has_key(key)):
                self._value += parameter_values[key] * self._parameters[key] * self.maximum_value

            if(self._value>self.maximum_value):
                self._value = self.maximum_value

            if(self._value<0):
                self._value=0
            
        return self._value


class Facility:
    ''' A base class for game facilities as school, hospital and so on.
    * Each facility can have one or more buildings. 
    * Each facility has levels of building, that uses differents amounts of
    resources to be achieved.
    * Each facility spends a resource list on each turn
    * Each facility produces a resource list on each turn
    level : The level of the buildings of a particular type
    number : The number of buildings of that facility type.
    cost_build : list of amount of resources used to build a building
    cost_inc_level : list of amount of resources required to increase the
    level of building.
    production : list of amount of resources produced by the facility
    consumption : list of amount of resources consumed by the facility
    LEVEL_INCR_PROD : Percentage of increase in production with each level
    wrt base_production.
    LEVEL_INCR_CONS : Percentage of increase in consumption with each level
    wrt base_production.
    '''
     
  

    def __init__(self, name, cost_build, cost_inc_level, base_production, base_consumption, level = 0, number = 0, LEVEL_INCREASE_PROD = facilities.LEVEL_INCR_PROD, LEVEL_INCREASE_CONS=facilities.LEVEL_INCR_PROD):
        ''' Constructor that takes parameters as name of the facility, cost to build that
        facility, cost to increase the level of an already settled facility, base
        production as a dictionary of the resources being produced by the facility
        and base consumption as the resources being consumed by the facility. level is by
        default initialised to 0 and number of installations to 0.
        '''

        self._name = name
        self._level = level
        self._number = number
        self.set_cost_build(cost_build)
        self.set_cost_inc_level(cost_inc_level)
        self.set_production(base_production)
        self.set_consumption(base_consumption)
        self.level_incr_prod = LEVEL_INCREASE_PROD
        self.level_incr_cons = LEVEL_INCREASE_CONS
        

    def get_name(self):
        ''' Returns the name of the facility
        THE NAME OF THE FACILITY SHOULD BE THE SAME AS THATS GIVEN IN facilities_constants.py
        IN DICTIONARY THATS GIVEN IN FACILITY_MANP_DICT A TODO OR AN ASSUMPTION FOR CONTROLLER
        '''                                                                   #ASSUMPTION

        return self._name
    
    def get_number(self):
        '''returns the number of facilites'''
        return self._number

    def get_level(self):
        '''returns level of facility'''    
        return self._level   

    def get_level_incr_prod(self):
        '''returns realtive increase in level of production'''
        return self.level_incr_prod

    def get_level_incr_cons(self):
        '''returns relative increse in level of consumption'''
        return self.level_incr_cons

    def set_cost_build(self, cost_build):
        ''' Sets the cost to build a facility if one needs to change the value that has
        been initialised by the constructor
        '''

        self.cost_build = cost_build
    
    def get_cost_build(self):
        ''' get cost of building a facility'''
        return self.cost_build

    def set_manp_req_build(self, manp_req_build):
        ''' Sets the manpower requirement to build a facility
        '''

        self.manp_req_build = manp_req_build

    def set_manp_rq_run(self, manp_req_run):
        ''' Sets the manpower requirement to run a facility
        '''

        self.manp_req_run = manp_req_run

    def set_cost_inc_level(self, cost_inc_level):
        ''' Sets the cost to increase the level of a facility that has been installed
        if one needs to change the value that has been initialised by the constructor
        '''
        
        self.cost_inc_level = cost_inc_level
    
    def get_cost_inc_level(self):
        '''returns increase in cost with updation in level'''
        return self.cost_inc_level
    #Production and consumption methods. 

    def set_production(self, base_production):
        ''' initialises the base production value of resources due to a facility
        '''
        
        self.base_production = base_production

    def set_consumption(self, base_consumption):
        ''' initialises the base consumption value of a resource due to a facility
        '''

        self.base_consumption = base_consumption

    def add_production(self, name, value):
        ''' adds a new key to the dictionary of resources being produced by the facility
        '''
        
        self.base_production[name] = value

    def rem_production(self, name):
        ''' removes a key from the dictionary of resources being produced by the facility
        '''
        
        del self.base_production[name]

    def get_prod_dict(self):
        '''returns production dictionary'''
        return self.base_production
    
    def get_cons_dict(self):
        '''returns consumption dictionary'''
        return self.base_consumption

    def get_production(self):
        ''' Returns the resourceas produecd by a facility.
        Multiply base_production with number of installations and add to it the
        extra amt of resources produced due to upgradation of the level of facility
        Multiply level * base_consumption * self. level_inr_prod
        '''
        
        production = {}
        
        for key in self.base_production.keys():
            production[key]=self._number * self.base_production[key] + (self.base_production[key] * self._number * self.level_incr_prod * self._level)
        return production

    def add_consumption(self, name, value):
        ''' adds a new key to the dictionary of resources being consumed by the facility
        '''

        self.base_consumption[name] = value

    def rem_consumption(self, name):
        ''' removes a key from the dictionary of resources being consumed by the facility
        '''
        
        del self.base_consumption[name]

    def get_consumption(self):
        ''' Returns the amt of resources consumed by the facility.
        Multiply base_consumption with number of installations and add to it the
        extra amt of resources being produced due to the upgradation of level of facility
        Multiply level * base_consumption * self.level_incr_cons
        '''
        consumption = {}
        for key in self.base_consumption.keys():
            consumption[key]=self._number * self.base_consumption[key] + (self.base_consumption[key] * self._number * self.level_incr_cons * self._level)
        return consumption


    #Other Methods

    def update_level(self, resources):
        ''' Updates the level of facility installed, all the buildings of a facility installed
        are upgraded at the same time. First check whether the resources are sufficient. If yes
        then upgrade and return the dictionary of the resources that are required for upgradation.
        If not then raises an exception.
        '''
        
        for i in range(len(resources)):
            name = resources[i].get_name()
            if self.cost_inc_level.has_key(name):
                if resources[i].get_vquantity() < self.cost_inc_level[name]:
                    raise Exceptions.Resources_Underflow_Exception
                else:
                    resources[i].change_vquantity(-self.cost_inc_level[name])
        if self._level == initial.MAX_LEVELS_FACILITY:
            raise Exceptions.Maximum_Level_Reached
        self._level += 1
        return resources

    def build_start(self, resources , people_obj):
        ''' Starts Building a new installation of a facility. Check whether the resources are sufficient.
        If yes than adds one to the no. of installations.If not then raises an exception
        also it returns a dictionary of resources with their values that are required to build the facility
        '''
        
        for i in range(len(resources)):
            name = resources[i].get_name()
            if self.cost_build.has_key(name):
                if resources[i].get_vquantity() < self.cost_build[name]:
                    raise Exceptions.Resources_Underflow_Exception
                else:
                    resources[i].change_vquantity(-self.cost_build[name])
        if self.check_manp_res(people_obj) < 0:
            raise Exceptions.Low_Manpower_Resources_Exception
        return resources

    def build_end(self, people_obj):
        ''' Changes the manpower distribution that occurs when a building has been finished its construction.
        It takes an object of class people and returns the same object with the updated population distribution.
        '''
        
        self.dict_res_build =facilities.FACILITY_MANP_DICT_BUILD[self._name]
        change = -self.dict_res_build['EMPLOYED PEOPLE IN CONSTRUCTION']
        people_obj.change_no_of_ppl_emp_in_cons(change)
        self._number = self._number + 1
        return people_obj

    def stop_facility(self):
        ''' Used to temporarily stop a facility in case the resources that are required to run a facility
        are low the facility can be resumed when sufficient resources are available using resume_facility()
        '''

        self.temp_number = self._number
        self.temp_level = self._level
        self._number = 0
        self._level = 0

    def resume_facility(self):
        ''' Used to resume a facility that was temporarily stopped using stop_facility()
        '''

        self._number = self.temp_number
        self._level = self.temp_level

        
    def demolish(self , people_obj):
        ''' Note that the demolish function is not taking any resources but releases the manpower
        allocated to run the facility. It takes an object of class people and returns the same object
        with the updated population distribution.
        '''
        
        self._number = self._number - 1
        
        self.dict_res_run =facilities.FACILITY_MANP_DICT_RUN[self._name]
        self.manp_dist_dict = MANP_DIST_DICT

        for keying in self.manp_dist_dict.keys():
            if self.dict_res_run.has_key(keying):
                self.manp_dist_dict[keying] = -self.dict_res_run[keying]

        people_obj.change_population_dist(self.manp_dist_dict['TOTAL POPULATION'], self.manp_dist_dict['SHELTERED PEOPLE'], self.manp_dist_dict['EDUCATED PEOPLE'], self.manp_dist_dict['HEALTHY PEOPLE'], self.manp_dist_dict['PEOPLE FED'], self.manp_dist_dict['EMPLOYED PEOPLE IN CONSTRUCTION'], self.manp_dist_dict['EMPLOYED PEOPLE IN HOSPITAL'], self.manp_dist_dict['EMPLOYED PEOPLE IN SCHOOL'], self.manp_dist_dict['EMPLOYED PEOPLE IN WORKSHOP'], self.manp_dist_dict['EMPLOYED PEOPLE IN FARM'])

        return people_obj

    def turn(self, resources):
        ''' Updates the resources allocated to the village by increasing the value of resources that
        have been produced in the current turn and decreasing the value of the resources that have
        been consumed by the facility
        '''

        production = self.get_production()
        consumption = self.get_consumption()
        
        for i in range(len(resources)):
            name = resources[i].get_name()
            if production.has_key(name):
                resources[i].change_vquantity(production[name])
            if consumption.has_key(name):
                if resources[i].get_vquantity() >= consumption[name]:
                    resources[i].change_vquantity(-consumption[name])
                else:
                    raise Exceptions.Resources_Underflow_Exception

        return resources

    def update_manp_res(self, people_obj):
        ''' Updates the manpower resources if available to build a facility.
        It takes an object of class people and returns the same object with the
        updated population distribution
        '''

        self.dict_res_build = facilities.FACILITY_MANP_DICT_BUILD[self._name]
        self.dict_res_run = facilities.FACILITY_MANP_DICT_RUN[self._name]
        self.manp_dist_dict = facilities.MANP_DIST_DICT
        self.dict_res_change = facilities.FACILITY_MANP_DICT_CH[self._name]
        for keying in self.manp_dist_dict.keys():

            if self.dict_res_build.has_key(keying):
                self.manp_dist_dict[keying] = self.dict_res_build[keying]

            if self.dict_res_run.has_key(keying):
                self.manp_dist_dict[keying] = self.dict_res_run[keying]

            if self.dict_res_change.has_key(keying):
                self.manp_dist_dict[keying] = self.dict_res_change[keying]

        people_obj.change_population_dist(self.manp_dist_dict['TOTAL POPULATION'], self.manp_dist_dict['SHELTERED PEOPLE'], self.manp_dist_dict['EDUCATED PEOPLE'], self.manp_dist_dict['HEALTHY PEOPLE'], self.manp_dist_dict['PEOPLE FED'], self.manp_dist_dict['EMPLOYED PEOPLE IN CONSTRUCTION'], self.manp_dist_dict['EMPLOYED PEOPLE IN HOSPITAL'], self.manp_dist_dict['EMPLOYED PEOPLE IN SCHOOL'], self.manp_dist_dict['EMPLOYED PEOPLE IN WORKSHOP'], self.manp_dist_dict['EMPLOYED PEOPLE IN FARM'])

        return people_obj

    def check_manp_res(self, people_obj):
        ''' Checks whether there are enough manpower resources to build a facility
        It takes an object of class people which stores the current population distribution
        it returns value >= 0 if the facility can be settled else returns value < 0
        '''

        people_req = 0
        self.dict_res_build = facilities.FACILITY_MANP_DICT_BUILD[self._name]
        self.dict_res_run = facilities.FACILITY_MANP_DICT_RUN[self._name]

        for keying in self.dict_res_build.keys():
            people_req += self.dict_res_build[keying]

        for keying in self.dict_res_run.keys():
            people_req += self.dict_res_run[keying]

        return people_obj.get_total_no_of_ppl_un_emp() - people_req








    
class Resource:
    '''A class for game resources such as food, books and so on. 
    The game will contain two quanitities of resources. One for the market.
    Other for the village. The market quantity will also determine
    buying and selling prices for every resource.
    MAX_RES_VAL : It is the maximum amount/quantity of resource that a
    village can hold. Market can hold any amount of any resource
    PRICE_VARIATION : It is the amount of variation that can occur in prices.
    Note that buying price and selling price are wrt village and not market. 
    '''



    def __init__(self, name, v_quantity, m_quantity, price, MAX_RESOURCE_VAL_VILLAGE = initial.MAX_RES_VAL_VILLAGE, MAX_RESOURCE_VAL_MARKET = initial.MAX_RES_VAL_MARKET ,PRICE_VAR = initial.PRICE_VARIATION):
        self._name = name
        self.vquantity = v_quantity
        self.mquantity = m_quantity
        self.price = price
        self.initial_price = price
        self.max_res_value_village = MAX_RESOURCE_VAL_VILLAGE
        self.max_res_value_market = MAX_RESOURCE_VAL_MARKET
        self.max_price_variation = PRICE_VAR


    def get_name(self):
        ''' Returns the name of the resource
        '''
        
        return self._name

    #Quantity related methods.  

    def set_vquantity(self, quantity):
        ''' Sets the quantity of the resource present in the village
        '''

        if quantity > self.max_res_value_village:
            self.vquantity = self.max_res_value_village
            raise Exceptions.Resources_Overflow_Exception
        if quantity < 0:
            raise Exceptions.Resources_Underflow_Exception
        
        self.vquantity = quantity

    def get_vquantity(self):
        '''Returns the quantity of resource present in the village
        '''
        
        return self.vquantity

    def set_mquantity(self, quantity):
        ''' Sets the quantity of the resource present in the market
        '''

        if quantity > self.max_res_value_market:
            self.mquantity = self.max_res_value_market
            raise Exceptions.Resources_Overflow_Exception
        if quantity < 0:
            raise Exceptions.Resources_Underflow_Exception
        
        self.mquantity = quantity

    def get_mquantity(self):
        ''' Returns the quantity of the resource present in the market
        '''
        
        return self.mquantity

    def change_vquantity(self, change):
        ''' Changes the quantity of resource present in the village
        '''

        if (self.vquantity + change) > self.max_res_value_village:
            self.vquantity = self.max_res_value_village
            raise Exceptions.Resources_Overflow_Exception
        if (self.vquantity + change) < 0:
            raise Exceptions.Resources_Underflow_Exception
        
        self.vquantity = self.vquantity + change

    def change_mquantity(self, change):
        ''' Changes the quantity of resource present in the market
        '''
        
        if (self.mquantity + change) > self.max_res_value_market:
            self.mquantity = self.max_res_value_market
            raise Exceptions.Resources_Overflow_Exception
        if (self.mquantity + change) < 0:
            raise Exceptions.Resources_Underflow_Exception
        
        self.mquantity = self.mquantity + change

    #Price related methods
        
    def get_price(self):
        ''' Returns the price of the resource
        '''

        return self.price

    def set_price(self, new_price):
        ''' Sets a new price for the resource
        '''

        self.price = new_price

    def change_price(self, change):
        ''' Changes the price of a resource
        '''

        if change > self.max_price_variation:
            change = self.max_price_variation
        self.price += change

    def update_price(self):
        ''' Updates the price of a resource in accordance with the market forces
        '''

        self.price = self.initial_price + (((self.max_res_value_village/2 - self.vquantity)/self.max_res_value_village) * self.max_price_variation) + (((self.max_res_value_market/2 - self.mquantity)/self.max_res_value_market) * self.max_price_variation)           
        
        if self.price < 0:
            self.price = 0
        
    #Buy and sell methods

    def buy(self, quantity, money):
        ''' This method is used to buy resources from the market.
        It takes quantity that is to be bought and the total money present
        with the village as parameters. It generates exception when the market
        resources are less than that to be bought or if the village doesnot have
        enough money to buy the resources. returns the cost to buy the resources
        '''
        
        if quantity > self.mquantity:
            raise Exceptions.Resources_Underflow_Exception
        buy_price = self.price
        cost = quantity * buy_price
        if cost < money.get_money():
            self.change_vquantity(quantity)
            self.change_mquantity(-quantity)
            money.change_money(-cost)
            return money
        else:
            raise Exceptions.Money_Underflow_Exception

    def sell(self, quantity, money):
        ''' This method is used to sell resources to the market
        It generates an exeption when the village has less resources
        than what is demanded to sell. returns the cost that the village
        gets by selling the resources
        '''
        if quantity > self.vquantity:
            raise Exceptions.Resources_Underflow_Exception
        sell_price = self.price
        cost = quantity * sell_price
        self.change_vquantity(-quantity)
        self.change_mquantity(quantity)
        money.change_money(cost)
        return money



class People:
    ''' A Class which manages the population of the village. The population has been
    classified on the basis of educated/or not, whether the person is provided food or
    not i.e he is fed or not , also on the basis of whther the person is employed or not
    and if he is employed than in which profession is he employed
    '''

    def __init__(self, total_population, no_of_ppl_sheltered, no_of_ppl_educated, no_of_ppl_healthy, no_of_ppl_fed, no_of_ppl_emp_in_cons, no_of_ppl_emp_in_hospital, no_of_ppl_emp_in_school, no_of_ppl_emp_in_workshop, no_of_ppl_emp_in_farm):
        ''' Constructor which initialises the initial population distribution
        '''

        self.total_population = total_population
        self.no_of_ppl_sheltered = no_of_ppl_sheltered
        self.no_of_ppl_educated = no_of_ppl_educated
        self.no_of_ppl_healthy = no_of_ppl_healthy
        self.no_of_ppl_fed = no_of_ppl_fed
        self.no_of_ppl_emp_in_cons = no_of_ppl_emp_in_cons
        self.no_of_ppl_emp_in_hospital = no_of_ppl_emp_in_hospital
        self.no_of_ppl_emp_in_school = no_of_ppl_emp_in_school
        self.no_of_ppl_emp_in_workshop = no_of_ppl_emp_in_workshop
        self.no_of_ppl_emp_in_farm = no_of_ppl_emp_in_farm
        self.total_no_of_ppl_emp = self.no_of_ppl_emp_in_cons + self.no_of_ppl_emp_in_hospital + self.no_of_ppl_emp_in_school + self.no_of_ppl_emp_in_workshop + self.no_of_ppl_emp_in_farm
        self.total_no_of_ppl_un_emp = self.total_population - self.total_no_of_ppl_emp
        self.check_bounds()
    # Methods to assign a value to the population distribution

    def set_population_dist(self, total_population , no_of_ppl_sheltered , no_of_ppl_educated , no_of_ppl_healthy , no_of_ppl_fed , no_of_ppl_emp_in_cons , no_of_ppl_emp_in_hospital , no_of_ppl_emp_in_school , no_of_ppl_emp_in_workshop , no_of_ppl_emp_in_farm ):
        ''' Changes the population distribution
        '''
               
        self.total_population = total_population
        self.no_of_ppl_sheltered = no_of_ppl_sheltered
        self.no_of_ppl_educated = no_of_ppl_educated
        self.no_of_ppl_healthy = no_of_ppl_healthy
        self.no_of_ppl_fed = no_of_ppl_fed
        self.no_of_ppl_emp_in_cons = no_of_ppl_emp_in_cons
        self.no_of_ppl_emp_in_hospital = no_of_ppl_emp_in_hospital
        self.no_of_ppl_emp_in_school = no_of_ppl_emp_in_school
        self.no_of_ppl_emp_in_workshop = no_of_ppl_emp_in_workshop
        self.no_of_ppl_emp_in_farm = no_of_ppl_emp_in_farm
        self.total_no_of_ppl_emp = self.no_of_ppl_emp_in_cons + self.no_of_ppl_emp_in_hospital + self.no_of_ppl_emp_in_school + self.no_of_ppl_emp_in_workshop + self.no_of_ppl_emp_in_farm
        self.total_no_of_ppl_un_emp = self.total_population - self.total_no_of_ppl_emp
        self.check_bounds()

    def set_total_population(self, total_population):
        ''' Changes the total population to a new value
        '''

        self.total_population = total_population
        self.check_bounds()

    def set_no_of_ppl_sheltered(self, no_of_ppl_sheltered):
        ''' Changes the number of people sheltered to a new value
        '''
    
        self.no_of_ppl_sheltered = no_of_ppl_sheltered
        self.check_bounds()

    def set_no_of_ppl_educated(self, no_of_ppl_educated):
        ''' Changes the no of people educated to a new value
        '''

        self.no_of_ppl_educated = no_of_ppl_educated
        self.check_bounds()

    def set_no_of_ppl_healthy(self, no_of_ppl_healthy):
        ''' Changes the no of people healthy to a new value
        '''
 
        self.no_of_ppl_healthy = no_of_ppl_healthy
        self.check_bounds()

    def set_no_of_ppl_fed(self, no_of_ppl_fed):
        ''' Changes the no of people fed to a new value
        '''

        self.no_of_ppl_fed = no_of_ppl_fed
        self.check_bounds()

    def set_no_of_ppl_emp_in_cons(self, no_of_ppl_emp_in_cons):
        ''' Changes the no of people employed in construction to a new value
        '''

        self.no_of_ppl_emp_in_cons = no_of_ppl_emp_in_cons
        self.update_total_no_of_ppl_employed()
        self.check_bounds()

    def set_no_of_ppl_emp_in_hospital(self, no_of_ppl_emp_in_hospital):
        ''' Changes the no of people employed in hospitals to a new value
        '''
 
        self.no_of_ppl_emp_in_hospital = no_of_ppl_emp_in_hospital
        self.update_total_no_of_ppl_employed()
        self.check_bounds()

    def set_no_of_ppl_emp_in_school(self, no_of_ppl_emp_in_school):
        ''' Changes the no of people employed in school to a new value
        '''

        self.no_of_ppl_emp_in_school = no_of_ppl_emp_in_school
        self.update_total_no_of_ppl_employed()
        self.check_bounds()

    def set_no_of_ppl_emp_in_workshop(self, no_of_ppl_emp_in_workshop):
        ''' Changes the no of people employed in workshop to a new value
        '''

        self.no_of_ppl_emp_in_workshop = no_of_ppl_emp_in_workshop
        self.update_total_no_of_ppl_employed()
        self.check_bounds()

    def set_no_of_ppl_emp_in_farm(self, no_of_ppl_emp_in_farm):
        ''' Changes the no of people employed in farm to a new value
        '''

        self.no_of_ppl_emp_in_farm = no_of_ppl_emp_in_farm
        self.update_total_no_of_ppl_employed()
        self.check_bounds()

    def set_total_no_of_ppl_emp(self, total_no_of_ppl_emp):
        ''' Changes the total no of people employed to a new value
        '''

        self.total_no_of_ppl_emp = total_no_of_ppl_emp
        self.total_no_of_ppl_un_emp = self.total_population - self.total_no_of_ppl_emp
        self.check_bounds()

    # Method definitions to change the value of population distribution


    def change_population_dist(self, change_in_total_population = 0, change_in_no_of_ppl_sheltered = 0, change_in_no_of_ppl_educated = 0, change_in_no_of_ppl_healthy = 0, change_in_no_of_ppl_fed = 0, change_in_no_of_ppl_emp_in_cons = 0, change_in_no_of_ppl_emp_in_hospital = 0, change_in_no_of_ppl_emp_in_school = 0, change_in_no_of_ppl_emp_in_workshop = 0, change_in_no_of_ppl_emp_in_farm = 0):
        ''' Changes the population distribution
        '''
        self.total_population += change_in_total_population
        self.no_of_ppl_sheltered += change_in_no_of_ppl_sheltered
        self.no_of_ppl_educated += change_in_no_of_ppl_educated
        self.no_of_ppl_healthy += change_in_no_of_ppl_healthy
        self.no_of_ppl_fed += change_in_no_of_ppl_fed
        self.no_of_ppl_emp_in_cons += change_in_no_of_ppl_emp_in_cons
        self.no_of_ppl_emp_in_hospital += change_in_no_of_ppl_emp_in_hospital
        self.no_of_ppl_emp_in_school += change_in_no_of_ppl_emp_in_school
        self.no_of_ppl_emp_in_workshop += change_in_no_of_ppl_emp_in_workshop
        self.no_of_ppl_emp_in_farm += change_in_no_of_ppl_emp_in_farm
        self.total_no_of_ppl_emp = self.no_of_ppl_emp_in_cons + self.no_of_ppl_emp_in_hospital + self.no_of_ppl_emp_in_school + self.no_of_ppl_emp_in_workshop + self.no_of_ppl_emp_in_farm
        self.total_no_of_ppl_un_emp = self.total_population - self.total_no_of_ppl_emp
        self.check_bounds()



    def change_total_population(self, change_in_total_population):
        ''' Changes the total population 
        '''

        self.total_population += change_in_total_population
        self.check_bounds()

    def change_no_of_ppl_sheltered(self, change_in_no_of_ppl_sheltered):
        ''' Changes the number of people sheltered 
        '''
    
        self.no_of_ppl_sheltered += change_in_no_of_ppl_sheltered
        self.check_bounds()

    def change_no_of_ppl_educated(self, change_in_no_of_ppl_educated):
        ''' Changes the no of people educated 
        '''

        self.no_of_ppl_educated += change_in_no_of_ppl_educated
        self.check_bounds()

    def change_no_of_ppl_healthy(self, change_in_no_of_ppl_healthy):
        ''' Changes the no of people healthy 
        '''

        self.no_of_ppl_healthy += change_in_no_of_ppl_healthy
        self.check_bounds()

    def change_no_of_ppl_fed(self, change_in_no_of_ppl_fed):
        ''' Changes the no of people fed 
        '''

        self.no_of_ppl_fed += change_in_no_of_ppl_fed
        self.check_bounds()

    def change_no_of_ppl_emp_in_cons(self, change_in_no_of_ppl_emp_in_cons):
        ''' Changes the no of people employed in construction 
        '''
 
        self.no_of_ppl_emp_in_cons += change_in_no_of_ppl_emp_in_cons
        self.update_total_no_of_ppl_employed()
        self.check_bounds()

    def change_no_of_ppl_emp_in_hospital(self, change_in_no_of_ppl_emp_in_hospital):
        ''' Changes the no of people employed in hospitals 
        '''

        self.no_of_ppl_emp_in_hospital += change_in_no_of_ppl_emp_in_hospital
        self.update_total_no_of_ppl_employed()
        self.check_bounds()

    def change_no_of_ppl_emp_in_school(self, change_in_no_of_ppl_emp_in_school):
        ''' Changes the no of people employed in school 
        '''

        self.no_of_ppl_emp_in_school += change_in_no_of_ppl_emp_in_school
        self.update_total_no_of_ppl_employed()
        self.check_bounds()

    def change_no_of_ppl_emp_in_workshop(self, change_in_no_of_ppl_emp_in_workshop):
        ''' Changes the no of people employed in workshop 
        '''

        self.no_of_ppl_emp_in_workshop += change_in_no_of_ppl_emp_in_workshop
        self.update_total_no_of_ppl_employed()
        self.check_bounds()

    def change_no_of_ppl_emp_in_farm(self, change_in_no_of_ppl_emp_in_farm):
        ''' Changes the no of people employed in farm 
        '''

        self.no_of_ppl_emp_in_farm += change_in_no_of_ppl_emp_in_farm
        self.update_total_no_of_ppl_employed()
        self.check_bounds()

    def change_total_no_of_ppl_emp(self, change_in_total_no_of_ppl_emp):
        ''' Changes the total no of people employed 
        '''
 
        self.total_no_of_ppl_emp += total_no_of_ppl_emp
        self.check_bounds()


    def update_total_no_of_ppl_employed(self):
        ''' Updates the total number of people employed 
        '''

        self.total_no_of_ppl_emp = self.no_of_ppl_emp_in_cons + self.no_of_ppl_emp_in_hospital + self.no_of_ppl_emp_in_school + self.no_of_ppl_emp_in_workshop + self.no_of_ppl_emp_in_farm
        self.total_no_of_ppl_un_emp = self.total_population - self.total_no_of_ppl_emp
        self.check_bounds()

    # Method definitions that return the population distribution

    def get_total_population(self):
        ''' Returns the value of total population 
        '''

        return self.total_population 

    def get_no_of_ppl_sheltered(self):
        ''' Returns the number of people sheltered 
        '''
    
        return self.no_of_ppl_sheltered 

    def get_no_of_ppl_educated(self):
        ''' Returns the no of people educated 
        '''

        return self.no_of_ppl_educated 

    def get_no_of_ppl_healthy(self):
        ''' Returns the no of people healthy 
        '''

        return self.no_of_ppl_healthy 

    def get_no_of_ppl_fed(self):
        ''' Returns the no of people fed 
        '''

        return self.no_of_ppl_fed 

    def get_no_of_ppl_emp_in_cons(self):
        ''' Returns the no of people employed in construction 
        '''

        return self.no_of_ppl_emp_in_cons 
        
    def get_no_of_ppl_emp_in_hospital(self):
        ''' Returns the no of people employed in hospitals 
        '''

        return self.no_of_ppl_emp_in_hospital 
        
    def get_no_of_ppl_emp_in_school(self):
        ''' Returns the no of people employed in school 
        '''

        return self.no_of_ppl_emp_in_school 
        
    def get_no_of_ppl_emp_in_workshop(self):
        ''' Returns the no of people employed in workshop 
        '''

        return self.no_of_ppl_emp_in_workshop 
        
    def get_no_of_ppl_emp_in_farm(self):
        ''' Returns the no of people employed in farm 
        '''

        return self.no_of_ppl_emp_in_farm 
        
    def get_total_no_of_ppl_emp(self):
        ''' Returns the total no of people employed 
        '''

        return self.total_no_of_ppl_emp

    def get_total_no_of_ppl_un_emp(self):
        ''' Returns total number of people unemployed
        '''

        return self.total_no_of_ppl_un_emp
    
    # Method to check Bounds
    
    def check_bounds(self):
        ''' Method to check bounds on all the variables regarding population distribution
        '''
        if(self.no_of_ppl_sheltered > self.total_population):
            self.no_of_ppl_sheltered = self.total_population
        if(self.no_of_ppl_sheltered < 0):
            self.no_of_ppl_sheltered = 0
    
        if(self.no_of_ppl_educated > self.total_population):
            self.no_of_ppl_educated = self.total_population
        if(self.no_of_ppl_educated < 0):
            self.no_of_ppl_educated = 0
    
        if(self.no_of_ppl_healthy > self.total_population):
            self.no_of_ppl_healthy = self.total_population
        if(self.no_of_ppl_healthy < 0):
            self.no_of_ppl_healthy = 0
    
        if(self.no_of_ppl_fed > self.total_population):
            self.no_of_ppl_fed = self.total_population
        if(self.no_of_ppl_fed < 0):
            self.no_of_ppl_fed = 0
    
        if(self.no_of_ppl_emp_in_cons > self.total_population):
            self.no_of_ppl_emp_in_cons = self.total_population
        if(self.no_of_ppl_emp_in_cons < 0):
            self.no_of_ppl_emp_in_cons = 0
    
        if(self.no_of_ppl_emp_in_hospital > self.total_population):
            self.no_of_ppl_emp_in_hospital = self.total_population
        if(self.no_of_ppl_emp_in_hospital < 0):
            self.no_of_ppl_emp_in_hospital = 0
    
        if(self.no_of_ppl_emp_in_school > self.total_population):
            self.no_of_ppl_emp_in_school = self.total_population
        if(self.no_of_ppl_emp_in_school < 0):
            self.no_of_ppl_emp_in_school = 0
    
        if(self.no_of_ppl_emp_in_workshop > self.total_population):
            self.no_of_ppl_emp_in_workshop = self.total_population
        if(self.no_of_ppl_emp_in_workshop < 0):
            self.no_of_ppl_emp_in_workshop = 0

        if(self.no_of_ppl_emp_in_farm > self.total_population):
            self.no_of_ppl_emp_in_farm = self.total_population
        if(self.no_of_ppl_emp_in_farm < 0):
            self.no_of_ppl_emp_in_farm = 0
            
        if(self.total_no_of_ppl_emp > self.total_population):
            self.total_no_of_ppl_emp = self.total_population
        if(self.total_no_of_ppl_emp < 0):
            self.total_no_of_ppl_emp = 0

        if(self.total_no_of_ppl_un_emp > self.total_population):
            self.total_no_of_ppl_un_emp = self.total_population
        if(self.total_no_of_ppl_un_emp < 0):
            self.total_no_of_ppl_un_emp = 0
         
    def update_turn(self,resources,facilities_list):
        ''' Method to calculate the amount of food items consumed by the manpower and the
        water consumption make the changes in resources and then return resources only
        '''

        food = 0.0                    

        for i in range(len(resources)):
            name = resources[i].get_name()
            temp=facilities.FOOD_DIST_DICT
            if temp.has_key(name):
                temp[name]=resources[i].get_vquantity()
                food+=temp[name]
        
        food_temp = food*initial.MAX_PER_FOOD_CONS/100
        
        if food_temp > (initial.FOOD_PP * self.total_population):
            food_temp = (initial.FOOD_PP) * self.total_population

        self.no_of_ppl_fed = int(food_temp/initial.FOOD_PP)
        food_temp = self.no_of_ppl_fed*initial.FOOD_PP
        ratio = food_temp/food

        for key in temp.keys():
            temp[key] -= ratio*temp[key]
        
            for i in range(len(resources)):
                name = resources[i].get_name()
                if temp.has_key(name):   
                    resources[i].set_vquantity(temp[name])

        for i in range(len(resources)):
            name = resources[i].get_name()
            if name == 'WATER':
                resources[i].change_vquantity(-ratio*resources[i].get_vquantity())

        for i in range(len(facilities_list)):
            name = facilities_list[i].get_name()
            if name == 'HOUSING':
                self.no_of_ppl_sheltered = facilities_list[i].get_number() * facilities.MANP_CH_HOUSE['SHELTERED PEOPLE']

        
        for i in range(len(facilities_list)):
            name = facilities_list[i].get_name()
            if name == 'HOSPITAL':
                self.no_of_ppl_healthy = facilities_list[i].get_number() * facilities.MANP_CH_HOSPITAL['HEALTHY PEOPLE']


        for i in range(len(facilities_list)):
            name = facilities_list[i].get_name()
            if name == 'SCHOOL':
                self.no_of_ppl_educated = facilities_list[i].get_number() * facilities.MANP_CH_SCHOOL['EDUCATED PEOPLE']

        self.check_bounds()
        return resources


        

          
       

            


class Money:
    ''' Class to manage the money present with the village
    '''

    def __init__(self,money = (initial.INIT_MONEY)):
        ''' Initialises the variable money with the initial amount which is
        to be given to the Village
        '''
        self.money = money
        self.check_bounds()

    def set_money(self, money):
        
        self.money=money
        self.check_bounds()

    def change_money(self,mchange):

        self.money +=mchange
        self.check_bounds()

    def get_money(self):

        return self.money
    
    def check_bounds(self):

        if(self.money >initial.MAX_MONEY):
            self.money =initial.MAX_MONEY
        if(self.money < 0):
            raise Exceptions.Money_Underflow_Exception
            

