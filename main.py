import glob
import pandas as pd
import os 

from Answer_file_generator import Answer_file_generator
from LABEL_Finder.Finder import Finder

from Csv_comparator import Csv_comparator
from LABEL_Finder.IDNUM_Finder import IDNUM_Finder
from LABEL_Finder.DOCTOR_Finder import DOCTOR_Finder
from LABEL_Finder.MEDICALRECORD_Finder import MEDICALRECORD_Finder
from LABEL_Finder.PATIENT_Finder import PATIENT_Finder
from LABEL_Finder.HOSPITAL_Finder import HOSPITAL_Finder
from LABEL_Finder.DATE_Finder import DATE_Finder
from LABEL_Finder.TIME_Finder import TIME_Finder
from LABEL_Finder.CITY_Finder import CITY_Finder
from LABEL_Finder.STREET_Finder import STREET_Finder
from LABEL_Finder.ZIP_Finder import ZIP_Finder
from LABEL_Finder.STATE_Finder import STATE_Finder
from LABEL_Finder.DEPARTMENT_Finder import DEPARTMENT_Finder
from LABEL_Finder.AGE_Finder import AGE_Finder
from LABEL_Finder.DURATION_Finder import DURATION_Finder
from LABEL_Finder.PHONE_Finder import PHONE_Finder
from LABEL_Finder.LOCATION_OTHER_Finder import LOCATION_OTHER_Finder
from LABEL_Finder.SET_Finder import SET_Finder
from LABEL_Finder.COUNTRY_Finder import COUNTRY_Finder

### all finder en
IDNUM_FINDER_EN               = 1
DOCTOR_FINDER_EN              = 1
MEDICALRECORD_FINDER_EN       = 1
PATIENT_FINDER_EN             = 1
HOSPITAL_FINDER_EN            = 1
DATE_FINDER_EN                = 1
TIME_FINDER_EN                = 1
CITY_FINDER_EN                = 1
STREET_FINDER_EN              = 1
ZIP_FINDER_EN                 = 1
STATE_FINDER_EN               = 1
DEPARTMENT_FINDER_EN          = 1
AGE_FINDER_EN                 = 1
DURATION_FINDER_EN            = 1
PHONE_FINDER_EN               = 1
LOCATION_OTHER_FINDER_EN      = 1
SET_FINDER_EN                 = 1
COUNTRY_FINDER_EN             = 1










FILE_DIR = './data/file/'
ANS_PATH = './data/file/answer.txt'
#
FILE_DIR = r'C:\Users\rui\Desktop\First_Phase_ReleaseCorrection\First_Phase_Release(Correction)\Validation_Release/'
ANS_PATH = r'C:\Users\rui\Desktop\answer_1V.txt'


file_listdir = os.listdir(FILE_DIR)
all_file_names = []
for file_name in file_listdir:
    if file_name.endswith(".txt"):  # Filter files with a .txt extension
        all_file_names.append(file_name)
# os.path.splitext(file_name)[0]

# finder  = Finder()
# finder.set_file(FILE_DIR+'100.txt')
# lb = finder.re_find(CONFIG.IDNUM_PATTERN)
# print(lb)
# exit()

file_gen = Answer_file_generator(r'output\test.csv')

for file_name in file_listdir:
    if file_name.endswith(".txt"):  # Filter files with a .txt extension
        print(file_name)

for file_name in all_file_names:
    name = os.path.splitext(file_name)[0]
    result = []
    #############################################################################
    ################################### IDNUM ###################################
    #############################################################################
    if IDNUM_FINDER_EN:
        finder  = IDNUM_Finder()
        finder.set_file(FILE_DIR+file_name)
        #find all pattern
        lb = finder.find()
        #add to file_gen
        for l in lb:
            file_gen.add_item(name, l[0], l[1], 'IDNUM', l[2])
    if DOCTOR_FINDER_EN:
        finder  = DOCTOR_Finder()
        finder.set_file(FILE_DIR+file_name)
        #find all pattern
        lb = finder.find(name)
        #add to file_gen
        for l in lb:
            file_gen.add_item(name, l[0], l[1], 'DOCTOR', l[2])
    

    #MEDICALRECORD_Finder
    if MEDICALRECORD_FINDER_EN: # 0.9971086327963651
        finder  = MEDICALRECORD_Finder()
        finder.set_file(FILE_DIR+file_name)
        #find all pattern
        lb = finder.find()
        #add to file_gen
        for l in lb:
            file_gen.add_item(name, l[0], l[1], 'MEDICALRECORD', l[2])
            
    if PATIENT_FINDER_EN: # 0.9860583016476553
        finder  = PATIENT_Finder()
        finder.set_file(FILE_DIR+file_name)
        #find all pattern
        lb = finder.find()
        #add to file_gen
        for l in lb:
            file_gen.add_item(name, l[0], l[1], 'PATIENT', l[2])
    if HOSPITAL_FINDER_EN: # 0.9860583016476553
        finder  = HOSPITAL_Finder()
        finder.set_file(FILE_DIR+file_name)
        #find all pattern
        lb = finder.find()
        #add to file_gen
        for l in lb:
            file_gen.add_item(name, l[0], l[1], 'HOSPITAL', l[2])
    if DATE_FINDER_EN:
        finder  = DATE_Finder()
        finder.set_file(FILE_DIR+file_name)
        #find all pattern
        lb = finder.find()
        lb = finder.date_normalization(lb)
        lb = finder.patch_change_MMDD(lb) ##from 0.8085106382978723 to 0.8636205092431112
        #add to file_gen
        for l in lb:
            file_gen.add_item(name, l[0], l[1], 'DATE', l[2] , l[3])
    
    if TIME_FINDER_EN:
        finder  = TIME_Finder()
        finder.set_file(FILE_DIR+file_name)
        #find all pattern
        lb = finder.find()
        lb = finder.time_normalization(lb)
        #add to file_gen
        for l in lb:
            file_gen.add_item(name, l[0], l[1], 'TIME', l[2] , l[3])
            
    if CITY_FINDER_EN:
        finder  = CITY_Finder()
        finder.set_file(FILE_DIR+file_name)
        #find all pattern
        lb = finder.find()
        #add to file_gen
        for l in lb:
            file_gen.add_item(name, l[0], l[1], 'CITY', l[2])
    if STREET_FINDER_EN:  # 0.9921259842519685
        finder = STREET_Finder()
        finder.set_file(FILE_DIR+file_name)
        #find all pattern
        lb = finder.find()
        #add to file_gen
        for l in lb:
            file_gen.add_item(name, l[0], l[1], 'STREET', l[2])    
    if ZIP_FINDER_EN:  # 0.9888641425389755
        finder  = ZIP_Finder()
        finder.set_file(FILE_DIR+file_name)
        #find all pattern
        lb = finder.find()
        #add to file_gen
        for l in lb:
            file_gen.add_item(name, l[0], l[1], 'ZIP', l[2])
    if STATE_FINDER_EN: # 0.991774383078731
        finder = STATE_Finder()
        finder.set_file(FILE_DIR+file_name)
        #find all pattern
        lb = finder.find()
        #add to file_gen
        for l in lb:
            file_gen.add_item(name, l[0], l[1], 'STATE', l[2])
    if DEPARTMENT_FINDER_EN:
        finder = DEPARTMENT_Finder()
        finder.set_file(FILE_DIR+file_name)
        #find all pattern
        lb = finder.find()
        #add to file_gen
        for l in lb:
            file_gen.add_item(name, l[0], l[1], 'DEPARTMENT', l[2])
    if AGE_FINDER_EN: # 0.9775280898876404
        finder = AGE_Finder()
        finder.set_file(FILE_DIR+file_name)
        #find all pattern
        lb = finder.find()
        #add to file_gen
        for l in lb:
            #print(l)
            file_gen.add_item(name, l[0], l[1], 'AGE', l[2])
    if DURATION_FINDER_EN: # 0.8275862068965517 # data too few
        finder = DURATION_Finder()
        finder.set_file(FILE_DIR+file_name)
        #find all pattern
        lb = finder.find()
        lb = finder.duration_normalization(lb)
        #add to file_gen
        for l in lb:
            file_gen.add_item(name, l[0], l[1], 'DURATION', l[2]  , l[3])
    if PATIENT_FINDER_EN: # 1
        finder = PHONE_Finder()
        finder.set_file(FILE_DIR+file_name)
        #find all pattern
        lb = finder.find()
        #add to file_gen
        for l in lb:
            file_gen.add_item(name, l[0], l[1], 'PHONE', l[2])
    if LOCATION_OTHER_FINDER_EN:
        finder = LOCATION_OTHER_Finder()
        finder.set_file(FILE_DIR+file_name)
        #find all pattern
        lb = finder.find()
        #add to file_gen
        for l in lb:
            file_gen.add_item(name, l[0], l[1], 'LOCATION-OTHER', l[2])
    if SET_FINDER_EN:
        finder = SET_Finder()
        finder.set_file(FILE_DIR+file_name)
        #find all pattern
        lb = finder.find()
        lb = finder.set_normalization(lb)
        #add to file_gen
        for l in lb:
            file_gen.add_item(name, l[0], l[1], 'SET', l[2], l[3])
    if COUNTRY_FINDER_EN:
        finder = COUNTRY_Finder()
        finder.set_file(FILE_DIR+file_name)
        #find all pattern
        lb = finder.find()
        #add to file_gen
        for l in lb:
            file_gen.add_item(name, l[0], l[1], 'COUNTRY', l[2])
    
    
    
    
file_gen.print_df()
file_gen.remove_overlap()
    #save
file_gen.save()

# check answer
    
my_ans_path = rf'output/test.csv'
#target_path = rf'data\answer.txt'
target_path  = ANS_PATH
comparator = Csv_comparator(my_ans_path,target_path ,  specify_label = 'COUNTRY' , ignore_time = 0 )
comparator.compare()
comparator.print_res()
comparator.calc_f1_score()

comparator.save_res()



