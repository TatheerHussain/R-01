from LABEL_Finder.Finder import Finder
import re 

class DURATION_Finder(Finder):
    def __init__(self):
        super().__init__()
        
        self.PATTERN = [ #DOCTOR
            ### '(\d{1,3}(?:-\d{1,3})?)'                        
                        
            r'(\d{1,3}(?:-\d{1,3})? *years)',
            r'(\d{1,3}(?:-\d{1,3})? *yrs)(?! old)',
            r'(\d{1,3}(?:-\d{1,3})? *yr\b)(?! old)',
            r'(\d{1,3}(?:-\d{1,3})? *weeks)',
            r'(\d{1,3}(?:-\d{1,3})? *week)',
            r'(\d{1,3}(?:-\d{1,3})? *wks)',
            r'(\d{1,3}(?:-\d{1,3})? *months)',
            r'(\d{1,3}(?:-\d{1,3})? *month)',
            
            
        ]
        self.res_label = []
        
        
    def find(self):
        self.res_label = self.re_find(self.PATTERN)
        self.res_label = self.del_same(self.res_label)
        self.res_label = self.remove_overlamp(self.res_label)
        
        
        ## patch for FIRST_PHASE_VALIDATION 887.txt 4-5 month 4.5month
        # for lb in self.res_label:
        #     # get before str see if \d*- before it
        #     before_str = self.get_before_str(lb)
        #     if before_str!=None:
        #         pattern = r'(\d{1,3})-$'
        #         mat = re.search(pattern , before_str)
        #         if mat!=None:
        #             lb[0] = mat.group(1) + ' - ' + lb[0]
        #             lb[2] = self.normalization(lb[0])
        #             break
        
        return self.res_label
    
    def normalization(self , date_str):
        pattern = r'(\d{1,3}(?:-\d{1,3})?) *(?:years|yrs|yr)'
        mat = re.search(pattern , date_str)
        if mat!=None:
            num = mat.group(1).replace('-' , '.')
            return f'P{num}Y'
        
        pattern = r'(\d{1,3}(?:-\d{1,3})?) *(?:weeks|week|wks)'
        mat = re.search(pattern , date_str)
        if mat!=None:
            num = mat.group(1).replace('-' , '.')
            return f'P{num}W'
        
        pattern = r'(\d{1,3}(?:-\d{1,3})?) *(?:months|month)'
        mat = re.search(pattern , date_str)
        if mat!=None:
            num = mat.group(1).replace('-' , '.')
            return f'P{num}M'
        
    
    
    def duration_normalization(self , lb):
        res_lb = []
        for l in lb:
            res_lb.append( [ *l , self.normalization(l[2]) ] )
        return res_lb

if __name__=='__main__':
    finder = DURATION_Finder()
    finder.set_file(rf'.\data\file\10.txt')
    
    
    print(finder.find() )