from numpy import load
import os

#define a function to import .npy files
def import_npy(path):
    #make sure the path to the file exists
    if not os.path.exists(path):
        print('File does not exist')
        return None
    #load the data
    data = load(path)
    return data

