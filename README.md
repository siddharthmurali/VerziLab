# geneClusters
Modifies/Searches through text files to find gene names.

Use FileManipulation before searchAndMatch
Always have text files ready before use.

SigGenes - txt file with list of XLOC ID's and gene names associated with each. Should be obtained using cufflinks and R(cummeRbund)
clusters- txt file with list of XlOC ID's and cluster each belongs to. Should also be obtained using cufflinks and R(cummeRbund).

FileManipulation - Will modify SigGenes file to easily read through and separate clusters into respective txt files.
searchAndMatch - Will take XLOC ID's from the new cluster file created from FileManipulation, search through the modified SigGenes file for the gene names and store them in a new txt file.


