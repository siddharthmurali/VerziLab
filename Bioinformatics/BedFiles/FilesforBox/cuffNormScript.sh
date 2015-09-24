#!/bin/bash

cut -f1 -f3- $1 > test.txt

#awk -v OFS='\t' '{print $1,  $4, $9, $13, $8, $13, $4, $7, $12, $5, $10, $2, $6, $11 }' test.txt > testTwo.txt
awk -v OFS='\t' '{print $1, $4, $8, $13, $12, $3, $7, $11, $5, $9, $2, $6, $10}' test.txt > testTwo.txt  #Use this for all genes cuffNorm Human RNASeq 


grep -v '^LINC' testTWO.txt > test3.txt

grep -v '^MIR' test3.txt > test4.txt

grep -v '^NOR' test4.txt > test5.txt

grep -v '^LOC' test5.txt > test6.txt

awk -f /Users/Sid/Documents/VerziLab/Bioinformatics/Scripts/AddOne.sh test6.txt > $2

Rscript /Users/Sid/Documents/VerziLab/Bioinformatics/Scripts/tableToBox.r $2 $3

# ^ ^ Change the path for two lines above based on preference.  
