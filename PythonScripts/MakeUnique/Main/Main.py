'''
Created on Jun 2, 2015

@author: Sid
'''
from GetGenesFirstCol import GetGenesFirstCol
from GetGenesLastCol import GetGenesLastCol
from MakeUnique import MakeUnique
from GetAllValues import GetAllValues
from GetGenesMiddle import GetGenesMiddle
from GetAllAfterJoin import GetAllAfterJoin
from Join import Join


print("Are you working with a table or a file with only gene names?...Enter table or genes or separate files")
answer = input()

if answer == "separate files":
    print("What is the name of your gene file?")
    geneFile = input()
    print("What is the name of your rpkm file?")
    rpkmFile = input()
    print("One intermediate file are needed for this...what is the name of the first one?")
    extraOne = input()
    print("What is the name of the file you wish to output to?")
    outputFile = input()
    Join(geneFile, rpkmFile, extraOne)
    GetAllAfterJoin(extraOne, outputFile)
    
    
if answer == "genes":
    print("What is the name of your input file?")
    fileOne = input()
    print("What is the name of your output file?")
    fileTwo = input()
    MakeUnique(fileOne, fileTwo)
        
if answer == "table":

    print("Do you want all unique values or just unique gene names?...Enter all or genes")
    values = input()
    
    if values == "all":
        
       print("What is the name of your input file?...Make sure it exists in your directory first") 
       fileOne = input()
       
       print("What is the name of your output file?...Make sure it exists in your directory first")
       fileTwo = input()
       
       GetAllValues(fileOne, fileTwo)
       
    if values == "genes":
        
        print ("Which column do your gene names exist?...Enter first or last or middle")
        geneCol = input()
            
        if geneCol == "first":
                
            print ("What is the name of your input file?...Make sure it exists in your directory first")
            fileOne = input()
                
            print ("You will need an intermediate file for this program which will contain a list of all the genes")
                
            print("What is the name of your intermediate file?...make sure it exists in your directory first")
            intermediateFile = input()
                
            print("What is the name of your output file?...Make sure it exists in your directory first")
            finalFile = input()
                    
            GetGenesFirstCol(fileOne, intermediateFile)
            MakeUnique(intermediateFile, finalFile)
            
                   
        if geneCol == "last":
                
            print ("What is the name of your input file?...Make sure it exists in your directory first")
            fileOne = input()
                
            print ("You will need an intermediate file for this program which will contain a list of all the genes")
                
            print("What is the name of your intermediate file?...make sure it exists in your directory first")
            intermediateFile = input()
                
            print("What is the name of your output file?...Make sure it exists in your directory first")
            finalFile = input()
                    
            GetGenesLastCol(fileOne, intermediateFile)
            MakeUnique(intermediateFile, finalFile) 
        
        if geneCol == "middle":
            
            print("Which column number do the gene names exist?...Enter starting from 1")
            colNum = input()
            
            print ("What is the name of your input file?...Make sure it exists in your directory first")
            fileOne = input()
                
            print ("You will need an intermediate file for this program which will contain a list of all the genes")
                
            print("What is the name of your intermediate file?...make sure it exists in your directory first")
            intermediateFile = input()
                
            print("What is the name of your output file?...Make sure it exists in your directory first")
            finalFile = input()
                    
            GetGenesMiddle(fileOne, intermediateFile, colNum)
            MakeUnique(intermediateFile, finalFile) 
            
        