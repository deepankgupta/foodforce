import string
import os
import sys
class initialize:
    rec_line = []    
    def _init_(self,file_name):
        self.file_name = file_name
        
    def get_data():
        file_dat = open(file_name,'r')
        dat_lines = file_dat.readlines()
        file_dat.close()
        for each_line in dat_lines:
          length = len(each_line) - 1
          if each_line[0] == '\n' or each_line[0] == '#':
            continue
          else:
            rec_line.append(each_line[0:length])
            
    def ini_val_facility():
        COST_HOUSE = {rec_line[0] : float(rec_line[1]),rec_line[2] : float(rec_line[3]),rec_line[4] : float(rec_line[5]}  

def init_val():
    global COST_HOUSE
    init_obj = initialize("initial.ini")
    init_obj.get_data()
    init_obj.ini_val_facility()
    print COST_HOUSE

def main():
    init_val()

if __name__ == "__main__" :
    main()
