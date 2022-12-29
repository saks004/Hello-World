import os
import pprint
filemap= []
file_name= []
def read_directory(path):
    
    dir_list= os.listdir(path)
    for file in dir_list:
        if file.endswith(".txt"): 
            file_name.append(file)
            a= process_file(file)          
            filemap.append(a)
       
    return(filemap)                                     
     
#Total count of lines in a txt file
def process_file(filename):
    
    file_dictionary ={
        "file_name": [],
        "total_lines" : 0,
        "line_index" : [],
        "line_list" : [],
        "total_words" : 0
    }
    for name in file_name:

        with open(filename, 'r') as fp:
            line_list, line_indexes, total_words = [],[],0
            for count, line in enumerate(fp):
                line_list.append(line.strip())
                line_indexes.append(count)
                total_words= total_words + len(line.split())

            # print("Lines in the file", count, line)

    file_dictionary = {
        "file_name": name,
        "total_lines" : count+1,
        "line_index" : line_indexes,
        "line_list" : line_list,
        "total_words": total_words 
    }   
    return (file_dictionary)

b= read_directory("//Users//sakshumsingh//Workspace//Python Practice")

pprint.pprint(b)






