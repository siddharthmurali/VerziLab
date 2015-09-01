'''
Created on Jun 3, 2015

@author: Sid
'''

def GetGenesMiddle(x,y,z):
    
    list = []
    
    f = open(x)
    lines = f.readlines()
    f.close()
    
    lines = lines[1:]
    
    z = int(z)
    
    for line in lines:
        words = line.split()
        list.append(words[(z-1)])
        
    
    g = open(y, 'w')
    for line in list:
        g.write("%s\n" % line)
    g.close()
    
    
    
