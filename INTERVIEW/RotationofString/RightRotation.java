package INTERVIEW.RotationofString;

public class RightRotation {
    public static String rotate(String s, int d) {
        StringBuilder sb = new StringBuilder(s);
        d = d % s.length(); // Ensure d is within [0, s.length()-1]
        
        for (int i = 0; i < d; i++) {
            // Move all characters one position to the right
            char temp = sb.charAt(0);
            for (int j = 1; j < sb.length(); j++) {
                sb.setCharAt(j - 1, sb.charAt(j));
            }
            sb.setCharAt(sb.length() - 1, temp);
        }
        
        return sb.toString();
    }

    public static void main(String[] args) {
        System.out.println(rotate("abcde", 2));  
        System.out.println(rotate("abcdefg", 7));  
        System.out.println(rotate("abcdefghijklmnopqrstuvwxyz", 26));  
    }
}