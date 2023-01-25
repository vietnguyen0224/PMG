import pandas as pd
import sys
import os

class Combine:
    def __init__(self, files_list):
        self.files = files_list[:-1]
        self.output_file = files_list[-1]
        '''A list contains items are data frames'''
        self.data = list()
        '''Merge all data frames'''
        self.merged_data= []

    def read(self):
        '''Each csv file is a list item'''
        for file in self.files:
            list_item = pd.read_csv(file, index_col=False)
            filename = os.path.split(file) #seperate filename from path
            list_item.insert(0, "filename" ,filename[1]) #insert the new column to data frame
            self.data.append(list_item)
        
    def combine(self):
        self.merged_data = pd.concat(self.data, axis=0)
      
    def write(self):
        df = pd.DataFrame(self.merged_data)
        df.to_csv(self.output_file, index=False)

if __name__ == '__main__':
    files = Combine(sys.argv[1:])
    files.read()
    files.combine()
    files.write()