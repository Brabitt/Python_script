#!/usr/local/bin/python3

import os, sys, time, os.path, shutil

# -----Global Variables----------- 
path = '/Users/ronny/Documents/test_python/images'
dest = '/Users/ronny/Documents/test_python/dates_backup'
log = '/Users/ronny/Documents/test_python/log.txt'


 #------Functions---------------------- 
def info_files(path, log_file):
    statinfo = os.stat(path)
    datum = time.ctime(statinfo.st_atime)
    modi_datum = time.ctime(statinfo.st_mtime)
    size_file = statinfo.st_size 

    log_file.write('\n'+ 'name: ' + path +  \
    '\ncrated at: ' + datum + \
    '\nlast modified: ' + modi_datum + \
    '\nsize: ' +  str(size_file)+ 'b' + '\n')

    print(os.linesep + 'name: ' + path +  \
    os.linesep + 'crated at: ' + datum + \
    os.linesep + 'last modified: ' + modi_datum + \
    os.linesep + 'size: ' +  str(size_file)+ 'b' + os.linesep)

def copy_file(src, dest):
    head, filename = os.path.split(src)
    shutil.copy(src, os.path.join(dest, filename))
    
              
# search sub folders  in a folder 
def list_files(path, log_file):
    dirs = os.listdir(path)

    for p in dirs:
        new_path = os.path.join(path, p)

        if os.path.isfile(new_path):
            info_files(new_path, log_file)
            copy_file(new_path, dest)
        else:
            list_files(new_path, log_file)

#### MAIN ###
f = open(log, 'w')
list_files(path, f)
f.close()
