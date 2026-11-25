import java.util.*;

class Solution {
    public String solution(String s) {
        String [] split = s.split(" ");
        int[] arr = new int[split.length];
        
        for (int i=0; i<split.length; i++) {
            arr[i] = Integer.parseInt(split[i]);
        }
        
        Arrays.sort(arr);
        
        return arr[0] + " " + arr[arr.length-1];
    }
}