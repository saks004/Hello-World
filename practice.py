import os
import pprint
import csv
import pandas as pd


def read_directory(path):
    new_df= pd.DataFrame() 
    file_name= []      
    dir_list= os.listdir(path)
    for file in dir_list:
        if file.endswith(".csv"): 
            file_name.append(file)
            new_df.append(process_file(file))          
   
    return(new_df)                                     


def process_file(filename):
    
        df= pd.read_csv(filename)
        return(df)
   

b= read_directory("//Users//sakshumsingh//Workspace//Python Practice")

pprint.pprint(b)


# def func(name):

#     df= pd.read_csv()
#     print (df.head())
#     return df
