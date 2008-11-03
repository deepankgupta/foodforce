import pickle
output = open('graphics_layout.pkl', 'wb')

# DICTIONARIES REGARDING RESOURCES REQD TO BUILD EACH FACILITY PER BUILDING

House_tiles_list = []
pickle.dump(House_tiles_list, output)
Hospital_tiles_list = []
pickle.dump(Hospital_tiles_list, output)
Farm_tiles = []
pickle.dump(Farm_tiles, output)
Workshop_tiles_list = []
pickle.dump(Workshop_tiles_list, output)
School_tiles_list = []
pickle.dump(School_tiles_list, output)
Fountain_tiles = []
pickle.dump(Fountain_tiles, output)
Earthquake_tiles = []
pickle.dump(Earthquake_tiles, output)
Man_tiles = []
pickle.dump(Man_tiles, output)
Woman_tiles = []
pickle.dump(Woman_tiles, output)
Boy_tiles = []
pickle.dump(Boy_tiles, output)
Girl_tiles = []
pickle.dump(Girl_tiles, output)
Map_images = []
pickle.dump(Map_images, output)

# Saving the positions of all the facilities
workshop_posn_list = [(200,2550),(2000,5000),  (6500,400),  (6000,5300)]
pickle.dump(workshop_posn_list, output)
house_posn_list = [(800,2000),(1000,2600),(1400,3300),(2000,2000),(2000,2600),  (2800,3800),(3800,3800),(3200,4500),  (5200,500),(4600,1100),(5500,1100),(6200,1600),(5000,1800),(5800,2200),(5200,2500),  (5000,3600),(5800,3500),(6500,3300),(6000,4100),(6750,3800),(6900,4500)]
pickle.dump(house_posn_list, output)
hospital_posn_list = [(1400,3900), (7700,2200), (4500,4200)]
pickle.dump(hospital_posn_list, output)
school_posn_list = [(2700,2000), (6100,2500), (7200,3000)]
pickle.dump(school_posn_list, output)
farm_posn_list = [(300,500),(3000,500), (7400,800), (7500,3600)]
pickle.dump(farm_posn_list, output)
fountain_posn_list = [(2100,1200),(2200,3000),(3600,3500), (4500,1800),(6900,2000), (5900,3000),(6000,4800)]
pickle.dump(fountain_posn_list, output)

facilities_posn_list = [house_posn_list,school_posn_list,hospital_posn_list,workshop_posn_list,farm_posn_list,fountain_posn_list]
pickle.dump(facilities_posn_list, output)
# Saving the attributes for the villagers with each facility
workshop_villagers = [ [ ('Man',(0,2400,1200,1500)), ('Man',(0,2400,1200,1500)) ], [ ('Man',(1500,4500,1200,1500)), ('Man',(1500,4500,1200,1500)) ], [ ('Man',(6200,0,1200,1500)), ('Man',(6200,0,1200,1500)) ], [ ('Man',(5500,4500,1200,1500)), ('Man',(5500,4500,1200,1500)) ] ]
pickle.dump(workshop_villagers, output)
house_villagers = [ [ ('Woman',(600,1800,2400,2000)), ('Woman',(600,1800,2400,2000)), ('Woman',(600,1800,2400,2000)), ('Boy',(600,1800,2400,2000)), ('Boy',(600,1800,2400,2000)), ('Girl',(600,1800,2400,2000)), ('Girl',(600,1800,2400,2000)) ],[],[],[],[], [ ('Woman',(2500,3500,2000,2000)), ('Woman',(2500,3500,2000,2000)), ('Boy',(2500,3500,2000,2000)), ('Girl',(2500,3500,2000,2000))],[],[], [ ('Man',(4500,0,2500,3000)), ('Woman',(4500,0,2500,3000)), ('Girl',(4500,0,2500,3000)), ('Girl',(4500,0,2500,3000)), ('Boy',(4500,0,2500,3000)), ('Boy',(4500,0,2500,3000)) ],[],[],[],[],[],[], [ ('Man',(4500,3000,3500,1800)), ('Woman',(4500,3000,3500,1800)), ('Woman',(4500,3000,3500,1800)), ('Boy',(4500,3000,3500,1800)), ('Girl',(4500,3000,3500,1800)) ],[],[],[],[],[] ]
pickle.dump(house_villagers, output)
hospital_villagers = [ [ ('Man',(1000,3500,1200,1200)), ('Woman',(1000,3500,1200,1200)), ('Boy',(1000,3500,1200,1200)), ('Girl',(1000,3500,1200,1200)) ], [ ('Man',(7400,1800,1200,1200)), ('Woman',(7400,1800,1200,1200)), ('Boy',(7400,1800,1200,1200)), ('Girl',(7400,1800,1200,1200)) ], [ ('Man',(4500,4000,1200,1200)), ('Woman',(4500,4000,1200,1200)), ('Boy',(4500,4000,1200,1200)), ('Girl',(4500,4000,1200,1200)) ] ]
pickle.dump(hospital_villagers, output)
school_villagers = [ [ ('Boy',(2500,1800,1500,1500)), ('Boy',(2500,1800,1500,1500)), ('Girl',(2500,1800,1500,1500)) ], [ ('Boy',(1800,5800,1500,1500)), ('Girl',(1800,5800,1500,1500)), ('Girl',(1800,5800,1500,1500)) ], [ ('Boy',(7000,2800,1500,1500)), ('Boy',(7000,2800,1500,1500)), ('Girl',(7000,2800,1500,1500)) ] ]
pickle.dump(school_villagers, output)
farm_villagers = [ [ ('Woman',(0,0,1000,1000)), ('Man',(0,0,1000,1000)) ], [ ('Woman',(2500,0,1000,1000)), ('Man',(2500,0,1000,1000)) ], [ ('Woman',(7000,600,1000,1000)), ('Man',(7000,600,1000,1000)) ], [ ('Woman',(7000,3500,1000,1000)), ('Man',(7000,3500,1000,1000)) ] ]
pickle.dump(farm_villagers, output)
fountain_villagers = [ [],[],[],[],[],[],[] ]
pickle.dump(fountain_villagers, output)
facility_villagers = { 'WORKSHOP':workshop_villagers , 'HOUSE':house_villagers , 'HOSPITAL':hospital_villagers , 'SCHOOL':school_villagers , 'FARM':farm_villagers,'FOUNTAIN':fountain_villagers }
pickle.dump(facility_villagers, output)
output.close()
