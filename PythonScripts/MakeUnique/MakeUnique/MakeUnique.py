'''
Created on May 29, 2015

@author: Siddharth Murali
'''

def MakeUnique(x, y): # x = the input file   y = the output file
    
    f = open(x) #This opens the input file. 
    lines = f.readlines() #This goes through the input and returns a list named lines
    f.close() # closes the reader
    
    
    lines = list(set(lines)) #changes our list into a set, and then changes it back into a list.
    
    #In python converting to a set automatically Unique-ify's the input, so this works out pretty well. 
    
    g = open(y, 'w') # Opens the output file
    for line in lines:
        g.write(line) # Loops trough our unique list and writes it to our output file.
    g.close()


MakeUnique("out6Genes.txt" ,"out6GenesUnique.txt")                                  
#===============================================================================
## Change the values of x and y in the method call on line 20 to use the script for different files.
#===============================================================================

    
        