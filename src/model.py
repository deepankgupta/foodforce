#! /usr/bin/env python
#
#   Author : Mohit Taneja (mohitgenii@gmail.com)
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

class Indicator:
    ''' A base class for one of the game indicators such as health, nutrition,
    and so on. Each indicator has a value e.g if health is 25% its value is 25
    and a dictionary of parameters->weight, which are
    responsible for indicator value. By parameter we mean the facilities and
    resources which affect the value of the indicator.
    '''
    
def __init__(self, value, pdict):

    ''' Constructor which takes the initial value of the indicator in variable value
    and pdict as a dictionary of resources affecting the indicator
    '''

    self.maximum_value = 999
    self.set_value(value)
    self.set_parameters(pdict)

 

def set_max(self, max_value=999):                                           # chaNGE; NEW METHOD to add bounds

    ''' methods to assign maximum value that can be assigned to a resource
    '''
    
    self.maximum_value = max_value


# value methods

def get_value(self):
    
    ''' Returns the value of the resource
    '''

    return self._value

def set_value(self, value):

    ''' Sets the value of the resource if its greater than the maximum value
    it makes it equal to the maximum value and if it is less than 0 than makes it 0
    '''
    
    if(value <= self.maximum_value and value >= 0):
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

                               
def add_parameter(self, parameter, weight):                                #earlier there was an error in this code most probably

    '''adds a new parameter to the dictionary, if a parameter and its value is passed to the function
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
    parameter_values is a dictionary of parameters and there values
    '''
    
    for key in parameter_values.keys():

        if(self._parameters.has_key(key)):
            self._value = self._value + (parameter_values[key] * self._parameters[key])

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
 
LEVEL_INCR_PROD = 0.2
LEVEL_INCR_CONS = 0.1

def __init__(self, name, cost_build, cost_inc_level, base_production, base_consumption, level = 0, number = 1, LEVEL_INCR_PROD = 0.2, LEVEL_INCR_CONS = 0.1):
    self._name = name
    self._level = level
    self._number = number
    self.set_cost_build(cost_build)
    self.set_cost_inc_level(cost_inc_level)
    self.set_production(base_production)
    self.set_consumption(base_consumption)
    Facility.LEVEL_INCR_PROD = LEVEL_INCR_PROD
    Facility.LEVEL_INCR_CONS = LEVEL_INCR_CONS

def get_name(self):
    return self._name

def set_cost_build(self, cost_build):
    self.cost_build = cost_build

def set_cost_inc_level(self, cost_inc_level):
    self.cost_inc_level = cost_inc_level

#Production and consumption methods. 
def set_production(self, base_production):
    self.base_production = base_production

def set_consumption(self, base_consumption):
    self.base_consumption = base_consumption

def add_production(self, name, value):
    self.base_production[name] = value

def rem_production(self, name):
    del self.base_production[name]

def get_production(self):
    #Multiply base_production with number.
    #Multiply level * base_consumption / 5 too.  
    for key in self.base_production.keys():
            self.production[key]=self._number * self.base_production[key] + (self.base_production[key] * Facility.LEVEL_INCR_PROD * self._level)
    return production

def get_consumption(self):
    #Multiply base_consumption with number
    #Multiply level * base_consumption * LEVEL_INCR_CONS too
    for key in self.base_consumption.keys():
            consumption[key]=self._number * self.base_consumption[key] + (self.base_consumption[key] * Facility.LEVEL_INCR_CONS * self._level)
    return consumption


def add_consumption(self, name, value):
    self.base_consumption[name] = value

def rem_consumption(self, name):
    del self.base_consumption[name]

#Other Methods
def update_level(self, resources):
    #Check whether the resources are sufficient. If not then return NULL.
    for resource in resources:
            name = resource.get_name()
            if name in self.cost_inc_level.keys():
                    if resource.get_village_quantity() < self.cost_inc_level[name]:
                            return NULL
    self._level = self._level + 1
    return self.cost_inc_level

def build(self, resources):
    #Check whether the resources are sufficient. If not then return NULL
    for resource in resources:
            name = resource.get_name()
            if name in self.cost_build.keys():
                    if resource.get_village_quantity() < self.cost_build[name]:
                            return NULL
    self._number = self._number + 1
    return self.cost_build

#Note that the demolish function is not taking or releasing any resources. 
def demolish(self):
    self._number = self._number - 1

def turn(self, resources):
    production = self.get_production()
    consumption = self.get_consumption()
    #Add production and comsumption to the list of resource objects and update their values.
    for resource in resources:
            name = resource.get_name()
            if name in production.keys():
                    resource.change_village_quantity(production[name])
            elif name in consumption.keys():
                    resource.change_village_quanitity(-consumption[name])

class Resource:
    '''A class for game resources such as food, books and so on. 
    The game will contain two quanitities of resources. One for the market.
    Other for the village. The market quantity will also determine
    buying and selling prices for every resource.
    MAX_RES_VAL : It is the maximum amount/quantity of resource that a
    village/market can hold.
    PRICE_VARIATION : It is the amount of variation that can occur in prices.
    Note that buying price and selling price are wrt village and not market. 
    '''

MAX_RES_VAL = 1000
PRICE_VARIATION = 50

def __init__(self, name, vquantity, mquantity, base_buying_price, base_selling_price, MAX_RES_VAL = 1000, PRICE_VARIATION = 50):
    self._name = name
    self.village_quantity = vquantity
    self.market_quantity = mquantity
    self.mar_buy_price = base_buying_price
    self.mar_sell_price = base_selling_price
    self.vil_buy_price = base_buying_price
    self.vil_sell_price = base_selling_price
    Resource.MAX_RES_VAL = MAX_RES_VAL
    Resource.PRICE_VARIATION = PRICE_VARIATION

#Name related methods
def get_name(self):
    return self._name

#Quantity related methods.	
def set_village_quantity(self, quantity):
    self.village_quantity = quantity

def get_village_quantity(self):
    return self.village_quantity

def set_market_quantity(self, quantity):
    self.market_quantity = quantity

def get_market_quantity(self):
    return self.market_quantity

def change_village_quantity(self, change):
    self.village_quantity = self.village_quantity + change

#Price related methods
def get_mar_buy_price(self):
    price = self.mar_buy_price + (((Resource.MAX_RES_VAL/2 - self.market_quantity)/Resource.MAX_RES_VAL) * Resource.PRICE_VARIATION)
    return price

def get_mar_sell_price(self):
    price = self.sell_price - (((Resource.MAX_RES_VAL/2 - self.market_quantity)/Resource.MAX_RES_VAL) * Resource.PRICE_VARIATION)
    return price

def get_vil_buy_price(self):
    price = self.mar_buy_price + (((Resource.MAX_RES_VAL/2 - self.village_quantity)/Resource.MAX_RES_VAL) * Resource.PRICE_VARIATION)
    return price

def get_vil_sell_price(self):
    price = self.sell_price - (((Resource.MAX_RES_VAL/2 - self.village_quantity)/Resource.MAX_RES_VAL) * Resource.PRICE_VARIATION)
    return price

#Buy and sell methods
def buy(self, quantity, money):
    if quantity > market_quantity:
            return -1
    buy_price = (self.get_vil_buy_price() + self.get_mar_sell_price()) / 2
    cost = quantity * buy_price
    if cost < money:
            self.village_quantity = self.village_quantity + quantity
            self.market_quantity = self.market_quantity - quantity
            return cost
    else:
            return -1

def sell(self, quantity):
    if quantity > village_quantity:
            return -1
    sell_price = (self.get_vil_sell_price() + self.get_mar_buy_price()) / 2
    cost = quantity * sell_price
    self.village_quantity = self.village_quantity - quantity
    self.market_quantity = self.market_quantity + quantity
    return cost
