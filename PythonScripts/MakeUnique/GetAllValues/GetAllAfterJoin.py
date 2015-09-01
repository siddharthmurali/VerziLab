'''
Created on Jun 16, 2015

@author: Sid
'''
from GetAllValues import GetAllValues
def GetAllAfterJoin(x,y):
    
    f = open(x)
    lines = f.readlines()
    f.close()
    
    genes = []
    rpkm = []
    
    
 

    
    for index, line in enumerate(lines):
        if line[0] != " ":
            genes.append(line)
            rpkm.append(lines[index + 1])
   
    for line in rpkm:
        line = [line.strip(' ')]
        
    
    header = genes[0]
    
    count = 1
    
    
    g = open(y, "w")
    g.write(header)

    
    while count != len(genes):
        line = [genes[count], rpkm[count]]
        line = list(line)
        g.write('%s%s\n' % (line[0].rstrip('\n'), line[1]))
        count = count + 1
    g.close()
    
        
