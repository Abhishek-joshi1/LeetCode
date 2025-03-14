import java.util.Scanner;

import org.ietf.jgss.Oid;

public class Solution {
    void Exercise_Hours(){
        Scanner sc = new Scanner(System.in);
        int n = 7;
        int [] arr = new int[7];
        int Total_hours = 0;
        for(int i = 0;i < n;i++){
            int curr = sc.nextInt();
            Total_hours += curr;
            arr[i] = curr;
            System.out.println("Day " + (i + 1) + " Exercise Duration (minutes): " + curr);
        }
        System.out.println("Total Exercise Hours in week : " + (float)Total_hours + "minutes");
        System.out.println("Average Exercise Hours in week : " + (float) Total_hours / 7.0 + "minutes");        
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        s.Exercise_Hours();
    }
}
