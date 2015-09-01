import java.io.*;
public class FileManipulation {
	
	/** FileManipulation prepares text files for easy search/match XLOC ID's in in each 
	 * cluster with large list of Significant XLOC ID's/Gene Names.
	 * Make sure all text files have been created and are in the proper directory before
	 * calling any method.
	 */
	public static void main (String[] args) throws IOException {
		beforeX("mySigGenesfeaturesCopy", "mySigGenesBeforeX.txt");
		afterXlocSeries("mySigGenesBeforeX.txt", "afterXlocSeries.txt");
		clusterOrganization("clusters.txt", "clusterOne.txt", '1');
		
	}
	
	/**
	 * beforeX: method used to delete all characters before the 'X' in the XLOC Gene ID
	 * @param fileInput: text file with list of Significant Genes.
	 * @param fileOutput: text file where modified list will write to.
	 * @throws IOException
	 */
	
	private static void beforeX(String fileInput, String fileOutput) throws IOException{
		
		FileReader fstream = new FileReader(fileInput);
		BufferedReader br = new BufferedReader(fstream);
		
		FileWriter fwriter = new FileWriter(fileOutput);
		BufferedWriter brw = new BufferedWriter(fwriter);
		
		String line;
		int count = 0;
		
		while((line = br.readLine()) != null){
			count = 0;
			line = line.trim();
			while(line.charAt(count) != 'X'){
				count++;
			}
			line = line.substring(count, line.length()-1);
			brw.write(line);
			brw.newLine();
			brw.flush();
			//System.out.println(line);
		}
		
	}

	/**
	 * afterXlocSeries: method used for deleting all characters between XLOC ID sequence and
	 * gene name.
	 * @param fileInput: ideally should be fileOutput from beforeX method
	 * @param fileOutput: text file where final copy of modified list will write to
	 * @throws IOException
	 */

	private static void afterXlocSeries(String fileInput, String fileOutput) throws IOException{
		
		FileReader fstream = new FileReader(fileInput);
		BufferedReader br = new BufferedReader(fstream);
		
		FileWriter fwriter = new FileWriter(fileOutput);
		BufferedWriter brw = new BufferedWriter(fwriter);
		
		String line;
		int count = 0;
		int count2 = 0;
		
		try{
		while((line = br.readLine()) != null){
			line = line.trim();
			while(line.charAt(count) != '"'){
				count++;
			}
			count2 = count+1;
			while(line.charAt(count2) != '"'){
				count2++;
			}
			
			line = line.substring(0, count) + " " + line.substring(count2+1, line.length());
			brw.write(line);
			brw.newLine();
			brw.flush();
			//System.out.println(line);
		
		}
		}catch (StringIndexOutOfBoundsException e){
			System.out.println("BeforeX: You may have an extra line in your input file.");
		}
	}
	
	/**
	 * clusterOrganization: method for taking list of XLOC ID's and the cluster each belongs to,
	 * and organizing each cluster into k text files. You will need to call this method k times
	 * in order to create k text files.	
	 * @param fileInput: list of XLOC ID's/cluster it belongs to
	 * @param clusterOutput: the text file you want to output each cluster to. 
	 * @param number: the cluster number that you want to separate. Type in '1' for first cluster
	 * '2' for second cluster, etc.
	 * @throws IOException
	 */
	private static void clusterOrganization(String fileInput, String clusterOutput, Character number) throws IOException{
		
		FileReader fstream = new FileReader(fileInput);
		BufferedReader br = new BufferedReader(fstream);
		
		FileWriter fw = new FileWriter(clusterOutput);
		BufferedWriter brw = new BufferedWriter(fw);
		
		
		String line;
		int countBeforeXloc = 0;
		int countAfterXloc = 0;
		int count = 0;
		
		
		try{
		while((line = br.readLine()) != null){
			line = line.trim();
			countBeforeXloc = 0;
			countAfterXloc = 0;
			count = 0;
			
			while(line.charAt(countBeforeXloc) != ' '){
				countBeforeXloc++;
			}
			countAfterXloc = countBeforeXloc;
			while(line.charAt(countAfterXloc) == ' '){
				countAfterXloc++;
			}
			if(line.charAt(countAfterXloc) == number){
				while(line.charAt(count) != ' '){
					count++;
				}
				line = line.substring(0, count);
				
				brw.write(line);
				brw.newLine();
				brw.flush();
			  //System.out.println(line);
			}
	}
		} catch (StringIndexOutOfBoundsException e){
			System.out.println("ClusterOrganization: You may have an extra line in your Clusters file.");
		}
	}
	

}
		
			
			
	
			
		
