from LABEL_Finder.Finder import Finder
import re 

class AGE_Finder(Finder):
    def __init__(self):
        super().__init__()
        
        self.PATTERN = [ #DOCTOR
            r'(\d{2}) *yr *old',
            r'(\d{2}) *yrs *old',
            r'(\d{2}) *year *old',
            r'(\d{2}) *old\b',
            r'(\d{2}) *year-old',
            r'(\d{2}) *yo\b',
            r'(\d{2}) *y\.o\.',
            r'\n(\d{2}) ?F\b', ##(?!\.)
            r'\n(\d{2}) ?M\b', ##(?!\.)
            r'\n(\d{2})yr\b',
            r'\bage *(\d{2})\b',
            
        ]
        self.res_label = []
        
        
    def find(self):
        self.res_label = self.re_find(self.PATTERN)
        self.res_label = self.del_same(self.res_label)
        
        return self.res_label
    

if __name__=='__main__':
    finder = AGE_Finder()
    finder.set_file(rf'.\data\file\10.txt')
    
    
    print(finder.find() )