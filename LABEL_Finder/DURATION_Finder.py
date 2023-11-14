from LABEL_Finder.Finder import Finder
import re 

class DURATION_Finder(Finder):
    def __init__(self):
        super().__init__()
        
        self.PATTERN = [ #DOCTOR
            r'(\d{1,3} *years)',
            r'(\d{1,3} *yrs)(?! old)',
            r'(\d{1,3} *weeks)',
            r'(\d{1,3} *week)',
            r'(\d{1,3} *wks)',
            r'(\d{1,3} *months)',
            r'(\d{1,3} *month)',
            
            
        ]
        self.res_label = []
        
        
    def find(self):
        self.res_label = self.re_find(self.PATTERN)
        self.res_label = self.del_same(self.res_label)
        self.res_label = self.remove_overlamp(self.res_label)
        
        return self.res_label
    
    def normalization(self , date_str):
        pattern = r'(\d{1,3}) *(?:years|yrs)'
        mat = re.search(pattern , date_str)
        if mat!=None:
            return f'P{mat.group(1)}Y'
        
        pattern = r'(\d{1,3}) *(?:weeks|week|wks)'
        mat = re.search(pattern , date_str)
        if mat!=None:
            return f'P{mat.group(1)}W'
        
        pattern = r'(\d{1,3}) *(?:months|month)'
        mat = re.search(pattern , date_str)
        if mat!=None:
            return f'P{mat.group(1)}M'
        
    
    
    def duration_normalization(self , lb):
        res_lb = []
        for l in lb:
            res_lb.append( [ *l , self.normalization(l[2]) ] )
        return res_lb

if __name__=='__main__':
    finder = DURATION_Finder()
    finder.set_file(rf'.\data\file\10.txt')
    
    
    print(finder.find() )