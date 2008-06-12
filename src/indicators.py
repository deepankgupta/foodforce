#! /usr/bin/env python
#
#   Author : Mohit Taneja (mohitgenii@gmail.com)
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

# DICTIONARY OF PARAMETERS ON WHICH THE INDICATORS DEPEND WITH THEIR WEIGHT (AS RATIO)

PDICT_HOUSING = { 'SHELTERED PEOPLE' : 1 } 						      # AS NO. OF HOUSES AND LEVEL OF HOUSES ARE DIRECTLY    #	PROPORTIONAL TO NO OF PEOPLE SHELTERED 

PDICT_HEALTH = { 'HEALTHY PEOPLE' : 0.5 , 'NUTRITION' : 0.3 , 'WATER' : 0.2}                  # BY NUTRITION I MEAN THE NUTRITION INDICATOR

PDICT_NUTRITION = { 'PEOPLE FED' : 0.3 , 'PROTIENS' : 0.3 , 'FATS' : 0.1 , 'VITAMINS' : 0.3 } # WE WOULD BE REQUIRED TO CALCULATE THE AMT OF PROTIENS ETC. 												      # FROM THE VALUE OF RICE ETC. 
PDICT_EDUCATION = { 'EDUCATED PEOPLE' : 0.6 , 'LEVEL OF EDUCATION' : 0.4 }

PDICT_TRAINING = { 'LEVEL OF WORKSHOPS' : 0.4 , 'EMPLOYED PEOPLE IN WORKSHOP' : 0.25 , 'EMPLOYED PEOPLE IN FARM' : 0.2 , 'EMPLOYED PEOPLE IN HOSPITAL' : 0.1 , 'EMPLOYED PEOPLE IN CONSTRUCTION' : 0.05 }


# WELL I SUPPOSE THAT THERE ISN'T ANY NEED FOR AN INDICATOR FOR FOOD ALSO AS WE HAVE ALREADY HAD TWO INDICATORS RELATED TO IT I.E. HEALTH AND NUTRITION 
# REGARDIN FORMULA TO CALCULATE VALUE OF AN INDICATOR = SUM OF ((ALL PARAMETERS MULTIPLIED BY THEIR RESPECTIVE WEIGHTS)/THEIR MAX VALUE)*1000
# REGARDIN THE MAX VALUE OF PROTIENS AND ALL WE CAN CALCULATE IT BY ASSUMING THAT WHAT WUD HAV BEEN THE VALUE OF PROTIENS IN THE DIET IF THE USER WUD HAV     # BEEN GROWIN ONLY THAT CROP WHICH HAS THE MAX PROTIEN CONTENT AND SO ON.............    
