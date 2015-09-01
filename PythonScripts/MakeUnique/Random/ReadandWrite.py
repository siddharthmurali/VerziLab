'''
Created on Jun 19, 2015

@author: Sid
'''

import shutil
import sys
if len(sys.argv) !=3:
    print 'usage: filecopy source destination'
else:
    try:
        shutil.copyfile(sys.argv[1], sys.argv[2])
    except IOError:
        print 'source file does not exist'
     


    
    