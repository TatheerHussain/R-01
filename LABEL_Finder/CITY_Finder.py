from LABEL_Finder.Finder import Finder
from LABEL_Finder.STATE_Finder import STATE_Finder
import re 

class CITY_Finder(Finder):
    def __init__(self , dict_path = rf'dictionary\CITY_dict.txt'):
        super().__init__()
        
        self.PATTERN = [ #CITY_Finder
        ]
        self.res_label = []
        
    def find(self):
        state_finder = STATE_Finder()
        state_finder.set_file_str(self.file)
        st_res = state_finder.find()
        
        for st in st_res:
            s,e,w = st
            line_start, line_end, line = self.get_label_line(st)
            
            lb_s = line_start
            lb_e = s
            
            city = self.file[lb_s:lb_e]
            mat = re.search(r'([A-Z]+(?: *[A-Z]+)*)', city)
            if mat == None:
                continue
            city = mat.group(1)
            lb = self.re_find( '(' + city + ')' )[0]
            self.res_label.append(lb)
                
        return self.res_label
    



if __name__=='__main__':
    finder = CITY_Finder()
    
    finder.set_file(rf'.\data\file\151.txt')
    
    res = finder.find()
    
    print(res)
        
    

    #finder.set_file(rf'.\data\file\10.txt')
    
    
    #print(finder.find() )