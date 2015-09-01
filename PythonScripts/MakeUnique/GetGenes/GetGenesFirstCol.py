'''
Created on Jun 2, 2015

@author: Sid
'''


def GetGenesFirstCol(x,y):

    geneList = []
    
    f = open(x)
    lines = f.readlines()
    f.close()
    
    lines = lines[1:]
    
    for line in lines:
        words = line.split()
        geneList.append(words[0])
        
    
    
    g = open(y, 'w')
    for line in geneList:
        g.write("%s\n" % line)
    g.close()
    
    
     
