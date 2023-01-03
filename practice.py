import os
import pprint
import csv

filemap= []
file_name= []
def read_directory(path):
    
    dir_list= os.listdir(path)
    for file in dir_list:
        if file.endswith(".csv"): 
            file_name.append(file)
            a= process_file(file)          
            filemap.append(a)
       
    return(filemap)                                     

line=[]
def process_file(filename):
    with open(filename, 'r') as fp:
            cereals= csv.reader(fp)
            for values in cereals:
                line.append(values)
    return(line)

b= read_directory("//Users//sakshumsingh//Workspace//Python Practice")

pprint.pprint(b)