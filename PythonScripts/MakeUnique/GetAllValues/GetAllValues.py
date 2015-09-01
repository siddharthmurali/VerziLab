'''
Created on Jun 3, 2015

@author: Sid
'''
from test.test_readline import readline

def GetAllValues(x,y):
    
    
    
    f = open(x)
    lines = f.readlines()
    f.close()
    
    header = lines[0]
 
    lines = lines[1:]
    
    lines = list(set(lines))
    
    lines.insert(0, header)
    
    
    
   
    g = open(y, 'w')
    for line in lines:
        g.write("%s\n" % line)
    g.close()
        
          
     