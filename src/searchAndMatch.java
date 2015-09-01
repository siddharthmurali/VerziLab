import java.io.*;
import java.util.*;
public class searchAndMatch {

	/**
	 * For use after FileManipulation.java
	 * searchAndMatch is designed to search for cluster specific XlocId's in a large list
	 * of significant XlocID's/gene names. It then creates a new text file that outputs the 
	 * gene names for that specific cluster.
	 * @param args
	 * @throws IOException
	 */
	public static void main(String[] args) throws IOException{
		compare("afterXlocSeries.txt", "clusterOne.txt", "firstClusterGeneNames.txt");
	}
	
	/**
	 * compare: compares XlocId's and outputs gene names in a text file.
	 * @param sigGeneNames: list of XlocId's/Gene Names. NOTE: should use afterXlocSeries.txt from 
	 * fileManipulation.java 
	 * @param cluster: list of XlocId's from specific cluster. NOTE: should use clusterOne.txt,
	 * clusterTwo.txt, etc, from FileManipulation.java
	 * @param fileOutput: predetermined text file to output gene names to.
	 * @throws IOException
	 */
	private static void compare(String sigGeneNames, String cluster, String fileOutput) throws IOException{
		
		FileReader frSig = new FileReader(sigGeneNames);
		BufferedReader brSig = new BufferedReader(frSig);
		
		FileReader frCluster = new FileReader(cluster);
		BufferedReader brCluster = new BufferedReader(frCluster);
		
		FileWriter newFile = new FileWriter(fileOutput);
		BufferedWriter brw = new BufferedWriter(newFile);
		
		Hashtable xlocGeneHash = new Hashtable();
		
		String line;
		String line2;
		String xloc;
		String gene;
		String geneName;
		int count = 0;
		int count2 =0;
		
		try{
		while((line = brSig.readLine()) !=null){
			while(line.charAt(count) != ' '){
				line = line.trim();
				count++;
			}
			xloc = line.substring(0, count);
			
			count2 = count+1;
			
			while(line.charAt(count2) == ' '){
				count2++;
			}			
			gene = line.substring(count2++, line.length());
			
			xlocGeneHash.put(xloc, gene);
		}
		
		} 
		
		catch (StringIndexOutOfBoundsException e){
		
		}
		
		try{
			while((line2 = brCluster.readLine()) != null){
				geneName = (String) xlocGeneHash.get(line2);
				
				brw.write(geneName);
				brw.newLine();
				brw.flush();
			}
		}
		
		catch (StringIndexOutOfBoundsException e){	
		}
		
	}
}
