#! /usr/bin/env python
#
#   Author : MohitTaneja (mohitgenii@gmail.com)
#   Date : 02/06/2008 
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


# initial values of variables



# PEOPLE AND HOUSES
INI_NO_OF_HOMES = 4
INI_NO_OF_PEOPLE = 100




# FACILITIES
INI_NO_OF_HOSPITALS = 0
INI_NO_OF_WORKSHOPS = 0
INI_NO_OF_SCHOOLS = 0
INI_NO_OF_FARMS = 0
INI_NO_OF_FOUNTAINS = 0




# MONEY
INI_MONEY = 10000




# RESOURCES
INI_WATER = 100
INI_BUILDING_MATERIAL = 100
INI_TOOLS = 100
INI_MEDICINE = 100
INI_BOOKS = 0

# FOOD RESOURCES
INI_RICE = 100
INI_WHEAT = 100
INI_BEANS = 100
INI_SUGAR = 100
INI_SALT = 100
INI_OILS = 100







# INITIAL COST OF RESOURCES PER UNIT (ASSUMPTION : THE INITIAL COST OF RESOURCES IN MARKET AS WELL AS FOR THE VILLAGE IS SAME)
COST_WATER = 5
COST_BUILDING_MATERIAL = 15
COST_TOOLS = 15
COST_MEDICINE = 20
COST_BOOKS = 20

COST_RICE = 10
COST_WHEAT = 10
COST_BEANS = 12
COST_SUGAR = 8
COST_SALT = 8
COST_OILS = 12





# BOUNDS ON INDICATORS AND RESOURCES AND FACILITIES
MAX_VAL_RES = 1000
MAX_COST_VARIATION = 20
MAX_VAL_IND = 1000
MAX_NO_INS_FACILITY = 10 # MAXIMUM NO. OF INSTALLATIONS OF A FACILITY
MAX_LEVELS_FACILITY = 5  # MAXIMUM NO OF LEVELS OF A FACILITY
LEVEL_INCR_PROD = 0.2
LEVEL_INCR_CONS = 0.1




# DICTIONARIES REGARDING NUTRITIVE VALUES OF FOOD ( THEY ARE IN % )

RICE_NUTR_VALUE = { 'PROTIENS' : 30 , 'FATS' : 50 , 'VITAMINS' : 20 }
WHEAT_NUTR_VALUE = { 'PROTIENS' : 15 , 'FATS' : 70 , 'VITAMINS' : 15 }
BEANS_NUTR_VALUE = { 'PROTIENS' : 40 , 'FATS' : 20 , 'VITAMINS' : 40 }
SUGAR_NUTR_VALUE = { 'PROTIENS' : 30 , 'FATS' : 55 , 'VITAMINS' : 15 }
SALT_NUTR_VALUE = { 'PROTIENS' : 40 , 'FATS' : 10 , 'VITAMINS' : 50 }
OILS_NUTR_VALUE = { 'PROTIENS' : 35 , 'FATS' : 20 , 'VITAMINS' : 45 }
