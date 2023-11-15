from LABEL_Finder.Finder import Finder
import re 

class AGE_Finder(Finder):
    def __init__(self):
        super().__init__()
        
        self.PATTERN = [ #DOCTOR
            r'(\d{2,3}) *yr *old',
            r'(\d{2,3}) *yrs *old',
            r'(\d{2,3}) *year *old',
            r'(\d{2,3}) *old\b',
            r'(\d{2,3}) *year-old',
            r'(\d{2,3}) *year\b',
            r'(\d{2,3}) *yo\b',
            r'(\d{2,3}) *y\.o\.',
            r'\n(\d{2,3}) ?F\b', ##(?!\.)
            r'\n(\d{2,3}) ?M\b', ##(?!\.)
            r'\n(\d{2,3})yr\b',
            r'\bage *(\d{2,3})\b',
            
            # for file29331 56 female
            r'(?i)(\d{2,3}) *female',
            r'(?i)(\d{2,3}) *male',
            
            
            
        ]
        self.res_label = []
        
        
    def find(self):
        self.res_label = self.re_find(self.PATTERN)
        self.res_label = self.del_same(self.res_label)
        
        self.res_label = self.remove_overlamp(self.res_label) # just add
        
        return self.res_label
    

if __name__=='__main__':
    finder = AGE_Finder()
    finder.set_file(rf'.\data\file\10.txt')
    
    
    print(finder.find() )