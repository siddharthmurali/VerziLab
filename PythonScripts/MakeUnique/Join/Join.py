'''
Created on Jun 11, 2015

@author: Sid
'''
from sysconfig import sys


def Join(x,y,z):
   
    
    
    f = open(x)
    firstCol = f.readlines()
    f.close()
    
    g = open(y)
    secondCol = g.readlines() 
    g.close()
    
    h = open(z, "w+")
    sys.stdout = h
    
    dictionary = dict(zip(firstCol, secondCol))
    
    print ("{:<8} {:<15}".format('Gene','RPKM'))
    for gene, rpkm in dictionary.items():
        print ("{:<20} {:<30}".format(gene, rpkm))
    
                   

