




my $Input_filename_1 = $ARGV[0]; #input file 1 for gene list
my $Input_filename_2 = $ARGV[1]; # input file 2 for gene expression
my $output = $ARGV[2]; # give output file name









#open RE, "<$Input_filename_1" or die;
open DAT, "<$Input_filename_1" or die; #list of all genes 
@data = <DAT>;



open OUTPUT, ">$output" ;
open IN, "<$Input_filename_2" or die; # expression file with tab separated Columns. 

while ($read = <IN>)


	{
	chomp $read;
		@a = split '\t', $read;
		#print "$a[0]\n";
		foreach $line(@data)

		{
			chomp $line;
			#print "$line";
				if ($line eq $a[0]) #give the column number. Note : perl start with 0. so if the gene column is 4th column, in perl it is 3rd column.

				{
							print OUTPUT "$read\n";						
				}		
		}
	}



