'''
Created on Jun 2, 2015

@author: Siddharth Murali
'''

def GetGenesLastCol(x,y):
    
    geneList = []
    
    f = open(x)
    lines = f.readlines()
    f.close()
    
    for line in lines:
        if line[0] != "#":
            pos = line.find("+")
            if pos != -1:
                line = line[(pos+1):]
                
            if pos == -1:
                pos = line.find("-")
                line = line[(pos+1):]
                
            
            geneList.append(line)
    
    
   
    
    g = open(y, 'w') # Opens the output file
    for line in geneList:
        g.write(line) # Loops trough our unique list and writes it to our output file.
    g.close()
    

