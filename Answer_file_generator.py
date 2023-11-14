#a calss that gen the cvs file at the end 
#it data is file_name start_index end_index label context
#can add item with add_item function
#can check if the label 2 index include the same word with check_same_word function
#it data store with pandas data frame

# it can search data with file_name and label or both


import pandas as pd


class Answer_file_generator:
    def __init__(self,file_name):
        self.file_name = file_name
        self.data = pd.DataFrame(columns=['file','label','start','end','content','time'])
        self.index = 0
    def add_item(self,file_name,start,end,label,content,time=None):
        self.data.loc[len(self.data)] = pd.Series({'file':file_name,'label':label,'start':start,'end':end,'content':content,'time':time})
        #[file_name,label,start,end,content,]
    
            
    def print_df(self):
        print(self.data)
        
        
    def check_same_word(self,start_index,end_index):
        for index,row in self.data.iterrows():
            if row['start_index'] == start_index and row['end_index'] == end_index:
                return True
        return False
    def save(self):
        self.data.to_csv(self.file_name,index=False , sep='\t' , header=False)
        # if row is not time info , it will be \t\t at the end of the line , del it 
        with open(self.file_name, 'r') as f:
            lines = f.readlines()
            lines = [line.replace('\t\n', '\n') for line in lines]
            f.close()
        with open(self.file_name, 'w') as f:
            f.writelines(lines)
            f.close()
        
    def search(self,file_name=None,label=None):
        if file_name == None and label == None:
            return self.data
        elif file_name == None:
            return self.data[self.data['label'] == label]
        elif label == None:
            return self.data[self.data['file_name'] == file_name]
        else:
            return self.data[(self.data['file_name'] == file_name) & (self.data['label'] == label)]        
        
if __name__ == '__main__':
    file_gen = Answer_file_generator('test.csv')

    file_gen.add_item('file1',"fuck" , 1,2,'name')
    file_gen.add_item('file1',"fuck" , 1,50,'hellio','22rrr')
    
    
    file_gen.print_df()
    
    #save
    file_gen.save()
 