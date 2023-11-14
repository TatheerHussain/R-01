from LABEL_Finder.Finder import Finder
import re 

class DOCTOR_Finder(Finder):
    def __init__(self):
        super().__init__()
        
        self.PATTERN = [ #DOCTOR
            r'(?i)[ \n]DR +([A-Za-z\-]* ?[A-Za-z\-]* ?[A-Za-z\-]*)[\n)]', # 100% correct 
            rf'(?i:Reported ?by ?Dr +)([A-Z][A-Za-z\-]*(?: [A-Z][A-Za-z\-]*)?(?: [A-Z][A-Za-z\-]*)?)' , #~100% correct
            rf'\(([A-Z][A-Z])/ ?ec' , 
            
            
            rf'[Dd][Rr]\.? ([A-Z][A-Za-z\-\.]*(?: [A-Z][A-Za-z\-]*)?(?: [A-Z][A-Za-z\-]*)?)' ,# this will get some wrong , but correct much 
            
            rf'Prof ([A-Z][A-Za-z\-]*(?: [A-Z][A-Za-z\-]*)?(?: [A-Z][A-Za-z\-]*)?)'# this will get some wrong , but correct much 
            
            
            #rf'\(TO: ?([A-Z][A-Z]);? ?([A-Z][A-Z])?/'            , # this cant apply to filexxxx.txt , but xxxx.txt is must
            
        ]
        self.res_label = []
        
        
    def find(self,file_name):
        self.res_label = self.re_find(self.PATTERN)

        if 'file' not in file_name: # filexxxx.txt
            self.res_label += self.re_find(rf'\(TO: *([A-Z][A-Z])[;:]? *([A-Z][A-Z])?/')
            self.res_label += self.re_find(rf'\(([A-Z][A-Z])/')
            
        self.res_label = self.del_same(self.res_label)
        
        return self.res_label
    



if __name__=='__main__':
    finder = DOCTOR_Finder()
    finder.set_file(rf'.\data\file\10.txt')
    
    
    print(finder.find() )