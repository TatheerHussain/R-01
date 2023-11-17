from LABEL_Finder.Finder import Finder
import re 
from LABEL_Finder.Finder_DICT import Finder_DICT
class ORGANIZATION_Finder(Finder):
    def __init__(self , dict_path = rf'dictionary\ORGANIZATION_dict_V2.txt'):
        super().__init__()
        self.dict_path = dict_path
        self.PATTERN = [ 
        ]
        self.res_label = []
        
    def find(self):
        dict_finder = Finder_DICT(self.dict_path)
        dict_finder.set_file(self.file)
        dict_finder.dict_len_filter(5)
        self.PATTERN = dict_finder.find_all()
        for i in range(len(self.PATTERN)):
            self.PATTERN[i] = '(?i)' + '(' + self.PATTERN[i] + ' (?:Inc|Corporation)?' +')'
        
        self.res_label = self.re_find(self.PATTERN)
        
        self.res_label = self.del_same(self.res_label)
        self.res_label = self.remove_overlamp(self.res_label)
                
        return self.res_label
    



if __name__=='__main__':
    finder = ORGANIZATION_Finder()
    
    finder.set_file(rf'.\data\file\151.txt')
    
    res = finder.find()
    
    print(res)
        
    

    #finder.set_file(rf'.\data\file\10.txt')
    
    
    #print(finder.find() )