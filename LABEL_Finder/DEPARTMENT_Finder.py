from LABEL_Finder.Finder import Finder
import re 

class DEPARTMENT_Finder(Finder):
    def __init__(self):
        super().__init__()
        
        self.PATTERN = [ #PATIENT
            
            
            ###### sel start
            # r'Site_name: *(.{6,})\n',
            # rf'Site: *([A-Z ]+ HOSPITAL(?:[A-Z ])*)\n',
            # rf'\nSiteName\n(.+)\n', #0.9971
            # rf"Location:.*?- *(?:OPERATIVE UNIT|OPERATIVEUNIT)?+[\- ]*([' &A-Z/\-\(\)]+) *\n" ,  #0.994
            ###### sel end
            
            
            # acc word r"[A-Za-z0-9\']"
            r"Location: *([A-Za-z0-9\']+(?: +[A-Za-z0-9\']+)*) *-"          ,
        ]
        self.res_label = []
        
        
    def find(self):
        self.res_label = self.re_find(self.PATTERN)
        self.res_label = self.del_same(self.res_label)
        
        
        res_add = []





        return self.res_label
    





if __name__=='__main__':
    finder = DEPARTMENT_Finder()
    finder.set_file(rf'.\data\file\file147.txt')
    
    print(finder.find() )