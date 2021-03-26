# cleans INPUT and OUTPUT folder and fills again with all train and val images
from os import listdir
import os
import shutil
from os.path import isdir

directory = 'data/'
out = 'INPUT/'
output = 'OUTPUT/'
encode = 'encodings/'

if isdir(out):
    shutil.rmtree(out)
os.mkdir(out)

if isdir(output):
    shutil.rmtree(output)
os.mkdir(output)

if isdir(encode):
    shutil.rmtree(encode)
os.mkdir(encode)

X, y = list(), list()
# enumerate folders, on per class
for subdir in listdir(directory):
    for sub in listdir(directory+subdir+'/'):
        print('Copying '+ sub )
        path = directory+subdir+'/'+sub+'/'
        for _file in listdir(path):
            # path
            filename = path + _file
            # get face
            shutil.copy(filename,out+_file)
        try:
            os.mkdir(output+sub)
        except FileExistsError:
            pass
os.mkdir(output+'unknown')