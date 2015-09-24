#!/usr/bin/awk -f

BEGIN{  # this ensures output is tab separated
	OFS="\t";
}
NR==1{print}  # just print the 1st line
NR>1{     # ignoring the 1st line
	for(i=2;i<=NF;i++){     #ignoring column 1
		
			$i= $1 + 1;
		
	}
	print;
}
