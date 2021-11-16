import java.util.*;
import java.util.regex.*;
import java.io.*;
import java.util.Collections;


public class partOneAssessment{
    static ArrayList<String> openFile(String fileName){
        //method to open .txt files and add words into an ArrayList
        ArrayList<String> listOfLines = new ArrayList<String>();
        
        try{
    
            BufferedReader bufReader = new BufferedReader(new FileReader(fileName));
            String line = bufReader.readLine();
            
            while(line != null){
                //adding words to arraylist
                    //regex 
                        String whatIWant = "[A-Za-z]{2,20}";
                        Pattern regexPattern = Pattern.compile(whatIWant);
                        Matcher regexMatcher = regexPattern.matcher(line);
    
                        while (regexMatcher.find()){
                            if(regexMatcher.group().length() != 0){
                                listOfLines.add(regexMatcher.group());
                            }   
                        }            
                 //resetting line variable
                 line = bufReader.readLine();
                }
            bufReader.close();
    } //end of try
    catch(IOException e){
        System.out.println("An exception");
    }//end of catch
    return listOfLines;
}
    public static void main(String[] args) {
    //initialising arraylists
    ArrayList<String> listOfLines = openFile("an_article.txt");
    ArrayList<String> twoOfLines = openFile("google-10000-english-no-swears.txt");
    ArrayList<String> setOfWords = new ArrayList<String>();
    

//calling mergesort()
    List<Object>return_twoOfLines = Mergesort.mergeSort(twoOfLines, 0, twoOfLines.size()-1); 

//sorting list to make it more efficient
    ArrayList<String> sortedTwoOfLines = (ArrayList<String>) return_twoOfLines.get(0);
//number of comparisons and moves that were made
    int comparisons = (Integer)return_twoOfLines.get(1);
    int moves = (Integer)return_twoOfLines.get(2);
    
//binary search to get valid words that are in both articles & run time
    long startTimeA = System.nanoTime();
    for(int a = 0; a < listOfLines.size(); a++){
        if(Collections.binarySearch(sortedTwoOfLines, listOfLines.get(a)) > 0){
            setOfWords.add(listOfLines.get(a));
        }
    }
    long endTimeA = System.nanoTime();
    
//Printing list for part A
for(int b = 0; b < setOfWords.size(); b++){
    System.out.println(setOfWords.get(b));
    }
//printing run time
System.out.println("run time for part A is: " + (endTimeA - startTimeA) + "ns");

//B: printing comparison/moves and timing

//sorting list made from A
    List<Object>returnSetOfWords = Mergesort.mergeSort(setOfWords, 0, setOfWords.size()-1); 
    ArrayList<String> sortedSetOfWords = (ArrayList<String>) returnSetOfWords.get(0);

//printing out sorted list 
    for(int c = 0; c < sortedSetOfWords.size(); c++){
        System.out.println(sortedSetOfWords.get(c));
    }
//printing comparisons+moves    
System.out.println("Moves: " + moves + " Comparisons: " + comparisons);

//timings
    for(int j = 100; j < setOfWords.size(); j+=100){
        
        ArrayList<String> testWords = new ArrayList<String>();
        for(int k = 0; k < j; k++){
            testWords.add(setOfWords.get(k));
        }
        System.out.println("Length of list is: " + testWords.size());
        long runningTotal = 0;
//getting average run time for all 10 tries
        for(int i = 0; i < 10; i++){
            long startTime = System.nanoTime();
            List<Object>return_listOfLines = Mergesort.mergeSort(testWords, 0, testWords.size()-1); 
            long endTime = System.nanoTime();
            long totalTime = endTime - startTime;
            runningTotal += totalTime;
        }
        System.out.println("Average run time is: " + (runningTotal / 10) + "ns");
    }
}
}
