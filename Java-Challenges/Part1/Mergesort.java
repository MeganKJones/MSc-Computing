import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class Mergesort {
    
    public static List<Object> merge(ArrayList<String> leftList, ArrayList<String> rightList, ArrayList <String> s, int comparisons, int moves){
        //System.out.println(leftList);
        //System.out.println(rightList);
        while((leftList.size() != 0) && (rightList.size() != 0)){
            if(leftList.get(0).compareTo(rightList.get(0)) <= 0){
                //comparing first element of leftList to rightList
                comparisons ++;
                //adding to new ArrayList
                s.add(leftList.get(0));
                //removing element from old list so that new element is now at 0
                leftList.remove(0);
            }
            else{
                comparisons ++;
                s.add(rightList.get(0));
                rightList.remove(0);
                //element is swapped as it comes first alphabetically
                moves ++;
            }
        }
        while(leftList.size() != 0){
            s.add(leftList.get(0));
            leftList.remove(0);
        }
    
        while(rightList.size() != 0){
            s.add(rightList.get(0));
            rightList.remove(0);
        }
        //System.out.println("comparisions: " + comparisons);
        //System.out.println("moves: " + moves);
        //System.out.println(s);

        return Arrays.asList(s,comparisons,moves);
        
    }
    
    public static List<Object> mergeSort(ArrayList<String> inputArray, int L, int R){
        ArrayList <String> s = new ArrayList <String>();
        //variables for moves + comparisons
        int total_comparisons = 0;
        int total_moves = 0;
        
        if (L < R){
            //finding middle of list
           int M = (L + R)/2;
           //ArrayList for first half of the split list
           ArrayList<String> leftArrayList = new ArrayList<String>();
           for (int i = 0; i < M+1; i++){
                leftArrayList.add(inputArray.get(i));
            }
            //calling mergeSort again
            List<Object>left_return_objects = mergeSort(leftArrayList, 0, leftArrayList.size()-1);
            //resetting variable for next mergesort()
            leftArrayList = (ArrayList<String>)left_return_objects.get(0);
            //casting objects into Integers
            total_comparisons += (Integer) left_return_objects.get(1);
            total_moves += (Integer) left_return_objects.get(2);
            
            //ArrayList for second half of the split list
           ArrayList<String> rightArrayList = new ArrayList<String>();
           for (int j = M+1; j < inputArray.size(); j++){
                rightArrayList.add(inputArray.get(j));
            }
            //calling mergeSort again
            List<Object>right_return_objects = mergeSort(rightArrayList, 0, rightArrayList.size()-1);
            //resetting variable for next mergesort()
            rightArrayList = (ArrayList<String>)right_return_objects.get(0);
            //casting objects into Integers
            total_comparisons += (Integer) right_return_objects.get(1);
            total_moves += (Integer) right_return_objects.get(2);

            return merge(leftArrayList, rightArrayList, s, total_comparisons, total_moves);
        }
        return Arrays.asList(inputArray, 0, 0);
    }
    
}
