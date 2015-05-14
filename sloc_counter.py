# Count the source lines of code in directory hierarchies and/or files.
# The full path(s) can be supplied with command line arguments:
#
# 'python sloc_counter.py C:\my_directory\ C:\my_other_directory C:\my.file'
#
# Author: John Paul Smith

import os
import sys
import string


SLOC = 0

def set_extensions():
    return {
        '.bat': [0, 0],
        '.c': [0, 0],
        '.cpp': [0, 0],
        '.cs': [0, 0],
        '.css': [0, 0],
        '.dtd': [0, 0],
        '.h': [0, 0],
        '.html': [0, 0],
        '.java': [0, 0],
        '.js': [0, 0],
        '.jsp': [0, 0],
        '.php': [0, 0],
        '.properties': [0, 0],
        '.py': [0, 0],
        '.rb': [0, 0],
        '.sql': [0, 0],
        '.tld': [0, 0],
        '.vbs': [0, 0],
        '.xml': [0, 0]
    }

def count_sl(in_file):
    try:
        read_file = open(in_file)
    except FileNotFoundException as e:
        print(e)
        input('\n Press enter to continue...')    
    e = os.path.splitext(in_file)[1].strip().lower()    
    if e not in extensions:
        return
    v = extensions[e][0] + 1
    extensions[e][0] = v    
    sloc = 0
    line = read_file.readline()
    while(line):        
        if not line.isspace():
            sloc = sloc + 1
        line = read_file.readline()
    v = extensions[e][1] + sloc
    extensions[e][1] = v    
    global SLOC
    SLOC = SLOC + sloc
    
def walk_dir_and_count(dir):
    if not dir:
        print(' No path specified. Using current directory: \n')
        return
    print(' Currently in \'' + dir + '\'')
    for w in os.walk(dir):        
        for f in w[2]:
            f = w[0] + os.sep + f
            count_sl(f)            
            
def print_stats():
    for k in sorted(extensions.keys()):        
        f = str(extensions[k][0])
        if f == '0':
            continue
        stats = []
        stats.append(k + ': ' + f + ' file')
        if f != '1':
            stats.append('s')
        stats.append(', ' + str(extensions[k][1]) + ' source lines')
        s = ''.join(stats)
        print(s)
        
extensions = set_extensions()
for a in sys.argv[1:]:    
    if os.path.isdir(a):
        walk_dir_and_count(a)
    elif os.path.isfile(a):
        count_sl(a)
print('\n Total SLOC: ' + str(SLOC) + '\n')
print_stats()
input('\n Press enter to close...')