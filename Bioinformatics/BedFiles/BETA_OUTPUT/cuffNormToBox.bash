#!/bin/bash

awk -v OFS='\t' '{print $1, $2, $6, $11, $3, $7, $12, $8, $13, $4, $9, $14, $5, $10 }' $1 > test.txt

grep -v '^LINC' test.txt > test2.txt

grep -v '^MIR' test2.txt > test3.txt

grep -v '^NOR' test3.txt > test4.txt

grep -v '^LINC' test4.txt > $2


